"""Plugin hierarchy, cached-path operation and canonical MCP scope regressions."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/team-brain"
spec = importlib.util.spec_from_file_location("sds_plugin_layout", ROOT / "scripts/check_plugin_layout.py")
layout = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layout)


class PluginTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "restricted repository"
        for directory in ("lib", "mcp/knowledge", "knowledge", "docs", "sources"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        for relative in ("lib/brain.py", "mcp/knowledge/server.py"):
            shutil.copyfile(ROOT / relative, self.root / relative)
        (self.root / "AGENT.md").write_text("# Synthetic SDS policy\n", encoding="utf-8")
        (self.root / "knowledge/check.md").write_text(
            "# Synthetic Ceph evidence\n\nBounded synthetic Ceph latency observation.\n", encoding="utf-8")
        for customer in ("customer-a", "customer-b"):
            folder = self.root / "private" / customer / "cluster-a/knowledge"
            folder.mkdir(parents=True)
            (folder / "private.md").write_text(
                '---\ncustomer: "' + customer + '"\ncluster: "cluster-a"\n---\n'
                "# Private evidence\n\n" + customer + " private payload.\n", encoding="utf-8")
        self.env = dict(os.environ, SDS_BRAIN_DIR=str(self.root), PYTHONDONTWRITEBYTECODE="1")
        self.env.pop("SDS_CUSTOMER", None)
        self.env.pop("SDS_CLUSTER", None)
        # Use a simulated install cache outside the repository tree.
        self.cached = self.base / "client cache/team-knowledge"
        shutil.copytree(PLUGIN / "mcp-servers/team-knowledge", self.cached)
        self.server = self.cached / "server.py"

    def run_server(self, *arguments, payload="", env=None):
        return subprocess.run([sys.executable, str(self.server), *arguments], input=payload,
                              text=True, capture_output=True, env=env or self.env,
                              cwd=self.base, timeout=30)

    def messages(self, calls):
        return "\n".join(json.dumps(message) for message in [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize",
             "params": {"protocolVersion": "2025-11-25", "capabilities": {},
                        "clientInfo": {"name": "sds-plugin-regression", "version": "1"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            *calls]) + "\n"

    def test_exact_reference_tree_and_real_archives(self):
        result = layout.check_layout(ROOT)
        self.assertTrue(result["ok"], result)
        self.assertEqual((result["files"], result["directories"], result["archives_verified"]), (29, 18, 6))

    def test_layout_rejects_missing_extra_and_wrong_type(self):
        package = self.base / "package"
        (package / "docs").mkdir(parents=True)
        shutil.copyfile(ROOT / "docs/PLUGIN_REFERENCE_TREE.json", package / "docs/PLUGIN_REFERENCE_TREE.json")
        target = package / "plugins/team-brain"
        record = json.loads((package / "docs/PLUGIN_REFERENCE_TREE.json").read_text())
        for entry in record["entries"]:
            path = target / entry["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            if entry["type"] == "tree":
                path.mkdir(exist_ok=True)
            else:
                path.write_bytes(b"")
        self.assertTrue(layout.check_layout(package, verify_archives=False)["ok"])
        (target / ".mcp.json").unlink()
        (target / ".mcp.json").mkdir()
        (target / "unexpected.txt").write_text("extra", encoding="utf-8")
        (target / "agents/hcp-architect.md").unlink()
        result = layout.check_layout(package, verify_archives=False)
        self.assertFalse(result["ok"])
        self.assertTrue(any("Wrong type: .mcp.json" == error for error in result["failures"]))
        self.assertTrue(any("Extra blob: unexpected.txt" == error for error in result["failures"]))
        self.assertTrue(any("Missing blob: agents/hcp-architect.md" == error for error in result["failures"]))

    def test_cached_adapter_check_and_missing_explicit_root(self):
        checked = self.run_server("--check")
        self.assertEqual(checked.returncode, 0, checked.stderr)
        self.assertEqual(json.loads(checked.stdout)["private_documents"], 0)
        for invalid in ("", "relative/repository"):
            env = dict(self.env, SDS_BRAIN_DIR=invalid)
            checked = self.run_server("--check", env=env)
            self.assertEqual(checked.returncode, 2)
            self.assertIn("absolute", checked.stderr)
            self.assertEqual(checked.stdout, "")

    def test_stdio_initialize_list_search_and_ping(self):
        payload = self.messages([
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "brain_search", "arguments": {"query": "synthetic Ceph", "limit": 2}}},
            {"jsonrpc": "2.0", "id": 4, "method": "ping"}])
        result = self.run_server(payload=payload)
        self.assertEqual(result.returncode, 0, result.stderr)
        replies = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual(replies[0]["result"]["protocolVersion"], "2025-11-25")
        tools = replies[1]["result"]["tools"]
        self.assertEqual({tool["name"] for tool in tools},
                         {"brain_search", "brain_read", "brain_sources", "brain_status"})
        self.assertTrue(all(tool["annotations"]["readOnlyHint"] for tool in tools))
        search = json.loads(replies[2]["result"]["content"][0]["text"])
        self.assertTrue(any(row["id"] == "knowledge/check.md" for row in search["results"]))
        self.assertEqual(replies[3]["result"], {})

    def test_private_context_is_fixed_and_cross_context_rejected(self):
        env = dict(self.env, SDS_CUSTOMER="customer-a", SDS_CLUSTER="cluster-a")
        payload = self.messages([
            {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
             "params": {"name": "brain_status", "arguments":
                        {"customer": "customer-a", "cluster": "cluster-a"}}},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "brain_read", "arguments":
                        {"id": "private/customer-b/cluster-a/knowledge/private.md",
                         "customer": "customer-b", "cluster": "cluster-a"}}}])
        result = self.run_server(payload=payload, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        replies = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual(json.loads(replies[1]["result"]["content"][0]["text"])["private_documents"], 1)
        self.assertTrue(replies[2]["result"]["isError"])
        self.assertNotIn("customer-b private payload", result.stdout)
        checked = self.run_server("--check", env=dict(self.env, SDS_CUSTOMER="customer-a"))
        self.assertEqual(checked.returncode, 2)

    def test_default_mcp_has_local_knowledge_only(self):
        config = json.loads((PLUGIN / ".mcp.json").read_text())
        self.assertEqual(set(config["mcpServers"]), {"team-knowledge"})
        self.assertEqual(config["mcpServers"]["team-knowledge"]["command"], "python3")

    def test_bash_hooks_and_exclusive_local_drafts(self):
        bundled = Path(sys.executable).parent.parent / "native/git/usr/bin/sh.exe"
        shell = str(bundled) if bundled.is_file() else shutil.which("bash")
        if not shell:
            self.skipTest("Bash is unavailable; target-host shell acceptance remains required")
        probe = subprocess.run([shell, "--version"], capture_output=True, timeout=10)
        if probe.returncode:
            self.skipTest("Bundled Bash cannot initialize in this sandbox")
        env = dict(self.env, SDS_TEST_PYTHON=Path(sys.executable).as_posix())
        command = 'python3() { "$SDS_TEST_PYTHON" "$@"; }; script=$1; shift; . "$script"'
        def invoke(name, *args):
            script = (PLUGIN / "scripts" / name).as_posix()
            syntax = subprocess.run([shell, "-n", script], capture_output=True, text=True, timeout=10)
            self.assertEqual(syntax.returncode, 0, syntax.stderr)
            return subprocess.run([shell, "-c", command, "sds-test", script, *args],
                                  capture_output=True, text=True, env=env, cwd=self.base, timeout=15)
        started = invoke("session-start.sh")
        self.assertEqual(started.returncode, 0, started.stderr)
        self.assertEqual(json.loads(started.stdout)["hookSpecificOutput"]["hookEventName"], "SessionStart")
        stopped = invoke("stop-capture-nudge.sh")
        self.assertEqual(stopped.returncode, 0, stopped.stderr)
        self.assertNotIn("decision", json.loads(stopped.stdout))
        first = invoke("brain-git.sh", "start", "learn", "fixture")
        self.assertEqual(first.returncode, 0, first.stderr)
        target = self.root / "inbox/learn-fixture.md"
        self.assertIn("human review required", target.read_text())
        before = target.read_bytes()
        second = invoke("brain-git.sh", "start", "learn", "fixture")
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(target.read_bytes(), before)
        self.assertFalse((self.root / ".git").exists())

    def test_vendor_check_does_not_execute(self):
        result = subprocess.run([sys.executable, str(PLUGIN / "mcp-servers/launch.py"), "--check"],
                                capture_output=True, text=True, env=self.env, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertFalse(report["executed"])
        self.assertEqual(len(report["archives"]), 6)
        result = subprocess.run([sys.executable, str(PLUGIN / "mcp-servers/launch.py"), "kubernetes"],
                                capture_output=True, text=True, env=self.env, timeout=30)
        self.assertEqual(result.returncode, 2)
        self.assertIn("disabled", result.stderr)


if __name__ == "__main__":
    unittest.main()

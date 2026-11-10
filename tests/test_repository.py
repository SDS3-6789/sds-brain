"""Repository packaging checks use synthetic local trees and never access a service."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sds_repository_check", ROOT / "scripts/check_repository.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in checker.REQUIRED_DIRS:
            (self.root / name).mkdir(parents=True, exist_ok=True)
        for name in checker.REQUIRED_FILES:
            self.write(name, "{}" if name.endswith(".json") else "# Synthetic fixture\n")
        self.write("AGENTS.md", "Read AGENT.md\n")
        self.write("CLAUDE.md", "@AGENT.md\n")
        self.write("knowledge/example.md", "# Shared knowledge\n")
        self.write("runbooks/example.md", "# Investigation\n")
        self.write("sources/example.json", "[]")
        self.write(".mcp.json", json.dumps({"mcpServers": {"knowledge": {
            "command": "python3", "args": ["${SDS_BRAIN_DIR}/mcp/knowledge/server.py"]}}}))

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_complete_fixture_passes(self):
        report = checker.check_repository(self.root)
        self.assertTrue(report["ok"], report["failures"])

    def test_wrong_root_and_partial_package_fail(self):
        self.assertFalse(checker.check_repository(self.root / "templates")["ok"])
        (self.root / "AGENT.md").unlink()
        report = checker.check_repository(self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("AGENT.md" in item for item in report["failures"]))

    def test_missing_mcp_script_is_reported_but_local_config_is_optional(self):
        self.write("config/integration.example.json", json.dumps({"mcpServers": {"objectify": {
            "command": "python3", "args": ["${SDS_BRAIN_DIR}/mcp/objectify/server.py", "--config",
                                          "${SDS_BRAIN_DIR}/mcp/objectify/config.local.json"]}}}))
        self.assertTrue(checker.check_repository(self.root)["ok"])
        self.write(".mcp.json", json.dumps({"mcpServers": {"missing": {
            "command": "python3", "args": ["${SDS_BRAIN_DIR}/mcp/absent/server.py"]}}}))
        report = checker.check_repository(self.root)
        self.assertTrue(any("missing or linked script target" in item for item in report["failures"]))

    def test_root_document_links_and_invalid_json_are_checked(self):
        self.write("README.md", "[Missing](docs/no-such-file.md)\n")
        self.write("config/broken.example.json", "{")
        report = checker.check_repository(self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("README.md:1: broken local link" in item for item in report["failures"]))
        self.assertTrue(any("config/broken.example.json: invalid JSON" in item for item in report["failures"]))

    def test_private_imported_and_local_material_is_excluded(self):
        for name in ("private/client/record.json", "docs/imported/vendor/page.json", "config/mcp.private.local.json",
                     "inbox/draft.json", "drafts/learning.json", "staging/review.json", "Private/other.json",
                     "config/hidden.LOCAL.JSON"):
            self.write(name, "deliberately not valid JSON")
        self.assertTrue(checker.check_repository(self.root)["ok"])

    def test_http_profile_url_is_validated_without_connecting(self):
        self.write("config/knowledge-okp.example.json", json.dumps({"mcpServers": {
            "okp": {"type": "http", "url": "http://127.0.0.1:8000/mcp"}}}))
        self.assertTrue(checker.check_repository(self.root)["ok"])
        for url in ("http://user:secret@127.0.0.1:8000/mcp", "http://[malformed", "http://localhost:invalid/mcp"):
            with self.subTest(url=url):
                self.write("config/knowledge-okp.example.json", json.dumps({"mcpServers": {
                    "okp": {"type": "http", "url": url}}}))
                report = checker.check_repository(self.root)
                self.assertFalse(report["ok"])
                self.assertTrue(any("credential-free URL" in item for item in report["failures"]))

    def test_malformed_transport_is_a_reported_failure(self):
        self.write("config/knowledge-okp.example.json", json.dumps({"mcpServers": {
            "okp": {"type": [], "url": "http://localhost/mcp"}}}))
        report = checker.check_repository(self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("transport must be a string" in item for item in report["failures"]))

    def test_manifest_hashes_are_explicit_and_detect_tampering(self):
        digest = hashlib.sha256((self.root / "AGENT.md").read_bytes()).hexdigest()
        self.write("MANIFEST.sha256", digest + "  AGENT.md\n")
        self.assertTrue(checker.check_repository(self.root, manifest=True)["ok"])
        self.write("AGENT.md", "Changed after packaging\n")
        self.assertTrue(checker.check_repository(self.root)["ok"])
        report = checker.check_repository(self.root, manifest=True)
        self.assertFalse(report["ok"])
        self.assertIn("MANIFEST.sha256: hash mismatch AGENT.md", report["failures"])

    def test_manifest_rejects_outside_paths_before_reading(self):
        self.write("MANIFEST.sha256", "0" * 64 + "  ../outside.txt\n")
        report = checker.check_repository(self.root, manifest=True)
        self.assertFalse(report["ok"])
        self.assertTrue(any("unsafe path" in item for item in report["failures"]))

    def test_cli_reports_partial_package_with_failure_exit(self):
        result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/check_repository.py"),
                                 "--root", str(self.root / "templates")],
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(result.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()

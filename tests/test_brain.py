"""Retrieval, context isolation, import, and stdio checks using temporary fixtures."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from link_support import create_hardlink_or_skip, create_symlink_or_skip

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib import brain as core


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


knowledge = module("sds_test_knowledge", "mcp/knowledge/server.py")
imports = module("sds_test_imports", "scripts/import_docs.py")
cli = module("sds_test_brain_cli", "scripts/brain.py")


def source(identifier="ceph-fixture", **changes):
    result = {"id": identifier, "title": "Synthetic official source " + identifier,
              "url": "https://docs.example.invalid/" + identifier,
              "vendor": "Red Hat", "product": "Ceph", "versions": ["8.1"],
              "topics": ["storage"], "access": "public", "verification": "opened",
              "checked_on": "2026-01-01", "notes": "Test fixture; no network lookup."}
    result.update(changes)
    return result


def page(title, body, **extra):
    meta = {"id": "fixture-page", "title": title, "area": "ceph", "type": "knowledge",
            "applies_to": ["8.1"], "confidence": "documented", "last_verified": "2026-01-01",
            "sources": ["ceph-fixture"]}
    meta.update(extra)
    return "---\n" + "\n".join(key + ": " + json.dumps(value) for key, value in meta.items()) + "\n---\n\n# " + title + "\n\n" + body + "\n"


class BrainTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.root = self.workspace / "repo"
        for folder in ("knowledge/ceph", "runbooks/ceph", "docs", "sources"):
            (self.root / folder).mkdir(parents=True)
        self.records = [source(), source("s3-fixture", vendor="AWS", product="S3", versions=["service"]),
                        source("grid-fixture", vendor="NetApp", product="StorageGRID", versions=["11.9"]),
                        source("rhel-fixture", product="RHEL", versions=["9.6"])]
        self.catalog()
        self.write("runbooks/ceph/slow-ops.md", page("Ceph slow operations triage",
                   "Slow ops can be investigated with bounded health evidence and OSD latency observations. Compare recovery and client latency.", type="runbook"))
        self.write("knowledge/ceph/other.md", page("Firmware inventory", "Gather HPE hardware model and firmware version before choosing an upgrade.", area="hardware", applies_to=["Gen10"]))

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def catalog(self):
        (self.root / "sources/fixture.json").write_text(json.dumps(self.records))

    def private(self, customer="customer-a", cluster="cluster-a", marker="tenant-a-only"):
        relative = "private/%s/%s/knowledge/incident.md" % (customer, cluster)
        self.write(relative, page("Private tenant note", marker, customer=customer, cluster=cluster))
        return relative

    def test_retrieval_ranks_relevant_runbook(self):
        brain = core.Brain(self.root)
        results = brain.search("Ceph slow ops latency", limit=3)
        self.assertTrue(results)
        self.assertEqual(results[0]["id"], "runbooks/ceph/slow-ops.md")
        self.assertEqual(results[0]["scope"], "shared")
        self.assertIn("Slow ops", results[0]["excerpt"])

    def test_compound_terms_match(self):
        self.write("knowledge/ceph/health.md", page("Ceph warning", "The SLOW_OPS warning needs investigation."))
        results = core.Brain(self.root).search("slow ops", area="ceph", limit=10)
        self.assertIn("knowledge/ceph/health.md", {r["id"] for r in results})

    def test_area_and_version_filter_results(self):
        brain = core.Brain(self.root)
        self.assertEqual(brain.search("firmware", area="ceph"), [])
        self.assertTrue(brain.search("firmware", area="hardware", version="Gen10"))
        self.assertEqual(brain.search("firmware", version="8.1"), [])

    def test_query_and_result_limits_are_enforced(self):
        brain = core.Brain(self.root)
        for query in ("", "  ", "x" * 1001, None):
            with self.subTest(query=str(query)[:20]):
                with self.assertRaises(ValueError):
                    brain.search(query)
        for limit in (0, -1, 21, True, 1.5):
            with self.subTest(limit=limit):
                with self.assertRaises(ValueError):
                    brain.search("Ceph", limit=limit)

    def test_read_is_bounded_and_paginates(self):
        brain = core.Brain(self.root)
        first = brain.read("runbooks/ceph/slow-ops.md", max_chars=20)
        self.assertEqual(len(first["text"]), 20)
        self.assertEqual(first["next_offset"], 20)
        second = brain.read(first["id"], offset=20, max_chars=20)
        complete = brain.read(first["id"])
        self.assertEqual(first["text"] + second["text"], complete["text"][:40])
        self.assertTrue(first["reference_material"])

    def test_read_rejects_arbitrary_files_and_traversal(self):
        outside = self.workspace / "outside.txt"
        outside.write_text("must-not-read")
        brain = core.Brain(self.root)
        for identifier in (str(outside), "../outside.txt", "../../etc/passwd", "private/customer-b/cluster-b/knowledge/incident.md"):
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValueError):
                    brain.read(identifier)

    def test_read_limits_reject_booleans_and_invalid_ranges(self):
        brain = core.Brain(self.root)
        for options in ({"offset": -1}, {"offset": True}, {"max_chars": 0}, {"max_chars": 24001}, {"max_chars": False}):
            with self.subTest(options=options):
                with self.assertRaises(ValueError):
                    brain.read("runbooks/ceph/slow-ops.md", **options)

    def test_source_pagination_and_filters(self):
        brain = core.Brain(self.root)
        first = knowledge.call(brain, "brain_sources", {"limit": 2})
        second = knowledge.call(brain, "brain_sources", {"limit": 2, "offset": first["next_offset"]})
        self.assertEqual(first["total"], 4)
        self.assertEqual(len(first["sources"]), 2)
        self.assertIsNone(second["next_offset"])
        self.assertEqual({s["id"] for s in first["sources"] + second["sources"]}, {s["id"] for s in self.records})
        filtered = knowledge.call(brain, "brain_sources", {"vendor": "red hat", "product": "RHEL"})
        self.assertEqual([s["id"] for s in filtered["sources"]], ["rhel-fixture"])
        self.assertEqual(first["content_status"], "reference_only")

    def test_invalid_source_pagination_is_rejected(self):
        brain = core.Brain(self.root)
        for arguments in ({"offset": -1}, {"limit": 31}, {"limit": True}, {"offset": "1"}):
            with self.assertRaises(ValueError):
                knowledge.call(brain, "brain_sources", arguments)

    def test_shared_server_cannot_search_or_read_private_documents(self):
        private_id = self.private()
        brain = core.Brain(self.root)
        self.assertEqual(brain.search("tenant-a-only"), [])
        with self.assertRaises(ValueError):
            brain.read(private_id)
        with self.assertRaises(ValueError):
            knowledge.call(brain, "brain_status", {"customer": "customer-a", "cluster": "cluster-a"})

    def test_private_server_indexes_exact_customer_and_cluster_only(self):
        own = self.private()
        other_cluster = self.private("customer-a", "cluster-b", "clusterbuniquemarker")
        other_customer = self.private("customer-b", "cluster-a", "customerbuniquemarker")
        brain = core.Brain(self.root, "customer-a", "cluster-a")
        self.assertEqual(brain.status()["private_documents"], 1)
        self.assertEqual(brain.search("tenant-a-only")[0]["id"], own)
        for inaccessible in (other_cluster, other_customer):
            with self.assertRaises(ValueError):
                brain.read(inaccessible)
        self.assertEqual(brain.search("customerbuniquemarker"), [])

    def test_private_tool_calls_require_matching_context(self):
        self.private()
        brain = core.Brain(self.root, "customer-a", "cluster-a")
        valid = {"customer": "customer-a", "cluster": "cluster-a"}
        self.assertEqual(knowledge.call(brain, "brain_status", valid)["private_documents"], 1)
        for arguments in ({}, {"customer": "customer-a"}, {"customer": "customer-b", "cluster": "cluster-a"},
                          {"customer": "customer-a", "cluster": "cluster-b"}):
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    knowledge.call(brain, "brain_status", arguments)

    def test_scope_aliases_reject_traversal_and_partial_bindings(self):
        for customer, cluster in (("../customer-a", "cluster-a"), ("customer-a", "../../cluster-b"),
                                  ("customer-a", None), (None, "cluster-a")):
            with self.assertRaises(ValueError):
                core.Brain(self.root, customer, cluster)

    def test_empty_scope_arguments_cannot_silently_select_shared_mode(self):
        for customer, cluster in (("", ""), ("", None), (None, ""),
                                  ("customer-a", ""), ("", "cluster-a")):
            with self.subTest(customer=customer, cluster=cluster):
                with self.assertRaises(ValueError):
                    core.Brain(self.root, customer, cluster)
        self.assertIsNone(core.Brain(self.root).status()["customer"])

    def test_private_stdio_startup_rejects_empty_scope_from_environment(self):
        result = subprocess.run([sys.executable, str(ROOT / "mcp/knowledge/server.py"),
                                 "--root", str(self.root), "--customer", "", "--cluster", "", "--check"],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Invalid context identifier", result.stderr)

    def test_private_frontmatter_scope_must_match(self):
        private_id = self.private()
        self.write(private_id, page("Wrong scope", "private detail", customer="customer-b", cluster="cluster-a"))
        with self.assertRaises(ValueError):
            core.Brain(self.root, "customer-a", "cluster-a")

    def test_customer_specific_frontmatter_cannot_be_shared(self):
        self.write("knowledge/ceph/leak.md", page("Private detail", "not for shared retrieval", customer="customer-a", cluster="cluster-a"))
        with self.assertRaises(ValueError):
            core.Brain(self.root)

    def test_empty_customer_markers_are_not_treated_as_shared_metadata(self):
        for markers in ({"customer": ""}, {"cluster": ""},
                        {"customer": [], "cluster": []}, {"customer": "", "cluster": ""}):
            with self.subTest(markers=markers):
                self.write("knowledge/ceph/unbound.md", page("Unbound private detail", "private content", **markers))
                with self.assertRaisesRegex(ValueError, "belong under private"):
                    core.Brain(self.root)

    def test_symlinked_private_customer_parent_is_rejected(self):
        outside = self.workspace / "outside-customer"
        (outside / "cluster-a/knowledge").mkdir(parents=True)
        (outside / "cluster-a/knowledge/secret.md").write_text(page("Private", "secret", customer="customer-a", cluster="cluster-a"))
        (self.root / "private").mkdir()
        create_symlink_or_skip(self, self.root / "private/customer-a", outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            core.Brain(self.root, "customer-a", "cluster-a")

    def test_symlinked_document_is_rejected(self):
        outside = self.workspace / "external.md"
        outside.write_text("not in repository")
        create_symlink_or_skip(self, self.root / "knowledge/ceph/link.md", outside)
        with self.assertRaises(ValueError):
            core.Brain(self.root)

    def test_symlinked_sources_parent_is_rejected(self):
        shutil.rmtree(self.root / "sources")
        outside = self.workspace / "outside-sources"
        outside.mkdir()
        (outside / "secret.json").write_text(json.dumps([source(title="PRIVATE-TENANT-METADATA")]))
        create_symlink_or_skip(self, self.root / "sources", outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            core.Brain(self.root)

    def test_catalog_duplicate_ids_and_invalid_types_are_rejected(self):
        cases = ([source(), source()], [source(id=["invalid"])], [source(title={"not": "a string"})])
        for records in cases:
            with self.subTest(records=records):
                self.records = records
                self.catalog()
                with self.assertRaises(ValueError):
                    core.Brain(self.root)

    def test_document_and_corpus_limits(self):
        self.write("knowledge/ceph/oversize.md", "x" * (core.MAX_FILE_BYTES + 1))
        with self.assertRaises(ValueError):
            core.Brain(self.root)
        (self.root / "knowledge/ceph/oversize.md").unlink()
        with mock.patch.object(core, "MAX_CORPUS_BYTES", 10):
            with self.assertRaises(ValueError):
                core.Brain(self.root)

    def test_metadata_and_title_limits_prevent_unbounded_tool_fields(self):
        bad = self.write("knowledge/ceph/large-meta.md", page("Small title", "short body", review_note="x" * core.MAX_METADATA_BYTES))
        with self.assertRaisesRegex(ValueError, "metadata limit"):
            core.Brain(self.root)
        bad.unlink()
        self.write("knowledge/ceph/large-title.md", page("x" * (core.MAX_TITLE_CHARS + 1), "short body"))
        with self.assertRaisesRegex(ValueError, "title exceeds"):
            core.Brain(self.root)

    def test_source_record_limit_bounds_source_list_results(self):
        self.records[0]["notes"] = "x" * core.MAX_SOURCE_RECORD_BYTES
        self.catalog()
        with self.assertRaisesRegex(ValueError, "Source record exceeds"):
            core.Brain(self.root)

    def test_frontmatter_round_trips_quoted_strings(self):
        original = 'A "quoted" title with a backslash \\ and a newline\nnext line'
        meta, _ = core.frontmatter(page(original, "body"))
        self.assertEqual(meta["title"], original)

    def test_nested_frontmatter_is_refused(self):
        with self.assertRaisesRegex(ValueError, "only strings"):
            core.frontmatter('---\nsources: [["nested"]]\n---\nbody')

    def test_validation_reports_unknown_source_and_future_date(self):
        self.write("knowledge/ceph/bad.md", page("Bad metadata", "content", sources=["missing-source"], last_verified="2999-01-01"))
        report = cli.validate(self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("unknown source" in failure for failure in report["failures"]))

    def test_index_never_contains_private_pages(self):
        self.private()
        cli.index(self.root)
        index = (self.root / "INDEX.md").read_text()
        self.assertIn("slow-ops.md", index)
        self.assertNotIn("private/customer", index)
        self.assertNotIn("tenant-a-only", index)

    def test_safe_files_uses_portable_case_sensitive_order(self):
        self.write("docs/Z-last-on-windows.md", "# Uppercase path\n")
        self.write("docs/a-first-on-windows.md", "# Lowercase path\n")
        paths = [path.relative_to(self.root / "docs").as_posix()
                 for path in core.safe_files(self.root / "docs")]
        self.assertEqual(paths, ["Z-last-on-windows.md", "a-first-on-windows.md"])

    def test_index_check_reports_missing_or_stale_files_without_writing(self):
        report = cli.index(self.root, check=True)
        self.assertFalse(report["ok"])
        self.assertEqual(report["stale_files"], ["INDEX.md", "docs/SOURCES.md"])
        self.assertFalse((self.root / "INDEX.md").exists())
        self.assertFalse((self.root / "docs/SOURCES.md").exists())
        cli.index(self.root)
        original = (self.root / "INDEX.md").read_bytes()
        self.assertNotIn(b"\r\n", original)
        self.assertTrue(cli.index(self.root, check=True)["ok"])
        self.write("knowledge/ceph/new.md", page("New page", "Additional evidence"))
        self.assertEqual(cli.index(self.root, check=True)["stale_files"], ["INDEX.md"])
        self.assertEqual((self.root / "INDEX.md").read_bytes(), original)

    def test_index_check_cli_returns_failure_for_stale_files(self):
        command = [sys.executable, "-B", str(ROOT / "scripts/brain.py"),
                   "--root", str(self.root), "index", "--check"]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(result.stdout)["ok"])
        self.assertFalse((self.root / "INDEX.md").exists())
        cli.index(self.root)
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["ok"])

    def test_catalog_header_uses_recorded_source_check_dates(self):
        self.records[0]["checked_on"] = "2026-02-01"
        self.catalog()
        cli.index(self.root)
        text = (self.root / "docs/SOURCES.md").read_text(encoding="utf-8")
        self.assertIn("Source checks recorded 2026-01-01 through 2026-02-01.", text)
        self.assertNotIn("Checked on 2026-11-09", text)

    def test_index_refuses_symlink_before_overwriting_other_outputs(self):
        outside = self.workspace / "outside-index.md"
        outside.write_text("Outside content must survive")
        create_symlink_or_skip(self, self.root / "INDEX.md", outside)
        (self.root / "docs/SOURCES.md").write_text("Existing catalog must survive")
        with self.assertRaisesRegex(ValueError, "symlink"):
            cli.index(self.root)
        self.assertEqual(outside.read_text(), "Outside content must survive")
        self.assertEqual((self.root / "docs/SOURCES.md").read_text(), "Existing catalog must survive")

    def test_index_replaces_hardlink_without_changing_external_file(self):
        outside = self.workspace / "outside-index.md"
        outside.write_text("Outside content must survive")
        create_hardlink_or_skip(self, self.root / "INDEX.md", outside)
        cli.index(self.root)
        self.assertEqual(outside.read_text(), "Outside content must survive")
        self.assertTrue((self.root / "INDEX.md").read_text().startswith("# SDS Brain index"))

    def test_index_preflights_catalog_before_writing(self):
        (self.root / "INDEX.md").write_text("Existing index must survive")
        self.records.append(copy.deepcopy(self.records[0]))
        self.catalog()
        with self.assertRaises(ValueError):
            cli.index(self.root)
        self.assertEqual((self.root / "INDEX.md").read_text(), "Existing index must survive")

    def session(self, version="2025-11-25"):
        session = knowledge.Session(core.Brain(self.root))
        response = session.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": version, "capabilities": {}, "clientInfo": {"name": "fixture-client", "version": "1"}}})
        session.handle({"jsonrpc": "2.0", "method": "notifications/initialized"})
        return session, response

    def test_mcp_negotiates_only_the_implemented_protocol(self):
        self.assertEqual(knowledge.VERSIONS, ("2025-11-25",))
        for version in ("2025-11-25", "2025-06-18", "2025-03-26", "2026-07-28"):
            with self.subTest(version=version):
                _, response = self.session(version)
                self.assertEqual(response["result"]["protocolVersion"], "2025-11-25")

    def test_mcp_requires_handshake_and_client_identity(self):
        session = knowledge.Session(core.Brain(self.root))
        self.assertIn("error", session.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}))
        response = session.handle({"jsonrpc": "2.0", "id": 2, "method": "initialize", "params": {
            "protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {}}})
        self.assertIn("error", response)

    def test_mcp_probe_malformed_ids_and_unknown_methods(self):
        session, _ = self.session()
        self.assertEqual(session.handle({"jsonrpc": "2.0", "id": 2, "method": "server/discover"})["error"]["code"], -32601)
        for value in (None, True, 3.14):
            self.assertEqual(session.handle({"jsonrpc": "2.0", "id": value, "method": "ping"})["error"]["code"], -32600)
        self.assertEqual(session.handle({"jsonrpc": "2.0", "id": 3, "method": "unknown"})["error"]["code"], -32601)

    def test_mcp_malformed_envelopes_preserve_readable_request_ids(self):
        session, _ = self.session()
        for message in ({"jsonrpc": "1.0", "id": 0, "method": "ping"},
                        {"jsonrpc": "2.0", "id": "known-request", "method": 42},
                        {"id": 7, "method": "ping"}):
            with self.subTest(message=message):
                response = session.handle(message)
                self.assertEqual(response["id"], message["id"])
                self.assertEqual(response["error"]["code"], -32600)

    def test_mcp_unknown_error_ids_are_omitted_instead_of_null(self):
        session, _ = self.session()
        for message in (None, [], {}, {"jsonrpc": "2.0", "id": None, "method": "ping"},
                        {"jsonrpc": "2.0", "id": True, "method": "ping"},
                        {"jsonrpc": "2.0", "id": 3.14, "method": "ping"}):
            with self.subTest(message=message):
                response = session.handle(message)
                self.assertNotIn("id", response)
                self.assertEqual(response["error"]["code"], -32600)

    def test_stdio_parse_error_omits_unknown_id_and_recovers(self):
        valid = json.dumps({"jsonrpc": "2.0", "id": "after-error", "method": "ping"})
        process = subprocess.run([sys.executable, str(ROOT / "mcp/knowledge/server.py"), "--root", str(self.root)],
                                 input="{\n" + valid + "\n", capture_output=True, text=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stderr)
        responses = [json.loads(line) for line in process.stdout.splitlines()]
        self.assertEqual(responses[0]["error"]["code"], -32700)
        self.assertNotIn("id", responses[0])
        self.assertEqual(responses[1]["id"], "after-error")

    def test_mcp_tool_schema_validation(self):
        brain = core.Brain(self.root)
        for arguments in ({"query": "ceph", "url": "https://unapproved.invalid"}, {"query": 42}, {"query": "ceph", "limit": True}):
            with self.assertRaises(ValueError):
                knowledge.call(brain, "brain_search", arguments)

    def test_mcp_tool_list_accepts_standard_metadata(self):
        session, _ = self.session()
        response = session.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list",
                                   "params": {"_meta": {"progressToken": "listing-2"}}})
        self.assertEqual(len(response["result"]["tools"]), 4)
        for params in ({"_meta": []}, {"cursor": "not-issued"}):
            result = session.handle({"jsonrpc": "2.0", "id": 3, "method": "tools/list", "params": params})
            self.assertEqual(result["error"]["code"], -32602)

    def test_mcp_tool_result_has_final_byte_limit(self):
        session, _ = self.session()
        with mock.patch.object(session.brain, "status", return_value={"oversized": "x" * knowledge.MAX_TOOL_RESULT_BYTES}):
            response = session.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                                       "params": {"name": "brain_status", "arguments": {}}})
        self.assertTrue(response["result"]["isError"])
        self.assertLess(len(json.dumps(response)), 1000)

    def test_stdio_surrogate_request_id_does_not_crash_server(self):
        messages = [
            {"jsonrpc": "2.0", "id": "\ud800", "method": "ping"},
            {"jsonrpc": "2.0", "id": 2, "method": "ping"},
        ]
        process = subprocess.run([sys.executable, str(ROOT / "mcp/knowledge/server.py"), "--root", str(self.root)],
                                 input="".join(json.dumps(item) + "\n" for item in messages), capture_output=True, text=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stderr)
        results = [json.loads(line) for line in process.stdout.splitlines()]
        self.assertEqual(results[0]["id"], "\ud800")
        self.assertEqual(results[1]["id"], 2)

    def test_stdio_process_is_protocol_only(self):
        messages = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "fixture", "version": "1"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "brain_search", "arguments": {"query": "slow ops"}}},
        ]
        process = subprocess.run([sys.executable, str(ROOT / "mcp/knowledge/server.py"), "--root", str(self.root)],
                                 input="".join(json.dumps(item) + "\n" for item in messages), capture_output=True, text=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stderr)
        results = [json.loads(line) for line in process.stdout.splitlines()]
        self.assertEqual(len(results), 2)
        self.assertFalse(results[1]["result"]["isError"])
        self.assertIn("slow-ops.md", results[1]["result"]["content"][0]["text"])

    def test_stdio_rejects_oversized_message(self):
        process = subprocess.run([sys.executable, str(ROOT / "mcp/knowledge/server.py"), "--root", str(self.root)],
                                 input=b"x" * (knowledge.MAX_LINE + 2) + b"\n", capture_output=True, timeout=5)
        self.assertEqual(process.returncode, 2)
        self.assertIn("error", json.loads(process.stdout))


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.root = self.workspace / "repo"
        (self.root / "sources").mkdir(parents=True)
        (self.root / "sources/fixture.json").write_text(json.dumps([source()]))
        self.input = self.workspace / "export.txt"
        self.input.write_text("Reviewed reference content.")
        self.args = argparse.Namespace(root=self.root, input=self.input, source_id="ceph-fixture", scope="shared",
                                       customer=None, cluster=None, product="ceph", version="8.1", reviewed=True)

    def output_files(self):
        return list(self.root.rglob("*.md"))

    def test_no_import_without_explicit_review(self):
        self.args.reviewed = False
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        self.assertEqual(self.output_files(), [])

    def test_subscription_source_still_requires_entitlement_review(self):
        (self.root / "sources/fixture.json").write_text(json.dumps([source(access="subscription")]))
        self.args.reviewed = False
        with self.assertRaises(ValueError):
            imports.perform(self.args)

    def test_shared_import_requires_known_source_and_no_private_context(self):
        self.args.source_id = "unknown-source"
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        self.args.source_id = "ceph-fixture"
        self.args.customer = "customer-a"
        self.args.cluster = "cluster-a"
        with self.assertRaises(ValueError):
            imports.perform(self.args)

    def test_private_import_requires_both_safe_context_identifiers(self):
        self.args.scope = "private"
        self.args.customer = "customer-a"
        for cluster in (None, "../cluster-b"):
            self.args.cluster = cluster
            with self.assertRaises(ValueError):
                imports.perform(self.args)

    def test_private_import_is_inaccessible_from_shared_server(self):
        self.args.scope = "private"
        self.args.customer = "customer-a"
        self.args.cluster = "cluster-a"
        self.args.source_id = "internal-confluence"
        result = imports.perform(self.args)
        self.assertEqual(result["scope"], "private")
        self.assertEqual(core.Brain(self.root).search("Reviewed reference"), [])
        private = core.Brain(self.root, "customer-a", "cluster-a")
        self.assertEqual(private.status()["private_documents"], 1)
        self.assertEqual(private.search("Reviewed reference")[0]["scope"], "private")

    def test_html_extraction_removes_script_and_style(self):
        text = imports.html_text("<h1>Ceph</h1><p>A &amp; B</p><script>do_not_import()</script><style>.secret{}</style><p>Next</p>")
        self.assertIn("A & B", text)
        self.assertIn("Next", text)
        self.assertNotIn("do_not_import", text)
        self.assertNotIn(".secret", text)

    def test_confluence_cdata_preserves_code_and_literal_characters(self):
        code = "ceph -s\nceph health detail\nprintf '%s' '<tag>&amp;'"
        raw = '<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">bash</ac:parameter><ac:plain-text-body><![CDATA[' + code + ']]></ac:plain-text-body></ac:structured-macro>'
        self.assertIn(code, imports.html_text(raw))
        self.assertNotIn("must-not-import", imports.html_text('<script><![CDATA[must-not-import]]></script><p>Visible</p>'))

    def test_html_table_cells_remain_separated(self):
        raw = '<table><tr><th>Cluster</th><th>Version</th></tr><tr><td>a</td><td>8.1</td></tr></table>'
        text = imports.html_text(raw)
        self.assertIn("Cluster\tVersion", text)
        self.assertIn("a\t8.1", text)

    def test_confluence_storage_and_view_extraction(self):
        self.input = self.workspace / "confluence.json"
        self.input.write_text(json.dumps({"results": [
            {"id": "101", "title": "Storage note", "version": {"number": 3}, "body": {"storage": {"value": "<p>Capacity evidence</p>"}}},
            {"id": "102", "title": "View note", "body": {"view": {"value": "<p>Read only</p>"}}},
        ]}))
        pages = imports.extract(self.input)
        self.assertEqual(len(pages), 2)
        self.assertEqual(pages[0][0], "Storage note")
        self.assertEqual(pages[0][1], "Capacity evidence")
        self.assertEqual(pages[0][2]["page_version"], 3)

    def test_adf_and_dashboard_json_are_not_mistaken_for_confluence(self):
        for document in ({"body": {"atlas_doc_format": {"value": "{}"}}}, {"panels": [], "title": "Grafana"}):
            path = self.workspace / "unsupported.json"
            path.write_text(json.dumps(document))
            with self.assertRaises(ValueError):
                imports.extract(path)

    def test_invalid_confluence_nested_shapes_are_cleanly_refused(self):
        for document in ({"body": None}, {"body": "unexpected"},
                         {"body": {"storage": {"value": "<p>Content</p>"}}, "version": None}):
            path = self.workspace / "unsupported.json"
            path.write_text(json.dumps(document))
            with self.assertRaises(ValueError):
                imports.extract(path)

    def test_secrets_are_rejected_before_any_output(self):
        for body in ("AKIAABCDEFGHIJKLMNOP", "-----BEGIN PRIVATE KEY-----", "Authorization: Bearer abcdefghijklmnop"):
            self.input.write_text(body)
            with self.assertRaises(ValueError):
                imports.perform(self.args)
            self.assertEqual(self.output_files(), [])

    def test_secret_in_confluence_title_is_also_rejected(self):
        path = self.workspace / "confluence.json"
        path.write_text(json.dumps({"id": "1", "title": "AKIAABCDEFGHIJKLMNOP", "body": {"storage": {"value": "<p>Otherwise harmless content.</p>"}}}))
        self.args.input = path
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        self.assertEqual(self.output_files(), [])

    def test_input_symlink_is_rejected(self):
        link = self.workspace / "link.txt"
        create_symlink_or_skip(self, link, self.input)
        self.args.input = link
        with self.assertRaises(ValueError):
            imports.perform(self.args)

    def test_input_with_symlinked_ancestor_is_rejected(self):
        actual = self.workspace / "actual"
        actual.mkdir()
        (actual / "export.txt").write_text("External content through an ancestor link.")
        link = self.workspace / "linked-parent"
        create_symlink_or_skip(self, link, actual, target_is_directory=True)
        self.args.input = link / "export.txt"
        with self.assertRaises(ValueError):
            imports.perform(self.args)

    def test_output_symlinked_parent_is_rejected(self):
        outside = self.workspace / "outside"
        outside.mkdir()
        create_symlink_or_skip(self, self.root / "docs", outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        self.assertEqual(list(outside.rglob("*.md")), [])

    def test_broken_output_symlink_cannot_write_outside_repository(self):
        digest = hashlib.sha256(self.input.read_bytes()).hexdigest()[:12]
        target = self.root / "docs/imported/ceph-fixture"
        target.mkdir(parents=True)
        outside = self.workspace / "must-not-be-created.md"
        create_symlink_or_skip(self, target / ("export-" + digest + "-0.md"), outside)
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        self.assertFalse(outside.exists())

    def test_conflicting_destination_is_detected_before_any_write(self):
        inputs = self.workspace / "inputs"
        inputs.mkdir()
        (inputs / "a.txt").write_text("First staged document")
        (inputs / "b.txt").write_text("Second staged document")
        self.args.input = inputs
        target = self.root / "docs/imported/ceph-fixture"
        target.mkdir(parents=True)
        digest_b = hashlib.sha256((inputs / "b.txt").read_bytes()).hexdigest()[:12]
        (target / ("b-" + digest_b + "-0.md")).write_text("Conflicting existing document")
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        self.assertEqual(len(list(target.glob("*.md"))), 1)

    def test_import_records_digest_scope_and_version(self):
        result = imports.perform(self.args)
        self.assertEqual(result["imported"], 1)
        document = self.output_files()[0]
        meta, body = core.frontmatter(document.read_text())
        self.assertEqual(meta["source_sha256"], hashlib.sha256(self.input.read_bytes()).hexdigest())
        self.assertEqual(meta["applies_to"], ["8.1"])
        self.assertEqual(meta["source_kind"], "operator-reviewed-export")
        self.assertIn("untrusted source content", body)

    def test_oversized_input_and_unsupported_files_are_refused(self):
        self.input.write_bytes(b"x" * (imports.MAX_INPUT_BYTES + 1))
        with self.assertRaises(ValueError):
            imports.perform(self.args)
        unsupported = self.workspace / "manual.pdf"
        unsupported.write_bytes(b"not a real PDF")
        self.args.input = unsupported
        with self.assertRaises(ValueError):
            imports.perform(self.args)

    def test_rendered_document_limit_is_checked_before_writing(self):
        self.input.write_bytes(b"x" * (imports.MAX_INPUT_BYTES - 10))
        with self.assertRaisesRegex(ValueError, "Rendered document exceeds"):
            imports.perform(self.args)
        self.assertEqual(self.output_files(), [])

    def test_import_batch_limit_is_checked_before_writing(self):
        folder = self.workspace / "batch"
        folder.mkdir()
        (folder / "a.txt").write_text("a" * 1500)
        (folder / "b.txt").write_text("b" * 1500)
        self.args.input = folder
        with mock.patch.object(imports, "MAX_IMPORT_BYTES", 3500):
            with self.assertRaisesRegex(ValueError, "Rendered import exceeds"):
                imports.perform(self.args)
        self.assertEqual(self.output_files(), [])

    def test_import_document_count_is_checked_before_writing(self):
        path = self.workspace / "pages.json"
        path.write_text(json.dumps({"results": [
            {"title": "one", "body": {"storage": {"value": "<p>One</p>"}}},
            {"title": "two", "body": {"storage": {"value": "<p>Two</p>"}}},
        ]}))
        self.args.input = path
        with mock.patch.object(imports, "MAX_IMPORT_DOCUMENTS", 1):
            with self.assertRaisesRegex(ValueError, "Too many documents"):
                imports.perform(self.args)
        self.assertEqual(self.output_files(), [])

    def test_import_uses_the_exact_bytes_that_were_hashed(self):
        raw = self.input.read_bytes()
        extract = imports.extract
        def changed_file(path, *args):
            path.write_text("Export changed after hashing")
            return extract(path, *args)
        with mock.patch.object(imports, "extract", side_effect=changed_file):
            imports.perform(self.args)
        meta, body = core.frontmatter(self.output_files()[0].read_text())
        self.assertEqual(meta["source_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertIn(raw.decode(), body)
        self.assertNotIn("Export changed after hashing", body)


if __name__ == "__main__":
    unittest.main()

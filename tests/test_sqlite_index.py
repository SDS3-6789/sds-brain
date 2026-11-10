"""SQLite snapshot round trips, shared boundaries, freshness and failure recovery."""
from contextlib import closing
import hashlib
import io
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib import sqlite_index as index


def source(identifier):
    return {"id": identifier, "title": identifier + " source reference", "url": "https://docs.example.invalid/" + identifier,
            "vendor": "Synthetic", "product": "Fixture", "versions": ["8.1"], "topics": ["storage"],
            "access": "public", "verification": "opened", "checked_on": "2026-11-10", "notes": "Offline test fixture"}


class SQLiteIndexTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.db = self.root / index.DEFAULT_DATABASE
        self.body = "# Recovery guide\n\nCeph slow_ops recovery quorum. Café שלום 存储.\n" + "Unicode recovery é שלום.\n" * 1600
        self.content = ('---\r\nid: recovery\r\ntitle: Recovery guide\r\narea: ceph\r\n'
                        'applies_to: [rhcs-8.1]\r\nsources: [available]\r\n---\r\n' + self.body.replace("\n", "\r\n"))
        self.put("sources/fixture.json", json.dumps([source("available"), source("unavailable")]))
        self.put("knowledge/ceph/recovery.md", self.content)
        self.put("knowledge/vendor/catalog/available.md", "---\ntitle: Saved vendor text\nsources: [available]\n---\n\nVendorbody saved locally.")
        self.raw = b"<html><body>Rawvendorunique exact original</body></html>"
        self.put("vendor-sources/catalog/available/original.html", self.raw)
        self.put("vendor-sources/netapp/source/original.adoc", "Original AsciiDoc bytes")
        self.put("plugins/team-brain/skills/search/SKILL.md", "---\nname: search\ndescription: |\n  Rich frontmatter\n---\n# Plugin guide\nPluginuniqueword instructions")
        self.put("config/example.json", '{"query": "configuniqueword"}')
        self.put("scripts/helper.py", 'print("codeuniqueword")\n')
        self.put("docs/OFFLINE_KNOWLEDGE_REPORT.json", json.dumps({"sources": [
            {"source_id": "available", "status": "body_available"},
            {"source_id": "unavailable", "status": "unavailable"}], "documents": [
                {"raw_file": "vendor-sources/catalog/available/original.html", "indexed_file": "knowledge/vendor/catalog/available.md"}]}))
        self.put("docs/manual.pdf", b"%PDF-1.7\nFixture original PDF bytes\n%%EOF")
        buffer = io.BytesIO()
        with ZipFile(buffer, "w") as archive:
            archive.writestr("word/document.xml", '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Word manual title</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Worduniqueword table text שלום</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>')
        self.word = buffer.getvalue()
        self.put("docs/manual.docx", self.word)

    def put(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value if isinstance(value, bytes) else value.encode("utf-8"))
        return path

    def build(self):
        return index.build_database(self.root)

    def test_full_unicode_round_trip_word_and_original_assets(self):
        report = self.build()
        self.assertEqual(report["scope"], "shared")
        self.assertEqual(report["catalog_references"], 2)
        self.assertEqual(report["sources_by_capture_status"], {"body_available": 1, "unavailable": 1})
        with closing(index.open_readonly(self.db)) as connection:
            row = connection.execute("SELECT body,content,metadata_json FROM documents WHERE path=?", ("knowledge/ceph/recovery.md",)).fetchone()
            self.assertEqual(row["body"].lstrip("\n"), self.body)
            self.assertEqual(row["content"], self.content)
            self.assertEqual(json.loads(row["metadata_json"])["area"], "ceph")
            asset = connection.execute("SELECT content,linked_document_path FROM assets WHERE path=?", ("vendor-sources/catalog/available/original.html",)).fetchone()
            self.assertEqual(asset["content"], self.raw)
            self.assertEqual(asset["linked_document_path"], "knowledge/vendor/catalog/available.md")
            self.assertEqual(connection.execute("SELECT content FROM assets WHERE path='docs/manual.docx'").fetchone()[0], self.word)
            self.assertIsNone(connection.execute("SELECT path FROM documents WHERE path LIKE 'vendor-sources/%'").fetchone())
            self.assertIsNone(connection.execute("SELECT path FROM documents WHERE path='docs/manual.pdf'").fetchone())
        word = index.search(self.db, "Worduniqueword")["results"]
        self.assertEqual(word[0]["title"], "Word manual title")
        self.assertIn("שלום", index.read(self.db, "docs/manual.docx")["text"])
        chunks, offset = [], 0
        while True:
            page = index.read(self.db, "knowledge/ceph/recovery.md", offset, 777, full_source=True)
            chunks.append(page["text"])
            if page["next_offset"] is None:
                break
            offset = page["next_offset"]
        self.assertEqual("".join(chunks), self.content)
        self.assertTrue(index.check(self.db, self.root)["ok"])

    def test_default_search_kinds_provenance_filters_and_plain_queries(self):
        self.build()
        result = index.search(self.db, "slow_ops", area="ceph", version="rhcs-8.1", source_id="available")
        self.assertEqual([row["path"] for row in result["results"]], ["knowledge/ceph/recovery.md"])
        self.assertEqual(result["results"][0]["sources"], ["available"])
        self.assertEqual(index.search(self.db, "Rawvendorunique")["results"], [])
        self.assertEqual(index.search(self.db, "configuniqueword")["results"], [])
        self.assertEqual(index.search(self.db, "configuniqueword", kind="config")["results"][0]["path"], "config/example.json")
        self.assertEqual(index.search(self.db, "codeuniqueword", kind="code")["results"][0]["path"], "scripts/helper.py")
        self.assertTrue(index.search(self.db, "Pluginuniqueword")["results"])
        self.assertTrue(index.search(self.db, "Café")["results"])
        self.assertTrue(index.search(self.db, 'recovery" OR * NEAR(:) --')["results"])
        self.assertFalse(index.search(self.db, "quorum", source_id="' OR 1=1 --")["results"])
        self.assertFalse(index.search(self.db, "quorum", version="%_")["results"])
        self.assertTrue(index.search(self.db, "recovery quorum", mode="phrase")["results"])
        for query, options in [("---", {}), ("x " * 65, {}), ("x", {"limit": 0}), ("x", {"limit": 51})]:
            with self.assertRaises(ValueError):
                index.search(self.db, query, **options)
        with self.assertRaises(ValueError):
            index.read(self.db, "knowledge/ceph/recovery.md", max_chars=24001)

    def test_private_unreviewed_local_runtime_and_self_outputs_excluded(self):
        ignored = ["Private/customer/secret.md", "WORK/draft.md", "inbox/unreviewed.md", "drafts/unreviewed.md",
                   "staging/pending.txt", "docs/imported/secret.md", "config/context.LOCAL.JSON", "config/name.local.toml",
                   "config/.ENV.production", "deploy/podman/rhokp.env", "keys/server.key", "vendor/runtime.zip",
                   "data/arbitrary.md", "MANIFEST.sha256", "docs/SQLITE_BUILD_REPORT.json", "docs/SQLITE_INDEX_REPORT.json"]
        for path in ignored:
            self.put(path, "Secretexcludeduniqueword")
        self.build()
        self.assertFalse(index.search(self.db, "Secretexcludeduniqueword", kind="all")["results"])
        with closing(index.open_readonly(self.db)) as connection:
            paths = {row[0] for row in connection.execute("SELECT path FROM inputs")}
        self.assertFalse(paths.intersection(ignored))
        old = index.corpus_fingerprint(self.root)
        self.put("docs/SQLITE_BUILD_REPORT.json", "new derived report")
        self.put("data/unrelated.db-wal", b"temporary")
        self.assertEqual(old, index.corpus_fingerprint(self.root))

    def test_rebuild_removes_stale_documents_and_preserves_originals(self):
        original = (self.root / "knowledge/ceph/recovery.md").read_bytes()
        self.build()
        obsolete = self.root / "knowledge/vendor/catalog/available.md"
        obsolete.unlink()
        self.assertFalse(index.check(self.db, self.root)["fresh"])
        self.build()
        with self.assertRaises(ValueError):
            index.read(self.db, "knowledge/vendor/catalog/available.md")
        self.assertFalse(index.search(self.db, "Vendorbody")["results"])
        self.assertEqual((self.root / "knowledge/ceph/recovery.md").read_bytes(), original)
        self.assertTrue(index.check(self.db, self.root)["fresh"])

    def test_failed_build_keeps_completed_database(self):
        self.build()
        before = hashlib.sha256(self.db.read_bytes()).hexdigest()
        self.put("knowledge/private-misplaced.md", "---\ncustomer: confidential\n---\nSecret")
        with self.assertRaisesRegex(ValueError, "Customer-scoped"):
            self.build()
        self.assertEqual(hashlib.sha256(self.db.read_bytes()).hexdigest(), before)
        self.assertFalse(list(self.db.parent.glob(".*.tmp")))
        self.assertTrue(index.search(self.db, "quorum")["results"])

    def test_customer_marker_in_rich_plugin_header_rejected(self):
        for declaration in ["Customer: private", "scope: private", "  'customer': private", 'metadata: {"cluster": "private"}', 'metadata: {"scope": "private"}', 'scope: >\n  private']:
            with self.subTest(declaration=declaration):
                self.put("plugins/team-brain/skills/scoped/SKILL.md", "---\ndescription: |\n  Nested YAML\n" + declaration + "\n---\nSecret")
                with self.assertRaisesRegex(ValueError, "Customer-scoped"):
                    self.build()

    def test_reviewed_incident_template_placeholder_exception_is_exact(self):
        template = '---\nid: replace-with-incident-id\ntitle: Replace with incident title\ncustomer: customer-a\ncluster: cluster-a\n---\n# Incident template\nTemplateuniqueword'
        self.put("templates/incident.md", template)
        self.build()
        self.assertFalse(index.search(self.db, "Templateuniqueword")["results"])
        self.assertEqual(index.search(self.db, "Templateuniqueword", kind="config")["results"][0]["path"], "templates/incident.md")
        result = index.read(self.db, "templates/incident.md", full_source=True)
        self.assertEqual(result["text"], template)
        self.assertEqual(result["metadata"]["template_placeholders"], {"customer": "customer-a", "cluster": "cluster-a"})
        self.assertNotIn("customer", result["metadata"])
        for original, replacement in [("customer-a", "real-customer"), ("replace-with-incident-id", "real-incident")]:
            self.put("templates/incident.md", template.replace(original, replacement))
            with self.assertRaisesRegex(ValueError, "Customer-scoped"):
                self.build()

    def test_readonly_and_hash_checks_detect_tampering(self):
        self.build()
        with closing(index.open_readonly(self.db)) as connection:
            with self.assertRaises(sqlite3.OperationalError):
                connection.execute("DELETE FROM documents")
        with closing(sqlite3.connect(self.db)) as connection:
            connection.execute("UPDATE assets SET content=? WHERE path='docs/manual.pdf'", (b"tampered",))
            connection.execute("UPDATE documents SET body='changed' WHERE path='knowledge/ceph/recovery.md'")
            connection.commit()
        check = index.check(self.db)
        self.assertFalse(check["ok"])
        self.assertTrue(any("body hash mismatch" in item for item in check["failures"]))
        self.assertTrue(any("asset hash mismatch" in item for item in check["failures"]))

    def test_readonly_check_detects_missing_fts_index(self):
        self.build()
        with closing(sqlite3.connect(self.db)) as connection:
            connection.execute("INSERT INTO documents_fts(documents_fts) VALUES('delete-all')")
            connection.commit()
        check = index.check(self.db)
        self.assertFalse(check["ok"])
        self.assertTrue(any("FTS" in item for item in check["failures"]))

    def test_linked_public_inputs_rejected_without_reading_targets(self):
        target = self.put("private/customer/private.md", "Secretprivate")
        link = self.root / "knowledge/linked.md"
        try:
            os.link(target, link)
        except (OSError, NotImplementedError) as error:
            self.skipTest("Hard-link capability is unavailable: " + str(error))
        with self.assertRaisesRegex(ValueError, "Hard-linked"):
            self.build()

    def test_cli_build_status_and_freshness_exit_codes(self):
        command = [sys.executable, "-B", str(ROOT / "scripts/sqlite_brain.py"), "--root", str(self.root)]
        built = subprocess.run(command + ["build"], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(built.stdout)["database"], str(self.db.resolve()))
        checked = subprocess.run(command + ["check", "--fresh"], capture_output=True, text=True)
        self.assertEqual(checked.returncode, 0, checked.stderr)
        self.put("docs/added.md", "Added later")
        checked = subprocess.run(command + ["check", "--fresh"], capture_output=True, text=True)
        self.assertEqual(checked.returncode, 1)
        self.assertFalse(json.loads(checked.stdout)["fresh"])


if __name__ == "__main__":
    unittest.main()

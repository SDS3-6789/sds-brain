"""Status distinguishes catalog metadata from actual local vendor content."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.brain import Brain


class VendorStatusTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "sources").mkdir()
        records = [{"id": identifier, "title": "Synthetic vendor reference",
                    "url": "https://example.com/" + identifier, "vendor": "Example",
                    "product": "Fixture", "versions": ["1"], "topics": ["fixture"],
                    "access": "public", "verification": "opened", "checked_on": "2026-01-01",
                    "notes": "Synthetic catalog metadata; no network access."}
                   for identifier in ("source-a", "source-b")]
        (self.root / "sources/fixture.json").write_text(json.dumps(records), encoding="utf-8")
        self.document("authored", source_kind="operator-reviewed-export")

    def document(self, name, **metadata):
        path = self.root / "knowledge" / (name + ".md")
        path.parent.mkdir(exist_ok=True)
        values = {"id": name, "title": "Fixture " + name, "sources": ["source-a"], **metadata}
        text = "---\n" + "\n".join(key + ": " + json.dumps(value) for key, value in values.items())
        path.write_text(text + "\n---\n\n# Fixture\n\nSynthetic reference body.\n", encoding="utf-8")

    def test_catalog_metadata_and_authored_pages_are_not_vendor_snapshots(self):
        status = Brain(self.root).status()
        self.assertEqual(status["catalog_references"], 2)
        self.assertEqual(status["vendor_snapshot_documents"], 0)
        self.assertEqual(status["vendor_snapshot_sources"], 0)
        self.assertEqual(status["vendor_documentation_repositories"], 0)
        self.assertFalse(status["vendor_manuals_bundled"])

    def test_page_snapshots_count_documents_and_distinct_sources(self):
        self.document("page-a", source_kind="public-vendor-snapshot", snapshot_scope="catalog-target-page")
        self.document("page-b", source_kind="public-vendor-snapshot", sources=["source-a", "source-b"])
        self.document("page-c", source_kind="public-vendor-snapshot", sources=["source-b"])
        status = Brain(self.root).status()
        self.assertEqual(status["vendor_snapshot_documents"], 3)
        self.assertEqual(status["vendor_snapshot_sources"], 2)
        self.assertEqual(status["vendor_documentation_repositories"], 0)
        self.assertFalse(status["vendor_manuals_bundled"])

    def test_pdf_book_counts_as_bundled_manual_without_complete_coverage_claim(self):
        self.document("pdf-book", source_kind="public-vendor-snapshot", snapshot_scope="pdf-book")
        status = Brain(self.root).status()
        self.assertEqual(status["vendor_snapshot_documents"], 1)
        self.assertEqual(status["vendor_snapshot_sources"], 1)
        self.assertTrue(status["vendor_manuals_bundled"])
        self.assertIn("do not establish complete manual or product coverage", status["notice"])

    def test_documentation_repositories_are_distinct_across_indexed_pages(self):
        self.document("repo-a-page-1", source_kind="pinned-vendor-documentation",
                      repository_url="https://example.com/repository-a")
        self.document("repo-a-page-2", source_kind="pinned-vendor-documentation",
                      repository_url="https://example.com/repository-a")
        self.document("repo-b-page", source_kind="pinned-vendor-documentation",
                      repository_url="https://example.com/repository-b", sources=["source-b"])
        status = Brain(self.root).status()
        self.assertEqual(status["vendor_snapshot_documents"], 3)
        self.assertEqual(status["vendor_snapshot_sources"], 2)
        self.assertEqual(status["vendor_documentation_repositories"], 2)
        self.assertTrue(status["vendor_manuals_bundled"])


if __name__ == "__main__":
    unittest.main()

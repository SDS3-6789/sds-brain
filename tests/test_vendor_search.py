"""Search diversity retains document identity and explicit version scopes."""
import collections
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.brain import Brain


class VendorSearchDiversityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def document(self, name, body, title="Alpha beta reference", **metadata):
        path = self.root / "knowledge" / (name + ".md")
        path.parent.mkdir(exist_ok=True)
        values = {"id": name, "title": title, "applies_to": ["generic"], **metadata}
        header = "---\n" + "\n".join(key + ": " + json.dumps(value) for key, value in values.items())
        path.write_text(header + "\n---\n\n" + body, encoding="utf-8")
        return path.relative_to(self.root).as_posix()

    def vendor(self, name, body, version, family="fixture-product", original="admin/capacity.adoc"):
        return self.document(name, body, source_kind="pinned-vendor-documentation",
                             source_family=family, original_path=original, applies_to=[version])

    def test_repeated_chunks_and_editions_do_not_crowd_out_other_documents(self):
        repeated = "\n\n".join("alpha beta " * 260 for _ in range(3))
        authored = self.document("authored", repeated)
        vendor_ids = {self.vendor("vendor-11", repeated, "11"), self.vendor("vendor-12", repeated, "12")}
        independent = self.document("independent", "alpha beta " + "background " * 200,
                                    title="Independent investigation")
        hits = Brain(self.root).search("alpha beta", limit=3)
        self.assertEqual(len({hit["id"] for hit in hits}), 3)
        self.assertIn(authored, [hit["id"] for hit in hits])
        self.assertIn(independent, [hit["id"] for hit in hits])
        self.assertEqual(sum(hit["id"] in vendor_ids for hit in hits), 1)

    def test_requested_version_filters_before_family_diversity(self):
        self.vendor("edition-11", "alpha beta documented behavior", "11")
        wanted = self.vendor("edition-12", "alpha beta different documented behavior", "12")
        hits = Brain(self.root).search("alpha beta", version="12", limit=5)
        self.assertEqual([hit["id"] for hit in hits], [wanted])
        self.assertEqual(hits[0]["metadata"]["applies_to"], ["12"])
        self.assertIn("different documented behavior", hits[0]["excerpt"])

    def test_same_original_path_in_distinct_families_stays_independent(self):
        expected = {self.vendor("product-a", "alpha beta " * 50, "1", family="product-a"),
                    self.vendor("product-b", "alpha beta " * 50, "1", family="product-b")}
        self.document("less-relevant", "alpha beta " + "background " * 200,
                      title="Different evidence")
        hits = Brain(self.root).search("alpha beta", limit=2)
        self.assertEqual({hit["id"] for hit in hits}, expected)

    def test_fallback_retains_editions_and_limits_each_document_to_two_chunks(self):
        repeated = "\n\n".join("alpha beta " * 260 for _ in range(3))
        expected = {self.vendor("edition-11", repeated, "11"), self.vendor("edition-12", repeated, "12")}
        hits = Brain(self.root).search("alpha beta", limit=20)
        self.assertEqual(collections.Counter(hit["id"] for hit in hits), {identifier: 2 for identifier in expected})
        self.assertEqual(len({(hit["id"], hit["chunk"]) for hit in hits}), 4)
        self.assertEqual({tuple(hit["metadata"]["applies_to"]) for hit in hits}, {("11",), ("12",)})

    def test_absent_explicit_family_does_not_infer_equivalence_from_path(self):
        expected = {self.document("source-a", "alpha beta " * 50,
                                  source_kind="pinned-vendor-documentation", original_path="admin/index.adoc"),
                    self.document("source-b", "alpha beta " * 50,
                                  source_kind="pinned-vendor-documentation", original_path="admin/index.adoc")}
        self.document("less-relevant", "alpha beta " + "background " * 200,
                      title="Different evidence")
        hits = Brain(self.root).search("alpha beta", limit=2)
        self.assertEqual({hit["id"] for hit in hits}, expected)


if __name__ == "__main__":
    unittest.main()

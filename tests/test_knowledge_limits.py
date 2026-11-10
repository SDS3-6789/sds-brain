"""Knowledge MCP wire-size regressions, using in-memory catalog fixtures."""
import importlib.util
import json
from pathlib import Path
import unittest

from lib.brain import Brain, MAX_SOURCE_RECORD_BYTES


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sds_knowledge_limits", ROOT / "mcp/knowledge/server.py")
knowledge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(knowledge)


class KnowledgeResultLimitsTests(unittest.TestCase):
    def session(self, notes, count=1):
        brain = Brain.__new__(Brain)
        brain.customer = brain.cluster = None
        brain.sources = [
            {"id": "synthetic-source-" + str(i), "title": "Synthetic reference",
             "url": "https://example.com/reference", "vendor": "Example",
             "product": "Synthetic product", "versions": ["1"], "topics": ["fixture"],
             "access": "public", "verification": "opened", "checked_on": "2026-11-10",
             "notes": notes}
            for i in range(count)
        ]
        for source in brain.sources:
            self.assertLessEqual(len(json.dumps(source, ensure_ascii=True).encode("ascii")),
                                 MAX_SOURCE_RECORD_BYTES)
        session = knowledge.Session(brain)
        session.initialized = session.ready = True
        return session

    def sources(self, session, limit):
        return session.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                               "params": {"name": "brain_sources", "arguments": {"limit": limit}}})["result"]

    def test_escaped_catalog_result_cannot_bypass_final_size_limit(self):
        # Every record satisfies the catalog limit, and the inner text JSON is
        # below 256 KiB. Escaping it into the MCP result nearly doubles it.
        session = self.session("\\" * 3880, count=30)
        data = knowledge.call(session.brain, "brain_sources", {"limit": 30})
        inner = json.dumps(data, ensure_ascii=True)
        self.assertLess(len(inner.encode("ascii")), knowledge.MAX_TOOL_RESULT_BYTES)
        result = self.sources(session, 30)
        self.assertTrue(result["isError"])
        self.assertIn("reduce the requested limit", result["content"][0]["text"])
        self.assertLessEqual(len(json.dumps(result, ensure_ascii=True).encode("ascii")),
                             knowledge.MAX_TOOL_RESULT_BYTES)

    def test_reduced_page_of_same_catalog_succeeds(self):
        session = self.session("\\" * 3880, count=30)
        result = self.sources(session, 10)
        self.assertFalse(result["isError"])
        data = json.loads(result["content"][0]["text"])
        self.assertEqual(len(data["sources"]), 10)
        self.assertEqual(data["next_offset"], 10)
        self.assertEqual(data["sources"][0]["notes"], "\\" * 3880)
        self.assertLessEqual(len(json.dumps(result, ensure_ascii=True).encode("ascii")),
                             knowledge.MAX_TOOL_RESULT_BYTES)

    def test_unicode_and_json_metacharacters_round_trip(self):
        notes = 'A "quoted" path C:\\docs\\RHEL — 日本語\nSecond line'
        result = self.sources(self.session(notes), 1)
        self.assertFalse(result["isError"])
        self.assertEqual(json.loads(result["content"][0]["text"])["sources"][0]["notes"], notes)


if __name__ == "__main__":
    unittest.main()

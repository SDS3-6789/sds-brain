#!/usr/bin/env python3
"""Check that priority questions retrieve their operational procedures."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.brain import Brain


def main():
    brain = Brain(ROOT)
    checks = json.loads((ROOT / "tests" / "golden_queries.json").read_text(encoding="utf-8"))
    results = []
    for check in checks:
        hits = brain.search(check["query"], limit=check["top"])
        results.append({"query": check["query"], "expected": check["expected"],
                        "passed": check["expected"] in [hit["id"] for hit in hits],
                        "retrieved": [hit["id"] for hit in hits]})
    passed = all(r["passed"] for r in results)
    print(json.dumps({"ok": passed, "checks": results}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

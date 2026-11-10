#!/usr/bin/env python3
"""Verify bundled vendor snapshot bytes and offline source-body retrieval."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.brain import Brain


def safe_file(root, name):
    relative = PurePosixPath(name)
    if relative.is_absolute() or ".." in relative.parts or ":" in name or "\\" in name:
        raise ValueError("Invalid snapshot manifest path")
    path = root.joinpath(*relative.parts)
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise ValueError("Snapshot manifest paths must not follow links")
        if parent == root:
            break
    if not path.is_file():
        raise ValueError("Missing snapshot file: " + name)
    return path


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def verify(root, retrieval=True):
    root = root.resolve(strict=True)
    catalog = json.loads((root / "docs/OFFLINE_KNOWLEDGE_REPORT.json").read_text(encoding="utf-8"))
    storagegrid = json.loads((root / "docs/OFFLINE_STORAGEGRID_REPORT.json").read_text(encoding="utf-8"))
    failures, checked = [], 0
    for record in catalog["documents"]:
        for name, expected in ((record["indexed_file"], record["indexed_sha256"]), (record["raw_file"], record["raw_sha256"])):
            if digest(safe_file(root, name)) != expected:
                failures.append("Hash mismatch: " + name)
            checked += 1
    for repository in storagegrid["repositories"]:
        for record in repository["indexed"]:
            if digest(safe_file(root, record["file"])) != record["sha256"]:
                failures.append("Hash mismatch: " + record["file"])
            raw_name = repository["raw_directory"] + "/source/" + record["source_path"]
            if digest(safe_file(root, raw_name)) != record["source_sha256"]:
                failures.append("Hash mismatch: " + raw_name)
            checked += 2
    results = []
    if retrieval:
        brain = Brain(root)
        cases = json.loads((root / "tests/offline_source_queries.json").read_text(encoding="utf-8"))
        for case in cases:
            hits = brain.search(case["query"], version=case.get("version"), limit=20)
            match = None
            for hit in hits:
                if not set(hit["metadata"].get("sources", [])) & set(case["source_ids"]):
                    continue
                body = brain.documents[hit["id"]].body
                position = body.lower().find(case["evidence"].lower())
                if position < 0:
                    continue
                read = brain.read(hit["id"], offset=max(0, position - 100), max_chars=2000)
                if case["evidence"].lower() in read["text"].lower():
                    match = hit["id"]
                    break
            passed = match is not None
            results.append({"query": case["query"], "version": case.get("version"), "passed": passed, "document": match})
            if not passed:
                failures.append("Source-body retrieval failed: " + case["query"] + " version=" + str(case.get("version")))
    return {"ok": not failures, "network": "none", "snapshot_hashes_checked": checked,
            "retrieval_checks": results, "failures": failures}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--hashes-only", action="store_true")
    args = parser.parse_args()
    try:
        report = verify(args.root, retrieval=not args.hashes_only)
        print(json.dumps(report, indent=2, ensure_ascii=True))
        return 0 if report["ok"] else 1
    except (OSError, ValueError, KeyError) as error:
        print("offline knowledge: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

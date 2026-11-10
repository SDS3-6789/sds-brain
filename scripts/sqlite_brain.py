#!/usr/bin/env python3
"""Build and query the additive SDS SQLite document snapshot without network access."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.sqlite_index import DEFAULT_DATABASE, build_database, check, read, search, status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Public project root; no private customer export is performed")
    parser.add_argument("--database", type=Path, help="Database file; default is <root>/data/sds-brain.db")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("build", help="Atomically rebuild the public snapshot; preserve original project files")
    find = commands.add_parser("search", help="Read-only parameterized FTS5 search")
    find.add_argument("query")
    find.add_argument("--limit", type=int, default=10)
    find.add_argument("--area")
    find.add_argument("--version")
    find.add_argument("--source-id")
    find.add_argument("--kind", choices=("document", "config", "code", "all"), default="document")
    find.add_argument("--mode", choices=("any", "all", "phrase"), default="any")
    get = commands.add_parser("read", help="Read a bounded section of an indexed document ID")
    get.add_argument("document_id")
    get.add_argument("--offset", type=int, default=0)
    get.add_argument("--max-chars", type=int, default=12000)
    get.add_argument("--full-source", action="store_true", help="Include original text/frontmatter rather than parsed body")
    commands.add_parser("status", help="Read-only counts and provenance")
    verify = commands.add_parser("check", help="Read-only SQLite integrity and optional source-freshness check")
    verify.add_argument("--fresh", action="store_true", help="Also compare all eligible public input hashes against this project")
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        database = args.database or root / DEFAULT_DATABASE
        if not database.is_absolute():
            database = root / database
        if args.command == "build":
            result = build_database(root, database)
        elif args.command == "search":
            result = search(database, args.query, args.limit, args.area, args.version, args.source_id, args.kind, args.mode)
        elif args.command == "read":
            result = read(database, args.document_id, args.offset, args.max_chars, args.full_source)
        elif args.command == "status":
            result = status(database)
        else:
            result = check(database, root=root if args.fresh else None)
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return 1 if result.get("ok") is False else 0
    except (OSError, ValueError, sqlite3.Error, KeyError) as error:
        print("sqlite brain: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

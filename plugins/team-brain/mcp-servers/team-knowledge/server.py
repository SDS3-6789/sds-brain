#!/usr/bin/env python3
"""Claude plugin adapter for the canonical, local-only SDS knowledge MCP."""
from __future__ import annotations
import argparse
import sys

sys.dont_write_bytecode = True
from tk.config import canonical_server, settings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate the explicitly selected local corpus")
    args = parser.parse_args(argv)
    try:
        root, customer, cluster = settings()
        canonical = canonical_server(root)
    except (ValueError, OSError, ImportError) as exc:
        print("SDS plugin startup failed: " + str(exc), file=sys.stderr)
        return 2
    arguments = ["sds-knowledge", "--root", str(root)]
    if customer:
        arguments += ["--customer", customer, "--cluster", cluster]
    if args.check:
        arguments.append("--check")
    previous = sys.argv
    try:
        sys.argv = arguments
        return canonical.main()
    finally:
        sys.argv = previous


if __name__ == "__main__":
    raise SystemExit(main())

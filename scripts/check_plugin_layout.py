#!/usr/bin/env python3
"""Check exact pinned reference paths/types and the six real vendor archive hashes."""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REFERENCE = "cd866d4ee510b299c415f92a90b7f525d30cf04c"
ROOT = Path(__file__).resolve().parents[1]


def linked(path):
    return path.is_symlink() or getattr(path, "is_junction", lambda: False)()


def check_layout(root=ROOT, verify_archives=True):
    root = Path(root).resolve(strict=True)
    plugin = root / "plugins/team-brain"
    record = json.loads((root / "docs/PLUGIN_REFERENCE_TREE.json").read_text(encoding="utf-8"))
    if (record.get("commit") != REFERENCE or record.get("prefix") != "plugins/team-brain"
            or record.get("tree_api_truncated") is not False):
        raise ValueError("Unexpected or incomplete reference tree")
    expected = {entry["path"]: entry["type"] for entry in record["entries"]}
    if len(expected) != 47 or sum(t == "blob" for t in expected.values()) != 29 or sum(t == "tree" for t in expected.values()) != 18:
        raise ValueError("Reference must contain exactly 29 files and 18 subdirectories")
    if not plugin.is_dir() or any(linked(p) for p in (plugin, plugin.parent)):
        raise ValueError("Plugin root must be a real directory")
    actual, failures = {}, []
    # Reject links before descending; never inspect linked subtrees.
    todo = [plugin]
    while todo:
        directory = todo.pop()
        for path in directory.iterdir():
            relative = path.relative_to(plugin).as_posix()
            if linked(path):
                failures.append("Linked path: " + relative)
                actual[relative] = "link"
            elif path.is_dir():
                actual[relative] = "tree"
                todo.append(path)
            elif path.is_file():
                actual[relative] = "blob"
            else:
                actual[relative] = "unsupported"
    for path in sorted(set(expected) - set(actual)):
        failures.append("Missing " + expected[path] + ": " + path)
    for path in sorted(set(actual) - set(expected)):
        failures.append("Extra " + actual[path] + ": " + path)
    for path in sorted(set(actual) & set(expected)):
        if actual[path] != expected[path]:
            failures.append("Wrong type: " + path)
    checked = 0
    if verify_archives and not failures:
        vendor = plugin / "mcp-servers/vendor"
        manifest = json.loads((vendor / "manifest.json").read_text(encoding="utf-8"))
        if set(manifest) != {"grafana", "kubernetes"}:
            failures.append("Vendor manifest must describe exactly grafana and kubernetes")
        for name, spec in manifest.items():
            assets = spec.get("assets", {})
            if spec.get("enabled_by_default") is not False or len(assets) != 3:
                failures.append("Vendor family must remain optional and pin three archives: " + name)
            for asset in assets.values():
                relative = "mcp-servers/vendor/" + name + "/" + asset.get("file", "")
                if expected.get(relative) != "blob":
                    failures.append("Archive path is outside the reference tree: " + relative)
                    continue
                path = plugin / relative
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for block in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(block)
                if path.stat().st_size != asset.get("bytes") or digest.hexdigest() != asset.get("sha256"):
                    failures.append("Archive size or SHA-256 mismatch: " + relative)
                else:
                    checked += 1
        if checked != 6:
            failures.append("Expected six verified vendor archives")
    return {"ok": not failures, "reference_commit": REFERENCE,
            "files": sum(t == "blob" for t in actual.values()),
            "directories": sum(t == "tree" for t in actual.values()),
            "archives_verified": checked, "failures": failures}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = check_layout(args.root)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        result = {"ok": False, "failures": [str(exc)]}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

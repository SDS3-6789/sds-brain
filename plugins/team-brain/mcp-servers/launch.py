#!/usr/bin/env python3
"""Verify shipped archives; optional Grafana delegates to the canonical SDS launcher."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
VENDOR = HERE / "vendor"
sys.path.insert(0, str(HERE / "team-knowledge"))
from tk.config import settings


def verify_assets():
    if VENDOR.is_symlink() or (VENDOR / "manifest.json").is_symlink():
        raise ValueError("Vendor paths must not be symbolic links")
    manifest = json.loads((VENDOR / "manifest.json").read_text(encoding="utf-8"))
    if set(manifest) != {"grafana", "kubernetes"}:
        raise ValueError("Expected exactly the two reference vendor families")
    result = []
    for name, spec in manifest.items():
        if spec.get("enabled_by_default") is not False or len(spec.get("assets", {})) != 3:
            raise ValueError("Optional vendor families must pin three assets and remain disabled by default")
        for platform, asset in spec["assets"].items():
            filename, size, digest = asset.get("file"), asset.get("bytes"), asset.get("sha256")
            if (not isinstance(filename, str) or Path(filename).name != filename
                    or "/" in filename or "\\" in filename or ":" in filename
                    or filename in {"", ".", ".."} or type(size) is not int
                    or not 0 < size <= 128 * 1024 * 1024
                    or not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest)):
                raise ValueError("Invalid archive pin")
            path = VENDOR / name / filename
            if path.is_symlink() or path.parent.is_symlink() or not path.is_file() or path.stat().st_size != size:
                raise ValueError("Missing or unsafe pinned archive: " + filename)
            hashed = hashlib.sha256()
            with path.open("rb") as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    hashed.update(block)
            if hashed.hexdigest() != digest:
                raise ValueError("Archive checksum mismatch: " + filename)
            result.append({"server": name, "platform": platform, "version": spec["version"],
                           "file": filename, "verified": True, "enabled_by_default": False})
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("server", nargs="?", choices=("grafana", "kubernetes"))
    parser.add_argument("--check", action="store_true", help="Hash archives only; do not extract or execute")
    args = parser.parse_args(argv)
    try:
        verified = verify_assets()
        if args.check:
            print(json.dumps({"archives": verified, "executed": False}, indent=2))
            return 0
        if args.server != "grafana":
            raise ValueError("Kubernetes is disabled in this SDS release; no binary is executed")
        root, _, _ = settings()
        # The canonical launcher fixes flags, HTTPS/CA inputs and executable hashes.
        # It uses the original root archive set, which also includes Linux ARM64.
        return subprocess.call([sys.executable, str(root / "mcp/grafana/launch.py")])
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print("SDS vendor launcher: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

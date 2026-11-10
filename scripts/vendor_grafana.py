#!/usr/bin/env python3
"""Check bundled Grafana archives, or explicitly download the manifest-pinned release."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
import tempfile
from http.client import HTTPException
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sds_grafana_bundle", ROOT / "mcp/grafana/launch.py")
bundle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)
ASSET_HOSTS = {"github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com", "github-releases.githubusercontent.com"}


def allowed_url(url):
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in ASSET_HOSTS
            or parsed.username is not None or parsed.password is not None or parsed.fragment
            or parsed.port not in {None, 443}):
        raise ValueError("Download redirect left the approved HTTPS GitHub asset hosts")


class PinnedRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        allowed_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def check(manifest_path=bundle.MANIFEST):
    manifest_path = Path(manifest_path)
    manifest = bundle.load_manifest(manifest_path)
    for asset in manifest["assets"]:
        bundle.verified_bytes(manifest_path.parent / "vendor" / asset["name"], asset["size_bytes"], asset["sha256"])
    return {"ok": True, "version": manifest["version"], "archives_verified": len(manifest["assets"]), "network": "none"}


def download_one(asset, destination, opener):
    destination = Path(destination)
    bundle.no_symlinks(destination)
    if destination.exists():
        bundle.verified_bytes(destination, asset["size_bytes"], asset["sha256"])
        return
    allowed_url(asset["url"])
    request = Request(asset["url"], headers={"User-Agent": "sds-brain-offline-bundle/1", "Accept-Encoding": "identity"})
    temporary = None
    try:
        with opener.open(request, timeout=30) as response:
            allowed_url(response.geturl())
            if response.status != 200:
                raise ValueError("Unexpected release download status")
            encoding = response.headers.get("Content-Encoding", "identity")
            if encoding.lower() not in {"identity", ""}:
                raise ValueError("Unexpected release download content encoding")
            length = response.headers.get("Content-Length")
            if length is not None and int(length) != asset["size_bytes"]:
                raise ValueError("Release download size differs from the manifest")
            with tempfile.NamedTemporaryFile(mode="wb", dir=destination.parent, prefix=".grafana-download-", delete=False) as output:
                temporary = Path(output.name)
                digest, total = hashlib.sha256(), 0
                while True:
                    block = response.read(min(1024 * 1024, asset["size_bytes"] - total + 1))
                    if not block:
                        break
                    total += len(block)
                    if total > asset["size_bytes"]:
                        raise ValueError("Release download exceeds its pinned size")
                    digest.update(block)
                    output.write(block)
                if total != asset["size_bytes"] or digest.hexdigest() != asset["sha256"]:
                    raise ValueError("Release download checksum differs")
        bundle.no_symlinks(destination)
        if destination.exists():
            bundle.verified_bytes(destination, asset["size_bytes"], asset["sha256"])
        else:
            os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def download(manifest_path=bundle.MANIFEST):
    manifest_path = Path(manifest_path)
    manifest = bundle.load_manifest(manifest_path)
    destination = manifest_path.parent / "vendor"
    bundle.no_symlinks(destination)
    destination.mkdir(parents=True, exist_ok=True)
    bundle.no_symlinks(destination)
    # Explicit connected-host operation; no ambient proxy or insecure TLS fallback.
    opener = build_opener(ProxyHandler({}), PinnedRedirect(), HTTPSHandler())
    for asset in manifest["assets"]:
        download_one(asset, destination / asset["name"], opener)
    result = check(manifest_path)
    result["network"] = "explicit pinned HTTPS downloads permitted"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Verify all bundled archives without using the network")
    mode.add_argument("--download", action="store_true", help="Explicit connected-host preparation: download only missing manifest-pinned archives")
    args = parser.parse_args()
    try:
        print(json.dumps(download() if args.download else check(), indent=2))
        return 0
    except (ValueError, OSError, RuntimeError, HTTPException):
        print("Grafana vendoring failed: verify the pinned manifest, bundled files, and connected-host HTTPS access. No unverified archive was installed.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Verify and launch the bundled Grafana MCP; never download at runtime."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import platform
import re
import stat
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import urlsplit

DIRECTORY = Path(__file__).resolve().parent
MANIFEST = DIRECTORY / "release-manifest.json"
PLATFORMS = {"Linux_x86_64", "Linux_arm64", "Darwin_arm64", "Windows_x86_64"}
MAX_ARCHIVE_BYTES = 128 * 1024 * 1024
MAX_BINARY_BYTES = 512 * 1024 * 1024
FLAGS = ("-t", "stdio", "--disable-write", "--usage-stats=disabled",
         "--enabled-tools=search,datasource,dashboard,elasticsearch")
PROXY_NAMES = {"HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY"}


def no_symlinks(path):
    path = Path(path).absolute()
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError("Symbolic links are not accepted in bundled or cache paths")


def safe_member(name):
    if (not isinstance(name, str) or not name or "\\" in name or ":" in name
            or any(ord(c) < 32 or ord(c) == 127 for c in name)
            or any(part in {"", ".", ".."} for part in name.split("/"))):
        raise ValueError("Unsafe archive member path")
    return name


def load_manifest(path=MANIFEST):
    path = Path(path)
    no_symlinks(path)
    if not path.is_file() or path.stat().st_size > 128 * 1024:
        raise ValueError("Release manifest is missing or oversized")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if (not isinstance(manifest, dict) or manifest.get("project") != "grafana/mcp-grafana"
            or not isinstance(manifest.get("version"), str)
            or not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", manifest["version"])):
        raise ValueError("Invalid Grafana release manifest")
    assets = manifest.get("assets")
    if not isinstance(assets, list) or len(assets) != len(PLATFORMS):
        raise ValueError("Manifest must pin all four supported platform archives")
    seen = set()
    for asset in assets:
        if (not isinstance(asset, dict) or not isinstance(asset.get("platform"), str)
                or asset["platform"] not in PLATFORMS):
            raise ValueError("Invalid manifest platform")
        key = asset["platform"]
        if key in seen:
            raise ValueError("Duplicate manifest platform")
        seen.add(key)
        suffix = ".zip" if key.startswith("Windows_") else ".tar.gz"
        expected_name = "mcp-grafana_" + key + suffix
        expected_url = "https://github.com/grafana/mcp-grafana/releases/download/" + manifest["version"] + "/" + expected_name
        if asset.get("name") != expected_name or asset.get("url") != expected_url:
            raise ValueError("Archive must use its pinned official GitHub release URL")
        expected_binary = "mcp-grafana.exe" if key.startswith("Windows_") else "mcp-grafana"
        if safe_member(asset.get("binary_path")) != expected_binary:
            raise ValueError("Unexpected Grafana executable archive member")
        for field, maximum in (("size_bytes", MAX_ARCHIVE_BYTES), ("binary_size_bytes", MAX_BINARY_BYTES)):
            if type(asset.get(field)) is not int or not 0 < asset[field] <= maximum:
                raise ValueError("Invalid pinned file size")
        for field in ("sha256", "binary_sha256"):
            if not isinstance(asset.get(field), str) or not re.fullmatch(r"[a-f0-9]{64}", asset[field]):
                raise ValueError("Invalid pinned SHA-256")
    return manifest


def verified_bytes(path, size, digest):
    path = Path(path)
    no_symlinks(path)
    if not path.is_file() or path.stat().st_size != size:
        raise ValueError("Pinned file is missing or its size differs: " + path.name)
    with path.open("rb") as stream:
        data = stream.read(size + 1)
    if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("Pinned file checksum differs: " + path.name)
    return data


def verify_binary(path, asset):
    path = Path(path)
    no_symlinks(path)
    if not path.is_file() or path.stat().st_size != asset["binary_size_bytes"]:
        raise ValueError("Cached executable is missing or its size differs")
    digest, total = hashlib.sha256(), 0
    with path.open("rb") as stream:
        while True:
            block = stream.read(1024 * 1024)
            if not block:
                break
            total += len(block)
            if total > asset["binary_size_bytes"]:
                raise ValueError("Cached executable exceeds its pinned size")
            digest.update(block)
    if total != asset["binary_size_bytes"] or digest.hexdigest() != asset["binary_sha256"]:
        raise ValueError("Cached executable checksum differs; remove the invalid cache file")


def platform_key(system=None, machine=None):
    system, machine = system or platform.system(), (machine or platform.machine()).lower()
    architecture = {"amd64": "x86_64", "x86_64": "x86_64", "aarch64": "arm64", "arm64": "arm64"}.get(machine)
    key = system + "_" + (architecture or machine)
    if key not in PLATFORMS:
        raise ValueError("No bundled Grafana executable for this operating system and architecture")
    return key


def cache_directory(manifest, asset, environ=None, cache_root=None):
    environ = os.environ if environ is None else environ
    if cache_root is None:
        if asset["platform"].startswith("Windows_"):
            cache_root = environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local"
        else:
            cache_root = environ.get("XDG_CACHE_HOME") or Path.home() / ".cache"
    base = Path(cache_root).expanduser()
    if not base.is_absolute():
        raise ValueError("Grafana cache root must be an absolute path")
    path = base / "sds-brain" / "grafana" / manifest["version"] / asset["platform"] / asset["sha256"][:16]
    no_symlinks(path)
    return path


def extract_binary(data, asset, destination):
    """Read only the exact regular executable member from already-verified bytes."""
    archive = (zipfile.ZipFile(io.BytesIO(data)) if asset["name"].endswith(".zip")
               else tarfile.open(fileobj=io.BytesIO(data), mode="r:gz"))
    with archive:
        entries = archive.infolist() if isinstance(archive, zipfile.ZipFile) else archive
        matches, expanded = [], 0
        for count, entry in enumerate(entries, 1):
            if count > 1024:
                raise ValueError("Archive contains too many members")
            name = entry.filename if isinstance(entry, zipfile.ZipInfo) else entry.name
            safe_member(name.rstrip("/"))
            size = entry.file_size if isinstance(entry, zipfile.ZipInfo) else entry.size
            if size < 0:
                raise ValueError("Invalid archive member size")
            expanded += size
            if expanded > asset["binary_size_bytes"] + 16 * 1024 * 1024:
                raise ValueError("Archive expanded size exceeds its bound")
            if name == asset["binary_path"]:
                if isinstance(entry, zipfile.ZipInfo):
                    mode = stat.S_IFMT(entry.external_attr >> 16)
                    regular = not entry.is_dir() and mode in {0, stat.S_IFREG} and not entry.flag_bits & 1
                else:
                    regular = entry.isreg() and not entry.sparse
                if not regular or size != asset["binary_size_bytes"]:
                    raise ValueError("Executable member must be a regular file of its pinned size")
                matches.append(entry)
        if len(matches) != 1:
            raise ValueError("Archive must contain exactly one pinned executable member")
        stream = (archive.open(matches[0]) if isinstance(archive, zipfile.ZipFile)
                  else archive.extractfile(matches[0]))
        if stream is None:
            raise ValueError("Cannot read executable member")
        temporary = None
        try:
            no_symlinks(destination)
            with stream, tempfile.NamedTemporaryFile(mode="wb", dir=destination.parent,
                                                      prefix=".mcp-grafana-", delete=False) as output:
                temporary = Path(output.name)
                digest, total = hashlib.sha256(), 0
                while True:
                    block = stream.read(min(1024 * 1024, asset["binary_size_bytes"] - total + 1))
                    if not block:
                        break
                    total += len(block)
                    if total > asset["binary_size_bytes"]:
                        raise ValueError("Executable member exceeds its pinned size")
                    digest.update(block)
                    output.write(block)
                if total != asset["binary_size_bytes"] or digest.hexdigest() != asset["binary_sha256"]:
                    raise ValueError("Executable member checksum differs")
            temporary.chmod(0o700)
            no_symlinks(destination)
            os.replace(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)


def prepare_binary(manifest_path=MANIFEST, cache_root=None, system=None, machine=None):
    manifest_path = Path(manifest_path)
    manifest = load_manifest(manifest_path)
    key = platform_key(system, machine)
    asset = next(asset for asset in manifest["assets"] if asset["platform"] == key)
    archive_path = manifest_path.parent / "vendor" / asset["name"]
    # Extraction consumes these exact hashed bytes, never a second path read.
    data = verified_bytes(archive_path, asset["size_bytes"], asset["sha256"])
    cache = cache_directory(manifest, asset, cache_root=cache_root)
    cache.mkdir(parents=True, exist_ok=True)
    no_symlinks(cache)
    destination = cache / asset["binary_path"]
    no_symlinks(destination)
    if not destination.exists():
        extract_binary(data, asset, destination)
    verify_binary(destination, asset)
    return destination, manifest, asset


def launch_configuration(binary, environ=None):
    original = os.environ if environ is None else environ
    url, token = original.get("SDS_GRAFANA_URL", ""), original.get("SDS_GRAFANA_TOKEN", "")
    if (not url or any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in url)
            or any(c in url for c in ("?", "#", "\\"))):
        raise ValueError("SDS_GRAFANA_URL must be an HTTPS URL without credentials, query or fragment")
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username is not None or parsed.password is not None:
        raise ValueError("SDS_GRAFANA_URL must be an HTTPS URL without credentials, query or fragment")
    parsed.port  # Reject malformed port syntax without echoing the URL.
    if not token.strip() or any(ord(c) < 32 or ord(c) == 127 for c in token):
        raise ValueError("SDS_GRAFANA_TOKEN must be nonempty and contain no control characters")
    child = {key: value for key, value in original.items()
             if not key.upper().startswith(("GRAFANA_", "OTEL_"))
             and key.upper() not in PROXY_NAMES | {"DO_NOT_TRACK"}}
    child.pop("SDS_GRAFANA_TOKEN", None)
    child.update(GRAFANA_URL=url, GRAFANA_SERVICE_ACCOUNT_TOKEN=token,
                 GRAFANA_USAGE_STATS="disabled", DO_NOT_TRACK="1")
    command = [str(binary), *FLAGS]
    ca = original.get("SDS_GRAFANA_CA_FILE")
    if ca:
        ca_path = Path(ca).expanduser().absolute()
        no_symlinks(ca_path)
        if not ca_path.is_file():
            raise ValueError("SDS_GRAFANA_CA_FILE must name an existing regular file")
        command += ["--tls-ca-file", str(ca_path)]
    return command, child


def execute(command, child):
    if os.name == "posix":
        # Replace the launcher so normal MCP termination reaches the actual server.
        os.execve(command[0], command, child)
        return 0
    return subprocess.call(command, env=child)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify bundled archive and cached executable without starting Grafana or using the network")
    args = parser.parse_args()
    try:
        binary, manifest, asset = prepare_binary()
        if args.check:
            print(json.dumps({"ok": True, "version": manifest["version"], "platform": asset["platform"],
                              "archive_sha256": asset["sha256"], "binary_sha256": asset["binary_sha256"],
                              "cached_binary": str(binary), "binary_executed": False, "network": "none"}, indent=2))
            return 0
        command, child = launch_configuration(binary)
        # Inherit stdio verbatim: protocol output belongs exclusively to the MCP binary.
        return execute(command, child)
    except (ValueError, OSError, tarfile.TarError, zipfile.BadZipFile, EOFError, RuntimeError):
        print("Grafana launcher refused: verify the bundle/cache and SDS_GRAFANA_* configuration; no download was attempted.", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())

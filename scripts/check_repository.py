#!/usr/bin/env python3
"""Check the distributable repository layout and references without network access."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "AGENT.md", "AGENTS.md", "CLAUDE.md", "README.md", "INDEX.md", ".mcp.json",
    ".gitignore", "NOTICE", "MANIFEST.sha256", "Makefile", "lib/brain.py",
    "scripts/brain.py", "scripts/acceptance.py", "scripts/import_docs.py",
    "scripts/vendor_grafana.py", "mcp/knowledge/server.py", "mcp/objectify/server.py",
    "mcp/objectify/config.example.json", "mcp/grafana/launch.py",
    "mcp/grafana/release-manifest.json", "mcp/grafana/LICENSE.upstream",
    "docs/ARCHITECTURE.md", "docs/COVERAGE.md", "docs/IMPORTING.md",
    "docs/SOURCES.md", "docs/VALIDATION.md", "docs/REVIEW.md",
    "scripts/check_repository.py", "mcp/okp/README.md", "mcp/okp/upstream-source.json",
    "config/knowledge-okp.example.json", "config/knowledge-grafana-okp-private.example.json",
    "deploy/podman/README.md", "deploy/podman/rhokp.env.example",
    "deploy/podman/existing-portal/sds-okp.container.example",
    "deploy/podman/new-portal/sds-okp.container.example",
    "deploy/podman/new-portal/sds-rhokp.container.example",
    "deploy/podman/new-portal/sds-okp.network",
    "deploy/podman/new-portal/sds-rhokp-data.volume",
    ".claude-plugin/marketplace.json", "plugins/team-brain/.claude-plugin/plugin.json",
    "plugins/team-brain/.mcp.json", "docs/PLUGIN.md", "docs/PLUGIN_REFERENCE_TREE.json",
    "scripts/check_plugin_layout.py", "lib/sqlite_index.py", "scripts/sqlite_brain.py",
    "docs/SQLITE.md", "data/sds-brain.db",
)
REQUIRED_DIRS = (
    "knowledge", "runbooks", "docs", "sources", "templates", "config", "lib",
    "scripts", "tests", "mcp/knowledge", "mcp/objectify", "mcp/grafana/vendor",
    "mcp/okp", "deploy/podman/existing-portal", "deploy/podman/new-portal",
    "plugins/team-brain", "data",
)
EXCLUDED_DIRS = {".git", ".codex", ".agents", ".venv", ".cache", "__pycache__",
                 ".pytest_cache", "private", "exports", "dist", "work", "outputs",
                 "inbox", "drafts", "staging"}
LOCAL_LINK = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)")
SCRIPT_SUFFIXES = {".py", ".js", ".mjs", ".cjs"}


def linked(path):
    return path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())


def safe_path(root, path):
    """Reject outside paths and linked ancestors before reading local content."""
    try:
        path.relative_to(root)
    except ValueError:
        return False
    for component in (path, *path.parents):
        if linked(component):
            return False
        if component == root:
            return True
    return False


def public_files(root, failures):
    """Omit private/imported/runtime material and never descend through links."""
    for base, directories, filenames in os.walk(root, followlinks=False):
        base = Path(base)
        retained = []
        for name in sorted(directories):
            path = base / name
            relative = path.relative_to(root).as_posix()
            if name.casefold() in EXCLUDED_DIRS or relative.casefold() == "docs/imported":
                continue
            if linked(path):
                failures.append(relative + ": linked directories are not package content")
            else:
                retained.append(name)
        directories[:] = retained
        for name in sorted(filenames):
            path = base / name
            if name.casefold().endswith((".local.json", ".local.md")) or name.casefold().startswith(".env"):
                continue
            if linked(path):
                failures.append(path.relative_to(root).as_posix() + ": linked files are not package content")
            elif path.is_file():
                yield path


def check_mcp(root, path, value, failures):
    if not isinstance(value, dict) or "mcpServers" not in value:
        return
    relative = path.relative_to(root).as_posix()
    servers = value["mcpServers"]
    if not isinstance(servers, dict):
        failures.append(relative + ": mcpServers must be an object")
        return
    for name, server in servers.items():
        label = relative + ": " + name
        if not isinstance(server, dict):
            failures.append(label + ": server entry must be an object")
            continue
        transport = server.get("type", "stdio")
        if not isinstance(transport, str):
            failures.append(label + ": MCP transport must be a string")
            continue
        if transport in {"http", "sse"}:
            url = server.get("url")
            try:
                parsed = urlsplit(url) if isinstance(url, str) else None
                valid = (parsed is not None and parsed.scheme in {"http", "https"}
                         and parsed.hostname and parsed.username is None and parsed.password is None)
                if parsed is not None:
                    parsed.port  # Validate the optional numeric port as well as the hostname.
            except ValueError:
                valid = False
            if not valid:
                failures.append(label + ": HTTP transport requires a valid credential-free URL")
            continue  # Validate configuration only; never contact the service.
        if transport != "stdio":
            failures.append(label + ": unsupported MCP transport")
            continue
        if not isinstance(server.get("command"), str) or not server["command"].strip():
            failures.append(label + ": stdio command is missing")
        arguments = server.get("args", [])
        if not isinstance(arguments, list) or not all(isinstance(item, str) for item in arguments):
            failures.append(label + ": args must be a string array")
            continue
        for argument in arguments:
            prefix = "${SDS_BRAIN_DIR}/"
            if argument.startswith(prefix):
                relative_target = argument[len(prefix):]
            elif argument.startswith(("mcp/", "scripts/")):
                relative_target = argument
            else:
                continue
            if Path(relative_target).suffix.lower() not in SCRIPT_SUFFIXES:
                continue  # Private *.local.json inputs are intentionally operator-supplied.
            portable = PurePosixPath(relative_target)
            if portable.is_absolute() or ".." in portable.parts or "\\" in relative_target or ":" in relative_target:
                failures.append(label + ": script target escapes the repository")
                continue
            target = root.joinpath(*portable.parts)
            if not safe_path(root, target) or not target.is_file():
                failures.append(label + ": missing or linked script target " + relative_target)


def check_manifest(root, failures):
    manifest = root / "MANIFEST.sha256"
    if not safe_path(root, manifest) or not manifest.is_file():
        return 0
    seen, entries = set(), 0
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
        if not match:
            failures.append("MANIFEST.sha256:" + str(number) + ": invalid record")
            continue
        expected, name = match.groups()
        portable = PurePosixPath(name)
        if portable.is_absolute() or ".." in portable.parts or "\\" in name or ":" in name:
            failures.append("MANIFEST.sha256:" + str(number) + ": unsafe path")
            continue
        if name in seen:
            failures.append("MANIFEST.sha256:" + str(number) + ": duplicate path")
            continue
        seen.add(name)
        entries += 1
        target = root.joinpath(*portable.parts)
        if not safe_path(root, target) or not target.is_file():
            failures.append("MANIFEST.sha256: missing or linked file " + name)
            continue
        digest = hashlib.sha256()
        with target.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        if digest.hexdigest() != expected.lower():
            failures.append("MANIFEST.sha256: hash mismatch " + name)
    if not entries:
        failures.append("MANIFEST.sha256: no file records")
    return entries


def check_repository(root, manifest=False):
    root = root.resolve(strict=True)
    failures = []
    if not root.is_dir():
        raise ValueError("Repository root must be a directory")
    for name in REQUIRED_FILES:
        path = root / name
        if not safe_path(root, path) or not path.is_file():
            failures.append(name + ": required regular file is missing or linked")
    for name in REQUIRED_DIRS:
        path = root / name
        if not safe_path(root, path) or not path.is_dir():
            failures.append(name + ": required directory is missing or linked")
    files = list(public_files(root, failures))
    for folder, suffix in (("knowledge", ".md"), ("runbooks", ".md"), ("sources", ".json")):
        if not any(path.relative_to(root).parts[0] == folder and path.suffix == suffix for path in files):
            failures.append(folder + ": required content is empty")
    json_files = 0
    for path in files:
        relative = path.relative_to(root).as_posix()
        if path.suffix == ".json":
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
                json_files += 1
                check_mcp(root, path, value, failures)
            except (ValueError, UnicodeError) as error:
                failures.append(relative + ": invalid JSON: " + str(error))
        elif path.suffix == ".md":
            text = path.read_text(encoding="utf-8")
            for match in LOCAL_LINK.finditer(text):
                target = match.group(1).strip("<>")
                if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                target = unquote(target.split("#", 1)[0])
                if not target:
                    continue
                destination = Path(os.path.abspath(path.parent / target))
                if not safe_path(root, destination) or not destination.exists():
                    line = text.count("\n", 0, match.start()) + 1
                    failures.append(relative + ":" + str(line) + ": broken local link " + target)
    for name, pointer in (("AGENTS.md", "AGENT.md"), ("CLAUDE.md", "@AGENT.md")):
        path = root / name
        if safe_path(root, path) and path.is_file() and pointer not in path.read_text(encoding="utf-8"):
            failures.append(name + ": canonical AGENT.md pointer is missing")
    entries = check_manifest(root, failures) if manifest else None
    return {"ok": not failures, "public_files_checked": len(files), "json_files_checked": json_files,
            "manifest_entries_checked": entries, "failures": failures,
            "scope": "Public layout, JSON, local links and MCP script targets; no runtime or infrastructure checks."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--manifest", action="store_true", help="Also verify every listed release-manifest hash")
    args = parser.parse_args()
    try:
        result = check_repository(args.root, manifest=args.manifest)
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return 0 if result["ok"] else 1
    except (OSError, ValueError, UnicodeError) as error:
        print("repository check: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

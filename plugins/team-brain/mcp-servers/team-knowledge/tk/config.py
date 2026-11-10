"""Resolve the explicit external SDS repository; never guess a cached install's root."""
from __future__ import annotations
import importlib.util
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")


def settings(environ=None):
    env = os.environ if environ is None else environ
    value = env.get("SDS_BRAIN_DIR", "")
    if not value or not Path(value).is_absolute():
        raise ValueError("Set SDS_BRAIN_DIR to the absolute path of the SDS Storage Brain repository")
    candidate = Path(value)
    if any(part.is_symlink() or getattr(part, "is_junction", lambda: False)()
           for part in (candidate, *candidate.parents)):
        raise ValueError("SDS_BRAIN_DIR must not traverse symbolic links or junctions")
    root = candidate.resolve(strict=True)
    if not root.is_dir() or not all((root / p).is_file() for p in
                                    ("AGENT.md", "lib/brain.py", "mcp/knowledge/server.py")):
        raise ValueError("SDS_BRAIN_DIR is not an SDS Storage Brain repository")
    customer, cluster = env.get("SDS_CUSTOMER") or None, env.get("SDS_CLUSTER") or None
    if bool(customer) != bool(cluster) or any(not SLUG.fullmatch(s) for s in (customer, cluster) if s):
        raise ValueError("SDS_CUSTOMER and SDS_CLUSTER must be a matching pair of valid aliases")
    return root, customer, cluster


def canonical_server(root):
    path = Path(root) / "mcp/knowledge/server.py"
    name = "_sds_team_brain_canonical_server"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def brain(environ=None):
    root, customer, cluster = settings(environ)
    server = canonical_server(root)
    return server.Brain(root, customer, cluster)

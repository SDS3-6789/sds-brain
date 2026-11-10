#!/usr/bin/env bash
# Original SDS local draft helper. No git network, commits, staging or cleanup.
# Usage: brain-git.sh start learn|curate|incident slug
set -eu
if [ "$#" -ne 3 ] || [ "$1" != "start" ]; then
  printf '%s\n' 'Usage: brain-git.sh start learn|curate|incident slug' >&2
  exit 2
fi
python3 - "$2" "$3" <<'PY'
import os, re, sys
from pathlib import Path
kind, slug = sys.argv[1:]
if kind not in {"learn", "curate", "incident"} or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", slug):
    raise SystemExit("Use a supported draft kind and a lowercase alias (1-64 characters)")
value = os.environ.get("SDS_BRAIN_DIR", "")
root = Path(value)
if not value or not root.is_absolute() or not (root / "AGENT.md").is_file():
    raise SystemExit("Set absolute SDS_BRAIN_DIR to the selected restricted SDS repository")
customer, cluster = os.environ.get("SDS_CUSTOMER"), os.environ.get("SDS_CLUSTER")
if bool(customer) != bool(cluster) or any(not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", x) for x in (customer, cluster) if x):
    raise SystemExit("SDS_CUSTOMER and SDS_CLUSTER must be a valid alias pair")
base = root / "private" / customer / cluster / "drafts" if customer else root / "inbox"
target = base / (kind + "-" + slug + ".md")
for part in (target, *target.parents):
    if part.is_symlink() or getattr(part, "is_junction", lambda: False)():
        raise SystemExit("Draft paths must not traverse symbolic links or junctions")
    if part == root:
        break
base.mkdir(parents=True, exist_ok=True)
with target.open("x", encoding="utf-8", newline="\n") as stream:
    stream.write("# Review draft: " + slug + "\n\nStatus: draft; human review required.\n"
                 "Confidence: hypothesis until evidence supports another label.\n\n"
                 "## Scope\n\nRecord customer/cluster aliases, product/build and UTC window.\n\n"
                 "## Evidence and citations\n\nUse bounded redacted evidence and source/document IDs.\n\n"
                 "## Finding and uncertainty\n\n\n## Proposed checks\n\nRead-only proposals only.\n\n"
                 "## Review\n\nOwner, review date, applicability and promotion decision.\n")
print(target)
PY

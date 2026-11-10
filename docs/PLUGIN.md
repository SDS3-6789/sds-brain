# SDS team-brain plugin

The project now contains plugins/team-brain with the **same 29 file paths and 18 subdirectory paths** as [redbull-brain at cd866d4ee510b299c415f92a90b7f525d30cf04c](https://github.com/team-redbull/redbull-brain/tree/cd866d4ee510b299c415f92a90b7f525d30cf04c/plugins/team-brain), checked on 2026-11-10. This is hierarchy parity. Runtime code and workflows are original SDS implementations, adapted to the existing offline storage project. They are not byte-for-byte copies of the reference.

[PLUGIN_REFERENCE_TREE.json](PLUGIN_REFERENCE_TREE.json) records the complete Git tree, file types, Git blob identities and original sizes. The tree API was not truncated. No files were added inside the plugin beyond those reference paths. Supporting documentation and the parity checker live outside it.

## Use on the internal Linux host

Prerequisites: an approved Claude Code installation and model connectivity supported by your internal policy; Python 3.9+; Bash; the complete SDS repository and corpus; permissions for only the selected customer checkout. The package and local retrieval run without public downloads. Claude itself still needs your organization's approved model endpoint.

From the extracted repository:

    export SDS_BRAIN_DIR="$PWD"
    unset SDS_CUSTOMER SDS_CLUSTER
    python3 scripts/check_plugin_layout.py
    python3 plugins/team-brain/mcp-servers/team-knowledge/server.py --check
    claude --plugin-dir "$SDS_BRAIN_DIR/plugins/team-brain"

This direct route needs no marketplace registration. The existing root .mcp.json can also expose sds-knowledge. Choose the existing project server or the plugin team-knowledge server in the client to avoid duplicate retrieval entries. Do not mistake duplicate names for separate corpora.

Optional persistent registration from this local directory uses the root .claude-plugin/marketplace.json:

    claude plugin validate "$SDS_BRAIN_DIR"
    claude plugin marketplace add "$SDS_BRAIN_DIR"
    claude plugin install team-brain@sds-storage-brain

These commands change local Claude configuration and are provided for the operator to run under the normal trust process. They were not executed during packaging. See the official [plugin overview](https://code.claude.com/docs/en/plugins) and [local marketplace instructions](https://code.claude.com/docs/en/plugin-marketplaces).

An installed plugin is cached away from this repository. **Always export the absolute SDS_BRAIN_DIR before starting Claude**, including after moving the project or USB. The plugin does not guess a corpus from its cache location. It rejects a missing root, relative path, symbolic link/junction root or unmatched customer/cluster aliases.

For a single customer's restricted checkout, set both aliases before startup:

    export SDS_CUSTOMER=customer-a
    export SDS_CLUSTER=cluster-a
    python3 plugins/team-brain/mcp-servers/team-knowledge/server.py --check

The wrapper delegates to the canonical knowledge server with these fixed aliases. Restart Claude and use a fresh conversation when changing customer. Filesystem/backend permissions remain the security boundary. Do not place real customer data in a shared project or export.

Inspect /plugin and /mcp in Claude. Try /team-brain:brain-lookup and a local query. Client loading, organization policy and internal infrastructure acceptance still require testing on the target host; no live connection or native client installation is claimed.

## What the package does

| Reference path | SDS implementation |
|---|---|
| .claude-plugin/plugin.json | Local version 0.4.0, name team-brain, SDS attribution |
| .mcp.json | Only local team-knowledge, no enabled network or Kubernetes server |
| mcp-servers/team-knowledge/server.py | Thin adapter to canonical mcp/knowledge/server.py |
| tk/config.py | Explicit repository and fixed customer/cluster validation |
| tk/textindex.py | Canonical bounded search/read adapters |
| tk/sources.py | Paginated source metadata, distinct from saved document bodies |
| tk/graph.py | Declared citation edges; no inferred topology |
| tk/tools.py | Canonical MCP schema, dispatch and session adapters |
| scripts/session-start.sh | Local policy/context reminder, no automatic git pull |
| scripts/stop-capture-nudge.sh | Nonblocking review reminder, no transcript capture |
| scripts/brain-git.sh | Exclusive local draft creation; no git staging/commit/push |
| skills/brain-lookup | Read applicable local evidence before troubleshooting |
| skills/brain-learn, brain-curate, incident-report | User-invoked drafts requiring review before promotion |
| skills/hypershift-debug, agents/hcp-architect.md | Original scope-gated guidance; names retained for hierarchy parity |
| mcp-servers/kubernetes.toml | Disabled integration; defensive read-only and Secret-denial settings |
| mcp-servers/launch.py | Verify bundled archives; optional Grafana delegates to canonical SDS launcher |

Shared drafts live in inbox/. Bound drafts live in private/<customer>/<cluster>/drafts/ and are not added to approved retrieval automatically. The draft helper never overwrites an existing file. Use repository templates and human review for promotion.

## Vendor bytes and licenses

All six reference archive paths contain real upstream release archives, not placeholders. No Kubernetes binary was executed.

- Grafana: three same-named archives from the project's existing official **v2.2.0** bundle. The reference uses v2.0.0; versions/content intentionally differ while paths match. The existing fourth Linux ARM64 archive remains at mcp/grafana/vendor and was not added to the exact plugin tree.
- Kubernetes: three official containers/kubernetes-mcp-server **v0.0.67** release bundles. Download URLs, sizes and SHA-256 are pinned in mcp-servers/vendor/manifest.json and match the reference pins.
- Both projects use Apache-2.0. Grafana archives contain their upstream LICENSE. The retained standard Apache license at third_party/openshift-hypershift/LICENSE supplies a license copy; upstream copyrights and notices remain with their archives. The original SDS hypershift skill and agent do not copy upstream prose.
- The reference's bespoke brain code has no blanket root LICENSE. Its code was not copied. The reference root NOTICE was reviewed; it attributes upstream HyperShift derivatives, documentation mirrors and the bundled vendors.

Verify, without extracting or executing:

    python3 plugins/team-brain/mcp-servers/launch.py --check
    python3 scripts/check_plugin_layout.py

Kubernetes remains disabled in .mcp.json and launch.py refuses to run it, even when a bundle is present. A later integration needs explicit scope, backend permissions, schema review and target-host acceptance. Its presence does not indicate a Kubernetes deployment.

For Grafana, prefer the existing approved profiles and acceptance steps in [mcp/grafana/README.md](../mcp/grafana/README.md). The optional command launch.py grafana delegates to that canonical launcher, fixing its read-only flags, archive/executable verification, HTTPS/CA settings and credential rules. The plugin's default MCP configuration does not activate it.

## Podman knowledge process

The reference Containerfile path is retained. Build from the **repository root**, using an approved Python image already present on the internal host:

    podman build --pull=never --build-arg SDS_PYTHON_IMAGE=registry.internal/approved/python:3.12 -f plugins/team-brain/mcp-servers/team-knowledge/Containerfile -t localhost/sds-team-knowledge:0.4.0 .
    podman run --rm -i --network=none --read-only --security-opt=no-new-privileges --cap-drop=ALL -v "$SDS_BRAIN_DIR:/data/brain:ro,Z" localhost/sds-team-knowledge:0.4.0 --check

Replace the example image with your approved digest and confirm UID 65532 has read access. Use the correct SELinux labeling for your organization's mount policy; do not relabel shared data without approval. No pip installation or runtime source fetch is used. This example tests local corpus validation and is not a deployed MCP service. The stdio process needs an MCP client to communicate over stdin/stdout. RHOKP setup remains separate under mcp/okp/.

## Verification scope

The parity checker rejects missing paths, extra paths, wrong file/directory types and links, and verifies six archive sizes/checksums. Python regression tests exercise a cached plugin location, explicit-root failure, fixed private context and MCP initialize/initialized/tools/list/search/ping. Shell hooks/draft behavior is checked on Bash when available. No infrastructure binary, production endpoint or hosted model was invoked by those tests.

# SDS Storage Brain

A source-backed operational brain for **Ceph/RGW, S3, NetApp StorageGRID, RHEL, HPE hardware, Grafana, custom exporters, Elasticsearch and Objectify**.

Version **0.4.0**, reviewed **2026-11-10**. A working repository foundation for Claude Code and multiple customer environments. Infrastructure integrations are read-only. It includes local retrieval, an installable local Claude plugin, a self-contained SQLite document index, an Objectify adapter with fail-closed defaults, offline Grafana packaging, optional Red Hat OKP MCP deployment templates, researched operational content, import tooling and tests. No customer system has been contacted.

The [Word installation and user guide](docs/SDS_Storage_Brain_Installation_and_User_Guide.docx) covers clean offline transfer, internal installation, customer profiles, Grafana, both RHOKP deployment paths, approved imports and daily investigations.

## What is included

| Component | Delivery |
|---|---|
| Agent instructions | `AGENT.md`, loaded by Claude Code through `CLAUDE.md`; portable `AGENTS.md` wrapper |
| Claude plugin | `plugins/team-brain/` preserves the reference plugin's exact 29-file path hierarchy, with SDS implementations and verified archives; [installation and behavior](docs/PLUGIN.md) |
| SQLite document index | `data/sds-brain.db` stores document text, full-text indexes, source metadata and original document assets; [schema and queries](docs/SQLITE.md) |
| Official source catalog | Version/scope/access/verification metadata in `sources/*.json`, readable in `docs/SOURCES.md` |
| Offline vendor knowledge | 2,608 searchable vendor documents, including 109 catalog-target captures and 2,499 versioned StorageGRID pages; originals, hashes and legal notices retained |
| Operational content | Original knowledge pages and read-only runbooks for the priority incident paths |
| Local knowledge MCP | Python stdlib BM25 search, bounded document reads, source listing and fixed private context |
| Objectify MCP | Context-bound adapter; only status is enabled until the real API contract and authorization are reviewed |
| Grafana integration | Four official v2.2.0 release archives, an offline launcher, checksum verification and private-session configuration; credentials are supplied internally |
| Red Hat OKP MCP | Optional HTTP client profiles and Linux/Podman templates for an existing or new RHOKP portal; images/content are prepared separately |
| Internal documentation | Local reviewed-export importer for HTML, text, Markdown and Confluence page JSON |
| Team memory | Incident, knowledge, runbook and metric-contract templates; review and stale-document workflow |
| Validation | Unit/regression tests, retrieval acceptance checks, source/frontmatter/link validation, CI example |

This is an SDS implementation based on the architecture in [team-redbull/redbull-brain](https://github.com/team-redbull/redbull-brain). It preserves that repository's plugin file hierarchy while retaining SDS storage policy and the existing project. It does not import the reference team's fleet assumptions or enable Kubernetes access by default. Local skills and hooks support lookup and reviewed knowledge capture. There is no complete git-history mirror or shared HTTP deployment. Public vendor text snapshots are bundled; [offline coverage and the 39 unavailable catalog targets](docs/OFFLINE_KNOWLEDGE.md) are recorded explicitly. See `docs/REVIEW.md` for review findings and reference-project comparison.

## Start locally

Requirements: **Python 3.9+**, an approved Claude Code installation and its permitted model connection. The stdlib knowledge/Objectify servers require no pip packages, embedding model or vector service. The added SQL index uses Python's bundled `sqlite3` with FTS5; no database server is required. Tests use Python stdlib; one Objectify transport test uses a loopback-only HTTP server.

Optional OKP deployment additionally requires a Linux/Podman host and prepared upstream images. Its upstream application uses Python 3.12+ inside the container; it does not change the Python requirement for SDS local retrieval. See the [MCP integration map](mcp/README.md).

From the extracted repository, using a Linux/WSL shell:

```bash
export SDS_BRAIN_DIR="$PWD"
python3 scripts/brain.py validate
python3 scripts/check_repository.py
python3 -m unittest discover -s tests
python3 scripts/acceptance.py
python3 mcp/knowledge/server.py --check
claude
```

In Claude Code, inspect `/memory` to confirm `CLAUDE.md` and its `AGENT.md` import, then `/mcp` to check `sds-knowledge`. The committed `.mcp.json` contains only the local knowledge server. Follow your organization's normal client trust process. [Claude project instructions](https://code.claude.com/docs/en/memory) and [MCP setup](https://code.claude.com/docs/en/mcp) are the configuration references.

If your client policy does not load project MCP configuration, add the same server in local scope:

```bash
claude mcp add --transport stdio --scope local sds-knowledge -- python3 "$SDS_BRAIN_DIR/mcp/knowledge/server.py" --root "$SDS_BRAIN_DIR"
```

This alternative writes local Claude configuration; choose one route rather than creating duplicate server entries. Run the local knowledge search without Claude when useful:

```bash
python3 scripts/brain.py search "Ceph slow operations recovery backfill"
python3 scripts/brain.py search "StorageGRID capacity metadata"
python3 scripts/brain.py search "SignatureDoesNotMatch"
```

The optional `--version` search filter matches stored metadata text. For the current RHCS runbooks, use `--version rhcs-8.1`; a patch token such as `rhcs-8.1z9` does not automatically match `rhcs-8.1`. Keep the exact installed build in the investigation context and check its release notes separately. An empty filtered search is not evidence that the product lacks documentation.

Example request to Claude: “Use SDS Brain to prepare a read-only investigation of slow S3 requests. Ask for the customer/cluster context and distinguish Ceph RGW from StorageGRID. Cite the relevant runbooks and show which evidence is still missing.”

## Plugin and SQLite entry points

Use [the local plugin guide](docs/PLUGIN.md) to load or install `plugins/team-brain`. Its path set is checked against the pinned reference tree; source content is adapted for the SDS operating boundaries. Avoid launching both the default local MCP profile and a duplicate plugin knowledge server in the same session unless that is intentional.

The added database is `data/sds-brain.db`. Existing Markdown, vendor snapshots, raw original assets, configurations and tools remain in place. [The SQL guide](docs/SQLITE.md) explains plain-language search, source/version filters, SQL queries, schema inspection and rebuilding after document changes. The database contains captured content; the 39 unavailable catalog sources remain marked as references rather than invented document bodies.

## Your environment

`config/reported-fleet.json` preserves the supplied inventory: RHCS 7.1z7, 8.1z3, 8.1z6–z9; StorageGRID 11.8/11.9/12; RHEL 9.6/9.8; candidate HPE XL420/XL170r/XL190r and DL385 families; Grafana/custom exporter/Elasticsearch. These are **fleet-level reports**, not verified per-cluster mappings. StorageGRID 12's minor, hardware generations and monitoring versions remain unresolved.

Fill `config/context.example.json` privately for each customer/cluster. Use separate restricted checkouts and fresh Claude sessions per customer. The included knowledge process can be bound to one exact context:

```bash
python3 mcp/knowledge/server.py --root "$SDS_BRAIN_DIR" --customer customer-a --cluster cluster-a --check
```

That process can index only shared knowledge plus `private/customer-a/cluster-a/{knowledge,runbooks,incidents}/`. Private pages must declare matching `customer` and `cluster` frontmatter. The `--check` command exits after validation; it does not change the shared-only server in `.mcp.json`.

To launch Claude with the bound private knowledge server, use the supplied configuration in the selected customer's restricted checkout:

```bash
export SDS_CUSTOMER=customer-a
export SDS_CLUSTER=cluster-a
cp config/knowledge-private.example.json config/mcp.private.local.json
claude --strict-mcp-config --mcp-config config/mcp.private.local.json
```

The copy is ignored by Git. Keep `SDS_BRAIN_DIR` set to this checkout, use the verified aliases, and start a fresh session when changing customer. This profile enables the bound knowledge server only. Add Objectify/Grafana entries to this same local configuration after their acceptance checks. Confirm effective servers with `/mcp`; organization-managed policy remains authoritative. The flags follow the official [Claude CLI reference](https://code.claude.com/docs/en/cli-reference); native client acceptance remains untested here.

Filesystem permissions and backend authorization are still required; process filters do not isolate other tools or the model's conversation history. See `docs/ARCHITECTURE.md`.

## Objectify

The screenshot identifies candidate API routes. The shipped configuration deliberately enables only `objectify_status`:

```bash
python3 mcp/objectify/server.py --config mcp/objectify/config.example.json --check
```

To activate approved reads later, provide `/openapi.json`, authentication details, an approved internal CA/origin, safe response fields and proof of customer/cluster authorization. Follow `docs/objectify-integration.md`. All mutations and ambiguous `GET /account/parlay` remain excluded. The adapter never guesses `obj_acc` path-parameter semantics. No internal connectivity is claimed.

## Grafana and Elasticsearch

The official Grafana MCP **v2.2.0 is bundled** for Linux x86-64/ARM64, macOS ARM64 and Windows x86-64. Its Python launcher verifies the local archive and executable, then runs the fixed read-only stdio profile. No download, package manager or container pull is needed inside the internal network. This implements the reference repository's vendoring approach with the already selected SDS release. Elasticsearch is explicitly enabled; Prometheus remains conditional until confirmed.

```bash
python3 scripts/vendor_grafana.py --check
python3 mcp/grafana/launch.py --check
```

Supply the approved internal HTTPS URL and scoped service-account token through `SDS_GRAFANA_URL` and `SDS_GRAFANA_TOKEN`. If needed, set `SDS_GRAFANA_CA_FILE` to the approved private CA bundle. With `SDS_BRAIN_DIR`, `SDS_CUSTOMER` and `SDS_CLUSTER` also set, the combined private profile is ready to copy:

```bash
cp config/knowledge-grafana-private.example.json config/mcp.private.local.json
claude --strict-mcp-config --mcp-config config/mcp.private.local.json
```

Use this copy step for a new local profile; preserve any approved Objectify/custom entries when updating an existing one. Read `mcp/grafana/README.md` and `docs/observability-integration.md` for setup, internal acceptance and connected-host-only updates. The offline package does not supply credentials, datasource permissions or a model endpoint. The Grafana integration remains unconnected to your infrastructure.

## Red Hat Offline Knowledge Portal MCP

The optional `sds-okp` connection follows the reference repository's separate Red Hat `okp-mcp` container architecture. Choose the [Linux/Podman existing-portal or new-portal setup](deploy/podman/README.md), then use [knowledge + OKP](config/knowledge-okp.example.json) or the [private knowledge + Grafana + OKP profile](config/knowledge-grafana-okp-private.example.json).

The committed default stays local-knowledge-only. The optional profiles connect to host loopback; they do not install or start services. Prepared image artifacts and any entitled RHOKP content are separate prerequisites. The [OKP integration guide](mcp/okp/README.md) records exact settings, source provenance and the Ceph/RHCS applicability check. RHEL-oriented result labels do not prove that the actual portal covers RHCS.

## Import your existing knowledge

Read `docs/IMPORTING.md` before importing the Red Hat corpus or Confluence exports. The importer uses local files only, preserves source hashes and version metadata, and requires an explicit completed-review acknowledgment. Customer content goes into the exact private context; vendor documentation shared across a team must retain its permitted audience.

The catalog records links and source metadata. Separately, the project now bundles **2,608 searchable vendor text documents** under `knowledge/vendor/`, with original captures under `vendor-sources/`. [The offline knowledge report](docs/OFFLINE_KNOWLEDGE.md) distinguishes document bodies, index pages, versioned StorageGRID repositories and the 39 unavailable targets. This remains partial vendor coverage; private Confluence content, dashboard exports, the custom exporter schema and the full internal Red Hat corpus were not supplied.

## Keep the brain useful

Use `templates/` for new findings. Review raw evidence privately, search for an existing page, then submit a scoped change for human review. Do not mark an assumption verified because it was generated confidently.

```bash
python3 scripts/brain.py stale --days 90
python3 scripts/brain.py index
python3 scripts/brain.py validate
python3 scripts/brain.py index --check
python3 scripts/check_repository.py --manifest
python3 -m unittest discover -s tests
python3 scripts/acceptance.py
```

`INDEX.md` and `docs/SOURCES.md` are generated. `docs/VALIDATION.md` records what was tested and what remains unverified. `docs/COVERAGE.md` distinguishes implemented behavior, configured candidates and missing internal evidence.

## Protocol and deployment limits

The two SDS Python stdio servers (knowledge and Objectify) support **MCP 2025-11-25 only**. The separately bundled official Grafana server negotiates its own supported revision. Older/newer initialize requests receive that revision as a counteroffer; a client must accept it or disconnect. The servers do not implement older batch-message requirements or the newer stateless-only protocol. Native Claude integration must be tested against your installed build. No generic SSH executor, live Ceph/StorageGRID/HPE MCP, automatic web crawler or shared HTTP service is shipped. Diagnostics for those systems are documented read-only procedures.

If a supported Claude Code build fails protocol discovery, its [MCP documentation](https://code.claude.com/docs/en/mcp) describes starting with `MCP_PROTOCOL_NEGOTIATION=legacy claude`. This setting affects every MCP server in that session. It has not been tested here with the native client.

Local retrieval works without internet. Claude Code still needs its authorized model endpoint; this repository does not turn Claude into an offline model. Integrations run where internal network access already exists. No cloud publication, production installation, scheduled synchronization or secret provisioning was performed.

# Validation record — reviewed release 0.4.0

Date: **2026-11-10**. Runtime: bundled Python 3.12 on Windows. The full suite was run with bytecode disabled and `TMP`/`TEMP` pointing to an ignored project-local work directory because the sandbox's default temporary-directory ACLs prevented fixture writes.

| Current check | Result | Scope |
|---|---|---|
| Full unit/regression suite | **199 tests: 185 passed, 14 skipped, 0 failures/errors** | The skips are 10 denied symbolic-link fixtures, two denied hard-link fixtures, one denied loopback connection and one Bash initialization denial; these tests are not counted as passed |
| Priority retrieval acceptance | **7/7 passed** | Six original incident queries plus OKP/RHOKP Ceph applicability |
| Source/frontmatter/link validation | **Passed** | 2,639 knowledge/runbook/vendor pages and 148 source records |
| Offline vendor capture integrity | **5,216 hashes passed** | Original captures and searchable derivatives; exact source and repository provenance retained |
| Offline source-body retrieval | **13/13 passed** | Distinctive vendor body text read after search, including all three StorageGRID editions; catalog-only matches do not satisfy the checks |
| Full repository hierarchy and config check | **Passed** | Required files/dirs, public JSON, root/subdirectory Markdown links, canonical entry points and MCP targets/HTTP URL syntax |
| Generated indexes | **Regenerated and checked** | Stable ordering, LF output and source check-date range |
| Release integrity manifest | **Regenerated and checked** | Current distributable files; runtime/private/work files excluded |
| Grafana offline archive verification | **4/4 passed** | Existing v2.2.0 archive pins; no Grafana executable launched |
| Exact plugin path parity | **29 files, 18 subdirectories; passed** | Complete non-truncated reference tree at `cd866d4ee510b299c415f92a90b7f525d30cf04c`; no missing/extra paths or wrong types |
| Plugin archive verification | **6/6 passed** | Three Grafana v2.2.0 archives and three Kubernetes v0.0.67 bundles; sizes/SHA-256 checked, actual tar/ZIP containers inspected; no vendor executable launched |
| Plugin MCP adapter | **Passed** | Cached install location, explicit root, startup validation, initialize/initialized/list/search/ping, fixed private context and cross-context refusal |
| Bash hooks and drafts | **Passed separately using bundled GNU Bash** | Requires MSYS initialization unavailable in the managed test run; local session/stop hooks, shell syntax, draft creation and overwrite rejection tested without network/Git writes |
| SQLite fixtures | **11 tests: 10 passed, 1 hard-link capability skip** | Unicode/body and DOCX round trips, original BLOB bytes, FTS filters/pagination, read-only SQL, integrity/tampering, stale records, atomic failure recovery, private/staging exclusions and rich YAML scope regression |
| Actual SQLite snapshot | **Recorded in `SQLITE_BUILD_REPORT.json`** | Final counts, document/asset hashes, source availability, SQLite/FTS integrity and public-input freshness; use `scripts/sqlite_brain.py check --fresh` to reproduce |
| Existing-project preservation | **Independent review recorded with SQL build** | All 5,615 previous manifest paths must remain; exact plugin parity, excluded-path checks, source/body/asset hashes and unchanged database after read-only review |
| Word guide | **13 pages rendered and visually inspected** | Version 0.4.0, local plugin setup and SQLite use added; native local Word PDF export followed by document-skill rasterization |
| OKP deployment review | **Static review only** | Profiles, relative paths, Podman 4.6.1 keys, internal/loopback networking, offline pull policy, placeholders and source provenance |

Earlier regression coverage checks the complete serialized knowledge ToolResult limit, portable generated indexes, stale-file detection, partial repository roots, config targets, malformed HTTP profiles and manifest tampering. The offline expansion added four vendor-status fixtures and five document/edition diversity cases. The current addition supplies eight plugin tests and eleven SQLite tests, with scope checks covering both ordinary and rich plugin frontmatter. The knowledge response-size reproduction and corrections are in [REVIEW.md](REVIEW.md).

No OKP/RHOKP image, Linux Podman generator, portal content/entitlement, actual internal URL or native Claude client was tested. Image preparation, disconnected first-start behavior and known RHCS document retrieval require acceptance inside the intended network. The upstream source review does not verify a published image digest.

Reproduce the local checks:

```bash
python3 scripts/brain.py validate
python3 scripts/brain.py index --check
python3 scripts/check_repository.py --manifest
python3 -m unittest discover -s tests
python3 scripts/acceptance.py
python3 scripts/verify_offline_knowledge.py
python3 scripts/vendor_grafana.py --check
python3 scripts/check_plugin_layout.py
python3 plugins/team-brain/mcp-servers/launch.py --check
python3 scripts/sqlite_brain.py check --fresh
```

The SQL build and its generated report are additional artifacts. The report and release manifest are excluded from the database fingerprint to avoid self-reference. Finish documentation, code, Word-guide and generated-index edits first, build/check the database, then regenerate the release manifest. The 39 unavailable source records remain explicit gaps; a successful database check does not turn their references into saved full manuals.

## Historical v0.2.0 validation

The remaining record preserves the earlier Linux results. It is not a rerun of the skipped Windows capabilities or proof of current infrastructure access.

Date: **2026-11-09**. Runtime used: **Python 3.12.14 on Linux**. All 12 Python files also passed parsing with Python 3.9 grammar. A separate 3.9 interpreter was not available for execution testing.

## Local checks completed

| Check | Result | What it establishes |
|---|---|---|
| Unit and regression suite | 154 tests passed | 68 knowledge/import, 65 Objectify and 21 Grafana launcher/vendor tests; synthetic/local fixtures; 30 tests added after v0.1.1 |
| Priority retrieval acceptance | 6/6 passed | Expected procedures appear in the top three returned chunks for selected incident queries |
| Source/frontmatter/link validation | Passed | Required metadata, source-ID resolution, current date fields and explicit local links |
| Source inventory | 144 references, 144 unique URLs | Catalog deduplication and recorded verification/access status |
| Objectify default startup | Passed; disabled/status only | No network check performed; no live operations exposed |
| Knowledge server local startup | Passed | Corpus can be indexed and described without infrastructure access |
| Stdio protocol exchanges | Passed in subprocess tests | MCP 2025-11-25 negotiation, metadata, known/unknown error IDs, malformed-input recovery, tool discovery and bounded requests |
| Private knowledge profile | Arguments expanded and server check passed; empty supplied scope refused | Correct customer/cluster binding; native Claude flags were not executed |
| Offline Grafana archive set | Four archives and four executable hashes verified | Exact official v2.2.0 release bytes are bundled for the selected platforms |
| Grafana launcher check | Passed without credentials or network | Selected archive/cache verification and extraction work locally |
| Grafana native Linux x86-64 | Version/help, MCP initialize, 11 read-only tools and ping passed | Direct binary and actual launcher process tested; no tool call or customer endpoint used |
| Static configuration | All JSON files and both CI YAML definitions parsed | Syntax only; neither external CI runner was executed |

## Important regression coverage

Knowledge tests exercise customer/cluster separation, traversal rejection, source/document symlinks, bounds, source pagination and retrieval. Import tests cover review requirements, Confluence/HTML extraction, secret-bearing titles/bodies, symlinked inputs/outputs, preflight conflict detection and private scope preservation.

Objectify tests cover disabled mode, fixed operations, mutation/parlay rejection, pinned OpenAPI verification, supported scalar constraints, mandatory response scope markers, conservative output projection, credential redaction, response limits, refusal of redirects, unknown upstream list completeness and recovery after deeply nested malformed JSON. One HTTP test uses a loopback server only; no vendor or internal endpoint is contacted.

The review identified defects in the first implementation, then added regression cases before fixing them. These included symlink containment, partial imports after a known conflict, secret-bearing titles, single-record response scope, incomplete schema constraints and misleading list completeness.

The additional review requested after delivery found Confluence CDATA command loss, rendered-import size overflow, unbounded returned metadata, generated-index link overwrites, a hash/conversion reread race, request metadata rejection, Unicode stdout crashes, unsafe configured-pattern backtracking, mixed enum typing, exponent overflow and overclaimed protocol revisions. Regression tests cover the corrections. Both servers now advertise only MCP 2025-11-25 and omit unreadable error IDs. See [REVIEW.md](REVIEW.md) for impact, corrections and remaining gaps.

Local `jq` fixtures also verified the corrected Ceph `stuck_pg_stats` envelope: populated/empty valid objects succeed; invalid envelopes fail; a 35-PG fixture returns a 20-entry projection with the original count. The StorageGRID policy-tag correction was checked against versioned NetApp documentation. These are procedure/content checks, not production execution.

Ten additional symptom-oriented searches covered recovery, daemon restarts, S3 authorization/checksums/TLS, ILM, quota, hardware, Elasticsearch and Linux memory. The expected procedure was among the first three distinct documents in the six returned chunks for each query. Exact queries and observed results are recorded in [REVIEW_CHECKS.json](REVIEW_CHECKS.json). This limited sample does not measure general recall, corpus completeness or correctness of a generated answer.

The fresh second review added regressions for empty startup scope, empty private markers in shared files, Objectify output/discovery amplification and accumulated pattern-validation work. The Grafana tests cover safe extraction, archive/cache corruption, offline checks, platform selection, explicit credentials/CA, ambient Grafana/telemetry/proxy removal, process dispatch and bounded mocked downloads. Full results and the exact 11-tool native smoke record are in [GRAFANA_OFFLINE_CHECKS.json](GRAFANA_OFFLINE_CHECKS.json).

## What was not tested

- Claude Code was not installed in this build environment. `/memory`, `/mcp`, native client negotiation and the real user's client settings require local acceptance.
- No Objectify authentication, internal DNS/CA, live route, tenant permission or real response schema was exercised.
- No live Grafana/Elasticsearch query, internal CA or service-account authorization was tested. Linux ARM64, macOS ARM64 and Windows x86-64 archives/executable hashes were verified but their binaries were not executed. The native Linux test used a synthetic loopback URL and sent only initialization, tool-list and ping messages.
- The maintained connected-host download script was tested with synthetic transport responses; actual release downloads were completed during packaging and verified separately. No package manager or runtime download is needed internally.
- No Ceph, StorageGRID, RHEL or HPE commands were run on customer infrastructure. Runbooks are documented proposals, not fleet-tested repair procedures.
- No internal Confluence pages, full Red Hat exports, dashboard JSON, exporter code or prior incidents were imported.
- CI definitions were prepared but not executed on a GitHub/GitLab runner. The GitLab example requires a vetted `SDS_CI_IMAGE`.

## Reproduce

```bash
python3 scripts/brain.py validate
python3 -m unittest discover -s tests
python3 scripts/acceptance.py
python3 mcp/knowledge/server.py --check
python3 mcp/objectify/server.py --config mcp/objectify/config.example.json --check
python3 scripts/vendor_grafana.py --check
python3 mcp/grafana/launch.py --check
```

These checks establish local software behavior within the tested cases. Production authorization and operational accuracy still depend on verified inventory, source applicability and the internal acceptance plan.

# Self-review — SDS Storage Brain 0.4.0

Review date: **2026-11-10**. This release adds the requested local plugin hierarchy and a persistent SQLite document snapshot, preserving the existing project. The public reference was rechecked at commit `cd866d4ee510b299c415f92a90b7f525d30cf04c`; the complete tree is retained in [PLUGIN_REFERENCE_TREE.json](PLUGIN_REFERENCE_TREE.json).

## Plugin hierarchy and behavior

`plugins/team-brain/` has exactly the reference's **29 files and 18 subdirectories**. The comparison checks every relative path and file/directory type, rejects missing or extra entries and links, and verifies all six real vendor archive hashes. Supporting documentation, the marketplace manifest and checks live outside this exact tree. Kubernetes v0.0.67 archives match the reference pins; the three Grafana paths use the existing SDS v2.2.0 bytes. Runtime content is an original SDS adaptation, with these deliberate behavior choices:

- The default plugin starts local knowledge only and delegates to the existing SDS server. Installed copies require an explicit absolute `SDS_BRAIN_DIR`; customer/cluster aliases stay fixed at startup.
- Local hooks provide reminders; learning/incident drafts require review. No automatic Git pull, push, transcript capture or shared promotion occurs. Draft staging roots are excluded from the shared SQL snapshot and release manifest.
- Kubernetes remains disabled and its launcher refuses execution. The retained HyperShift filenames do not establish a deployed SDS environment. Optional Grafana delegates to the existing verified read-only launcher.

The reference code has no blanket root license, so its bespoke implementation was not copied. Original vendor archives retain their upstream notices; a standard Apache license is retained at the reference license path. See [PLUGIN.md](PLUGIN.md) for installation, provenance, packaging and runtime limits.

## SQLite document snapshot

`data/sds-brain.db` is additive. It stores actual public document bodies, a full-text FTS5 index, metadata/version/source relations and original document assets as BLOBs. The 148 catalog references remain separate rows, including the 39 unavailable targets with their actual capture status. No body is fabricated for those gaps. Existing Markdown, vendor originals, configuration and tools remain on disk.

The builder uses a temporary sibling file, a transaction, integrity checks and atomic replacement. Search/read helpers use read-only SQLite connections, parameterized inputs and bounded results. Rebuilding removes obsolete index records while preserving source files. Stored source/body/asset hashes and a public-input fingerprint support integrity and freshness checks. DB files, sidecars, release manifests and generated SQL build reports are excluded from the corpus to avoid indexing itself.

Independent review caught missing staging/import exclusions and Windows case differences before the final build. The scanner now excludes `docs/imported`, private/local/customer inputs, draft staging, runtime executables/archives, work and caches; hardlinked public inputs are rejected. Original vendor assets are retained without adding a duplicate raw corpus to FTS; the normalized vendor text is searchable. The Word guide's main paragraphs and table text are indexed, with the original DOCX retained as an asset. The existing MCP still uses its in-memory search; this SQL snapshot has a separate CLI and direct SQL interface.

A rich plugin-frontmatter fallback initially discarded a `scope: private` marker. Scope/customer/cluster declarations are now checked before that fallback, with six forms independently retested. The existing incident template is retained as configuration only when its known dummy aliases and replacement ID/title are intact; placeholder scope fields are labeled inside template metadata. Changed customer aliases or a real incident ID are rejected. SQL guide examples were executed against the fixture database; the nonexistent sample path and an unsuitable aggregate FTS query were corrected before release.

See [SQLITE.md](SQLITE.md) for schema and commands and `SQLITE_BUILD_REPORT.json` for the final actual counts and verification. [VALIDATION.md](VALIDATION.md) records the combined checks. Native Claude installation, Linux container execution, Kubernetes binaries and customer infrastructure were not exercised. The Word guide was updated, rendered through local Word PDF export and the document skill rasterizer, and all 13 pages were visually inspected.

## Historical review — v0.3.0

The following record describes the earlier OKP integration and offline knowledge work; its counts and limits refer to that release unless superseded above.

Review date: **2026-11-10**. The requested OKP MCP integration and repository self-review are complete for local source/configuration work. No service was deployed and no customer infrastructure was accessed.

## Offline knowledge expansion

The later request to save the actual knowledge added 2,608 searchable vendor documents. The capture covers 109 catalog targets (89 bodies/files and 20 explicit indexes) plus 2,499 versioned StorageGRID pages. Raw captures, hashes, pinned repository commits, notices and derivative transformations are retained. The 39 unavailable targets are reported without fabricated contents; authorized internal Red Hat exports remain unavailable here. Full details are in [OFFLINE_KNOWLEDGE.md](OFFLINE_KNOWLEDGE.md).

Larger-corpus acceptance exposed search crowding: repeated chunks and the same vendor chapter in alternate editions pushed the StorageGRID capacity runbook from the initial top three. Search now first selects different documents and explicitly identified documentation families, then backfills remaining matches under the existing two-chunk cap. Requested version filters apply first; editions remain separate and no scores/boosts were changed. Five focused regression tests and all seven actual-corpus priority checks passed.

The status response now reports actual vendor snapshot document/source/repository counts instead of a hardcoded absence of vendor manuals. Four fixture tests cover the distinction. The offline verifier checked 5,216 original/derivative hashes and passed 13 searches followed by actual source-body reads, including distinct 11.8, 11.9 and 12.0 queries. Images and external AsciiDoc targets remain outside the text snapshots.

## Changes and findings

| Finding | Correction | Evidence |
|---|---|---|
| OKP integration missing | Added optional client profiles, Linux/Podman templates for an existing or new RHOKP portal, pinned upstream source evidence, and a searchable applicability page | Local paths/JSON verified; independent comparison against pinned Red Hat source; target Linux runtime acceptance remains open |
| Knowledge result size measured before outer JSON escaping | Measure the complete serialized tool result against 256 KiB | A valid synthetic catalog produced a 479,694-byte result before the fix; three new tests verify rejection, smaller pagination and preserved Unicode |
| Generated index order depended on operating system | Sort relative POSIX paths explicitly and write LF output | Regression checks cover mixed-case filenames and read-only stale-index detection |
| Content-only validation could accept an empty/partial project | Added a separate full repository checker for required files/directories, JSON, local links, entry-point pointers, MCP script targets and HTTP profile syntax | Missing-root/target, malformed JSON/HTTP, broken-link and manifest-tampering tests; content validation remains usable for isolated corpora |
| Test fixtures assumed Linux link privileges and path syntax | Use platform-native path expectations and skip only denied link/socket fixture creation | Final Windows run: 171 tests, 159 passed, 12 capability skips, no failures/errors |
| New deployment templates initially used newer naming keys | Removed `NetworkName`/`VolumeName` overrides to match the cited Podman 4.6.1 baseline | Static review against primary Quadlet reference; references use their `.network`/`.volume` unit names |
| OKP acceptance text initially implied local citation URLs | Documented canonical public Red Hat citations and acceptance by document ID/offline MCP retrieval | Upstream document formatter inspected; HTML mirror setting does not rewrite citations |
| Source catalog header and import handoff could imply stale current facts | Derive catalog check-date range, update current coverage/version and label original import evidence as historical | 148 unique source URLs: 142 opened, 5 search-verified, 1 unverified; four new source records were actually reviewed |

## Hierarchy reviewed

```text
AGENT.md / AGENTS.md / CLAUDE.md   canonical policy and client entry points
config/                          shared/private and optional MCP profiles
knowledge/ / runbooks/            curated technical content
sources/                         structured official-source catalog
mcp/knowledge/                   local stdlib retrieval server
mcp/objectify/                   disabled-by-default internal API adapter
mcp/grafana/                     offline launcher and existing vendored archives
mcp/okp/                         integration guide and pinned source-review provenance
deploy/podman/                   existing/new portal templates and installation guide
scripts/                         validation, indexing, import and packaging checks
tests/                           regression cases and seven retrieval checks
docs/                            architecture, coverage, evidence and current review
```

The default client configuration still starts shared local retrieval only. Optional OKP HTTP profiles do not provision Podman or modify Ceph. Runtime image placeholders remain intentionally unconfigured; they require the operator's actual approved images. Secrets and local/generated work are excluded from the shared package.

## Verification and limits

See [VALIDATION.md](VALIDATION.md) for the current execution record. Required hierarchy, public JSON, local Markdown links and MCP references passed. The generated indexes and release manifest were refreshed after edits. The four bundled Grafana archives still match their existing pins.

No Linux Podman/Quadlet generator, OKP/RHOKP container, entitlement activation, internal portal query, native Claude connection or Ceph cluster was exercised. The 12 skipped tests require unavailable filesystem-link or loopback socket capabilities; they remain active on a capable host. The prior source catalog and runbook claims were not all re-researched during this pass.

The upstream OKP code is RHEL-oriented and can mislabel applicability; a known RHCS document and exact product/version must be checked in the actual portal. Source pinning is distinct from image pinning. These unresolved deployment inputs are documented rather than represented as a working live connection.

## Historical review — v0.2.0

The remaining sections preserve the earlier review record; their test counts and runtime observations refer to v0.2.0.

### Review findings and offline Grafana correction

Review date: **2026-11-09**. Reviewed release: **v0.2.0**. First review: v0.1.0 → v0.1.1. Fresh second review: v0.1.1 → v0.2.0, including the user's explicit requirement to ship Grafana MCP for an internal network without runtime downloads.

## v0.2.0 verdict

The second review found and fixed **five additional code defects**: two scope-validation gaps in knowledge loading, and three Objectify availability/output problems. The prior 124 passing tests had not covered them. The v0.2.0 suite passed **154 tests**: 68 knowledge/import, 65 Objectify and 21 Grafana packaging/launcher tests. The findings below are reproducible local failures, not claims of a production exploit or a customer incident.

The user's Grafana correction was also necessary. v0.1.1 supplied only release metadata and an external executable path; that was insufficient for the stated internal-network deployment. v0.2.0 carries the actual four official Grafana MCP v2.2.0 release archives, a local verifying launcher and a combined private-session configuration. It follows the reference repository's offline packaging approach. No internal endpoint, credential or customer record was used during this work.

This remains a working foundation for controlled internal evaluation. Full reference-project parity, native Claude acceptance, the actual Objectify contract, customer inventory and the internal documentation corpus are not complete. Bundling Grafana removes the download dependency inside the network; it does not establish backend authorization or live query correctness.

## Second-review findings corrected

| ID / severity | Reproduction in v0.1.1 | Correction and evidence |
|---|---|---|
| R14 — Low: private startup configuration | Explicit empty customer/cluster strings selected shared mode rather than rejecting a broken private launch. | Only omitted `None, None` selects shared mode; supplied values must both be valid nonempty aliases. CLI and library regressions confirm refusal. This reproduction did not disclose another customer's records. |
| R15 — Medium: document scope classification | Shared-path pages containing `customer: ""`, `cluster: ""` or empty arrays bypassed a truthiness-based placement guard. | Any customer/cluster metadata key in a shared path is rejected. Private markers must appear in the selected private tree with matching values. This cannot identify sensitive text that has no scope markers; review and filesystem isolation remain necessary. |
| R16 — Medium: Objectify result amplification | A 419,511-byte synthetic upstream response expanded to a 25,709,807-byte successful MCP reply through 32 repeated projections and duplicate text/structured representations. | Bound the complete ASCII-serialized tool-result object to 256 KiB, including both representations and escaping. Oversize results produce a short error without partial records. Numeric and Unicode regressions cover the amplification and continued operation. |
| R17 — Medium: Objectify accumulated validation work | A valid 9,311-byte response with 20 records, 32 string projections and `[a-z]{1,256}` took 18.358 seconds to project despite `max_records=1`. The finite-state matcher avoided backtracking but total repeated work was still excessive. | Share a conservative 2,097,152-unit validation-work budget across request and response patterns. Preflight before matching; check every returned record's scope first, including beyond the output limit. The reproduced workload was rejected in 0.000706 seconds on the review host. Timing is an observation, not a universal wall-clock guarantee. |
| R18 — Medium: Objectify discovery expansion | A scalar enum of 100 strings × 10,000 characters produced a 1,001,688-byte tool-list response; repeated references could expand it further. | Limit string enum members to the supported 256-character scalar input, and reject enabled configuration when its expanded discovery result exceeds 256 KiB. Test shared references and Unicode expansion. |

Nine focused tests were added for these code findings. The 21 new Grafana tests cover the additional offline implementation. Objectify's work/result limits fail with explicit errors rather than silently dropping fields or records. Narrow the reviewed upstream query, projection or output when a limit is reached.

## Offline Grafana correction

The reference brain stores compressed release archives beside a platform-selecting Python launcher and a hash manifest. Its current manifest pins Grafana MCP v2.0.0 for Linux x86-64, macOS ARM64 and Windows x86-64. SDS adopts that packaging model while keeping the separately selected official v2.2.0 and adding Linux ARM64. No executable was copied from the reference project's repository; all four archives were obtained from the official Grafana release and matched its published sizes and SHA-256 values.

| Delivered component | Current behavior |
|---|---|
| Four archives in `mcp/grafana/vendor/` | Complete official release bytes, with license material retained inside each archive |
| `mcp/grafana/release-manifest.json` | Pins archive and extracted-executable sizes/hashes and records observed verification |
| `mcp/grafana/launch.py` | Selects the platform, checks the archive, extracts only the exact regular executable member, verifies cached bytes and launches locally; no download or PATH fallback |
| Fixed launch settings | Stdio, writes disabled, anonymous usage reporting disabled, search/datasource/dashboard/Elasticsearch categories only |
| Explicit connection settings | `SDS_GRAFANA_URL`, `SDS_GRAFANA_TOKEN`, optional approved `SDS_GRAFANA_CA_FILE`; inherited Grafana, OTEL and proxy settings are cleared |
| Private profile | `config/knowledge-grafana-private.example.json` combines fixed private knowledge scope with the local Grafana launcher |
| Maintainer refresh | `scripts/vendor_grafana.py --download` is explicit connected-host preparation; internal checks use `--check` and local files only |

All four archives and all four extracted executable hashes were verified. On Linux x86-64, the official executable reported version 2.2.0 and completed MCP initialization, tool discovery and ping both directly and through the new launcher. The fixed profile exposed exactly **11 read-only tools**, including `query_elasticsearch`, and no mutation tools. Deliberately conflicting ambient Grafana credentials were not used. No tool call or customer endpoint was used; the process received only a synthetic loopback endpoint. Exact results are in [GRAFANA_OFFLINE_CHECKS.json](GRAFANA_OFFLINE_CHECKS.json).

The upstream initialization text generically mentions dashboard creation/update even with writes disabled. The tested tool list contains no corresponding mutation tools; the review records the actual exposed interface rather than treating that generic text as the access policy. Backend permissions remain required. Non-Linux-x86-64 binaries were byte-verified but not executed here.

## First-review findings retained

The following findings were fixed in v0.1.1 and remain regression-covered. They are historical findings from v0.1.0, not newly discovered in this pass.

Severity describes the observed impact within this local prototype, not a production exploit assessment.

| ID / severity | Defect in the initial release | Correction and evidence |
|---|---|---|
| R01 — High: content integrity | Confluence storage CDATA code blocks silently disappeared during import. A block containing `ceph -s` and `ceph health detail` retained only its language label. | Preserve literal CDATA text and code-body boundaries. Add table-cell separators. Regression imports the affected storage format and confirms commands survive. |
| R02 — Medium: import availability | An input just below 4 MiB became a rendered page above 4 MiB after its header was added. Import reported success, then the knowledge server refused it. | Validate rendered pages before writes; enforce input/output batch limits and document limits during staging. Oversize tests confirm refusal without output files. |
| R03 — Medium: output bounds | `brain_read(max_chars=1)` could still return more than 200,000 characters through unbounded metadata. | Bound title, metadata and source-record sizes; add a final 256 KiB serialized tool-content limit. Corpus accounting includes title and metadata. |
| R04 — Medium: unintended file overwrite | `brain.py index` followed an `INDEX.md` symlink and overwrote a file outside the repository. Direct writes also modified the other name of a hard-linked file. | Preflight both generated destinations, refuse symlinks and atomically replace directory entries. Regressions preserve the outside file and detect invalid inputs before index mutation. |
| R05 — Medium: provenance | The importer hashed one read of a source file, then reread it for conversion. A change between reads could detach the stored hash from the imported content. | Convert the exact bytes already hashed. A regression changes the original file before conversion and confirms consistent content and hash. |
| R06 — Medium: MCP interoperability | Both servers rejected legitimate object-valued `_meta` metadata on `tools/list`. | Accept standard metadata while retaining fixed tools and rejecting unissued pagination cursors. Add initialized-session protocol tests. |
| R07 — Medium: process availability | An escaped lone-surrogate request ID could trigger a UTF-8 stdout error and terminate a server. | Use ASCII-safe JSON wire output. Objectify additionally rejects invalid Unicode during parsing. Regressions send malformed/unusual input followed by a valid request and verify recovery. |
| R08 — Medium: Objectify availability | An accepted OpenAPI pattern such as `(a+)+$` could stall the sequential adapter on a short crafted value. | Use a bounded finite-state matcher for the documented pattern subset. Reject groups/alternation and other unsupported syntax. Test valid/rejected patterns, bounds and hostile values. |
| R09 — Low: scalar validation | Python equality allowed boolean/numeric confusion in mixed-type enum constraints; exponent overflow could bypass strict JSON finite-number checks. | Enforce declared scalar enum types and exact boolean/integer separation; reject non-finite exponent results. Add focused regressions. |
| R10 — Medium: Ceph procedure correctness | The three `ceph pg dump_stuck` filters expected a root array. Reef and Squid clients read `stuck_pg_stats` inside a root object. | Validate the actual envelope, then project a maximum of 20 PGs. Local `jq` fixtures cover populated/empty results, a 35-PG result and malformed envelopes. |
| R11 — Medium: StorageGRID diagnosis | ILM guidance referred to a single active policy without resolving the affected bucket's policy tag. | Resolve bucket tag to the assigned active policy; use the Default mapping only when applicable. Keep mapping evidence and stop placement conclusions when it is unresolved. |
| R12 — Low: private-context setup | Running the documented `--check --customer ... --cluster ...` command validated one process but did not change Claude's shared-only MCP connection. | Add `config/knowledge-private.example.json` and an explicit private-session launch using a local configuration. Native client acceptance is still required. |
| R13 — Medium: protocol claims and errors | The servers advertised older MCP revisions whose required behavior they did not fully implement, and emitted `id: null` for uncorrelated errors. | Support only MCP 2025-11-25; counteroffer it to other versions. Omit unreadable IDs and preserve valid readable IDs, including zero. Add negotiation and error-correlation regressions. |

Related corrections preserve quoted frontmatter values, reject nested frontmatter arrays, refuse malformed Confluence body/version shapes cleanly, and use exclusive import-manifest creation. The Ceph baseline now describes an initial snapshot accurately: its commands do not have hard output/time limits. Daemon version evidence points to the scoped cephadm procedure.

## Coverage and reference-project comparison

The repository contains 11 original knowledge pages, 19 read-only incident runbooks and 144 unique official documentation references. Their recorded verification status is 138 opened, 5 search-verified and 1 unverified. This second pass checked record counts and claims and rechecked targeted primary sources; it did not reread every chapter or download all vendor manuals. The Grafana catalog entry now points to the pinned v2.2.0 README.

Reported RHCS, RHEL and StorageGRID versions remain fleet-level statements, not a verified customer inventory. StorageGRID "12" still needs its exact minor/build. HPE family interpretations remain tentative. StorageGRID procedures primarily target 11.9 and need corresponding 11.8/12.x chapter checks before use. Prometheus remains unconfirmed.

| Reference capability | SDS v0.2.0 status |
|---|---|
| Versioned operational knowledge and runbooks | Present, tailored to the storage stack |
| Local keyword retrieval | Present, with fixed private scope and a narrower tool set |
| Offline Grafana executable packaging | Present, with four official archives and verifying local launcher |
| Installable Claude plugin | Absent; project instructions and explicit MCP profiles are supplied |
| Session hooks and automatic learning/capture | Manual workflow and templates only |
| Full documentation snapshots and source mirrors | Absent; source catalog plus reviewed local import tooling |
| Shared HTTP deployment | Absent; local stdio processes only |

## Remaining integration limits

**Objectify:** the example still exposes only status. Actual OpenAPI, auth, HTTPS/CA, bounded query behavior, response mappings and backend permissions are needed. Customer/cluster checks do not yet compare a requested logical account ID with the returned account ID; that mapping must come from the real contract. Projections are reviewed configuration, not full automatic response-schema validation. Upstream list completeness remains unknown. DNS/response-header timing is not a whole-request hard deadline.

**Claude:** the native client was not installed here. The two SDS Python servers implement a limited MCP 2025-11-25 stdio subset; the official Grafana binary negotiates its own supported revision and accepted 2025-11-25 in the local test. Native `/memory`, `/mcp`, managed settings and real backend acceptance remain outstanding. Markdown instructions and MCP filters do not restrict unrelated shell/file tools or conversation history.

**Grafana/Elasticsearch:** executable delivery is now complete for the four included platforms. Internal URL/CA, service-account scope, Grafana/plugin compatibility, datasource mapping and a bounded known query still need internal acceptance. The direct launcher profile does not support an ambient proxy or username/password fallback. Custom-exporter metric and label names remain unknown.

**Documentation:** the complete authorized Red Hat corpus, Confluence exports, dashboard JSON and previous incidents were not supplied. The importer handles reviewed local text/HTML/Markdown and supported Confluence page JSON, not PDF/DOCX/ZIP/ADF/dashboard JSON or every macro/layout. Batch limits do not preflight all previously accumulated corpus capacity.

**Retrieval/resources:** keyword ranking is not semantic understanding. Version filters match metadata substrings, not compatibility ranges. In-memory indexing uses more memory than its text-byte limit. Objectify's output and validation budgets bound the tested work categories; they are not universal RAM or wall-clock guarantees.

**Live operations:** no Ceph, StorageGRID, RHEL or HPE command was run on a customer system. No generic SSH executor or product-specific live MCP is supplied for those systems. No private Git remote, deployment, credential provisioning or scheduled synchronization was created.

## Validation and next internal inputs

See [VALIDATION.md](VALIDATION.md) for the test counts, reproduction commands and explicit untested areas. Priority retrieval remains 6/6; additional symptom checks are recorded separately. The complete v0.1.1 archive was checked against the working tree before edits: all 77 files matched, its CRC checks passed and all 76 listed file hashes were valid. The new package is rebuilt from the corrected tree and checked separately.

For internal integration, provide the real Objectify `/openapi.json` and redacted response/auth examples, then a verified per-customer inventory and approved Grafana dashboard/exporter sample. Use the bundled Grafana files directly inside the network and run a small scoped backend acceptance. These missing inputs do not prevent local offline package verification; they prevent claiming a completed production integration.

## Primary references

- [Reference brain Grafana guide](https://github.com/team-redbull/redbull-brain/blob/main/mcp/servers/grafana.md), [vendor manifest](https://github.com/team-redbull/redbull-brain/blob/main/plugins/team-brain/mcp-servers/vendor/manifest.json) and [launcher](https://github.com/team-redbull/redbull-brain/blob/main/plugins/team-brain/mcp-servers/launch.py).
- [Official Grafana MCP v2.2.0 release](https://github.com/grafana/mcp-grafana/releases/tag/v2.2.0) and [tagged README](https://github.com/grafana/mcp-grafana/blob/v2.2.0/README.md).
- [Ceph Reef QA client](https://github.com/ceph/ceph/blob/reef/qa/tasks/ceph_manager.py) and [Squid QA client](https://github.com/ceph/ceph/blob/squid/qa/tasks/ceph_manager.py): stuck-PG JSON envelope.
- [StorageGRID 11.9 ILM policies](https://docs.netapp.com/us-en/storagegrid-119/ilm/ilm-policy-overview.html) and [Confluence storage format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html).
- [MCP 2025-11-25 base protocol](https://modelcontextprotocol.io/specification/2025-11-25/basic), [schema](https://modelcontextprotocol.io/specification/2025-11-25/schema) and [Claude CLI configuration](https://code.claude.com/docs/en/cli-reference).

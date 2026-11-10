# Coverage, implementation status and evidence gaps

Original research date: **2026-11-09**. Version **0.4.0** review, local plugin and SQLite additions: **2026-11-10**. This is a working repository with a documented integration boundary. It is not a claim to have collected every page or accessed internal systems.

## Source inventory

The catalog has **148 unique official URLs**. Of those, **142** had readable content retrieved, **5** were verified through official search results, and **1** remains unverified behind an access wall. The four new records cover pinned OKP MCP source and Podman Quadlet documentation; the earlier sources were not all rechecked in this review. Opening a guide index does not mean every chapter was reviewed. The catalog records the distinction per reference.

| Publisher | References | Coverage focus |
|---|---:|---|
| Red Hat | 32 | RHCS 7/8 release notes, compatibility, administration, RGW, operations, RHEL 9 networking/storage/performance/security, pinned OKP MCP source |
| IBM | 9 | Storage Ceph references, version/package mapping, recovery and support material |
| Ceph upstream | 16 | Versioned Ceph behavior, health, cephadm, RGW/S3, multisite, multitenancy, metrics, service specifications, configuration precedence and PG JSON evidence |
| NetApp | 39 | StorageGRID 11.8/11.9/12.0, S3 behavior, ILM policy selection, capacity, monitoring, APIs, tenant operations and release references |
| AWS | 15 | S3 reference semantics, signing, authorization, request/error handling, multipart, lifecycle and retention |
| HPE | 9 | Candidate hardware families, iLO/Redfish, inventory and diagnostic references |
| Grafana Labs | 6 | MCP, datasources, service accounts, dashboards and Elasticsearch querying |
| Prometheus | 6 | Conditional exporter/metric/query reference, pending confirmation that it is deployed |
| Elastic | 2 | Search and cluster-health API boundaries |
| Atlassian | 3 | Confluence Cloud/Data Center export/API distinctions and storage format |
| Anthropic | 3 | Claude Code instructions, CLI and MCP configuration |
| Model Context Protocol | 5 | Implemented 2025-11-25 handshake, base/schema, stdio transport and tools |
| Linux kernel project | 1 | Upstream administration reference with RHEL applicability caveats |
| Podman | 2 | Scoped container inspection, safe field projection and versioned Quadlet deployment reference |

Full details are in `docs/SOURCES.md` and `sources/*.json` at repository root. Sources are selected for the reported stack; unrelated IBM/NetApp products are not represented as deployed.

The review and comparison with the reference repository are in `docs/REVIEW.md`. The local `plugins/team-brain/` package now matches the reference plugin's exact file/directory paths at commit `cd866d4ee510b299c415f92a90b7f525d30cf04c`. Its implementation follows SDS policy, with local session hooks and shared retrieval enabled by default. It is not a full reference-repository mirror or a deployed shared HTTP service. See [PLUGIN.md](PLUGIN.md) for provenance and differences.

## What works locally now

- Canonical `AGENT.md` plus a Claude `CLAUDE.md` import and portable `AGENTS.md` wrapper.
- An installable local Claude plugin with all 29 reference file paths and 18 subdirectories; real Grafana and Kubernetes archives are preserved, with Kubernetes access disabled by default.
- A self-contained SQLite FTS5 database at `data/sds-brain.db`, containing public document text, source metadata and original document assets. See [SQLITE.md](SQLITE.md) for scope, schema, queries and rebuilding. Private/imported/customer material and runtime executable archives are excluded.
- Dependency-free local knowledge search/read/source listing with context-bound private retrieval.
- Original knowledge pages and 19 read-only investigation runbooks.
- 2,608 searchable offline vendor documents: 109 catalog-target snapshots and 2,499 pinned StorageGRID documentation pages. Originals and provenance are preserved; see [OFFLINE_KNOWLEDGE.md](OFFLINE_KNOWLEDGE.md) for the 39 unavailable targets and text-only coverage limits.
- Objectify status and adapter configuration validation, with mocked/local transport coverage for approved read operations.
- A complete offline Grafana MCP archive set with a verified local launcher and a combined private knowledge/Grafana profile.
- Optional Red Hat OKP HTTP client profiles and Linux/Podman templates for an existing or new portal; source provenance and Ceph applicability guidance.
- Local HTML/text/Confluence JSON import with source hashes, scope and review metadata.
- Source/frontmatter/link checks, generated human indexes, stale-document reporting, retrieval acceptance tests and CI templates.

## What is prepared but not connected

| Integration | State | What remains |
|---|---|---|
| Objectify | Adapter implemented; live operations disabled | Actual OpenAPI, auth method, CA/origin, supported query/response maps, identity evidence, scoped credentials and internal acceptance |
| Grafana | Four bundled official archives, offline launcher and private profile | Native client/backend acceptance, internal HTTPS/CA, scoped service account and datasource mapping |
| Red Hat OKP MCP | Client profiles and optional Linux/Podman templates | Approved/preloaded images, existing or newly prepared RHOKP content, target-host generator checks, live client acceptance and known RHCS document retrieval |
| Elasticsearch | Read-only correlation procedure; optional Grafana path | Version, index authorization, field/time mapping and known query examples |
| Confluence | Local export importer | Cloud/DC identification and approved scoped exports |
| Red Hat corpus | Source catalog and local importer | The full authorized internal documents and exact release/audience mapping |
| Ceph/StorageGRID/HPE live tools | Read-only runbooks | No SSH executor or product-specific live MCP is implemented in this package |

## Version facts and unresolved inventory

The source reports in `research-ceph-linux.md` and `research-storagegrid-s3.md` document valid RHCS 7.1z7, 8.1z3/z6–z9 and RHEL 9.6/9.8 references. StorageGRID 12.0 documentation exists, while the user's “12” still needs its actual minor/build. None of these research findings proves a specific customer's installed version or image digest.

Hardware family interpretation is tentative. Confirm XL420/Apollo, XL170r, XL190r and DL385 generation/controller/iLO details. Grafana, exporter and Elasticsearch versions are unknown. Prometheus and actual AWS service usage are not confirmed.

## What is not bundled or claimed

Exhaustive vendor coverage, subscription support cases, internal customer records, dashboard JSON, custom exporter code/schema and credentials are not included. Actual public vendor source text and selected original captures are now bundled, including an IBM PDF book and three StorageGRID documentation-source snapshots. Images and external include targets are not comprehensively mirrored; the 39 unavailable catalog entries remain gaps in the SQL source table as well. Official Grafana and Kubernetes archives carry version/hash records and upstream licenses; bundled Kubernetes bytes are not an enabled live integration. OKP/RHOKP images, source code and entitled content are not included. No scheduled update, private Git remote, deployed HTTP MCP service, native Claude plugin installation or production action was performed. Runtime retrieval uses local files; source acquisition was an explicit connected-host task.

Read-only authorization does not make all data nonsensitive or all queries cheap. Backend permissions, field projection, bounded queries and separate customer sessions remain part of the deployment boundary.

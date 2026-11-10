# SDS Storage Brain — Codex project handoff

Prepared on 2026-11-10 from the existing ChatGPT conversation [Create Storage Agent Brain](https://chatgpt.com/c/6af1aaa3-ccc4-83ed-8db8-e469ffec4063).

## Working baseline

The current development version is **0.4.0**. The local `plugins/team-brain/` tree matches the pinned reference plugin hierarchy, with SDS-specific behavior and all six expected vendor archive paths. The additive `data/sds-brain.db` stores public documents, original document assets and the 148-source catalog for offline SQL/FTS5 queries. Existing source files remain in place. See `docs/PLUGIN.md`, `docs/SQLITE.md` and `docs/REVIEW.md`. The checks below describe project creation at v0.2.0; current validation is in `docs/VALIDATION.md`.

Offline knowledge was subsequently expanded at the user's request: 2,608 vendor document bodies/source-text pages are now indexed locally, including 109 catalog-target captures and 2,499 StorageGRID pages across 11.8/11.9/12.0. There are still 39 unavailable catalog targets, predominantly Red Hat pages returning HTTP 403; the user confirmed no authorized Red Hat exports are available on this computer yet. See `docs/OFFLINE_KNOWLEDGE.md` for exact scope and `scripts/verify_offline_knowledge.py` for byte/body retrieval checks.

This project originally imported `SDS_Storage_Brain_v0.2.0.zip` from the user's Downloads folder. At import, its 88 files were extracted without modification and all 87 original manifest hashes matched. The current repository includes later reviewed changes and a regenerated release manifest; those original import counts are historical.

Source ZIP SHA-256: `ed2349edf4cdb7b0be1cc91ef013d32583765c429abbf4ab4948ff2c9edbe689`.

Read `AGENTS.md`, the canonical `AGENT.md`, `README.md`, `knowledge/meta/environment.md` and `docs/COVERAGE.md` when resuming work. Preserve the existing implementation and extend it after inspection.

## Accepted scope

Build and maintain a complete knowledge and diagnostic repository for Ceph/RGW managed by cephadm, S3, NetApp StorageGRID, RHEL, HPE hardware, Grafana, the custom exporter, Elasticsearch and Objectify. The initial client preference was Claude Code; the repository also includes the Codex-discoverable `AGENTS.md` entry point.

Initial live operations are read-only. Keep each customer's private information, credentials and sessions separate, with explicit customer and cluster context. Grafana MCP installation must work inside the internal network using bundled, verified release archives and a local launcher, without runtime downloads.

The three priorities are Ceph health/recovery/slow operations, S3 errors/permissions/latency/compatibility, and StorageGRID capacity/ILM/connectivity. Reported product versions and unresolved hardware names are preserved in `config/reported-fleet.json`; verify them per cluster before applying guidance.

## Verification on this workstation

The following checks succeeded on 2026-11-10 using the bundled Python interpreter:

- `scripts/brain.py validate`: 30 knowledge/runbook pages, 144 sources, no failures.
- `scripts/acceptance.py`: all 6 priority retrieval checks passed.
- `mcp/knowledge/server.py --check`: v0.2.0, 41 documents, 272 chunks, no private context or network access.
- `mcp/objectify/server.py --config mcp/objectify/config.example.json --check`: disabled, awaiting OpenAPI and scope review; no network check performed.
- `scripts/vendor_grafana.py --check`: all 4 bundled v2.2.0 archives verified locally.

The full 154-test suite reported in the source conversation was not rerun during project creation. No Grafana executable, native Claude connection or customer infrastructure was tested here.

## Next development inputs

1. Obtain Objectify's actual `/openapi.json`, authentication details, approved scope mappings and redacted response examples before enabling reads.
2. Validate Grafana inside the internal network with its approved HTTPS URL, CA, scoped read-only token, datasource mapping and one known Elasticsearch query.
3. Import approved Red Hat and Confluence exports, dashboard JSON and exporter definitions through the existing importer.
4. Confirm exact product builds, StorageGRID 12 minor/build, HPE generations, and Grafana/Elasticsearch/exporter versions.
5. Verify native Claude/MCP connectivity in the intended runtime. Local offline retrieval does not establish an offline model connection.

These are follow-up priorities, not actions already completed or scheduled.

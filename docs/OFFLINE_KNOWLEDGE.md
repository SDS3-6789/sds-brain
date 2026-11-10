# Offline vendor knowledge

Capture and import date: **2026-11-10**. These are local searchable document bodies and source files, in addition to the original authored knowledge and runbooks. No web connection is used when searching or reading them.

## Available content

| Collection | Searchable documents | Scope |
|---|---:|---|
| Catalog targets | 109 | 89 document/source-file bodies and 20 explicitly marked landing pages or indexes, drawn from the 148 catalog entries |
| StorageGRID 11.8 | 861 | Text documentation from the official versioned repository at commit `9066339be246ef04b60100d49a31f887c58e7ae0` |
| StorageGRID 11.9 | 811 | Text documentation from commit `aa58c9affae3bb1994d6bd2e525851e3fd088517` |
| StorageGRID 12.0 | 827 | Text documentation from commit `92a3f4cb2ac43fd5f151e410f99e7b9d4b019938` |
| **Total vendor documents** | **2,608** | Catalog snapshots and the three versioned documentation collections |

The captured bodies include Ceph health, RGW, multisite and configuration; AWS S3 APIs, errors and authorization; StorageGRID; Grafana, Prometheus and Elasticsearch; selected HPE management references; MCP and Claude setup; Podman; and an IBM Ceph book extracted from its 174-page PDF. The original PDF and upstream text are preserved alongside searchable derivatives.

The NetApp acquisition preserved 2,583 documentation source files, plus navigation and shared legal notices. The searchable selection excludes short fragments and repository readmes that carry little technical content. Original source copies remain available for inspection. These are text snapshots: binary images, external linked documents and a completely rendered website are not included. Some AsciiDoc `include`, `xref` and image references remain unresolved.

## Where the knowledge lives

- `knowledge/vendor/catalog/` contains searchable catalog-target snapshots.
- `knowledge/vendor/storagegrid/<version>/` contains searchable versioned StorageGRID pages.
- `vendor-sources/catalog/` preserves original downloaded HTML, PDF or upstream text, attribution and capture metadata.
- `vendor-sources/netapp/<version>/` preserves pinned source text, provenance, byte manifests, legal notices and a documentation-only archive.
- [OFFLINE_KNOWLEDGE_REPORT.json](OFFLINE_KNOWLEDGE_REPORT.json) accounts for every catalog target, including unavailable sources, hashes and transformations.
- [OFFLINE_STORAGEGRID_REPORT.json](OFFLINE_STORAGEGRID_REPORT.json) lists the exact imported repository documents and their source hashes.

Credential-shaped public documentation examples are redacted in searchable derivatives. Original bytes retain their own hashes; derivative hashes and transformation counts are separate. PDF extraction normalizes known font-bullet artifacts and does not preserve diagrams. No source text is executed.

## Sources still unavailable

**39 catalog entries are not saved as usable source bodies:**

- 29 public Red Hat documentation targets returned HTTP 403 through the available ordinary download path. Official HTML-single/PDF alternatives were checked for the priority RHCS guides and were also blocked. This is a capture limitation, not a claim that those public manuals require a subscription.
- Three IBM Ceph documentation pages returned HTTP 403, and one supported-configuration page exposed only a public abstract plus a login requirement.
- Four HPE product-document targets exposed no usable article body; the Apollo QuickSpecs target timed out.
- NetApp IMT is subscription-only and was not accessed through login.

Authorized internal exports are still needed for those gaps. Red Hat portal content, internal Confluence, private incidents, dashboards and customer inventory have not been invented or imported. A captured contents page is explicitly labeled and does not stand in for all its linked chapters.

## Use and verify offline

Restart the knowledge MCP after copying this updated project. The normal local server indexes the new files automatically; there is no additional database or pip dependency for search.

```bash
python3 mcp/knowledge/server.py --check
python3 scripts/brain.py search "BLUEFS_SPILLOVER db partitions"
python3 scripts/brain.py search "HeadObject ListBucket 403 404"
python3 scripts/brain.py search "ILM reference time" --version 11.9
python3 scripts/verify_offline_knowledge.py
```

`brain_status` distinguishes the source-reference catalog from the vendor snapshot documents and repository counts. A version filter is still a metadata match; confirm the installed build and actual vendor applicability. The search keeps separate editions and uses diversity to prevent repeated chunks or alternate versions of one chapter from occupying all initial results.

The offline verifier checks original and derivative hashes and searches for distinctive body text in Ceph, S3, monitoring, HPE, Podman and all three StorageGRID editions. It reads the matched document body; a source title or catalog-only match cannot satisfy those checks.

## Transfer and refresh

The new `knowledge/vendor/` and `vendor-sources/` trees are part of the release manifest and must travel with the project for the same offline content to be available internally. Do not transfer only the source catalog or only the old 109-file package. The Word guide's manifest-based packaging procedure includes the new content after manifest refresh.

Copies preserve source provenance and original legal notices. Apply the documentation's permitted audience and usage terms. Future captures happen deliberately on an approved connected staging host; runtime retrieval remains local. Preserve exact product versions and old editions for older clusters rather than replacing them with current documentation silently.

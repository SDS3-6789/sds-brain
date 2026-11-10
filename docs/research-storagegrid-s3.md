# StorageGRID and S3 research findings

Research date: **2026-11-09**. The environment inventory is user-reported; no customer grid, S3 endpoint, or Objectify instance was queried.

## Coverage delivered

`sources/storagegrid-s3.json` contains **54 unique primary-source references**: 39 NetApp resources and 15 AWS resources. Of these, 53 public pages were opened; the Interoperability Matrix is recorded as unverified because access redirected to sign-in. The release-note landing pages are readable, but the authenticated fixed/known-issue PDFs have not been obtained. A source catalog entry is not a claim that its full content has been imported offline.

The repository includes five original knowledge pages and eight read-only runbooks in `knowledge/storagegrid`, `knowledge/s3`, `runbooks/storagegrid`, and `runbooks/s3`. These are documented guidance, not procedures tested on the user's fleet.

Coverage includes version routing, management API boundaries, S3 compatibility, capacity/metadata, ILM including bucket policy-tag selection, endpoint paths, tenant quota reconciliation, access denial, signatures/TLS, latency/server errors, multipart/checksums, and retention concepts. Sources also route to upgrades, network design, supported operations, event notifications, and search integration.

## Version findings and implications

| Finding | Consequence for the brain | Primary source |
|---|---|---|
| Separate official 11.8, 11.9, and 12.0 documentation trees exist | Preserve each release and hotfix in inventory; user-reported "12" remains unresolved | [11.8](https://docs.netapp.com/us-en/storagegrid-118/), [11.9](https://docs.netapp.com/us-en/storagegrid-119/), [12.0](https://docs.netapp.com/us-en/storagegrid-120/) |
| Unversioned documentation can advance beyond the reported fleet | Use an explicit release URL in operational answers | [Version selector](https://docs.netapp.com/us-en/storagegrid-120/) |
| 11.9 adds selected SHA-256 checksum support; 12.0 adds STS AssumeRole/session policy | Verify operation/header/release, rather than extrapolating from generic S3 support | [11.9 S3 updates](https://docs.netapp.com/us-en/storagegrid-119/s3/index.html), [12.0 S3 updates](https://docs.netapp.com/us-en/storagegrid-120/s3/index.html) |
| AWS and StorageGRID 11.8/11.9 describe different default consistency behavior | Route consistency questions to the actual provider | [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel), [SG 11.8](https://docs.netapp.com/us-en/storagegrid-118/s3/consistency-controls.html), [SG 11.9](https://docs.netapp.com/us-en/storagegrid-119/s3/consistency-controls.html) |
| Full known/fixed-issue notes require authenticated support access | A public feature page cannot settle a hotfix-specific defect | [11.9 notes](https://docs.netapp.com/us-en/storagegrid-119/release-notes/index.html), [12.0 notes entry](https://docs.netapp.com/us-en/storagegrid-120/release-notes/whats-new.html) |

## Internal evidence still needed

- Exact grid minor releases, builds, and hotfixes; confirmed customer/grid/site aliases.
- Authorized release-note and Interoperability Matrix exports for the deployed hardware/OS combinations.
- Installed Grid/Tenant API Swagger exports for any proposed direct management integration.
- Objectify OpenAPI, authentication scheme, account-to-tenant mapping, units, freshness, and authorization rules.
- Grafana datasource IDs and custom-exporter metric/label definitions for each customer/cluster.
- Elasticsearch index mappings, ingestion paths, permitted fields, and time filters; the user has not confirmed whether it stores logs, StorageGRID search-integration metadata, or another dataset.
- Sanitized operational evidence to validate and promote a runbook from documented to environment-verified.

No automatically initiated ingest test, payload retrieval, broad tenant dump, configuration mutation, or vendor-portal login is included.

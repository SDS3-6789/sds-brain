# Official documentation source catalog

Source checks recorded 2026-11-09 through 2026-11-10. Links and source metadata are included; complete vendor manuals are not bundled.
`opened` means readable content was retrieved; `search-verified` means an official indexed result was found; `unverified` requires follow-up. A source's existence is not proof of its applicability to an installed build.

## AWS

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `aws-iam-policy-evaluation` — [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) | IAM / service-current-reference | public / opened | AWS identity/resource/organization policy model; do not assume identical backend support. |
| `aws-s3-access-denied` — [Troubleshoot access denied errors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshoot-403-errors.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-consistency` — [Amazon S3 overview and consistency model](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-errors` — [Amazon S3 error responses](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/ErrorResponses.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-head-bucket` — [HeadBucket API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-head-object` — [HeadObject API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-kms` — [Server-side encryption with AWS KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-lifecycle` — [Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-list-multipart` — [AWS CLI list-multipart-uploads reference](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-multipart-uploads.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-multipart` — [Multipart upload overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-object-lock` — [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-performance` — [Performance guidelines for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-presigned` — [Download and upload using presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-sigv4` — [Authenticating requests with AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/sig-v4-authenticating-requests.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |
| `aws-s3-versioning` — [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) | Amazon S3 / service-current-reference | public / opened | AWS behavior only; not evidence of Ceph RGW or StorageGRID support. |

## Anthropic

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `claude-code-cli-reference` — [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) | Claude Code / installed version unknown | public / opened | Official CLI reference supports explicit --mcp-config and --strict-mcp-config for a deliberately selected server configuration. Actual installed client still requires internal acceptance. |
| `claude-mcp` — [Claude Code MCP configuration](https://code.claude.com/docs/en/mcp) | Claude Code / installed version unknown | public / opened | Reference for project/local configuration; actual client has not been tested here. |
| `claude-memory` — [Claude Code project instructions and memory](https://code.claude.com/docs/en/memory) | Claude Code / installed version unknown | public / opened | Use CLAUDE.md to import AGENT.md; verify loaded instructions locally. |

## Atlassian

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `confluence-cloud-pages` — [Confluence Cloud REST API v2 pages](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/) | Confluence Cloud / Cloud | public / opened | Deployment type is unknown; do not apply Cloud routes to Data Center. |
| `confluence-dc-content` — [Confluence Data Center page content API](https://support.atlassian.com/confluence/kb/how-to-get-page-content-or-child-list-via-rest-api/) | Confluence Data Center / match installed release | public / opened | Documented Data Center route; export each allowed space with its access scope. |
| `confluence-storage-format` — [Confluence storage format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html) | Confluence Data Center / storage format; match installed release | public / opened | Official XML/XHTML storage-format reference used to review preservation of code blocks and table text in approved local exports. It does not imply complete rendering of all macros. |

## Ceph upstream

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `ceph-reef-health` — [Ceph Reef health checks](https://docs.ceph.com/en/reef/rados/operations/health-checks/) | Ceph / reef | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-reef-pg-json` — [Ceph Reef QA client: stuck PG JSON structure](https://github.com/ceph/ceph/blob/reef/qa/tasks/ceph_manager.py) | Ceph / reef | public / opened | The get_stuck_pgs method reads the stuck_pg_stats array from the JSON object returned by pg dump_stuck. Retrieved file blob f2ad7a29ec60091db420958f88d237c7e871a2be. Release-family source evidence; the installed downstream build remains authoritative. |
| `ceph-squid-cephadm` — [Ceph Squid cephadm troubleshooting](https://docs.ceph.com/en/squid/cephadm/troubleshooting/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-configuration` — [Ceph Squid configuration sources and inspection commands](https://docs.ceph.com/en/squid/rados/configuration/ceph-conf/) | Ceph / Squid | public / opened | Distinguishes Monitor database/default configuration from values reported by a running daemon. Match the installed vendor release before choosing an inspection command. |
| `ceph-squid-health` — [Ceph Squid health checks](https://docs.ceph.com/en/squid/rados/operations/health-checks/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-mclock` — [Ceph Squid mClock configuration reference](https://docs.ceph.com/en/squid/rados/configuration/mclock-config-ref/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-monitoring` — [Ceph Squid cluster monitoring](https://docs.ceph.com/en/squid/rados/operations/monitoring/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-multisite` — [Ceph Squid RGW multi-site](https://docs.ceph.com/en/squid/radosgw/multisite/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-multitenancy` — [Ceph Squid RGW multi-tenancy and qualified identities](https://docs.ceph.com/en/squid/radosgw/multitenancy/) | Ceph RGW / Squid | public / opened | User IDs can repeat across tenant namespaces; an explicit tenant mapping or fully qualified UID is necessary for a scoped administrative read. |
| `ceph-squid-pg-json` — [Ceph Squid QA client: stuck PG JSON structure](https://github.com/ceph/ceph/blob/squid/qa/tasks/ceph_manager.py) | Ceph / squid | public / opened | The get_stuck_pgs method reads the stuck_pg_stats array from the JSON object returned by pg dump_stuck. Retrieved file blob ffa7bd75506c2bb60425438a8b4a93e64c014acb. Release-family source evidence; the installed downstream build remains authoritative. |
| `ceph-squid-prometheus` — [Ceph Squid Prometheus module](https://docs.ceph.com/en/squid/mgr/prometheus/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-rgw-admin` — [Ceph Squid RGW administration](https://docs.ceph.com/en/squid/radosgw/admin/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-rgw-metrics` — [Ceph Squid RGW metrics](https://docs.ceph.com/en/squid/radosgw/metrics/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-rgw-service` — [Ceph Squid RGW service specification and TLS](https://docs.ceph.com/en/squid/cephadm/services/rgw/) | Ceph RGW / Squid | public / opened | RGW and ingress specification examples include certificate/private-key material; do not export unrestricted specifications into agent context. |
| `ceph-squid-s3` — [Ceph Squid S3 API and feature support](https://docs.ceph.com/en/squid/radosgw/s3/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |
| `ceph-squid-s3-auth` — [Ceph Squid S3 authentication and ACLs](https://docs.ceph.com/en/squid/radosgw/s3/authentication/) | Ceph / squid | public / opened | Pinned upstream release-family reference. Downstream Red Hat/IBM support and backports take precedence for their own installations. |

## Elastic

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `elastic-health-api` — [Elasticsearch cluster health API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-health) | Elasticsearch / installed version unknown | public / opened | Cluster monitoring privilege is distinct from index read access. |
| `elastic-search-api` — [Elasticsearch Search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search) | Elasticsearch / installed version unknown | public / opened | Current API reference; bind index and fields to the active customer. |

## Grafana Labs

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `grafana-dashboard-export` — [Grafana dashboard sharing and export](https://grafana.com/docs/grafana/latest/visualizations/dashboards/share-dashboards-panels/) | Grafana / installed version unknown | public / opened | Provide reviewed dashboard JSON privately; do not create public snapshots. |
| `grafana-elasticsearch` — [Grafana Elasticsearch data source](https://grafana.com/docs/grafana/latest/datasources/elasticsearch/) | Grafana / installed version unknown | public / opened | Latest reference only; confirm installed Grafana and Elasticsearch/plugin versions. |
| `grafana-es-query` — [Grafana Elasticsearch query editor](https://grafana.com/docs/grafana/latest/datasources/elasticsearch/query-editor/) | Grafana / installed version unknown | public / opened | Map existing panels and actual field names before constructing queries. |
| `grafana-mcp` — [Official Grafana MCP v2.2.0](https://github.com/grafana/mcp-grafana/blob/v2.2.0/README.md) | mcp-grafana / v2.2.0 | public / opened | Four verified official release archives are bundled for offline launch. Fixed read-only stdio profile includes Elasticsearch; backend authorization and installed Grafana/plugin compatibility still require internal acceptance. |
| `grafana-prometheus` — [Grafana Prometheus data source](https://grafana.com/docs/grafana/latest/datasources/prometheus/) | Grafana / installed version unknown | public / opened | Prometheus usage in this environment remains unconfirmed. |
| `grafana-service-accounts` — [Grafana service accounts](https://grafana.com/docs/grafana/latest/administration/service-accounts/) | Grafana / installed version unknown | public / opened | Use backend-enforced customer scope and minimum permissions. |

## HPE

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `hpe-apollo-utilities` — [HPE Apollo 4200 Gen10 software and configuration utilities](https://support.hpe.com/hpesc/public/docDisplay?docId=a00066162en_us&docLocale=en_US) | Apollo 4200 / Gen10 candidate | public / search-verified | Use model-specific tools and review diagnostic output before sharing. |
| `hpe-dl385` — [HPE ProLiant DL385 Gen11 User Guide](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00002188en_us&docLocale=en_US) | DL385 / Gen11 candidate | public / search-verified | DL385 family reported; Gen11 is a candidate reference, not confirmed inventory. |
| `hpe-ilorest` — [HPE iLOrest overview](https://servermanagementportal.ext.hpe.com/docs/redfishclients/ilorest-userguide) | iLOrest / match iLO and server generation | public / opened | Choose tool/API documentation for the actual iLO generation and firmware. |
| `hpe-ilorest-usage` — [HPE iLOrest usage](https://servermanagementportal.ext.hpe.com/docs/redfishclients/ilorest-userguide/usage) | iLOrest / match installed release | public / opened | Use reviewed read-only inventory operations; management actions remain excluded. |
| `hpe-redfish-concepts` — [HPE Redfish concepts](https://servermanagementportal.ext.hpe.com/docs/concepts) | Redfish / match service schema | public / opened | Discover resource links from the service root; do not assume numeric system IDs. |
| `hpe-redfish-services` — [HPE Redfish service references](https://servermanagementportal.ext.hpe.com/docs/redfishservices) | iLO Redfish / iLO version unknown | public / opened | Select the service generation matching inventory before interpreting fields. |
| `hpe-xl170r` — [HPE ProLiant XL170r Gen10 product information](https://support.hpe.com/hpesc/public/docDisplay?docId=a00027628en_us) | XL170r / Gen10 candidate | public / search-verified | Official indexed page; direct reader yielded no body. Match actual generation. |
| `hpe-xl190r` — [HPE ProLiant XL190r Gen10 manuals](https://support.hpe.com/connect/s/product?kmpmoid=1010192754&language=en_CA&tab=manuals) | XL190r / Gen10 candidate | public / search-verified | Official manuals index; candidate interpretation of 'exel190'. |
| `hpe-xl420-apollo` — [HPE Apollo 4200 Gen10 Plus QuickSpecs](https://www.hpe.com/int/en/collaterals/collateral.a50002573enw.html) | Apollo 4200 / XL420 / Gen10 Plus candidate | public / opened | Candidate interpretation of 'exel420'; generation and product identity need confirmation. |

## IBM

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `ibm-ceph-architecture` — [IBM Storage Ceph Concepts and Architecture Guide REDP-5721](https://www.redbooks.ibm.com/redpapers/pdfs/redp5721.pdf) | IBM Storage Ceph / 7 | public / opened | June 2024 first edition applies to IBM Storage Ceph 7. Architecture background, not 8.1 patch-level authority. |
| `ibm-ceph-deployment` — [IBM Storage Ceph 8.1 RGW deployment guidelines](https://www.ibm.com/docs/en/storage-ceph/8.1.0?topic=gateway-deployment-guidelines) | IBM Storage Ceph / 8.1.0 | public / opened | Describes site and realm/zone planning. |
| `ibm-ceph-low-level` — [IBM Storage Ceph low-level monitoring](https://www.ibm.com/docs/en/storage-ceph/8.0.0?topic=cluster-low-level-monitoring) | IBM Storage Ceph / 8.0.0 | public / opened | Older product version; useful conceptual material, not 8.1 patch-level confirmation. |
| `ibm-ceph-master-reference` — [IBM Storage Ceph Master Troubleshooting and Operations Reference Guide](https://www.ibm.com/support/pages/node/7239015) | IBM Storage Ceph / 5.x+, 7.1, 8.1 | mixed / opened | Broad support index; linked articles may have separate access requirements and version caveats. |
| `ibm-ceph-multisite` — [IBM Storage Ceph 8.1 Multi-site considerations](https://www.ibm.com/docs/en/storage-ceph/8.1.0?topic=gateway-multi-site-considerations) | IBM Storage Ceph / 8.1.0 | public / search-verified | Search result verified content; direct retrieval returned HTTP 403. Not a downloaded offline document. |
| `ibm-ceph-recovery` — [Differences between backfill, recovery and peering](https://www.ibm.com/support/pages/node/7176025) | IBM Storage Ceph / 5.x+ | public / opened | Read conceptual distinctions; older general tuning examples need current scheduler and vendor validation. |
| `ibm-ceph-supported` — [IBM Storage Ceph Supported Configurations](https://www.ibm.com/support/pages/node/7236061) | IBM Storage Ceph / version-dependent | mixed / opened | Support landing page opened. Follow its product/version-specific documents; no cross-vendor support equivalence is assumed. |
| `ibm-ceph-throttling` — [Managing backfill, recovery and rebalancing throttles](https://www.ibm.com/support/pages/node/6963280) | IBM Storage Ceph / 5.x+ | public / opened | Reference only. Do not copy legacy throttling settings onto mClock-managed OSDs without checking the current product guidance. |
| `ibm-ceph-version-matrix` — [Red Hat and IBM Storage Ceph releases and corresponding package versions](https://www.ibm.com/support/pages/what-are-red-hat-and-ibm-storage-ceph-releases-and-corresponding-ceph-package-versions) | IBM Storage Ceph / 7.1, 8.1 | public / opened | Maps vendor releases to package versions, upstream families and image tags. IBM rows do not establish a Red Hat image digest; inspect each deployed image. |

## Linux kernel project

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `linux-upstream-admin` — [Linux kernel administration guide](https://docs.kernel.org/admin-guide/index.html) | Linux / upstream; not RHEL support policy | public / opened | Upstream behavior requires checking RHEL backports and vendor support. |

## Model Context Protocol

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `mcp-basic-2025` — [MCP base protocol, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic) | MCP / 2025-11-25 | public / opened | Primary base-protocol reference for request metadata and framing review. Native client acceptance is still required. |
| `mcp-lifecycle-2025` — [MCP lifecycle, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle) | MCP / 2025-11-25 | public / opened | Implementation targets the documented legacy handshake, not the newer stateless protocol. |
| `mcp-schema-2025` — [MCP schema reference, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/schema) | MCP / 2025-11-25 | public / opened | Authoritative message schema used to audit optional request metadata. This package implements a limited stdio subset. |
| `mcp-stdio-2025` — [MCP transports, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) | MCP / 2025-11-25 | public / opened | Local newline-delimited JSON-RPC transport; no inbound network listener in this repository. |
| `mcp-tools-2025` — [MCP tools, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) | MCP / 2025-11-25 | public / opened | Tool annotations describe intent; server checks and backend permissions enforce access. |

## NetApp

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `netapp-imt` — [NetApp Interoperability Matrix Tool](https://imt.netapp.com/matrix/) | Interoperability Matrix / live-matrix | subscription / unverified | Linked from official version docs; fetch redirected to login. Matrix contents unverified. |
| `netapp-sg118-consistency` — [StorageGRID 11.8 consistency values](https://docs.netapp.com/us-en/storagegrid-118/s3/consistency-controls.html) | StorageGRID / 11.8 | public / opened |  |
| `netapp-sg118-docs` — [StorageGRID 11.8 documentation](https://docs.netapp.com/us-en/storagegrid-118/) | StorageGRID / 11.8 | public / opened |  |
| `netapp-sg118-ilm` — [Manage objects with ILM in 11.8](https://docs.netapp.com/us-en/storagegrid-118/ilm/index.html) | StorageGRID / 11.8 | public / opened |  |
| `netapp-sg118-s3` — [StorageGRID 11.8 S3 API versions and updates](https://docs.netapp.com/us-en/storagegrid-118/s3/index.html) | StorageGRID / 11.8 | public / opened |  |
| `netapp-sg119-bucket-operations` — [StorageGRID operations on buckets](https://docs.netapp.com/us-en/storagegrid-119/s3/operations-on-buckets.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-capacity` — [Monitor storage capacity](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-storage-capacity.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-client-connections` — [Configure S3 client connections](https://docs.netapp.com/us-en/storagegrid-119/admin/configuring-client-connections.html) | StorageGRID / 11.9 | public / opened | Read configuration as evidence; do not run setup wizard during diagnosis. |
| `netapp-sg119-client-ports` — [IP addresses and ports for client connections](https://docs.netapp.com/us-en/storagegrid-119/admin/summary-ip-addresses-and-ports-for-client-connections.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-consistency` — [StorageGRID 11.9 consistency values](https://docs.netapp.com/us-en/storagegrid-119/s3/consistency-controls.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-docs` — [StorageGRID 11.9 documentation](https://docs.netapp.com/us-en/storagegrid-119/) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-errors` — [StorageGRID S3 error responses](https://docs.netapp.com/us-en/storagegrid-119/s3/error-responses.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-grid-api` — [Use the Grid Management API](https://docs.netapp.com/us-en/storagegrid-119/admin/using-grid-management-api.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-ilm` — [Manage objects with ILM in 11.9](https://docs.netapp.com/us-en/storagegrid-119/ilm/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-ilm-lifecycle` — [How ILM operates throughout an object life](https://docs.netapp.com/us-en/storagegrid-119/ilm/how-ilm-operates-throughout-objects-life.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-ilm-monitor` — [Monitor information lifecycle management](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-information-lifecycle-management.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-ilm-policies` — [StorageGRID 11.9 ILM policy selection and bucket policy tags](https://docs.netapp.com/us-en/storagegrid-119/ilm/ilm-policy-overview.html) | StorageGRID / 11.9 | public / opened | Multiple policies may be active simultaneously. Resolve the bucket policy tag to the assigned active policy; untagged buckets use the Default tag policy. Read-only investigation must preserve the tag. |
| `netapp-sg119-lb-endpoints` — [Configure load balancer endpoints](https://docs.netapp.com/us-en/storagegrid-119/admin/configuring-load-balancer-endpoints.html) | StorageGRID / 11.9 | public / opened | Reference only; configuration operations are outside read-only release. |
| `netapp-sg119-lb-monitor` — [Monitor load balancing operations](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-load-balancing-operations.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-logs` — [StorageGRID log files reference](https://docs.netapp.com/us-en/storagegrid-119/monitor/logs-files-reference.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-metadata` — [Troubleshoot metadata issues](https://docs.netapp.com/us-en/storagegrid-119/troubleshoot/troubleshooting-metadata-issues.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-monitor` — [Monitor StorageGRID](https://docs.netapp.com/us-en/storagegrid-119/monitor/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-network` — [StorageGRID networking guidelines](https://docs.netapp.com/us-en/storagegrid-119/network/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-notifications` — [Understand notifications for buckets](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-notifications-for-buckets.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-object-lock` — [Manage objects with S3 Object Lock](https://docs.netapp.com/us-en/storagegrid-119/ilm/managing-objects-with-s3-object-lock.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-object-operations` — [StorageGRID operations on objects](https://docs.netapp.com/us-en/storagegrid-119/s3/operations-on-objects.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-release-notes` — [StorageGRID 11.9 release notes access](https://docs.netapp.com/us-en/storagegrid-119/release-notes/index.html) | StorageGRID / 11.9 | mixed / opened | Public landing page opened; authenticated release-note PDF not retrieved. |
| `netapp-sg119-s3` — [StorageGRID 11.9 S3 API versions and updates](https://docs.netapp.com/us-en/storagegrid-119/s3/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-s3-quick-reference` — [Quick reference to supported S3 API requests](https://docs.netapp.com/us-en/storagegrid-119/s3/quick-reference-support-for-aws-apis.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-search-integration` — [Understand search integration service](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-search-integration-service.html) | StorageGRID / 11.9 | public / opened | User Elasticsearch role is unconfirmed; do not assume this integration is enabled. |
| `netapp-sg119-tenant` — [StorageGRID tenant account model](https://docs.netapp.com/us-en/storagegrid-119/tenant/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-tenant-api` — [Understand Tenant Management API](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-tenant-management-api.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-tenant-dashboard` — [Understand Tenant Manager dashboard](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-tenant-manager-dashboard.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-troubleshoot` — [StorageGRID troubleshooting overview](https://docs.netapp.com/us-en/storagegrid-119/troubleshoot/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg119-upgrade` — [Upgrade StorageGRID software to 11.9](https://docs.netapp.com/us-en/storagegrid-119/upgrade/index.html) | StorageGRID / 11.9 | public / opened |  |
| `netapp-sg120-docs` — [StorageGRID 12.0 documentation](https://docs.netapp.com/us-en/storagegrid-120/) | StorageGRID / 12.0 | public / opened | Candidate for user-reported 12; exact installed minor/build unconfirmed. |
| `netapp-sg120-s3` — [StorageGRID 12.0 S3 API versions and updates](https://docs.netapp.com/us-en/storagegrid-120/s3/index.html) | StorageGRID / 12.0 | public / opened |  |
| `netapp-sg120-upgrade` — [Upgrade StorageGRID software to 12.0](https://docs.netapp.com/us-en/storagegrid-120/upgrade/index.html) | StorageGRID / 12.0 | public / opened |  |
| `netapp-sg120-whats-new` — [What is new in StorageGRID 12.0](https://docs.netapp.com/us-en/storagegrid-120/release-notes/whats-new.html) | StorageGRID / 12.0 | mixed / opened | Full fixed/known-issue release notes require support login. |

## Podman

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `podman-container-inspect` — [Podman container inspect command reference](https://docs.podman.io/en/latest/markdown/podman-container-inspect.1.html) | Podman / current-reference, installed-version-unconfirmed | public / opened | Formatting can select approved fields for one verified container ID; the complete inspect response includes sensitive configuration. Confirm syntax against the installed RHEL Podman manual. |
| `podman-quadlet` — [Podman 4.6.1 — Quadlet systemd container, network and volume units](https://docs.podman.io/en/v4.6.1/markdown/podman-systemd.unit.5.html) | Podman Quadlet / 4.6.1 | public / opened | Primary reference for Pull=never, loopback PublishPort, EnvironmentFile, generated service dependencies and network/volume units. Target host generator validation remains required. |

## Prometheus

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `prometheus-api` — [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/) | Prometheus / installed version unknown | public / opened | Bound query windows and series; validate backend version. |
| `prometheus-exporters` — [Writing Prometheus exporters](https://prometheus.io/docs/instrumenting/writing_exporters/) | Prometheus / exporter version unknown | public / opened | Conditional on confirmed Prometheus-compatible exporter format. |
| `prometheus-exposition` — [Prometheus exposition formats](https://prometheus.io/docs/instrumenting/exposition_formats/) | Prometheus / general | public / opened | Capture a reviewed metric schema sample, not arbitrary full metric dumps. |
| `prometheus-functions` — [PromQL query functions](https://prometheus.io/docs/prometheus/latest/querying/functions/) | Prometheus / installed version unknown | public / opened | Use only after metric type, labels and units have been established. |
| `prometheus-histograms` — [Prometheus histograms and summaries](https://prometheus.io/docs/practices/histograms/) | Prometheus / general | public / opened | Check actual histogram format and aggregation semantics. |
| `prometheus-naming` — [Prometheus metric and label naming](https://prometheus.io/docs/practices/naming/) | Prometheus / general | public / opened | A design reference, not evidence of custom exporter field names. |

## Red Hat

| ID / source | Product / version | Access / verification | Scope notes |
|---|---|---|---|
| `redhat-okp-mcp` — [Red Hat OKP MCP — upstream setup and RHOKP prerequisites](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/README.md) | Offline Knowledge Portal MCP / source-1.0.2, a4469e1365789d1619a9d2276fa0ed2e80ee18b3 | public / opened | Upstream setup read at the pinned commit. Requires a separately prepared RHOKP index; container images and entitled portal content are not bundled. Source pin does not verify published image identity. |
| `redhat-okp-mcp-config` — [Red Hat OKP MCP — actual runtime configuration](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/src/okp_mcp/config.py) | Offline Knowledge Portal MCP / source-1.0.2, a4469e1365789d1619a9d2276fa0ed2e80ee18b3 | public / opened | Reviewed MCP_ settings, base Solr URL, HTML lookup and response-character limits. Actual transport default is streamable-http; README contains a conflicting stdio-default sentence. Image behavior requires acceptance. |
| `redhat-okp-mcp-formatting` — [Red Hat OKP MCP — result product-applicability annotations](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/src/okp_mcp/formatting.py) | Offline Knowledge Portal MCP / source-1.0.2, a4469e1365789d1619a9d2276fa0ed2e80ee18b3 | public / opened | Non-EOL results can receive a generic RHEL applicability label. Verify actual product/version and known RHCS content before relying on results for Ceph. Portal corpus coverage is not established by source review. |
| `rhcs-7-compat` — [Red Hat Ceph Storage 7 Compatibility Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html/compatibility_guide/index) | Red Hat Ceph Storage / 7 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-7-release` — [Red Hat Ceph Storage 7.1 Release Notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html-single/7.1_release_notes/index) | Red Hat Ceph Storage / 7.1, 7.1z7 | public / opened | Confirms 7.1z7 as a container-only update. Scope each issue to its z-stream; this evolving page also describes later patches. |
| `rhcs-7-rgw` — [Red Hat Ceph Storage 7 Object Gateway Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html/object_gateway_guide/index) | Red Hat Ceph Storage / 7 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-7-troubleshooting` — [Red Hat Ceph Storage 7 Troubleshooting Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html/troubleshooting_guide/index) | Red Hat Ceph Storage / 7 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-administration` — [Red Hat Ceph Storage 8 Administration Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/administration_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-compat` — [RHCS 8.1 Compatibility Matrix](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/compatibility_guide/compatibility-matrix-for-red-hat-ceph-storage-8.1) | Red Hat Ceph Storage / 8.1 | public / opened | Live page lists RHEL 9.6 and 9.8 on retrieval. Applies to the product matrix, not proof of every patch/hardware combination. |
| `rhcs-8-configuration` — [Red Hat Ceph Storage 8 Configuration Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/configuration_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-hardening` — [Red Hat Ceph Storage 8 Data Security and Hardening Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/data_security_and_hardening_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-hardware` — [Red Hat Ceph Storage 8 Hardware Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/hardware_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-installation` — [Red Hat Ceph Storage 8 Installation Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/installation_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-multisite` — [RHCS 8 Multi-site configuration and administration](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/object_gateway_guide/multisite-configuration-and-administration) | Red Hat Ceph Storage / 8 | public / opened | Scope every command to the selected realm/zone. The document also contains write workflows, excluded from this initial brain. |
| `rhcs-8-operations` — [Red Hat Ceph Storage 8 Operations Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/operations_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-osd-troubleshooting` — [RHCS 8 Troubleshooting Ceph OSDs](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/troubleshooting_guide/troubleshooting-ceph-osds) | Red Hat Ceph Storage / 8 | public / opened | Includes full, backfillfull, nearfull, down/flapping OSD and slow-request diagnosis; remediation commands in the source are not authorized by read-only mode. |
| `rhcs-8-pg-troubleshooting` — [RHCS 8 Troubleshooting Ceph placement groups](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/troubleshooting_guide/troubleshooting-ceph-placement-groups) | Red Hat Ceph Storage / 8 | public / opened | Use diagnostic portions only. Recovery and repair actions require a separate reviewed change. |
| `rhcs-8-release` — [Red Hat Ceph Storage 8.1 Release Notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/8.1_release_notes/8.1_release_notes) | Red Hat Ceph Storage / 8.1, 8.1z3, 8.1z6, 8.1z7, 8.1z8, 8.1z9 | public / opened | The requested z-streams appear in official release notes. Feature and fix applicability still require the installed image/build. |
| `rhcs-8-rgw` — [Red Hat Ceph Storage 8 Object Gateway Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/object_gateway_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-troubleshooting` — [Red Hat Ceph Storage 8 Troubleshooting Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/troubleshooting_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhcs-8-upgrade` — [Red Hat Ceph Storage 8 Upgrade Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/upgrade_guide/index) | Red Hat Ceph Storage / 8 | public / opened | Official guide/index opened. Follow version-specific chapters for procedures; index presence is not a claim that every linked chapter was reviewed. |
| `rhel-9-containers` — [RHEL 9 Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-9-kernel` — [RHEL 9 Managing, monitoring, and updating the kernel](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-9-networking` — [RHEL 9 Configuring and managing networking](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-9-performance` — [RHEL 9 Monitoring and managing system status and performance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-9-performance-overview` — [RHEL 9 Overview of performance monitoring options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/overview-of-performance-monitoring-options) | RHEL / 9, 9.6, 9.8 | public / opened | Documents available monitoring utilities; exact flags should be checked against locally installed man pages. |
| `rhel-9-selinux` — [RHEL 9 Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-9-selinux-troubleshooting` — [RHEL 9 Troubleshooting problems related to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/troubleshooting-problems-related-to-selinux_using-selinux) | RHEL / 9, 9.6, 9.8 | public / opened | Diagnostic logging and label inspection are relevant; policy modifications remain outside read-only mode. |
| `rhel-9-storage` — [RHEL 9 Managing storage devices](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-9-tls` — [RHEL 9 Securing networks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/index) | RHEL / 9, 9.6, 9.8 | public / opened | Rolling RHEL 9 guide. Check the release notes and installed package versions for minor-specific behavior. |
| `rhel-96-release` — [RHEL 9.6 Release Notes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/9.6_release_notes/index) | RHEL / 9.6 | public / opened | Confirms official RHEL 9.6 documentation; retain host RPM build and architecture. |
| `rhel-98-release` — [RHEL 9.8 Release Notes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index) | RHEL / 9.8 | public / opened | Official 9.8 release notes were opened. Do not misclassify the user-reported version as nonexistent. |


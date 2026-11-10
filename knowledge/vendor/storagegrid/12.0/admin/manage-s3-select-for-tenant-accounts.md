---
id: "storagegrid-120-1c0e167cd376607f"
title: "StorageGRID 12.0 Manage S3 Select for tenant accounts in StorageGRID"
area: "storagegrid"
type: "import"
applies_to: ["12.0", "storagegrid-12.0"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg120-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-120"
repository_commit: "92a3f4cb2ac43fd5f151e410f99e7b9d4b019938"
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/manage-s3-select-for-tenant-accounts.adoc"
source_sha256: "74c51a853f4b41d31e972c6ec32cc1812552b4106bbbc6b189c393020f3d4e6a"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/manage-s3-select-for-tenant-accounts.adoc"
---

# StorageGRID 12.0 Manage S3 Select for tenant accounts in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/manage-s3-select-for-tenant-accounts.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Manage S3 Select for tenant accounts in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
You can allow certain S3 tenants to use S3 Select to issue SelectObjectContent requests on individual objects. 

S3 Select provides an efficient way to search through large amounts of data without having to deploy a database and associated resources to enable searches. It also reduces the cost and latency of retrieving data.

## What is S3 Select?

S3 Select allows S3 clients to use SelectObjectContent requests to filter and retrieve only the data needed from an object. The StorageGRID implementation of S3 Select includes a subset of S3 Select commands and features.

## Considerations and requirements for using S3 Select

### Grid administration requirements
The grid administrator must grant tenants S3 Select ability. Select *Allow S3 Select* when link:creating-tenant-account.html[creating a tenant] or link:editing-tenant-account.html[editing a tenant].

### Object format requirements
The object you want to query must be in one of the following formats: 

* *CSV*. Can be used as is or compressed into GZIP or BZIP2 archives. 
* *Parquet*. Additional requirements for Parquet objects:

** S3 Select supports only columnar compression using GZIP or Snappy. S3 Select doesn't support whole-object compression for Parquet objects.
** S3 Select doesn't support Parquet output. You must specify the output format as CSV or JSON.
** The maximum uncompressed row group size is 512 MB.
** You must use the data types specified in the object's schema.
** You can't use INTERVAL, JSON, LIST, TIME, or UUID logical types.

### Endpoint requirements
The SelectObjectContent request must be sent to a link:configuring-load-balancer-endpoints.html[StorageGRID load balancer endpoint].

The Admin and Gateway Nodes used by the endpoint must be one of the following: 

* A services appliance node 
* A VMware-based software node
* A bare metal node running a kernel with cgroup v2 enabled 

### General considerations
Queries can't be sent directly to Storage Nodes.

CAUTION: SelectObjectContent requests can decrease load-balancer performance for all S3 clients and all tenants. Enable this feature only when required and only for trusted tenants.

See the link:../s3/use-s3-select.html[instructions for using S3 Select].

To view link:../monitor/reviewing-support-metrics.html[Grafana charts] for S3 Select operations over time, select *Support* > *Tools* > *Metrics* in the Grid Manager.

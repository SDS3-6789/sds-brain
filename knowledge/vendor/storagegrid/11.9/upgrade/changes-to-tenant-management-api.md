---
id: "storagegrid-119-1055c173c12cc567"
title: "StorageGRID 11.9 Changes to the Tenant Management API"
area: "storagegrid"
type: "import"
applies_to: ["11.9", "storagegrid-11.9"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg119-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-119"
repository_commit: "aa58c9affae3bb1994d6bd2e525851e3fd088517"
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/upgrade/changes-to-tenant-management-api.adoc"
source_sha256: "84b40af0785f3a753f1e6a2e411bbabd5817b847b1170da8bb0896a16a65f2dd"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "upgrade/changes-to-tenant-management-api.adoc"
---

# StorageGRID 11.9 Changes to the Tenant Management API

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/upgrade/changes-to-tenant-management-api.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Changes to the Tenant Management API
:icons: font
:imagesdir: ../media/

[.lead]
StorageGRID 11.9 uses version 4 of the Tenant Management API. Version 4 deprecates version 3; however, versions 1, 2, and 3 are still supported. 

NOTE: You can continue to use deprecated versions of the Tenant Management API with StorageGRID 11.9; however, support for these versions of the API will be removed in a future release of StorageGRID. After upgrading to StorageGRID 11.9, you can deactivate the deprecated APIs by using the `PUT /grid/config/management` API.

To learn more, go to link:../tenant/understanding-tenant-management-api.html[Understand the Tenant Management API].

## New API for bucket capacity limit
You can use the `/org/containers/{bucketName}/quota-object-bytes` API with GET/PUT operations to get and set the storage capacity limit for a bucket.

// 2024 JUL 10, SGWS-31727

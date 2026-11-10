---
id: "storagegrid-118-1055c173c12cc567"
title: "StorageGRID 11.8 Changes to the Tenant Management API"
area: "storagegrid"
type: "import"
applies_to: ["11.8", "storagegrid-11.8"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg118-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-118"
repository_commit: "9066339be246ef04b60100d49a31f887c58e7ae0"
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/upgrade/changes-to-tenant-management-api.adoc"
source_sha256: "a1948b887b2d53560674da7360a7c9e6ed34dacbdd81d08fe3561ecfed579cd4"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "upgrade/changes-to-tenant-management-api.adoc"
---

# StorageGRID 11.8 Changes to the Tenant Management API

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/upgrade/changes-to-tenant-management-api.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Changes to the Tenant Management API
:icons: font
:imagesdir: ../media/

[.lead]
StorageGRID 11.8 uses version 4 of the Tenant Management API. Version 4 deprecates version 3; however, versions 1, 2, and 3 are still supported. 

NOTE: You can continue to use deprecated versions of the Tenant Management API with StorageGRID 11.8; however, support for these versions of the API will be removed in a future release of StorageGRID. After upgrading to StorageGRID 11.8, the deprecated APIs can be deactivated using the `PUT /grid/config/management` API.

To learn more, go to link:../tenant/understanding-tenant-management-api.html[Understand the Tenant Management API].

## New endpoints for ILM policy tags

You can use the */org/ilm-policy-tags* and */org/containers/{bucketName}/ilm-policy-tags* API endpoints to perform operations related to ILM policy tags.

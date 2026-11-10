---
id: "storagegrid-120-7ba7bc04a589fb20"
title: "StorageGRID 12.0 Risks of single-copy replication in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/why-you-should-not-use-single-copy-replication.adoc"
source_sha256: "1860805694e86a4160715a17428b2e862beb92957afeec6163de1aade07b4d6a"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/why-you-should-not-use-single-copy-replication.adoc"
---

# StorageGRID 12.0 Risks of single-copy replication in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/why-you-should-not-use-single-copy-replication.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Risks of single-copy replication in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
When creating an ILM rule to create replicated copies, you should always specify at least two copies for any time period in the placement instructions.

NOTE: Don't use an ILM rule that creates only one replicated copy for any time period. If only one replicated copy of an object exists, that object is lost if a Storage Node fails or has a significant error. You also temporarily lose access to the object during maintenance procedures such as upgrades.

In the following example, the Make 1 Copy ILM rule specifies that one replicated copy of an object be placed in a storage pool that contains three Storage Nodes. When an object is ingested that matches this rule, StorageGRID places a single copy on only one Storage Node.

image:ilm_replication_make_1_copy.png[ILM Replication Make 1 Copy]

When an ILM rule creates only one replicated copy of an object, the object becomes inaccessible when the Storage Node is unavailable. In this example, you will temporarily lose access to object AAA whenever Storage Node 2 is offline, such as during an upgrade or other maintenance procedure. You will lose object AAA entirely if Storage Node 2 fails.

image:ilm_replication_make_1_copy_sn_fails.png[ILM Replication Make 1 Copy SN Fails]

To avoid losing object data, you should always make at least two copies of all objects you want to protect with replication. If two or more copies exist, you can still access the object if one Storage Node fails or goes offline.

image:ilm_replication_make_2_copies_sn_fails.png[ILM Replication Make 2 Copies SN Fails]

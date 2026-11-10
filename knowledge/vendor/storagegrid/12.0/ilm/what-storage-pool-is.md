---
id: "storagegrid-120-a4419c4c3f714007"
title: "StorageGRID 12.0 Learn about storage pools in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/what-storage-pool-is.adoc"
source_sha256: "ceee64716bb0e557d0d7a54a0293077bd8ab4b4829bb63a6d0edd37f0f3547c8"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/what-storage-pool-is.adoc"
---

# StorageGRID 12.0 Learn about storage pools in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/what-storage-pool-is.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Learn about storage pools in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
A storage pool is a logical grouping of Storage Nodes.

When you install StorageGRID, one storage pool per site is automatically created. You can configure additional storage pools as needed for your storage requirements.

NOTE: Storage Nodes can be configured during installation to contain object data and metadata ("combined" Storage Node), only object metadata, or only object data. Metadata-only Storage Nodes can't be used in storage pools. For more information, refer to link:../primer/what-storage-node-is.html#types-of-storage-nodes[Types of Storage Nodes].

Storage pools have two attributes:

* *Storage grade*: For Storage Nodes, the relative performance of backing storage.
* *Site*: The data center where objects will be stored.

Storage pools are used in ILM rules to determine where object data is stored and the type of storage used. When you configure ILM rules for replication, you select one or more storage pools.

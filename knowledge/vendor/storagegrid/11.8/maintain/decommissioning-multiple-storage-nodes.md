---
id: "storagegrid-118-45d6927c32626b14"
title: "StorageGRID 11.8 Decommission multiple Storage Nodes"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/decommissioning-multiple-storage-nodes.adoc"
source_sha256: "90b6ecc9a54ce5dc7fcb0518828e460d9be60d8998e17059f4eb80e96d6ee42d"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/decommissioning-multiple-storage-nodes.adoc"
---

# StorageGRID 11.8 Decommission multiple Storage Nodes

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/decommissioning-multiple-storage-nodes.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Decommission multiple Storage Nodes
:icons: font
:imagesdir: ../media/

[.lead]
If you need to remove more than one Storage Node, you can decommission them either sequentially or in parallel.

CAUTION: Use caution when you decommission Storage Nodes in a grid containing software-based metadata-only nodes. If you decommission all nodes configured to store _both_ objects and metadata, the ability to store objects is removed from the grid. See link:../primer/what-storage-node-is.html#types-of-storage-nodes[Types of Storage Nodes] for more information about metadata-only Storage Nodes.

* If you decommission Storage Nodes sequentially, you must wait for the first Storage Node to complete decommissioning before starting to decommission the next Storage Node.
* If you decommission Storage Nodes in parallel, the Storage Nodes simultaneously process decommission tasks for all Storage Nodes being decommissioned. This can result in a situation where all permanent copies of a file are marked as "read‐only," temporarily disabling deletion in grids where this functionality is enabled.

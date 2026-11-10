---
id: "storagegrid-118-98ae56ae830fd43a"
title: "StorageGRID 11.8 Consolidate Storage Nodes"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/consolidating-storage-nodes.adoc"
source_sha256: "036abab63e5b12976b596c4ced3bb7f3890a449f17d768bbba64c1b3c92679c3"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/consolidating-storage-nodes.adoc"
---

# StorageGRID 11.8 Consolidate Storage Nodes

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/consolidating-storage-nodes.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Consolidate Storage Nodes
:icons: font
:imagesdir: ../media/

[.lead]
You can consolidate Storage Nodes to reduce the Storage Node count for a site or deployment while increasing storage capacity.

When you consolidate Storage Nodes, you link:../expand/index.html[expand the StorageGRID system] by adding new, larger capacity Storage Nodes and then decommission the old, smaller capacity Storage Nodes. During the decommission procedure, objects are migrated from the old Storage Nodes to the new Storage Nodes.

NOTE: If you are consolidating older and smaller appliances with new models or larger capacity appliances, consider https://docs.netapp.com/us-en/storagegrid-appliances/commonhardware/how-appliance-node-cloning-works.html[cloning the appliance node^] (or use appliance node cloning and the decommission procedure if you aren't doing a one-to-one replacement).  

For example, you might add two new, larger capacity Storage Nodes to replace three older Storage Nodes. You would first use the expansion procedure to add the two new, larger Storage Nodes, and then use the decommission procedure to remove the three old, smaller capacity Storage Nodes.

By adding new capacity before removing existing Storage Nodes, you ensure a more balanced distribution of data across the StorageGRID system. You also reduce the possibility that an existing Storage Node might be pushed beyond the storage watermark level.

---
id: "storagegrid-118-c6b2bbbdf6a10c8f"
title: "StorageGRID 11.8 Add storage capacity for replicated objects"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/adding-storage-capacity-for-replicated-objects.adoc"
source_sha256: "b06970a6437b8567df12ba1b9287ed234eee2d40499d34f0f95f3e6e647b29e0"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "expand/adding-storage-capacity-for-replicated-objects.adoc"
---

# StorageGRID 11.8 Add storage capacity for replicated objects

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/adding-storage-capacity-for-replicated-objects.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Add storage capacity for replicated objects
:icons: font
:imagesdir: ../media/

[.lead]
If the information lifecycle management (ILM) policy for your deployment includes a rule that creates replicated copies of objects, you must consider how much storage to add and where to add the new storage volumes or Storage Nodes. 

For guidance on where to add additional storage, examine the ILM rules that create replicated copies. If ILM rules create two or more object copies, plan to add storage in each location where object copies are made. As a simple example, if you have a two-site grid and an ILM rule that creates one object copy at each site, you must link:../expand/adding-storage-volumes-to-storage-nodes.html[add storage] to each site to increase the overall object capacity of the grid. For information about object replication, see link:../ilm/what-replication-is.html[What is replication].

For performance reasons, you should attempt to keep storage capacity and compute power balanced across sites. So, for this example, you should add the same number of Storage Nodes to each site or additional storage volumes at each site.

If you have a more complex ILM policy that includes rules that place objects in different locations based on criteria such as bucket name, or rules that change object locations over time, your analysis of where storage is required for the expansion will be similar, but more complex.

Charting how quickly overall storage capacity is being consumed can help you understand how much storage to add in the expansion, and when the additional storage space will be required. You can use the Grid Manager to link:../monitor/monitoring-storage-capacity.html[monitor and chart storage capacity].

When planning the timing of an expansion, remember to consider how long it might take to procure and install additional storage.

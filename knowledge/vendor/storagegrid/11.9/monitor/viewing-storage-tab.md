---
id: "storagegrid-119-db501324848a9f44"
title: "StorageGRID 11.9 View the Storage tab"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/viewing-storage-tab.adoc"
source_sha256: "39808c4c0f65e3cc508cbc578eab1865d45a7d3b3c76f8859bfcc556dfcfb18c"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/viewing-storage-tab.adoc"
---

# StorageGRID 11.9 View the Storage tab

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/viewing-storage-tab.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View the Storage tab
:icons: font
:imagesdir: ../media/

[.lead]
The Storage tab summarizes storage availability and other storage metrics.

The Storage tab is shown for all nodes, each site, and the entire grid.

## Storage used graphs

For Storage Nodes, each site, and the entire grid, the Storage tab includes graphs showing how much storage has been used by object data and object metadata over time.

include::../_include/metrics-can-contain-wrong-values.adoc[]

image::../media/nodes_storage_node_storage_tab.png[Nodes > Storage Node > Storage tab]

## Disk devices, Volumes, and Object stores tables

For all nodes, the Storage tab contains details for the disk devices and volumes on the node. For Storage Nodes, the Object Stores table provides information about each storage volume.

image::../media/nodes_page_storage_tables.png[Nodes Page Storage Tables]

.Related information

link:monitoring-storage-capacity.html[Monitor storage capacity]

---
id: "storagegrid-120-db501324848a9f44"
title: "StorageGRID 12.0 View the StorageGRID Storage tab"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/viewing-storage-tab.adoc"
source_sha256: "b3bb6971dea780a4b94646c769f182a37c33463a996480f2e7668c052bf4e21a"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/viewing-storage-tab.adoc"
---

# StorageGRID 12.0 View the StorageGRID Storage tab

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/viewing-storage-tab.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View the StorageGRID Storage tab
:icons: font
:imagesdir: ../media/

[.lead]
The Storage tab summarizes storage availability and other storage metrics.

The Storage tab is shown for all nodes, each site, and the entire grid.

## Storage used graphs

For Storage Nodes, each site, and the entire grid, the Storage tab includes graphs showing how much storage has been used by object data and object metadata over time.

include::../_include/metrics-can-contain-wrong-values.adoc[]

image:nodes_storage_node_storage_tab.png[Nodes > Storage Node > Storage tab]

## Disk devices, Volumes, and Object stores tables

For all nodes, the Storage tab contains details for the disk devices and volumes on the node. For Storage Nodes, the Object Stores table provides information about each storage volume.

image:nodes_page_storage_tables.png[Nodes Page Storage Tables]

.Related information

link:monitoring-storage-capacity.html[Monitor storage capacity]

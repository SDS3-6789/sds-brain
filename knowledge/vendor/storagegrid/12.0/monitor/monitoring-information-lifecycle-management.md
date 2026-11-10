---
id: "storagegrid-120-cb3aae7bfb7b5775"
title: "StorageGRID 12.0 Monitor information lifecycle management in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/monitoring-information-lifecycle-management.adoc"
source_sha256: "303cfd912989857e492916c0fac0d6bac7f3d4b61b81e4a021fd55bda9a092e0"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/monitoring-information-lifecycle-management.adoc"
---

# StorageGRID 12.0 Monitor information lifecycle management in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/monitoring-information-lifecycle-management.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Monitor information lifecycle management in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
The information lifecycle management (ILM) system provides data management for all objects stored on the grid. You must monitor ILM operations to understand if the grid can handle the current load, or if more resources are needed.

.About this task
The StorageGRID system manages objects by applying the active ILM policies. The ILM policies and associated ILM rules determine how many copies are made, the type of copies that are created, where copies are placed, and the length of time each copy is retained.

Object ingest and other object-related activities can exceed the rate at which StorageGRID can evaluate ILM, causing the system to queue objects whose ILM placement instructions can't be fulfilled in near real time. You should monitor whether StorageGRID is keeping up with client actions.

## Use Grid Manager dashboard tab

.Steps

Use the ILM tab on the Grid Manager dashboard to monitor ILM operations:

. Sign in to the Grid Manager.
. From the dashboard, select the ILM tab and note the values on the ILM queue (Objects) card and ILM evaluation rate card.
+
Temporary spikes in the ILM queue (Objects) card on the dashboard are to be expected. But if the queue continues to increase and never declines, the grid needs more resources to operate efficiently: either more Storage Nodes, or, if the ILM policy places objects in remote locations, more network bandwidth.

## Use the Nodes page

.Steps

Additionally, investigate ILM queues using the *Nodes* page:

NOTE: The charts on the *Nodes* page will be replaced with the corresponding dashboard cards in a future StorageGRID release.

. Select *Nodes*.
. Select *_grid name_* > *ILM*.
. Position your cursor over the ILM queue graph to see the value of following attributes at a given point in time:
 ** *Objects queued (from client operations)*: The total number of objects awaiting ILM evaluation because of client operations (for example, ingest).
 ** *Objects queued (from all operations)*: The total number of objects awaiting ILM evaluation.
 ** *Scan rate (objects/sec)*: The rate at which objects in the grid are scanned and queued for ILM.
 ** *Evaluation rate (objects/sec)*: The current rate at which objects are being evaluated against the ILM policy in the grid.

+
NOTE: The ILM queue section is included for the grid only. This information is not shown on the ILM tab for a site or Storage Node.
. In the ILM Queue section, look at the following attributes.
 ** *Scan period - estimated*: The estimated time to complete a full ILM scan of all objects.
+
NOTE: A full scan does not guarantee that ILM has been applied to all objects.

 ** *Repairs attempted*: The total number of object repair operations for replicated data that have been attempted. This count increments each time a Storage Node tries to repair a high-risk object. High-risk ILM repairs are prioritized if the grid becomes busy.
+
The same object repair might increment again if replication failed after the repair. +
These attributes can be useful when you are monitoring the progress of Storage Node volume recovery. If the number of Repairs attempted has stopped increasing and a full scan has been completed, the repair has probably completed.

. Alternatively, submit a Prometheus query for `storagegrid_ilm_scan_period_estimated_minutes` and `storagegrid_ilm_repairs_attempted`.

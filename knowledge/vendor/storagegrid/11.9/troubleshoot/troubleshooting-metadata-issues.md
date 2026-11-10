---
id: "storagegrid-119-ca7ee3a0bebc58fe"
title: "StorageGRID 11.9 Troubleshoot metadata issues"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/troubleshoot/troubleshooting-metadata-issues.adoc"
source_sha256: "764a86c16fd7f6a910ef43c2cf6b57360aedac1c789023cc0d6f8016556b6021"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "troubleshoot/troubleshooting-metadata-issues.adoc"
---

# StorageGRID 11.9 Troubleshoot metadata issues

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/troubleshoot/troubleshooting-metadata-issues.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Troubleshoot metadata issues
:icons: font
:imagesdir: ../media/

[.lead]
If metadata issues occur, alerts will inform you of the source of the issues and recommended actions to take. In particular, you must add new Storage Nodes if the Low metadata storage alert is triggered.

.Before you begin
You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.About this task
Follow the recommended actions for each metadata-related alert that is triggered. If the *Low metadata storage* alert is triggered, you must add new Storage Nodes.

StorageGRID reserves a certain amount of space on volume 0 of each Storage Node for object metadata. This space, known as the _actual reserved space_, is subdivided into the space allowed for object metadata (the allowed metadata space) and the space required for essential database operations, such as compaction and repair. The allowed metadata space governs overall object capacity.

image::../media/metadata_allowed_space_volume_0.png[Metadata Allowed Space Volume 0]

If object metadata consumes more than 100% of the space allowed for metadata, database operations can't run efficiently and errors will occur.

You can link:../monitor/monitoring-storage-capacity.html#monitor-object-metadata-capacity-for-each-storage-node[monitor object metadata capacity for each Storage Node] to help you anticipate errors and correct them before they occur.

StorageGRID uses the following Prometheus metric to measure how full the allowed metadata space is:

----
storagegrid_storage_utilization_metadata_bytes/storagegrid_storage_utilization_metadata_allowed_bytes
----

When this Prometheus expression reaches certain thresholds, the *Low metadata storage* alert is triggered.

* *Minor*: Object metadata is using 70% or more of the allowed metadata space. You should add new Storage Nodes as soon as possible.
* *Major*: Object metadata is using 90% or more of the allowed metadata space. You must add new Storage Nodes immediately.
+
CAUTION: When object metadata is using 90% or more of the allowed metadata space, a warning appears on the dashboard. If this warning appears, you must add new Storage Nodes immediately. You must never allow object metadata to use more than 100% of the allowed space.

* *Critical*: Object metadata is using 100% or more of the allowed metadata space and is starting to consume the space required for essential database operations. You must stop the ingest of new objects, and you must add new Storage Nodes immediately.

CAUTION: If the size of volume 0 is smaller than the Metadata Reserved Space storage option (for example, in a non-production environment), the calculation for the *Low metadata storage* alert might be inaccurate.

.Steps
. Select *ALERTS* > *Current*.
. From the table of alerts, expand the *Low metadata storage* alert group, if required, and select the specific alert you want to view.
. Review the details in the alert dialog box.
. If a major or critical *Low metadata storage* alert has been triggered, perform an expansion to add Storage Nodes immediately.
+
NOTE: Because StorageGRID keeps complete copies of all object metadata at each site, the metadata capacity of the entire grid is limited by the metadata capacity of the smallest site. If you need to add metadata capacity to one site, you should also link:../expand/adding-grid-nodes-to-existing-site-or-adding-new-site.html[expand any other sites] by the same number of Storage Nodes.
+
After you perform the expansion, StorageGRID redistributes the existing object metadata to the new nodes, which increases the overall metadata capacity of the grid. No user action is required. The *Low metadata storage* alert is cleared.

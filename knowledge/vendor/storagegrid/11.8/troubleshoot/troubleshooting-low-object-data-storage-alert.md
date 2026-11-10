---
id: "storagegrid-118-39ca8fec3af7a2ba"
title: "StorageGRID 11.8 Troubleshoot the Low object data storage alert"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/troubleshooting-low-object-data-storage-alert.adoc"
source_sha256: "c5ac8c2473db1dbee98f72cf484269dd4c954c0620101bf032ae4f7740ec25b8"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "troubleshoot/troubleshooting-low-object-data-storage-alert.adoc"
---

# StorageGRID 11.8 Troubleshoot the Low object data storage alert

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/troubleshooting-low-object-data-storage-alert.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Troubleshoot the Low object data storage alert
:icons: font
:imagesdir: ../media/


[.lead]
The *Low object data storage* alert monitors how much space is available for storing object data on each Storage Node.

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:../admin/admin-group-permissions.html[specific access permissions].

.About this task
The *Low object data storage* alert is triggered when the total amount of replicated and erasure-coded object data on a Storage Node meets one of the conditions configured in the alert rule.

By default, a major alert is triggered when this condition evaluates as true:

----
(storagegrid_storage_utilization_data_bytes/
(storagegrid_storage_utilization_data_bytes + storagegrid_storage_utilization_usable_space_bytes)) >=0.90
----

In this condition:

* `storagegrid_storage_utilization_data_bytes` is an estimate of the total size of replicated and erasure-coded object data for a Storage Node.
* `storagegrid_storage_utilization_usable_space_bytes` is the total amount of object storage space remaining for a Storage Node.

If a major or minor *Low object data storage* alert is triggered, you should perform an expansion procedure as soon as possible.

.Steps
. Select *ALERTS* > *Current*.
+
The Alerts page appears.

. From the table of alerts, expand the *Low object data storage* alert group, if required, and select the alert you want to view.
+
NOTE: Select the alert, not the heading for a group of alerts.

. Review the details in the dialog box, and note the following:
 ** Time triggered
 ** The name of the site and node
 ** The current values of the metrics for this alert
. Select *NODES* > *_Storage Node or Site_* > *Storage*.
. Position your cursor over the Storage Used - Object Data graph.
+
The following values are shown:

 ** *Used (%)*: The percentage of the Total usable space that has been used for object data.
 ** *Used*: The amount of the Total usable space that has been used for object data.
 ** *Replicated data*: An estimate of the amount of replicated object data on this node, site, or grid.
 ** *Erasure-coded data*: An estimate of the amount of erasure-coded object data on this node, site, or grid.
 ** *Total*: The total amount of usable space on this node, site, or grid.
The Used value is the `storagegrid_storage_utilization_data_bytes` metric.

+
image::../media/nodes_page_storage_used_object_data.png[Nodes Page Storage Used Object Data]

. Select the time controls above the graph to view storage use over different time periods.
+
Looking at storage use over time can help you understand how much storage was used before and after the alert was triggered and can help you estimate how long it might take for the node's remaining space to become full.

. As soon as possible, link:../expand/guidelines-for-adding-object-capacity.html[add storage capacity] to your grid.
+
You can add storage volumes (LUNs) to existing Storage Nodes, or you can add new Storage Nodes.
+
NOTE: For more information, see link:../admin/managing-full-storage-nodes.html[Manage full Storage Nodes].

.Related information

link:troubleshooting-storage-status-alarm.html[Troubleshoot the Storage Status (SSTS) alarm (legacy)]

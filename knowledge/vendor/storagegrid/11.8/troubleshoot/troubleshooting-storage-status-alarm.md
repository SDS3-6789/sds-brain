---
id: "storagegrid-118-4272eedd69d84789"
title: "StorageGRID 11.8 Troubleshoot the Storage Status (SSTS) alarm"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/troubleshooting-storage-status-alarm.adoc"
source_sha256: "b6891d9c9e68ff028d814f10a08a23addb8f079b37fb71e1bdc5a0a62d230484"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "troubleshoot/troubleshooting-storage-status-alarm.adoc"
---

# StorageGRID 11.8 Troubleshoot the Storage Status (SSTS) alarm

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/troubleshooting-storage-status-alarm.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Troubleshoot the Storage Status (SSTS) alarm
:icons: font
:imagesdir: ../media/

[.lead]
The Storage Status (SSTS) alarm is triggered if a Storage Node has insufficient free space remaining for object storage.

.Before you begin
* You must be signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:../admin/admin-group-permissions.html[specific access permissions].

.About this task
The SSTS (Storage Status) alarm is triggered at the Notice level when the amount of free space on every volume in a Storage Node falls below the value of the Storage Volume Soft Read Only Watermark (*CONFIGURATION* > *System* > *Storage options*).

image::../media/storage_watermarks.png[Storage Options Overview]

For example, suppose the Storage Volume Soft Read-Only Watermark is set to 10 GB, which is its default value. The SSTS alarm is triggered if less than 10 GB of usable space remains on each storage volume in the Storage Node. If any of the volumes has 10 GB or more of available space, the alarm is not triggered.

If an SSTS alarm has been triggered, you can follow these steps to better understand the issue.

.Steps
. Select *SUPPORT* > *Alarms (legacy)* > *Current alarms*.
. From the Service column, select the data center, node, and service that are associated with the SSTS alarm.
+
The Grid Topology page appears. The Alarms tab shows the active alarms for the node and service you selected.
+
image::../media/ssts_alarm.png[Storage Node > LDR > Storage > Alarms tab]
+
In this example, both the SSTS (Storage Status) and SAVP (Total Usable Space (Percent)) alarms have been triggered at the Notice level.
+
NOTE: Typically, both the SSTS alarm and the SAVP alarm are triggered at about the same time; however, whether both alarms are triggered depends on the the watermark setting in GB and the SAVP alarm setting in percent.

. To determine how much usable space is actually available, select *LDR* > *Storage* > *Overview*, and find the Total Usable Space (STAS) attribute.
+
image::../media/storage_node_total_usable_space.png[Total Usable Space]
+
In this example, only 19.6 GB of the 164 GB of space on this Storage Node remains available. Note that the total value is the sum of the *Available* values for the three object store volumes. The SSTS alarm was triggered because each of the three storage volumes had less than 10 GB of available space.

. To understand how storage has been used over time, select the *Reports* tab, and plot Total Usable Space over the last few hours.
+
In this example, Total Usable Space dropped from roughly 155 GB at 12:00 to 20 GB at 12:35, which corresponds to the time at which the SSTS alarm was triggered.
+
image::../media/total_usable_space_chart.png[Total Usable Space - Chart]

. To understand how storage is being used as a percent of the total, plot Total Usable Space (Percent) over the last few hours.
+
In this example, the total usable space dropped from 95% to just over 10% at approximately the same time.
+
image::../media/total_usable_storage_percent_chart.png[Total Usable Space (Percent) - Chart]

. As required, link:../expand/guidelines-for-adding-object-capacity.html[add storage capacity].
+
Also see link:../admin/managing-full-storage-nodes.html[Manage full Storage Nodes].

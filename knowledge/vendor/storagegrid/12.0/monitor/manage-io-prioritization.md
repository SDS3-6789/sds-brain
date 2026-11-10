---
id: "storagegrid-120-d5c1d0210f06b265"
title: "StorageGRID 12.0 Change I/O prioritization in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/manage-io-prioritization.adoc"
source_sha256: "a9a7bfcba543557b4738f7c40817d39765d5683b83d49e9d060e1faff3c51b6c"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/manage-io-prioritization.adoc"
---

# StorageGRID 12.0 Change I/O prioritization in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/manage-io-prioritization.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Change I/O prioritization in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
Input/output (I/O) prioritization allows you to change the relative priorities for I/O operations on the grid. 

By default, client PUT and GET I/O traffic is given the highest priority over background activities such as purging erasure-coded (EC) data and EC repair. By increasing the priority of purging erasure-coded (EC) data and EC repair activities, these tasks can possibly complete faster. The effectiveness of I/O prioritization changes is impacted by the rate of client requests, network traffic fluctuations, and other ongoing network tasks. 

.Before you begin

* Review the I/O prioritization page, to determine which options might impact your grid.
* Assess whether the ongoing client traffic can safely handle longer wait times or client timeouts.
* Be prepared to monitor the effect of the prioritization change and adjust as necessary. These changes are implemented quickly but their effect might need hours to become visible.

.Steps

. Select *Support* > *I/O prioritization*.
. (Optional) Change the EC purge and repair priority, for background operations that purge EC data, from their default values.
+
NOTE: Use the default low EC purge and repair priority for grids that have RAID-based nodes.

. Select *Save*.
. Monitor the link:../monitor/commonly-used-prometheus-metrics.html#where-are-prometheus-metrics-used[metrics] to assess the effect of prioritization changes.

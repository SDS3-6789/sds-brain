---
id: "storagegrid-120-b5ef3dc17e6865de"
title: "StorageGRID 12.0 Monitor a StorageGRID system"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/index.adoc"
source_sha256: "a4617cbd18ed074ad98b94d2cf7fa02a07bc8160b5cb9030876db2bee74e7206"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/index.adoc"
---

# StorageGRID 12.0 Monitor a StorageGRID system

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/index.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Monitor a StorageGRID system
:icons: font
:imagesdir: ../media/

[.lead]
Monitor your StorageGRID system regularly to ensure it is performing as expected. 

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:../admin/admin-group-permissions.html[specific access permissions].

NOTE: To change units for the storage values displayed in the Grid Manager, select the user drop-down in the upper right of the Grid Manager, then select *User preferences*.

.About this task

These instructions describe how to:

* link:viewing-dashboard.html[View and manage the dashboard]
* link:viewing-nodes-page.html[View the Nodes page]
* link:information-you-should-monitor-regularly.html[Monitor these aspects of the system regularly:]
** link:monitoring-system-health.html[System health]
** link:monitoring-storage-capacity.html[Storage capacity]
** link:monitoring-information-lifecycle-management.html[Information lifecycle management]
** link:monitoring-network-connections-and-performance.html[Networking and system resources]
** link:monitoring-tenant-activity.html[Tenant activity]
** link:monitoring-load-balancing-operations.html[Load balancing operations]
** link:grid-federation-monitor-connections.html[Grid federation connections]
* link:managing-alerts.html[Manage alerts]
* link:logs-files-reference.html[View log files]
* link:configure-log-management.html[Configure log management and external syslog server]
* link:considerations-for-external-syslog-server.html[Use an external syslog server] to collect audit information
* link:using-snmp-monitoring.html[Use SNMP for monitoring]
* link:manage-io-prioritization.html[Change I/O prioritization] to change the relative priorities for I/O operations

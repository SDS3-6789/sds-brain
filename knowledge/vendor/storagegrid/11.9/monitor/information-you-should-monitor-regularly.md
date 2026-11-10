---
id: "storagegrid-119-2e66d12d647ed6e7"
title: "StorageGRID 11.9 What and when to monitor"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/information-you-should-monitor-regularly.adoc"
source_sha256: "ef59b0a905e239861b4ee83f125d6a06bd76d9aadf00cde2499192c2db6088b0"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/information-you-should-monitor-regularly.adoc"
---

# StorageGRID 11.9 What and when to monitor

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/information-you-should-monitor-regularly.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# What and when to monitor
:icons: font
:imagesdir: ../media/

[.lead]
Even though the StorageGRID system can continue to operate when errors occur or parts of the grid are unavailable, you should monitor and address potential issues before they affect the grid's efficiency or availability.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:../admin/admin-group-permissions.html[specific access permissions].

.About monitoring tasks

A busy system generates large amounts of information. The following list provides guidance about the most important information to monitor on an ongoing basis.

[cols="1a,1a" options="header"]
|===
| What to monitor| Frequency

| link:monitoring-system-health.html[System health status]
| Daily

| Rate at which link:monitoring-storage-capacity.html[Storage Node object and metadata capacity] is being consumed
| Weekly

| link:monitoring-information-lifecycle-management.html[Information lifecycle management operations]
| Weekly

| link:monitoring-network-connections-and-performance.html[Networking and system resources]
| Weekly

| link:monitoring-tenant-activity.html[Tenant activity]
| Weekly

| link:monitoring-object-ingest-and-retrieval-rates.html[S3 client operations]
| Weekly

| link:monitoring-load-balancing-operations.html[Load balancing operations]
| After the initial configuration and after any configuration changes

| link:grid-federation-monitor-connections.html[Grid federation connections]
| Weekly
|===

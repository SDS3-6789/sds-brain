---
id: "storagegrid-119-3fa3f2a3277045c9"
title: "StorageGRID 11.9 Restore object data to storage volume for appliance"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/restoring-object-data-to-storage-volume-for-appliance.adoc"
source_sha256: "85d56a1824680571c52b8c84bfc53a15f5aeaf5abf30af4c91e0c4fc52beb19d"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/restoring-object-data-to-storage-volume-for-appliance.adoc"
---

# StorageGRID 11.9 Restore object data to storage volume for appliance

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/restoring-object-data-to-storage-volume-for-appliance.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Restore object data to storage volume for appliance
:icons: font
:imagesdir: ../media/

[.lead]
After recovering storage volumes for the appliance Storage Node, you can restore the replicated or erasure-coded object data that was lost when the Storage Node failed.

include::../_include/restore-data-intro.adoc[]
include::../_include/restore-data-repair.adoc[]

## Monitor repairs
Monitor the status of the repair jobs, based on whether you use *replicated data*, *erasure-coded (EC) data*, or both.

You can also monitor the status of volume restoration jobs in process and view a history of restoration jobs completed in 
link:../maintain/restoring-volume.html[Grid Manager].

include::../_include/restore-data-monitor.adoc[]

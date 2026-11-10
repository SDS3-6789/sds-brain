---
id: "storagegrid-120-933046e917562391"
title: "StorageGRID 12.0 GTST audit message for started grid tasks in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/gtst-grid-task-started.adoc"
source_sha256: "cc536c66d95f3f487c3244c59259d19def0e20791bc2c6985d73f20b24840a64"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/gtst-grid-task-started.adoc"
---

# StorageGRID 12.0 GTST audit message for started grid tasks in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/gtst-grid-task-started.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# GTST audit message for started grid tasks in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
This audit message indicates that the CMN service has started to process the specified grid task. The audit message immediately follows the Grid Task Submitted message for grid tasks initiated by the internal Grid Task Submission service and selected for automatic activation. For grid tasks submitted into the Pending table, this message is generated when the user starts the grid task.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
TSID
a|
Task ID
a|
This field uniquely identifies a generated grid task and allows the task to be managed over its lifecycle.

*Note:* The Task ID is assigned at the time that a grid task is generated, not the time that it is submitted. It is possible for a given grid task to be submitted multiple times, and in this case the Task ID field is not sufficient to uniquely link the Submitted, Started, and Ended audit messages.

a|
RSLT
a|
Result
a|
The result. This field has only one value:

* SUCS: The grid task was started successfully.

|===

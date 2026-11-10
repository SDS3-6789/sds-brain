---
id: "storagegrid-118-933046e917562391"
title: "StorageGRID 11.8 GTST: Grid Task Started"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/gtst-grid-task-started.adoc"
source_sha256: "a4d0fed15f98f9fe52c18019b9cde4f78ab2be972e2ee43a76c147bc4bb62b1b"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/gtst-grid-task-started.adoc"
---

# StorageGRID 11.8 GTST: Grid Task Started

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/gtst-grid-task-started.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# GTST: Grid Task Started
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

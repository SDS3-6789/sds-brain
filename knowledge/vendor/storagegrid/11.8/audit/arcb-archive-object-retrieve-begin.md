---
id: "storagegrid-118-9e761767e7dee476"
title: "StorageGRID 11.8 ARCB: Archive Object Retrieve Begin"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/arcb-archive-object-retrieve-begin.adoc"
source_sha256: "77cce5b7088db2a42387d9d518fd053b405c936b89062cd3615796b236465964"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/arcb-archive-object-retrieve-begin.adoc"
---

# StorageGRID 11.8 ARCB: Archive Object Retrieve Begin

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/arcb-archive-object-retrieve-begin.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# ARCB: Archive Object Retrieve Begin
:icons: font
:imagesdir: ../media/

[.lead]
This message is generated when a request is made to retrieve archived object data and the retrieval process begins. Retrieval requests are processed immediately, but can be reordered to improve efficiency of retrieval from linear media such as tape.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
CBID
a|
Content Block ID
a|
The unique identifier of the Content Block to be retrieved from the external archival storage system.
a|
RSLT
a|
Result
a|
Indicates the result of starting the archive retrieval process. Currently defined value is:SUCS: The content request was received and queued for retrieval.

|===
This audit message marks the time of an archive retrieval. It allows you to match the message with a corresponding ARCE end message to determine the duration of archive retrieval, and whether the operation was successful.

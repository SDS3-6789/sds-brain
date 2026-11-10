---
id: "storagegrid-120-8a0594371f355218"
title: "StorageGRID 12.0 CBRE audit message for object receive end in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/cbre-object-receive-end.adoc"
source_sha256: "d0ab3e6071763d7dd72d653f606e94ec6eb6da1983215e903ae92419218f3608"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/cbre-object-receive-end.adoc"
---

# StorageGRID 12.0 CBRE audit message for object receive end in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/cbre-object-receive-end.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# CBRE audit message for object receive end in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
When transfer of a content block from one node to another is completed, this message is issued by the destination entity.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
CNID
a|
Connection Identifier
a|
The unique identifier of the node-to-node session/connection.
a|
CBID
a|
Content Block Identifier
a|
The unique identifier of the content block being transferred.
a|
CTDR
a|
Transfer Direction
a|
Indicates if the CBID transfer was push-initiated or pull-initiated:

PUSH: The transfer operation was requested by the sending entity.

PULL: The transfer operation was requested by the receiving entity.

a|
CTSR
a|
Source Entity
a|
The node ID of the source (sender) of the CBID transfer.
a|
CTDS
a|
Destination Entity
a|
The node ID of the destination (receiver) of the CBID transfer.
a|
CTSS
a|
Start Sequence Count
a|
Indicates the sequence count on which the transfer started.
a|
CTAS
a|
Actual End Sequence Count
a|
Indicates the last sequence count successfully transferred. If the Actual End Sequence Count is the same as the Start Sequence Count, and the Transfer Result was not successful, no data was exchanged.
a|
RSLT
a|
Transfer Result
a|
The result of the transfer operation (from the perspective of the sending entity):

SUCS: transfer successfully completed; all requested sequence counts were sent.

CONL: connection lost during transfer

CTMO: connection timed-out during establishment or transfer

UNRE: destination node ID unreachable

CRPT: transfer ended due to reception of corrupt or invalid data

|===

This audit message means a node-to-node data transfer operation was completed. If the Transfer Result was successful, the operation transferred data from "Start Sequence Count" to "Actual End Sequence Count". Sending and receiving nodes are identified by their node IDs. This information can be used to track system data flow and to locate, tabulate, and analyze errors. When combined with storage audit messages, it can also be used to verify replica counts.

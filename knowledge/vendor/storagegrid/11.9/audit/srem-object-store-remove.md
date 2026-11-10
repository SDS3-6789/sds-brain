---
id: "storagegrid-119-31e0af3e2b54260b"
title: "StorageGRID 11.9 SREM: Object Store Remove"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/srem-object-store-remove.adoc"
source_sha256: "d0d52d704d8d94f0cd42a6f506f20d7fbd4dd3fd08bb1c30ff8787e3f24f6aeb"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/srem-object-store-remove.adoc"
---

# StorageGRID 11.9 SREM: Object Store Remove

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/srem-object-store-remove.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# SREM: Object Store Remove
:icons: font
:imagesdir: ../media/

[.lead]
This message is issued when content is removed from persistent storage and is no longer accessible through regular APIs.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
CBID
a|
Content Block Identifier
a|
The unique identifier of the content block deleted from permanent storage.
a|
RSLT
a|
Result Code
a|
Indicates the result of the content removal operations. The only defined value is:

SUCS: Content removed from persistent storage

|===
This audit message means a given content block has been deleted from a node and can no longer be requested directly. The message can be used to track the flow of deleted content within the system.

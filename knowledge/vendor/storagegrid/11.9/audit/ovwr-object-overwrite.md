---
id: "storagegrid-119-8324f3a56e251877"
title: "StorageGRID 11.9 OVWR: Object Overwrite"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/ovwr-object-overwrite.adoc"
source_sha256: "146a7e0884dc778d8baf486b2f9d91c59953f67c70309299fe7dda58bcc440cc"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/ovwr-object-overwrite.adoc"
---

# StorageGRID 11.9 OVWR: Object Overwrite

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/ovwr-object-overwrite.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# OVWR: Object Overwrite
:icons: font
:imagesdir: ../media/

[.lead]
This message is generated when an external (client-requested) operation causes one object to be overwritten by another object.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
|
CBID
|
Content Block Identifier (new)
|
The CBID for the new object.
|
CSIZ
|
Previous Object Size
|
The size, in bytes, of the object being overwritten.
|
OCBD
|
Content Block Identifier (previous)
|
The CBID for the previous object.
|
UUID
|
Universally Unique ID (new)
|
The identifier of the new object within the StorageGRID system.
|
OUID
|
Universally Unique ID (previous)
|
The identifier for the previous object within the StorageGRID system.
|
PATH
|
S3 Object Path
|
The S3 object path used for both the previous and new object
|
RSLT
|
Result Code
|
Result of the Object Overwrite transaction. Result is always:

SUCS: Successful

|SGRP
|Site (Group)
|If present, the overwritten object was deleted at the site specified, which is not the site where the overwritten object was ingested.

|===

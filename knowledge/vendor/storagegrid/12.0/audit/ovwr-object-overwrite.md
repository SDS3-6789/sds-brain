---
id: "storagegrid-120-8324f3a56e251877"
title: "StorageGRID 12.0 OVWR audit message for object overwrites in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/ovwr-object-overwrite.adoc"
source_sha256: "40debce7f65965e47745f4ff64d11d8ca14aca785a76feda829e9ed40b8179b9"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/ovwr-object-overwrite.adoc"
---

# StorageGRID 12.0 OVWR audit message for object overwrites in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/ovwr-object-overwrite.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# OVWR audit message for object overwrites in StorageGRID
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

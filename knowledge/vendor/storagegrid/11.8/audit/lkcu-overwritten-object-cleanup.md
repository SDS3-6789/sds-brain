---
id: "storagegrid-118-3e7e964ecedf6dc2"
title: "StorageGRID 11.8 LKCU: Overwritten Object Cleanup"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/lkcu-overwritten-object-cleanup.adoc"
source_sha256: "10163a58770a92d1d746e43bbf6965e162e1ac08c860f5d9873e4e9ec5515b02"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/lkcu-overwritten-object-cleanup.adoc"
---

# StorageGRID 11.8 LKCU: Overwritten Object Cleanup

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/lkcu-overwritten-object-cleanup.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# LKCU: Overwritten Object Cleanup
:icons: font
:imagesdir: ../media/

[.lead]
This message is generated when StorageGRID removes an overwritten object that previously required cleanup to free up storage space. An object is overwritten when an S3 or Swift client writes an object to a path already containing a object. The removal process occurs automatically and in the background.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
CSIZ
a|
Content size
a|
The size of the object in bytes.
a|
LTYP
a|
Type of cleanup
a|
_Internal use only._
a|
LUID
a|
Removed Object UUID
a|
The identifier of the object that was removed.
a|
PATH
a|
S3 Bucket/Key or Swift Container/Object ID
a|
The S3 bucket name and S3 key name, or the Swift container name and Swift object identifier.
a|
SEGC
a|
Container UUID
a|
UUID of the container for the segmented object. This value is available only if the object is segmented.
a|
UUID
a|
Universally Unique Identifier
a|
The identifier of the object that still exists. This value is available only if the object has not been deleted.
|===

---
id: "storagegrid-118-0c271bab161767b4"
title: "StorageGRID 11.8 ASCT: Archive Store Cloud-Tier"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/asct-archive-store-cloud-tier.adoc"
source_sha256: "ec11b8138455ad9252cc8857b4327cdc60c89a2c330cd0abb98566da793ef08a"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/asct-archive-store-cloud-tier.adoc"
---

# StorageGRID 11.8 ASCT: Archive Store Cloud-Tier

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/asct-archive-store-cloud-tier.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# ASCT: Archive Store Cloud-Tier
:icons: font
:imagesdir: ../media/

[.lead]
This message is generated when archived object data is stored to an external archival storage system, which connects to StorageGRID through the S3 API.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
CBID
a|
Content Block ID
a|
The unique identifier for the content block that was retrieved.
a|
CSIZ
a|
Content Size
a|
The size of the object in bytes.
a|
RSLT
a|
Result Code
a|
Returns successful (SUCS) or the error reported by the backend.
a|
SUID
a|
Storage Unique Identifier
a|
Unique identifier (UUID) of the cloud-tier the content was stored to.
a|
TIME
a|
Time
a|
Total processing time for the request in microseconds.
|===

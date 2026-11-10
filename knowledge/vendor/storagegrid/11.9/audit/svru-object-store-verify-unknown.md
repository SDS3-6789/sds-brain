---
id: "storagegrid-119-6238d35a78a66482"
title: "StorageGRID 11.9 SVRU: Object Store Verify Unknown"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/svru-object-store-verify-unknown.adoc"
source_sha256: "160a6465b643dc78b28516d043e9998184156d5cc907e4e82edee0aa5cbaa5b2"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/svru-object-store-verify-unknown.adoc"
---

# StorageGRID 11.9 SVRU: Object Store Verify Unknown

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/svru-object-store-verify-unknown.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# SVRU: Object Store Verify Unknown
:icons: font
:imagesdir: ../media/

[.lead]
The LDR service's Storage component continuously scans all copies of replicated object data in the object store. This message is issued when an unknown or unexpected copy of replicated object data is detected in the object store and moved to the quarantine directory.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description

| FPTH
| File Path

| The file path of the unexpected object copy.
| RSLT

| Result
| This field has the value 'NONE'. RSLT is a mandatory message field, but is not relevant for this message. 'NONE' is used rather than 'SUCS' so that this message is not filtered.
|===

NOTE: The SVRU: Object Store Verify Unknown audit message should be monitored closely. It means unexpected copies of object data were detected in the object store. This situation should be investigated immediately to determine how theses copies were created, because it can indicate impending hardware failures.

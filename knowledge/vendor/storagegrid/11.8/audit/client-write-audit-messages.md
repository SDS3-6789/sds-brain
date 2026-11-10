---
id: "storagegrid-118-bb4b6f0dc6aa4e5e"
title: "StorageGRID 11.8 Client write audit messages"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/client-write-audit-messages.adoc"
source_sha256: "a8c1d959410312307ff27c937faf47b98f3fab322bc7c346f89c49adb27649a4"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/client-write-audit-messages.adoc"
---

# StorageGRID 11.8 Client write audit messages

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/client-write-audit-messages.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Client write audit messages
:icons: font
:imagesdir: ../media/

[.lead]
Client write audit messages are logged when an S3 or Swift client application makes a request to create or modify an object.

[cols="1a,3a,1a,1a" options="header"]
|===
| Code
| Description
| Used by
| See

| OVWR
| Object Overwrite: Logs a transaction to overwrite one object with another object.
| S3 and Swift clients
| link:ovwr-object-overwrite.html[OVWR: Object Overwrite]

| SDEL
| S3 DELETE: Logs a successful transaction to delete an object or bucket.

*Note:* If the transaction operates on a subresource, the audit message will include the field S3SR.

| S3 client
| link:sdel-s3-delete.html[SDEL: S3 DELETE]

| SPOS
| S3 POST: Logs a successful transaction to restore an object from AWS Glacier storage to a Cloud Storage Pool.
| S3 client
| link:spos-s3-post.html[SPOS: S3 POST]

| SPUT
| S3 PUT: Logs a successful transaction to create a new object or bucket.

*Note:* If the transaction operates on a subresource, the audit message will include the field S3SR.

| S3 client
| link:sput-s3-put.html[SPUT: S3 PUT]

| SUPD
| S3 Metadata Updated: Logs a successful transaction to update the metadata for an existing object or bucket.
| S3 client
| link:supd-s3-metadata-updated.html[SUPD: S3 Metadata Updated]

| WDEL
| Swift DELETE: Logs a successful transaction to delete an object or container.
| Swift client
| link:wdel-swift-delete.html[WDEL: Swift DELETE]

| WPUT
| Swift PUT: Logs a successful transaction to create a new object or container.
| Swift client
| link:wput-swift-put.html[WPUT: Swift PUT]
|===

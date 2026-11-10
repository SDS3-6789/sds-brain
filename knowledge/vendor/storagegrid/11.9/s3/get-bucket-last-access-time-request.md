---
id: "storagegrid-119-3bfd0bed501c1b51"
title: "StorageGRID 11.9 GET Bucket last access time"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/get-bucket-last-access-time-request.adoc"
source_sha256: "715b89e67dd4a17b4ee8dee9e67d11f00e15115e13ae5f1c95c548c91feeba4f"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/get-bucket-last-access-time-request.adoc"
---

# StorageGRID 11.9 GET Bucket last access time

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/get-bucket-last-access-time-request.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# GET Bucket last access time
:icons: font
:imagesdir: ../media/

[.lead]
The GET Bucket last access time request allows you to determine if last access time updates are enabled or disabled for individual buckets.

You must have the s3:GetBucketLastAccessTime permission, or be account root, to complete this operation.

## Request example

[subs="specialcharacters,quotes"]
----
GET /bucket?x-ntap-sg-lastaccesstime HTTP/1.1
Date: _date_
Authorization: _authorization string_
Host: _host_
----

## Response example

This example shows that last access time updates are enabled for the bucket.

----
HTTP/1.1 200 OK
Date: Sat, 29 Nov 2015 01:02:18 GMT
Connection: CLOSE
Server: StorageGRID/10.3.0
x-amz-request-id: 12345
Content-Length: 127
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<LastAccessTime xmlns="http://s3.storagegrid.com/doc/2015-02-01/">enabled
</LastAccessTime>
----

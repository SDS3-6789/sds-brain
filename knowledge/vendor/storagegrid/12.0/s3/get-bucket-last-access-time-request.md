---
id: "storagegrid-120-3bfd0bed501c1b51"
title: "StorageGRID 12.0 Retrieve the bucket last access time status in StorageGRID with the GET Bucket last access time request"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/s3/get-bucket-last-access-time-request.adoc"
source_sha256: "8baee9bd5e99e950a877bf6b56074279eafe87ddf5f49793c7de2d8d2a3186d8"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/get-bucket-last-access-time-request.adoc"
---

# StorageGRID 12.0 Retrieve the bucket last access time status in StorageGRID with the GET Bucket last access time request

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/s3/get-bucket-last-access-time-request.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Retrieve the bucket last access time status in StorageGRID with the GET Bucket last access time request
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

---
id: "storagegrid-120-7f21dead4ea53465"
title: "StorageGRID 12.0 Retrieve bucket consistency level in StorageGRID with the GET Bucket consistency request"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/s3/get-bucket-consistency-request.adoc"
source_sha256: "73905c69405a8c05e2315c58c89a6be687a9f313b9d51c8d90b84367bb873af1"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/get-bucket-consistency-request.adoc"
---

# StorageGRID 12.0 Retrieve bucket consistency level in StorageGRID with the GET Bucket consistency request

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/s3/get-bucket-consistency-request.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Retrieve bucket consistency level in StorageGRID with the GET Bucket consistency request
:icons: font
:imagesdir: ../media/

[.lead]
The GET Bucket consistency request allows you to determine the consistency being applied to a particular bucket.

The default consistency is set to guarantee read-after-write for newly created objects.

You must have the s3:GetBucketConsistency permission, or be account root, to complete this operation. 

## Request example

[subs="specialcharacters,quotes"]
----
GET /bucket?x-ntap-sg-consistency HTTP/1.1
Date: _date_
Authorization: _authorization string_
Host: _host_
----

## Response

In the response XML, `<Consistency>` will return one of the following values:

[cols="1a,2a" options="header"]
|===
| Consistency| Description

|all
|All nodes receive the data immediately, or the request will fail.

|strong-global
|Guarantees read-after-write consistency for all client requests across all sites.

|strong-site
|Guarantees read-after-write consistency for all client requests within a site.

|read-after-new-write
|(Default) Provides read-after-write consistency for new objects and eventual consistency for object updates. Offers high availability and data protection guarantees. Recommended for most cases.

|available
|Provides eventual consistency for both new objects and object updates. For S3 buckets, use only as required (for example, for a bucket that contains log values that are rarely read, or for HEAD or GET operations on keys that don't exist). Not supported for S3 FabricPool buckets.
|===

## Response example

----
HTTP/1.1 200 OK
Date: Fri, 18 Sep 2020 01:02:18 GMT
Connection: CLOSE
Server: StorageGRID/11.5.0
x-amz-request-id: 12345
Content-Length: 127
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<Consistency xmlns="http://s3.storagegrid.com/doc/2015-02-01/">read-after-new-write</Consistency>
----

.Related information

link:consistency.html[Consistency]

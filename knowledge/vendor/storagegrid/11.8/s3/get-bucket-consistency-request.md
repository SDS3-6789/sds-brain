---
id: "storagegrid-118-7f21dead4ea53465"
title: "StorageGRID 11.8 GET Bucket consistency"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/s3/get-bucket-consistency-request.adoc"
source_sha256: "dd9c0f3bb4ed127092deda323f4e3bff252ea5e3cf4119f0fa745abf90562179"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/get-bucket-consistency-request.adoc"
---

# StorageGRID 11.8 GET Bucket consistency

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/s3/get-bucket-consistency-request.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# GET Bucket consistency
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

link:consistency-controls.html[Consistency values]

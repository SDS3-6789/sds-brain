---
id: "storagegrid-119-1379d9f2c48b8ed2"
title: "StorageGRID 11.9 Understand notifications for buckets"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/understanding-notifications-for-buckets.adoc"
source_sha256: "474e7c3caeb9a1ac7bf9bb441298156759029cad2d7a35607f59ca099b296fed"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/understanding-notifications-for-buckets.adoc"
---

# StorageGRID 11.9 Understand notifications for buckets

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/understanding-notifications-for-buckets.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Understand notifications for buckets
:icons: font
:imagesdir: ../media/

[.lead]
You can enable event notification for an S3 bucket if you want StorageGRID to send notifications about specified events to a destination Kafka cluster or Amazon Simple Notification Service.

For example, you could configure alerts to be sent to administrators about each object added to a bucket, where the objects represent log files associated with a critical system event.

Event notifications are created at the source bucket as specified in the notification configuration and are delivered to the destination. If an event associated with an object succeeds, a notification about that event is created and queued for delivery.

The uniqueness and ordering of notifications aren't guaranteed. More than one notification of an event might be delivered to the destination as a result of operations taken to guarantee delivery success. And because delivery is asynchronous, the time ordering of notifications at the destination is not guaranteed to match the ordering of events on the source bucket, particularly for operations that originate from different StorageGRID sites. You can use the `sequencer` key in the event message to determine the order of events for a particular object, as described in Amazon S3 documentation.

StorageGRID event notifications follow the Amazon S3 API with some limitations.

* The following event types are supported:

** s3:ObjectCreated:
** s3:ObjectCreated:Put
** s3:ObjectCreated:Post
** s3:ObjectCreated:Copy
** s3:ObjectCreated:CompleteMultipartUpload
** s3:ObjectRemoved:
** s3:ObjectRemoved:Delete
** s3:ObjectRemoved:DeleteMarkerCreated
** s3:ObjectRestore:Post

* Event notifications sent from StorageGRID use the standard JSON format but don't include some keys and use specific values for others, as shown in the table:

[cols="1a,2a" options="header"]
|===
| Key name| StorageGRID value
| eventSource
| `sgws:s3`

| awsRegion
| _not included_

| x-amz-id-2
| _not included_

| arn
| `urn:sgws:s3:::bucket_name`
|===

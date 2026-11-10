---
id: "storagegrid-119-f5b6f1c8e1f93685"
title: "StorageGRID 11.9 StorageGRID custom operations"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/custom-operations-on-buckets.adoc"
source_sha256: "c72b3d366321e901fd82d64803f4ae8675e2cf4a4d9a750a6ac6e6fd86999536"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/custom-operations-on-buckets.adoc"
---

# StorageGRID 11.9 StorageGRID custom operations

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/custom-operations-on-buckets.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# StorageGRID custom operations
:icons: font
:imagesdir: ../media/

[.lead]
The StorageGRID system supports custom operations that are added on to the S3 REST API.

The following table lists the custom operations supported by StorageGRID.

[cols="1a,2a" options="header"]
|===
| Operation| Description

| link:get-bucket-consistency-request.html[GET Bucket consistency]
| Returns the consistency being applied to a particular bucket.

| link:put-bucket-consistency-request.html[PUT Bucket consistency]
| Sets the consistency applied to a particular bucket.

| link:get-bucket-last-access-time-request.html[GET Bucket last access time]
| Returns whether last access time updates are enabled or disabled for a particular bucket.

| link:put-bucket-last-access-time-request.html[PUT Bucket last access time]
| Allows you to enable or disable last access time updates for a particular bucket.

| link:delete-bucket-metadata-notification-configuration-request.html[DELETE Bucket metadata notification configuration]
| Deletes the metadata notification configuration XML associated with a particular bucket.

| link:get-bucket-metadata-notification-configuration-request.html[GET Bucket metadata notification configuration]
| Returns the metadata notification configuration XML associated with a particular bucket.

| link:put-bucket-metadata-notification-configuration-request.html[PUT Bucket metadata notification configuration]
| Configures the metadata notification service for a bucket.

| link:get-storage-usage-request.html[GET Storage Usage]
| Tells you the total amount of storage in use by an account and for each bucket associated with the account.

| link:deprecated-put-bucket-request-modifications-for-compliance.html[Deprecated: CreateBucket with compliance settings]
| Deprecated and not supported: You can no longer create new buckets with Compliance enabled.

| link:deprecated-get-bucket-compliance-request.html[Deprecated: GET Bucket compliance]
| Deprecated but supported: Returns the compliance settings currently in effect for an existing legacy Compliant bucket.

| link:deprecated-put-bucket-compliance-request.html[Deprecated: PUT Bucket compliance]
| Deprecated but supported: Allows you to modify the compliance settings for an existing legacy Compliant bucket.

|===

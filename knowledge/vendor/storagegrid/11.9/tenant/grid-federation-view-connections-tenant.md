---
id: "storagegrid-119-fc8db9260dcf7a92"
title: "StorageGRID 11.9 View grid federation connections"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/grid-federation-view-connections-tenant.adoc"
source_sha256: "de4ead6b92c6fb39d56a96c5b2b0e38d93e511ddc6d55d8653c64bb526671fee"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/grid-federation-view-connections-tenant.adoc"
---

# StorageGRID 11.9 View grid federation connections

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/grid-federation-view-connections-tenant.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View grid federation connections
:icons: font
:imagesdir: ../media/

[.lead]
If your tenant account has the *Use grid federation connection* permission, you can view the allowed connections.

.Before you begin

* The tenant account has the *Use grid federation connection* permission.
* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the link:tenant-management-permissions.html[Root access permission].

.Steps

. Select *STORAGE (S3)* > *Grid federation connections*.
+
The Grid federation connection page appears and includes a table that summarizes the following information:
+
[cols="1a,2a" options="header"]
|===
| Column
| Description

| Connection name
| The grid federation connections this tenant has permission to use. 

| Buckets with cross-grid replication 
| For each grid federation connection, the tenant buckets that have cross-grid replication enabled. Objects added to these buckets will be replicated to the other grid in the connection.

| Last error
| For each grid federation connection, the most recent error to occur, if any, when data was being replicated to the other grid. See <<clear-last-error,Clear the last error>>.

|===


. Optionally, select a bucket name to link:viewing-s3-bucket-details.html[view bucket details].

## [[clear-last-error]]Clear the last error

An error might appear in the *Last error* column for one of these reasons:

* The source object version was not found.
* The source bucket was not found.
* The destination bucket was deleted.
* The destination bucket was re-created by a different account.	
* The destination bucket has versioning suspended.
* The destination bucket was re-created by the same account but is now unversioned.

NOTE: This column only shows the last cross-grid replication error to occur; previous errors that might have occurred will not be shown.

.Steps

. If a message appears in the *Last error* column, view the message text.
+
For example, this error indicates that the destination bucket for cross-grid replication was in an invalid state, possibly because versioning was suspended or S3 Object Lock was enabled.
+
image::../media/grid-federation-cgr-object-example-last-error.png[grid-federation-cgr-object-example-last-error]

. Perform any recommended actions. For example, if versioning was suspended on the destination bucket for cross-grid replication, reenable versioning for that bucket.

. Select the connection from the table.
. Select *Clear error*.
. Select *Yes* to clear the message and update the system's status.
. Wait 5-6 minutes and then ingest a new object into the bucket. Confirm that the error message does not reappear.
+
NOTE: To ensure the error message is cleared, wait at least 5 minutes after the timestamp in the message before ingesting a new object.

. To determine if any objects failed to be replicated because of the bucket error, see link:../admin/grid-federation-retry-failed-replication.html[Identify and retry failed replication operations].

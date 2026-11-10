---
id: "storagegrid-119-680002094043377c"
title: "StorageGRID 11.9 View another user's S3 access keys"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/viewing-another-users-s3-access-keys.adoc"
source_sha256: "8f95c30357d0f5212ee90f8ce7bd201d1c2abc0d278906be493d599f01be42f5"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/viewing-another-users-s3-access-keys.adoc"
---

# StorageGRID 11.9 View another user's S3 access keys

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/viewing-another-users-s3-access-keys.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View another user's S3 access keys
:icons: font
:imagesdir: ../media/

[.lead]
If you are using an S3 tenant and you have appropriate permissions, you can view another user's S3 access keys. You can sort the list by expiration time so you can determine which keys will expire soon. As needed, you can create new keys and delete keys that are no longer in use.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:tenant-management-permissions.html[Root access permission].

CAUTION: The S3 buckets and objects belonging to a user can be accessed using the access key ID and secret access key displayed for that user in the Tenant Manager. For this reason, protect access keys as you would a password. Rotate access keys on a regular basis, remove any unused keys from the account, and never share them with other users.

.Steps
. Select *ACCESS MANAGEMENT* > *Users*.

. From the Users page, select the user whose S3 access keys you want to view.

. From the User details page, select *Access keys*.

. Sort the keys by *Expiration time* or *Access key ID*.

. As needed, create new keys and manually delete keys that the are no longer in use.
+
If you create new keys before the existing keys expire, the user can begin using the new keys without temporarily losing access to the objects in the account.
+
Expired keys are removed automatically.

.Related information

* link:creating-another-users-s3-access-keys.html[Create another user's S3 access keys]

* link:deleting-another-users-s3-access-keys.html[Delete another user's S3 access keys]

---
id: "storagegrid-118-0f0c31c9b4f6a268"
title: "StorageGRID 11.8 Use S3 Console"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/use-s3-console.adoc"
source_sha256: "3ad7e1aac39785e7c690faf923d1717e453edadf8a26ea20a683c3e8efab72df"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/use-s3-console.adoc"
---

# StorageGRID 11.8 Use S3 Console

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/use-s3-console.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Use S3 Console
:icons: font
:imagesdir: ../media/

[.lead]
You can use S3 Console to view and manage the objects in an S3 bucket.

S3 Console allows you to:

* Upload, download, rename, copy, move, and delete objects
* View, revert, download, and delete object versions
* Search for objects by prefix
* Manage object tags
* View object metadata
* View, create, rename, copy, move, and delete folders

[NOTE]
#### S3 Console provides an improved user experience for the most common cases. It is not designed to replace CLI or API operations in all situations.
 
If using S3 Console results in operations taking too long (for example, minutes or hours), consider:

* Reducing the number of selected objects
* Using non-graphical (API or CLI) methods to access your data
#### .Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* If you want to manage objects, you belong to a user group that has the Root access permission. Alternatively, you belong to a user group that has the Use S3 Console tab permission and either the View all buckets permission or Manage all buckets permission. See link:tenant-management-permissions.html[Tenant management permissions].
* An S3 Group or Bucket policy has been configured for the user. See link:../s3/bucket-and-group-access-policies.html[Use bucket and group access policies].
* You know the user's access key ID and secret access key. Optionally, you have a `.csv` file containing this information. See the link:creating-your-own-s3-access-keys.html[instructions for creating access keys].

.Steps

. Select *STORAGE* > *Buckets* > *_bucket name_*.
. Select the S3 Console tab.
. Paste the access key ID and secret access key into the fields. Otherwise, select *Upload access keys* and select your `.csv` file.
. Select *Sign in*.
. The table of bucket objects appears. You can manage objects as needed. 

.Additional information

* *Search by prefix*: The prefix search feature only searches for objects that begin with a specific word relative to the current folder. The search does not include objects that contain the word elsewhere. This rule also applies to objects within folders. For example, a search for `folder1/folder2/somefile-` would return objects that are within the `folder1/folder2/` folder and begin with the word `somefile-`.

* *Drag and drop*: You can drag and drop files from your computer's file manager to S3 Console. However, you cannot upload folders.

* *Operations on folders*: When you move, copy, or rename a folder, all objects in the folder are updated one at a time, which might take time.

* *Permanent deletion when bucket versioning is disabled*: When you overwrite or delete an object in a bucket with versioning disabled, the operation is permanent. See link:changing-bucket-versioning.html[Change object versioning for a bucket].

// 2023 AUG 23, SGWS-27720 and SGWS-27719

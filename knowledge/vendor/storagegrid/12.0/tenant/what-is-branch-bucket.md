---
id: "storagegrid-120-228c83e5189486bc"
title: "StorageGRID 12.0 Learn about StorageGRID branch buckets"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/what-is-branch-bucket.adoc"
source_sha256: "c3553a498e9f3023971f1836014b4f35a3425c3353152624049b967e9802c1c4"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/what-is-branch-bucket.adoc"
---

# StorageGRID 12.0 Learn about StorageGRID branch buckets

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/what-is-branch-bucket.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Learn about StorageGRID branch buckets
:icons: font
:imagesdir: ../media/

[.lead]
A branch bucket provides access to objects in a bucket as they existed at a certain time.

You create a branch bucket from an existing bucket. After you create a branch bucket, the original bucket it was created from is called the _base bucket_. Additionally, you can create a branch bucket from another branch bucket.

A branch bucket provides access to protected data, but doesn't serve as a backup. To continue to protect data, use these features on base buckets:

* link:../tenant/using-s3-object-lock.html[S3 Object Lock]
* link:../admin/grid-federation-what-is-cross-grid-replication.html[Cross-grid replication] for base buckets
* link:../tenant/manage-bucket-policy.html[Bucket policies] for versioned buckets to clean up old object versions

Note the following characteristics of branch buckets:

* You can access the objects in branch buckets by using link:../tenant/use-s3-console.html[S3 Console to download objects].
* When clients access objects in a branch bucket, the branch bucket's link:../s3/use-access-policies.html[access policies], rather than the policies of the base bucket, determine whether access is granted or denied.
* Objects created in a base bucket are evaluated based on how link:../ilm/access-create-ilm-rule-wizard.html[ILM rules] apply to the base bucket. Objects created in a branch bucket are evaluated based on how ILM rules apply to the branch bucket.
* Cross-grid replication isn't supported for branch buckets.
* Platform services aren't supported for branch buckets.

## Examples for branch bucket usage

* You can use a branch bucket to remove corrupt objects by creating a branch bucket from a point in time before the corruption occurred, and then pointing applications to the branch bucket instead of to the base bucket that contains corrupt objects.

* You're saving data in a versioned bucket. There was an accidental vulnerability that caused many unwanted objects to be ingested after time _T_. You can create a branch bucket for the Before time value, _T_, and redirect client operations to that branch bucket. Then, only objects ingested earlier than the Before time _T_ are exposed to clients.

## Operations on objects in branch buckets 

* A PUT object operation on a branch bucket creates an object in the branch.

* A GET object operation on a branch bucket retrieves an object from the branch. If the object doesn't exist in the branch bucket, the object is retrieved from the base bucket.

* Object deletions from branch buckets occur as follows: 
+
[cols="1a,1a,2a,2a,2a" options="header"]
|===
| Operation|	Target|	Result|	Object visibility in base bucket|	Object visibility in branch bucket

| Delete without version ID
|	Base bucket
|	Delete marker is created only for the base bucket
|	HEAD/GET returns Object doesn't exist, but specific versions can still be accessed
|	HEAD/GET returns Object exists, and specific versions can still be accessed

The delete marker would have been created after the branch bucket's `beforeTime`.

| Delete with version ID
|	Base bucket
|	Specific object version is deleted for both base and branch bucket
|	HEAD/GET returns Object version doesn't exist
|	HEAD/GET returns Object version doesn't exist

| Delete without version ID
|	Branch bucket
|	Delete marker is created only for the branch bucket
|	HEAD/GET returns object (base bucket object not affected)
|	HEAD/GET returns Object doesn't exist

| Delete with version ID
|	Branch bucket
|	Specific object version is deleted only for branch bucket
|	HEAD/GET returns specific object version (base bucket object not affected)
|	HEAD/GET returns Object version doesn't exist
|===

Also refer to link:../ilm/how-objects-are-deleted.html#delete-s3-versioned-objects[How S3 versioned objects are deleted].

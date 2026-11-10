---
id: "storagegrid-118-e32b78c6e51ba8fd"
title: "StorageGRID 11.8 Use Last access time in ILM rules"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/using-last-access-time-in-ilm-rules.adoc"
source_sha256: "ad8bd61a8cf6af0e4b0c6489dd6667bdf539770253648d305eb7a2cb40885ed0"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/using-last-access-time-in-ilm-rules.adoc"
---

# StorageGRID 11.8 Use Last access time in ILM rules

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/using-last-access-time-in-ilm-rules.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Use Last access time in ILM rules
:icons: font
:imagesdir: ../media/

[.lead]
You can use Last access time as the reference time in an ILM rule. For example, you might want to leave objects that have been viewed in the last three months on local Storage Nodes, while moving objects that have not been viewed as recently to an off-site location. You can also use Last access time as an advanced filter if you want an ILM rule to apply only to objects that were last accessed on a specific date.

.About this task

Before using Last access time in an ILM rule, review the following considerations:

* When using Last access time as a reference time, be aware that changing the Last access time for an object does not trigger an immediate ILM evaluation. Instead, the object's placements are assessed and the object is moved as required when background ILM evaluates the object. This could take two weeks or more after the object is accessed.
+
Take this latency into account when creating ILM rules based on Last access time and avoid placements that use short time periods (less than one month).

* When using Last access time as an advanced filter or as a reference time, you must enable last access time updates for S3 buckets. You can use the link:../tenant/enabling-or-disabling-last-access-time-updates.html[Tenant Manager] or the link:../s3/put-bucket-last-access-time-request.html[Tenant Management API].
+
NOTE: Last access time updates are always enabled for Swift containers, but are disabled by default for S3 buckets.
+
NOTE: Be aware that enabling last access time updates can reduce performance, especially in systems with small objects. The performance impact occurs because StorageGRID must update the objects with new timestamps every time the objects are retrieved.

The following table summarizes whether the Last access time is updated for all objects in the bucket for different types of requests.
[cols="1a,1a,1a" options="header"]
|===
| Type of request| Whether Last access time is updated when last access time updates are disabled| Whether Last access time is updated when last access time updates are enabled

|Request to retrieve an object, its access control list, or its metadata
|No
|Yes

|Request to update an object's metadata
|Yes
|Yes

|Request to copy an object from one bucket to another
|
* No, for the source copy
* Yes, for the destination copy
|
* Yes, for the source copy
* Yes, for the destination copy

|Request to complete a multipart upload
|Yes, for the assembled object
|Yes, for the assembled object
|===

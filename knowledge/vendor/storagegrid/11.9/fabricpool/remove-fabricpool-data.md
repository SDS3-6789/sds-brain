---
id: "storagegrid-119-9f2b96b78d42159a"
title: "StorageGRID 11.9 Remove FabricPool data from StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/fabricpool/remove-fabricpool-data.adoc"
source_sha256: "e835cab25807609e622c4ddccecbccbe803481a31bbcd64fef889603da17a762"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "fabricpool/remove-fabricpool-data.adoc"
---

# StorageGRID 11.9 Remove FabricPool data from StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/fabricpool/remove-fabricpool-data.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Remove FabricPool data from StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
If you need to remove the FabricPool data that is currently stored in StorageGRID, you must use ONTAP to retrieve all data for the FabricPool volume and promote it to the performance tier.

.Before you begin

* You have reviewed the instructions and considerations in https://docs.netapp.com/us-en/ontap/fabricpool/promote-data-performance-tier-task.html[Promote data to the performance tier^].

* You are using ONTAP 9.8 or later.

* You are using a link:../admin/web-browser-requirements.html[supported web browser].

* You belong to a StorageGRID user group for the FabricPool tenant account that has the link:../tenant/tenant-management-permissions.html[Manage all buckets or Root access permission]. 

.About this task

These instructions explain how to move data from StorageGRID back to FabricPool. You perform this procedure using ONTAP and StorageGRID Tenant Manager.


.Steps

. From ONTAP, issue the `volume modify` command.
+
Set `tiering-policy` to `none` to stop new tiering and set `cloud-retrieval-policy` to `promote` to return all data that was previously tiered to StorageGRID.
+
See https://docs.netapp.com/us-en/ontap/fabricpool/promote-all-data-performance-tier-task.html[Promote all data from a FabricPool volume to the performance tier^].

. Wait for the operation to complete.
+
You can use the `volume object-store` command with the `tiering` option to https://docs.netapp.com/us-en/ontap/fabricpool/check-status-performance-tier-promotion-task.html[check the status of the performance tier promotion^]. 

. When the promote operation is complete, sign in to StorageGRID Tenant Manager for the FabricPool tenant account. 

. Select *View buckets* from the dashboard, or select  *STORAGE (S3)* > *Buckets*.

. Confirm that the FabricPool bucket is now empty. 

. If the bucket is empty, link:../tenant/deleting-s3-bucket.html[delete the bucket].

.After you finish
When you delete the bucket, tiering from FabricPool to StorageGRID can no longer continue. However, because the local tier is still attached to the StorageGRID cloud tier, ONTAP System Manager will return error messages indicating that the bucket is inaccessible.

To prevent these error messages, do either of the following:

* Use FabricPool Mirror to attach a different cloud tier to the aggregate.

* Move the data from the FabricPool aggregate to a non-FabricPool aggregate and then delete the unused aggregate. 

See the https://docs.netapp.com/us-en/ontap/fabricpool/index.html[ONTAP documentation for FabricPool^] for instructions.

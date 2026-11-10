---
id: "storagegrid-120-047f253fcf5df7f1"
title: "StorageGRID 12.0 Edit a Cloud Storage Pool in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/editing-cloud-storage-pool.adoc"
source_sha256: "c1cdbdf7efd00f646c809134af5d717fff39669bce1975625f6058994a665ad2"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/editing-cloud-storage-pool.adoc"
---

# StorageGRID 12.0 Edit a Cloud Storage Pool in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/editing-cloud-storage-pool.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Edit a Cloud Storage Pool in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
You can edit a Cloud Storage Pool to change its name, service endpoint, or other details; however, you can't change the S3 bucket or Azure container for a Cloud Storage Pool.

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:../admin/admin-group-permissions.html[specific access permissions].
* You have reviewed the link:considerations-for-cloud-storage-pools.html[considerations for Cloud Storage Pools].

.Steps
. Select *ILM* > *Storage pools* > *Cloud Storage Pools*.
+
The Cloud Storage Pools table lists the existing Cloud Storage Pools.

. Select the checkbox for the Cloud Storage Pool you want to edit, then select *Actions* > *Edit*.
+
Alternatively, select the name of the Cloud Storage Pool, then select *Edit*.

. As required, change the Cloud Storage Pool name, service endpoint, authentication credentials, or certificate verification method.
+
NOTE: You can't change the provider type or the S3 bucket or Azure container for a Cloud Storage Pool.
+
If you previously uploaded a server or client certificate, you can expand the *Certificate details* accordion to review the certificate that is currently in use.

. Select *Save*.
+
When you save a Cloud Storage Pool, StorageGRID validates that the bucket or container and the service endpoint exist, and that they can be reached using the credentials that you specified.
+
If Cloud Storage Pool validation fails, an error message is displayed. For example, an error might be reported if there is a certificate error.
+
See the instructions for link:troubleshooting-cloud-storage-pools.html[troubleshooting Cloud Storage Pools], resolve the issue, and then try saving the Cloud Storage Pool again.

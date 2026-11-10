---
id: "storagegrid-120-d2925c5eb143816c"
title: "StorageGRID 12.0 Delete a StorageGRID platform services endpoint"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/deleting-platform-services-endpoint.adoc"
source_sha256: "988ea83312a64e375cb134ed7032a0f7275bc296eba2695a5032edf3cd54f890"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/deleting-platform-services-endpoint.adoc"
---

# StorageGRID 12.0 Delete a StorageGRID platform services endpoint

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/deleting-platform-services-endpoint.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Delete a StorageGRID platform services endpoint
:icons: font
:imagesdir: ../media/

[.lead]
You can delete an endpoint if you no longer want to use the associated platform service.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the link:tenant-management-permissions.html[Manage endpoints or Root access permission].

.Steps

. Select *STORAGE (S3)* > *Platform services endpoints*.
+
The Platform services endpoints page appears and shows the list of platform services endpoints that have already been configured.

. Select the checkbox for each endpoint you want to delete.
+
NOTE: If you delete a platform services endpoint that is in use, the associated platform service will be disabled for any buckets that use the endpoint. Any requests that have not yet been completed will be dropped. Any new requests will continue to be generated until you change your bucket configuration to no longer reference the deleted URN. StorageGRID will report these requests as unrecoverable errors.

. Select *Actions* > *Delete endpoint*.
+
A confirmation message appears.

. Select *Delete endpoint*.

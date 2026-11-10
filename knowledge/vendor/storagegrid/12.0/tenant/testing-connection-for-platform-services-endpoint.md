---
id: "storagegrid-120-ff347a852c1cbfd6"
title: "StorageGRID 12.0 Test the connection for a StorageGRID platform services endpoint"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/testing-connection-for-platform-services-endpoint.adoc"
source_sha256: "72ffec0e16db9792389ef28db84281a6580cc92fdb7546090abaa45af84bac82"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/testing-connection-for-platform-services-endpoint.adoc"
---

# StorageGRID 12.0 Test the connection for a StorageGRID platform services endpoint

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/testing-connection-for-platform-services-endpoint.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Test the connection for a StorageGRID platform services endpoint
:icons: font
:imagesdir: ../media/

[.lead]
If the connection to a platform service has changed, you can test the connection for the endpoint to validate that the destination resource exists and that it can be reached using the credentials you specified.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the link:tenant-management-permissions.html[Manage endpoints or Root access permission].

.About this task

StorageGRID does not validate that the credentials have the correct permissions.

.Steps

. Select *STORAGE (S3)* > *Platform services endpoints*.
+
The Platform services endpoints page appears and shows the list of platform services endpoints that have already been configured.

. Select the endpoint whose connection you want to test.
+
The endpoint details page appears.

. Select *Test connection*.
 ** A success message appears if the endpoint can be reached using the specified credentials. The connection to the endpoint is validated from one node at each site.
 ** An error message appears if endpoint validation fails. If you need to modify the endpoint to correct the error, select *Configuration* and update the information. Then, select *Test and save changes*.

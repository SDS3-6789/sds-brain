---
id: "storagegrid-118-2f47b939fdaed717"
title: "StorageGRID 11.8 Edit platform services endpoint"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/editing-platform-services-endpoint.adoc"
source_sha256: "6b5ebc162817c1774d0ea021315aa42c944e5815572c11773e28c15192b59192"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/editing-platform-services-endpoint.adoc"
---

# StorageGRID 11.8 Edit platform services endpoint

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/editing-platform-services-endpoint.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Edit platform services endpoint
:icons: font
:imagesdir: ../media/

[.lead]
You can edit the configuration for a platform services endpoint to change its name, URI, or other details. For example, you might need to update expired credentials or change the URI to point to a backup Elasticsearch index for failover. You can't change the URN for a platform services endpoint.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the link:tenant-management-permissions.html[Manage endpoints or Root access permission].

.Steps

. Select *STORAGE (S3)* > *Platform services endpoints*.
+
The Platform services endpoints page appears and shows the list of platform services endpoints that have already been configured.
+
image::../media/endpoints_list.png[Endpoints List]

. Select the endpoint you want to edit.
+
The endpoint details page appears.

. Select *Configuration*.

. As needed, change the configuration of the endpoint.
+
NOTE: You can't change an endpoint's URN after the endpoint has been created.

 .. To change the display name for the endpoint, select the edit icon image:../media/icon_edit_tm.png[Edit Icon].
 .. As needed, change the URI.
 .. As needed, change the authentication type.
  *** For Access Key authentication, change the key as necessary by selecting *Edit S3 key* and pasting a new access key ID and secret access key. If you need to cancel your changes, select *Revert S3 key edit*.
  *** For CAP (C2S Access Portal) authentication, change the temporary credentials URL or optional client private key passphrase and upload new certificate and key files as needed.
+
NOTE: The Client private key must be in OpenSSL encrypted format or unencrypted private key format.

 .. As needed, change the method for verifying the server.

. Select *Test and save changes*.
 ** A success message appears if the endpoint can be reached using the specified credentials. The connection to the endpoint is verified from one node at each site.
 ** An error message appears if endpoint validation fails. Modify the endpoint to correct the error, and then select *Test and save changes*.

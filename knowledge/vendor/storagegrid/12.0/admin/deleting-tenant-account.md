---
id: "storagegrid-120-bf9f219ead1ba0b1"
title: "StorageGRID 12.0 Delete a StorageGRID tenant account"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/deleting-tenant-account.adoc"
source_sha256: "29c1076d4dfa4f148ab5ee88411a8f44e680f36d7e4ee6991350c41bb77f90cc"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/deleting-tenant-account.adoc"
---

# StorageGRID 12.0 Delete a StorageGRID tenant account

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/deleting-tenant-account.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Delete a StorageGRID tenant account
:icons: font
:imagesdir: ../media/

[.lead]
You can delete a tenant account if you want to permanently remove the tenant's access to the system.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:admin-group-permissions.html[specific access permissions].
* You have removed all S3 buckets and objects associated with the tenant account.
* If the tenant is permitted to use a grid federation connection, you have reviewed the considerations for link:grid-federation-manage-tenants.html[deleting a tenant with the Use grid federation connection permission].

.Steps

. Select *Tenants*.

. Locate the tenant account or accounts you want to delete.
+
Use the search box to search for a tenant by name or tenant ID.

. To delete multiple tenants, select the checkboxes and select *Actions* > *Delete*.

. To delete a single tenant, do either of the following:

**  Select the checkbox, and select *Actions* > *Delete*.

** Select the tenant name to display the details page, and then select *Actions* > *Delete*.

. Select *Yes*.

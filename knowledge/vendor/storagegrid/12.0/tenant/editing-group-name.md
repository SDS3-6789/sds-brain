---
id: "storagegrid-120-e12fbefe55e9d7ee"
title: "StorageGRID 12.0 Edit a tenant group name in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/editing-group-name.adoc"
source_sha256: "6cce4bb48c6b5d186aec8e6b5fb1311ef3942df86ab5ddfbeac68edda8e00cb3"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/editing-group-name.adoc"
---

# StorageGRID 12.0 Edit a tenant group name in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/editing-group-name.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Edit a tenant group name in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
You can edit the display name for a group. You can't edit the unique name for a group.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the Root access permission. See link:tenant-management-permissions.html[Tenant management permissions].

.Steps
. Select *Access Management* > *Groups*.
. Select the checkbox for the group whose display name you want to edit.
. Select *Actions* > *Edit group name*.
+
The Edit group name dialog box appears.
+
image:edit_group_name.png[Edit group name]

. If you are editing a local group, update the display name as needed.
+
You can't change a group's unique name. You can't edit the display name for a federated group.

. Select *Save changes*.
+
A confirmation message appears in the upper right corner of the page.

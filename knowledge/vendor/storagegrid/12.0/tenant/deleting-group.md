---
id: "storagegrid-120-d3d3b2c62ad5bf8b"
title: "StorageGRID 12.0 Delete a StorageGRID tenant group"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/deleting-group.adoc"
source_sha256: "dd5acfd89ad59d9ca45a19343e7d9012e22e74a03c3eecaed32290313bd908d2"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/deleting-group.adoc"
---

# StorageGRID 12.0 Delete a StorageGRID tenant group

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/deleting-group.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Delete a StorageGRID tenant group
:icons: font
:imagesdir: ../media/

[.lead]
You can delete a group from the system. Any users who belong only to that group will no longer be able to sign in to the Tenant Manager or use the tenant account.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the Root access permission. See link:tenant-management-permissions.html[Tenant management permissions].

.Steps
. Select *Access Management* > *Groups*.

. Select the checkbox for each group you want to delete.
. Select *Actions* > *Delete group*.

. Select *Delete group*.

---
id: "storagegrid-120-17bcc2a9be5e7389"
title: "StorageGRID 12.0 Manage external SSH access in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/manage-external-ssh-access.adoc"
source_sha256: "9f78273410b31b9941f34ab6057a6a09fe74b980c3c2457d3228a5d8f569fb4c"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/manage-external-ssh-access.adoc"
---

# StorageGRID 12.0 Manage external SSH access in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/manage-external-ssh-access.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Manage external SSH access in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
Manage SSH access for inbound traffic into the grid by blocking or allowing external access. Managing SSH external access doesn't have an impact on traffic between nodes in the grid. 

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:admin-group-permissions.html[Root access permission].

.About this task 

To enhance system security, external SSH access is blocked by default. If you need to perform tasks that require inbound SSH access, such as troubleshooting, temporarily allow external access. When you've finished the task, block external access.

.Steps
. Select *Configuration* > *Security* > *Security settings*.
. Select the *Block SSH* tab.
. Use the *Block inbound SSH access* option to manage external SSH access:
.. Select the checkbox to block access (default).
.. Unselect the checkbox to allow access.
+
NOTE: Requires access on port 22 between the service laptop and all other grid nodes. Remove access on port 22 when you complete the maintenance task.

. Select *Save*.

// 2025 NOV 4, SGRIDDOC-199 and 202
// 2025 APR 22, SGWS-35048

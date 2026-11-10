---
id: "storagegrid-120-23b2778f8c3a84e7"
title: "StorageGRID 12.0 Check storage state after recovering a StorageGRID Storage Node system drive"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/checking-storage-state-after-recovering-storage-node-system-drive.adoc"
source_sha256: "6d0cf160bb0b535caae7e49a8494cf3630ff14401be2076b2df2b1ab5b7fa2f8"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/checking-storage-state-after-recovering-storage-node-system-drive.adoc"
---

# StorageGRID 12.0 Check storage state after recovering a StorageGRID Storage Node system drive

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/checking-storage-state-after-recovering-storage-node-system-drive.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Check storage state after recovering a StorageGRID Storage Node system drive
:icons: font
:imagesdir: ../media/

[.lead]
After recovering the system drive for a Storage Node, you must verify that the desired state of the Storage Node is set to online and ensure that the state will be online by default whenever the Storage Node server is restarted.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* The Storage Node has been recovered, and data recovery is complete.

.Steps
. Select *Nodes* > *_Storage Node_* > *Tasks*.
. If the *Storage state* drop-down list is set to Read-only or Offline, select *Online*.
. Select *Save*.

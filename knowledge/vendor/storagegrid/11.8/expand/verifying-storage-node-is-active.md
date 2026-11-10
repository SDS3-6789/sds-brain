---
id: "storagegrid-118-a95a8e9e81c923aa"
title: "StorageGRID 11.8 Verify that Storage Node is active"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/verifying-storage-node-is-active.adoc"
source_sha256: "ca9eeaa23d8445f7d5b7d865fcdc1c0727a8a22606e726c73375346daefab88a"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "expand/verifying-storage-node-is-active.adoc"
---

# StorageGRID 11.8 Verify that Storage Node is active

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/verifying-storage-node-is-active.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Verify that Storage Node is active
:icons: font
:imagesdir: ../media/

[.lead]
After an expansion operation that adds new Storage Nodes completes, the StorageGRID system should automatically start using the new Storage Nodes. You must use the StorageGRID system to verify that the new Storage Node is active.

.Steps
. Sign in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
. Select *NODES* > *_Expansion Storage Node_* > *Storage*.
. Position your cursor over the *Storage Used - Object Data* graph to view the value for *Used*, which is the amount of the Total usable space that has been used for object data.
. Verify that the value of *Used* is increasing as you move your cursor to the right on the graph.

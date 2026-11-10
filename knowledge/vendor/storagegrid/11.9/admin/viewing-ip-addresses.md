---
id: "storagegrid-119-082994f22ea2d323"
title: "StorageGRID 11.9 View IP addresses"
area: "storagegrid"
type: "import"
applies_to: ["11.9", "storagegrid-11.9"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg119-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-119"
repository_commit: "aa58c9affae3bb1994d6bd2e525851e3fd088517"
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/viewing-ip-addresses.adoc"
source_sha256: "8973f593a1093d7b76c1a26375ccfa287c0af4d0f50ea70042ed0d639d9ac445"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/viewing-ip-addresses.adoc"
---

# StorageGRID 11.9 View IP addresses

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/viewing-ip-addresses.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View IP addresses
:icons: font
:imagesdir: ../media/

[.lead]
You can view the IP address for each grid node in your StorageGRID system. You can then use this IP address to log in to the grid node at the command line and perform various maintenance procedures.

.Before you begin
You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.About this task

For information about changing IP addresses, see link:../maintain/configuring-ip-addresses.html[Configure IP addresses].

.Steps

. Select *NODES* > *_grid node_* > *Overview*.
. Select *Show more* to the right of the IP Addresses title.
+
The IP addresses for that grid node are listed in a table.
+
image::../media/nodes_page_overview_tab_extended.png[Nodes Page IP Addresses]

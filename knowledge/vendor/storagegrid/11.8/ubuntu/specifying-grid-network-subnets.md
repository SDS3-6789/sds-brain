---
id: "storagegrid-118-f05c8660d2197e6e"
title: "StorageGRID 11.8 Specify Grid Network subnets"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ubuntu/specifying-grid-network-subnets.adoc"
source_sha256: "af91143e906d957423571068b72ab3945fae90fc2ce3a44fa0c68daae733ce6b"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ubuntu/specifying-grid-network-subnets.adoc"
---

# StorageGRID 11.8 Specify Grid Network subnets

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ubuntu/specifying-grid-network-subnets.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Specify Grid Network subnets
:icons: font
:imagesdir: ../media/

[.lead]
You must specify the subnets that are used on the Grid Network.

.About this task

The subnet entries include the subnets for the Grid Network for each site in your StorageGRID system, along with any subnets that need to be reachable through the Grid Network.

If you have multiple grid subnets, the Grid Network gateway is required. All grid subnets specified must be reachable through this gateway.

.Steps

. Specify the CIDR network address for at least one Grid Network in the *Subnet 1* text box.
. Click the plus sign next to the last entry to add an additional network entry.
+
If you have already deployed at least one node, click *Discover Grid Networks Subnets* to automatically populate the Grid Network Subnet List with the subnets reported by grid nodes that have registered with the Grid Manager.
+
image::../media/4_gmi_installer_grid_network_page.gif[Specify subnets]

. Click *Next*.

---
id: "storagegrid-120-fba38dfd9c08430d"
title: "StorageGRID 12.0 Specify Grid Network subnets for StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/specifying-grid-network-subnets.adoc"
source_sha256: "ede2df1a816ca028550318a658a4e712f057551c5dd4ccd659161ecabca793db"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "swnodes/specifying-grid-network-subnets.adoc"
---

# StorageGRID 12.0 Specify Grid Network subnets for StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/specifying-grid-network-subnets.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Specify Grid Network subnets for StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
You must specify the subnets that are used on the Grid Network. 

.About this task

The subnet entries include the subnets for the Grid Network for each site in your StorageGRID system, along with any subnets that need to be reachable through the Grid Network.

If you have multiple grid subnets, the Grid Network gateway is required. All grid subnets specified must be reachable through this gateway.

.Steps

. Specify the CIDR network address for at least one Grid Network in the *Subnet 1* text box.
. Click the plus sign next to the last entry to add an additional network entry. You must specify all subnets for all sites in the Grid Network.
+
* If you have already deployed at least one node, click *Discover Grid Networks Subnets* to automatically populate the Grid Network Subnet List with the subnets reported by grid nodes that have registered with the Grid Manager.
* You must manually add any subnets for NTP, DNS, LDAP, or other external servers accessed through the Grid Network gateway.
+
image:4_gmi_installer_grid_network_page.gif[Specify subnets]

. Click *Next*.

---
id: "storagegrid-118-fc5d6770e9acee77"
title: "StorageGRID 11.8 Required information and materials"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/required-materials.adoc"
source_sha256: "bbdb3d5137618ef1076ec5d0401b7d833c7a544fd9c4fd79ac95b1e593141562"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "vmware/required-materials.adoc"
---

# StorageGRID 11.8 Required information and materials

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/required-materials.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Required information and materials
:icons: font
:imagesdir: ../media/

[.lead]
Before you install StorageGRID, gather and prepare the required information and materials.

## Required information

Network plan:: Which networks you intend to attach to each StorageGRID node. StorageGRID supports multiple networks for traffic separation, security, and administrative convenience.
+
See the StorageGRID link:../network/index.html[Networking guidelines].

Network information:: Unless you are using DHCP, IP addresses to assign to each grid node and the IP addresses of the DNS and NTP servers.

Servers for grid nodes:: Identify a set of servers (physical, virtual, or both) that, in aggregate, provide sufficient resources to support the number and type of StorageGRID nodes you plan to deploy.
+
NOTE: If your StorageGRID installation will not use StorageGRID appliance (hardware) Storage Nodes, you must use hardware RAID storage with battery-backed write cache (BBWC). StorageGRID does not support the use of virtual storage area networks (vSANs), software RAID, or no RAID protection.

Related information:: https://imt.netapp.com/matrix/#welcome[NetApp Interoperability Matrix Tool^]

## Required materials

NetApp StorageGRID license:: You must have a valid, digitally signed NetApp license.

NOTE: A non-production license, which can be used for testing and proof of concept grids, is included in the StorageGRID installation archive.

StorageGRID installation archive:: link:downloading-and-extracting-storagegrid-installation-files.html[Download the StorageGRID installation archive and extract the files].

Service laptop:: The StorageGRID system is installed through a service laptop.
+
The service laptop must have:

* Network port
* SSH client (for example, PuTTY)
* link:../admin/web-browser-requirements.html[Supported web browser]

StorageGRID documentation:: 
* link:../release-notes/index.html[Release notes]
* link:../admin/index.html[Instructions for administering StorageGRID]

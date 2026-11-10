---
id: "storagegrid-118-a0b02282fb081056"
title: "StorageGRID 11.8 Specify Network Time Protocol server information"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/specifying-network-time-protocol-server-information.adoc"
source_sha256: "0f5da70d7bb1f0e155f2f4ad472823c1e7b5f1613a547afddc8852663d1e9ff9"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "vmware/specifying-network-time-protocol-server-information.adoc"
---

# StorageGRID 11.8 Specify Network Time Protocol server information

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/specifying-network-time-protocol-server-information.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Specify Network Time Protocol server information
:icons: font
:imagesdir: ../media/

[.lead]
You must specify the Network Time Protocol (NTP) configuration information for the StorageGRID system, so that operations performed on separate servers can be kept synchronized.

.About this task

You must specify IPv4 addresses for the NTP servers.

You must specify external NTP servers. The specified NTP servers must use the NTP protocol.

You must specify four NTP server references of Stratum 3 or better to prevent issues with time drift.

NOTE: When specifying the external NTP source for a production-level StorageGRID installation, don't use the Windows Time (W32Time) service on a version of Windows earlier than Windows Server 2016. The time service on earlier versions of Windows is not sufficiently accurate and is not supported by Microsoft for use in high-accuracy environments, such as StorageGRID.

https://support.microsoft.com/en-us/help/939322/support-boundary-to-configure-the-windows-time-service-for-high-accura[Support boundary to configure the Windows Time service for high-accuracy environments^]

The external NTP servers are used by the nodes to which you previously assigned Primary NTP roles.

CAUTION: Make sure that at least two nodes at each site can access at least four external NTP sources. If only one node at a site can reach the NTP sources, timing issues will occur if that node goes down. In addition, designating two nodes per site as primary NTP sources ensures accurate timing if a site is isolated from the rest of the grid.

Perform additional checks for VMware, such as ensuring that the hypervisor uses the same NTP source as the virtual machine, and using VMTools to disable the time sync between the hypervisor and StorageGRID virtual machines.

.Steps

. Specify the IPv4 addresses for at least four NTP servers in the *Server 1* to *Server 4* text boxes.
. If necessary, select the plus sign next to the last entry to add additional server entries.
+
image::../media/8_gmi_installer_ntp_page.gif[This image is explained by the surrounding text.]

. Select *Next*.

---
id: "storagegrid-120-17cbcfe6cff5673e"
title: "StorageGRID 12.0 Subnet requirements for StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/network/subnet-requirements.adoc"
source_sha256: "a36f6c23a071d50ab428f60b9419764eebd11da4bbca16b8aad7927225d96d3e"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "network/subnet-requirements.adoc"
---

# StorageGRID 12.0 Subnet requirements for StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/network/subnet-requirements.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Subnet requirements for StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
Follow these requirements and guidelines for network subnets.

NOTE: Each network must be connected to its own subnet that does not overlap with any other network on the node.

The following restrictions are enforced by the Grid Manager during deployment. They are provided here to assist in pre-deployment network planning.

* The subnet mask for any network IP address can't be 255.255.255.254 or 255.255.255.255 (/31 or /32 in CIDR notation).
* The subnet defined by a network interface IP address and subnet mask (CIDR) can't overlap the subnet of any other interface configured on the same node.
* Do not use subnets that contain the following IPv4 addresses for the Grid Network, Admin Network, or Client Network of any node:

** 192.168.130.101
** 192.168.130.121
** 192.168.131.101
** 192.168.131.121
** 192.168.130.102
** 192.168.130.122
** 192.168.131.102
** 192.168.131.122
** 198.51.100.2
** 198.51.100.4

+
For example, do not use the following subnet ranges for the Grid Network, Admin Network, or Client Network of any node:

** 192.168.130.0/24 because this subnet range contains the IP addresses 192.168.130.101 and 192.168.130.102 
** 192.168.131.0/24 because this subnet range contains the IP addresses 192.168.131.101 and 192.168.131.102
** 198.51.100.0/24 because this subnet range contains the IP addresses 198.51.100.2 and 198.51.100.4

* The Grid Network subnet for each node must be included in the GNSL.
* The Admin Network subnet can't overlap the Grid Network subnet, the Client Network subnet, or any subnet in the GNSL.
* The subnets in the AESL can't overlap with any subnets in the GNSL.
* The Client Network subnet can't overlap the Grid Network subnet, the Admin Network subnet, any subnet in the GNSL, or any subnet in the AESL.

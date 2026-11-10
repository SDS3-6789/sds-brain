---
id: "storagegrid-120-43630ab68d9f88ec"
title: "StorageGRID 12.0 How grid nodes discover the primary Admin Node in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/how-grid-nodes-discover-primary-admin-node.adoc"
source_sha256: "e25f27c1902a320dbd7b81838245f8f9d9fac743a7582e977784c7e2fc4cdc8c"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "swnodes/how-grid-nodes-discover-primary-admin-node.adoc"
---

# StorageGRID 12.0 How grid nodes discover the primary Admin Node in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/how-grid-nodes-discover-primary-admin-node.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# How grid nodes discover the primary Admin Node in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
Grid nodes communicate with the primary Admin Node for configuration and management. Each grid node must know the IP address of the primary Admin Node on the Grid Network.

To ensure that a grid node can access the primary Admin Node, you can do either of the following when deploying the node:

* You can use the ADMIN_IP parameter to enter the primary Admin Node's IP address manually.
* You can omit the ADMIN_IP parameter to have the grid node discover the value automatically. Automatic discovery is especially useful when the Grid Network uses DHCP to assign the IP address to the primary Admin Node.

Automatic discovery of the primary Admin Node is accomplished using a multicast domain name system (mDNS). When the primary Admin Node first starts up, it publishes its IP address using mDNS. Other nodes on the same subnet can then query for the IP address and acquire it automatically. However, because multicast IP traffic is not normally routable across subnets, nodes on other subnets can't acquire the primary Admin Node's IP address directly.

[NOTE]
#### If you use automatic discovery:

* You must include the ADMIN_IP setting for at least one grid node on any subnets that the primary Admin Node is not directly attached to. This grid node will then publish the primary Admin Node's IP address for other nodes on the subnet to discover with mDNS.
* Ensure that your network infrastructure supports passing multi-cast IP traffic within a subnet.
####

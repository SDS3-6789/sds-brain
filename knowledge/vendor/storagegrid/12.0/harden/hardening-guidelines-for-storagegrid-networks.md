---
id: "storagegrid-120-5b7cf9dfed2a80c0"
title: "StorageGRID 12.0 Hardening guidelines for StorageGRID networks"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/harden/hardening-guidelines-for-storagegrid-networks.adoc"
source_sha256: "08ad8fff621dbec27280429a98b56d4fb722b0e1e1f84e291b5559eb71a5f041"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "harden/hardening-guidelines-for-storagegrid-networks.adoc"
---

# StorageGRID 12.0 Hardening guidelines for StorageGRID networks

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/harden/hardening-guidelines-for-storagegrid-networks.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Hardening guidelines for StorageGRID networks
:icons: font
:imagesdir: ../media/

[.lead]
The StorageGRID system supports up to three network interfaces per grid node, allowing you to configure the networking for each individual grid node to match your security and access requirements.

For detailed information about StorageGRID networks, see the link:../network/storagegrid-network-types.html[StorageGRID network types].

## Guidelines for Grid Network

You must configure a Grid Network for all internal StorageGRID traffic. All grid nodes are on the Grid Network, and they must be able to talk to all other nodes.

When configuring the Grid Network, follow these guidelines:

* Ensure that the network is secured from untrusted clients, such as those on the open internet.
* When possible, use the Grid Network exclusively for internal traffic. Both the Admin Network and the Client Network have additional firewall restrictions that block external traffic to internal services. Using the Grid Network for external client traffic is supported, but this use offers fewer layers of protection.
* If the StorageGRID deployment spans multiple data centers, use a virtual private network (VPN) or equivalent on the Grid Network to provide additional protection for internal traffic.
* Some maintenance procedures require secure shell (SSH) access on port 22 between the primary Admin Node and all other grid nodes. Use an external firewall to restrict SSH access to trusted clients.

## Guidelines for Admin Network

The Admin Network is typically used for administrative tasks (trusted employees using the Grid Manager or SSH) and for communicating with other trusted services such as LDAP, DNS, NTP, or KMS (or KMIP server). However, StorageGRID does not enforce this usage internally.

If you are using the Admin Network, follow these guidelines:

* Block all internal traffic ports on the Admin Network. See the link:../network/internal-grid-node-communications.html[list of internal ports].
* If untrusted clients can access the Admin Network, block access to StorageGRID on the Admin Network with an external firewall.

## Guidelines for Client Network

The Client Network is typically used for tenants and for communicating with external services, such as the CloudMirror replication service or another platform service. However, StorageGRID does not enforce this usage internally.

If you are using the Client Network, follow these guidelines:

* Block all internal traffic ports on the Client Network. See the link:../network/internal-grid-node-communications.html[list of internal ports].
* Accept inbound client traffic only on explicitly configured endpoints. See the information about link:../admin/manage-firewall-controls.html[managing firewall controls].

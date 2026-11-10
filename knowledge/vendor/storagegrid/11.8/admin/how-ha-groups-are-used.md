---
id: "storagegrid-118-9f7a7006be537df5"
title: "StorageGRID 11.8 How are HA groups used?"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/how-ha-groups-are-used.adoc"
source_sha256: "43346ca212a39b8fdaf59e5b64cd8808f3d4e653f9fb4bcd633d71bd35ebb38f"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/how-ha-groups-are-used.adoc"
---

# StorageGRID 11.8 How are HA groups used?

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/how-ha-groups-are-used.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# How are HA groups used?
:icons: font
:imagesdir: ../media/

[.lead]
You can use high availability (HA) groups to provide highly available connections to StorageGRID for object data and for administrative use.

* An HA group can provide highly available administrative connections to the Grid Manager or the Tenant Manager.
* An HA group can provide highly available data connections for S3 and Swift clients.
* An HA group that contains only one interface allows you to provide many VIP addresses and to explicitly set IPv6 addresses.

An HA group can provide high availability only if all nodes included in the group provide the same services. When you create an HA group, add interfaces from the types of nodes that provide the services you require.

* *Admin Nodes*: Include the Load Balancer service and enable access to the Grid Manager or the Tenant Manager.
* *Gateway Nodes*: Include the Load Balancer service.

[cols="1a,2a" options="header"]
|===
| Purpose of HA group| Add nodes of this type to the HA group
a|
Access to Grid Manager
a|

* Primary Admin Node (*Primary*)
* Non-primary Admin Nodes

*Note:* The primary Admin Node must be the Primary interface. Some maintenance procedures can only be performed from the primary Admin Node.

a|
Access to Tenant Manager only
a|

* Primary or non-primary Admin Nodes

a|
S3 or Swift client access -- Load Balancer service
a|

* Admin Nodes
* Gateway Nodes

a|S3 client access for link:../admin/manage-s3-select-for-tenant-accounts.html[S3 Select]
a|* Services appliances
* VMware-based software nodes

*Note*: HA groups are recommended when using S3 Select, but not required.


a|

* Gateway Nodes

|===

## Limitations of using HA groups with Grid Manager or Tenant Manager

If a Grid Manager or Tenant Manager service fails, HA group failover is not triggered.

If you are signed in to the Grid Manager or the Tenant Manager when failover occurs, you are signed out and must sign in again to resume your task.

Some maintenance procedures can't be performed when the primary Admin Node is unavailable. During failover, you can use the Grid Manager to monitor your StorageGRID system.

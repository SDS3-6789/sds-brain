---
id: "storagegrid-120-9f7a7006be537df5"
title: "StorageGRID 12.0 How StorageGRID HA groups provide high availability"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/how-ha-groups-are-used.adoc"
source_sha256: "e43d746718b9865474ccb0a09c89252c6b8c65e6be73267b4afe377c542a7ed9"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/how-ha-groups-are-used.adoc"
---

# StorageGRID 12.0 How StorageGRID HA groups provide high availability

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/how-ha-groups-are-used.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# How StorageGRID HA groups provide high availability
:icons: font
:imagesdir: ../media/

[.lead]
You can use high availability (HA) groups to provide highly available connections to StorageGRID for object data and for administrative use.

* An HA group can provide highly available administrative connections to the Grid Manager or the Tenant Manager.
* An HA group can provide highly available data connections for S3 clients.
* An HA group that contains only one interface allows you to provide many VIP addresses and to explicitly set IPv6 addresses.

An HA group can provide high availability only if all nodes included in the group provide the same services. When you create an HA group, add interfaces from the types of nodes that provide the services you require.

* *Admin Nodes*: Include the Load Balancer service and enable access to the Grid Manager or the Tenant Manager.
* *Gateway Nodes*: Include the Load Balancer service.

[cols="1a,2a" options="header"]
|===
| Purpose of HA group| Add nodes of this type to the HA group

| Access to Grid Manager
| * Primary Admin Node (*Primary*)
* Non-primary Admin Nodes

*Note:* The primary Admin Node must be the Primary interface. Some maintenance procedures can only be performed from the primary Admin Node.

| Access to Tenant Manager only
| * Primary or non-primary Admin Nodes

| S3 client access--Load Balancer service
| * Admin Nodes
* Gateway Nodes

| S3 client access for link:../admin/manage-s3-select-for-tenant-accounts.html[S3 Select]
| * Services appliances
* VMware-based software nodes

*Note*: HA groups are recommended when using S3 Select, but not required.
|===

## Limitations of using HA groups with Grid Manager or Tenant Manager

If a Grid Manager or Tenant Manager service fails, HA group failover is not triggered.

If you are signed in to the Grid Manager or the Tenant Manager when failover occurs, you are signed out and must sign in again to resume your task.

Some maintenance procedures can't be performed when the primary Admin Node is unavailable. During failover, you can use the Grid Manager to monitor your StorageGRID system.

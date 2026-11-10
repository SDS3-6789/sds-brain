---
id: "storagegrid-120-6133027773accc5e"
title: "StorageGRID 12.0 What is a StorageGRID Gateway Node?"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/primer/what-gateway-node-is.adoc"
source_sha256: "e51566a3db4b422c0ea7d38e2233d641428bedf242bae43d4f85065284d966c9"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "primer/what-gateway-node-is.adoc"
---

# StorageGRID 12.0 What is a StorageGRID Gateway Node?

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/primer/what-gateway-node-is.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# What is a StorageGRID Gateway Node?
:icons: font
:imagesdir: ../media/

[.lead]
Gateway Nodes provide a dedicated load-balancing interface that S3 client applications can use to connect to StorageGRID. Load balancing maximizes speed and connection capacity by distributing the workload across multiple Storage Nodes. Gateway Nodes are optional.

The StorageGRID Load Balancer service is provided on all Admin Nodes and all Gateway Nodes. It performs Transport Layer Security (TLS) termination of client requests, inspects the requests, and establishes new secure connections to the Storage Nodes. The Load Balancer service seamlessly directs clients to an optimal Storage Node, so that the failure of nodes or even an entire site is transparent. 

You configure one or more load balancer endpoints to define the port and network protocol (HTTPS or HTTP) that incoming and outgoing client requests wil use to access the Load Balancer services on Gateway and Admin Nodes. The load balancer endpoint also defines the client type (S3), the binding mode, and optionally a list of allowed or blocked tenants. See link:../admin/managing-load-balancing.html[Considerations for load balancing]. 

As required, you can group the network interfaces of multiple Gateway Nodes and Admin Nodes into a high availability (HA) group. If the active interface in the HA group fails, a backup interface can manage the client application workload. See link:../admin/managing-high-availability-groups.html[Manage high availability (HA) groups].

## Primary services for Gateway Nodes

The following table shows the primary services for Gateway Nodes; however, this table does not list all node services.

[cols="1a,2a" options="header"]
|===
| Service| Key function

| Cache Service
|	Manages a local cache of object content.

| High Availability
| Manages high availability virtual IP addresses for groups of Admin Nodes and Gateway Nodes.

*Note:* This service is also found on Admin Nodes.

| Load Balancer
| Provides Layer 7 load balancing of S3 traffic from clients to Storage Nodes. This is the recommended load balancing mechanism.

*Note:* This service is also found on Admin Nodes.

| Server Status Monitor (SSM)
| Monitors the operating system and underlying hardware.
|===

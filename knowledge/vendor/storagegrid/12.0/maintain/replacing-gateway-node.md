---
id: "storagegrid-120-18bc7ee9fb3c1eec"
title: "StorageGRID 12.0 Replace StorageGRID Gateway Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/replacing-gateway-node.adoc"
source_sha256: "872538b85f951be6993ae0ba7e9782229cde2671ce9747851d32792340ccb8c1"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/replacing-gateway-node.adoc"
---

# StorageGRID 12.0 Replace StorageGRID Gateway Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/replacing-gateway-node.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Replace StorageGRID Gateway Node
:icons: font
:imagesdir: ../media/

[.lead]
You can replace a failed Gateway Node with a Gateway Node running on the same physical or virtual hardware, or you can replace a Gateway Node running on VMware or a Linux host with a Gateway Node hosted on a services appliance.

The node replacement procedure you must follow depends on which platform will be used by the replacement node. After you complete the node replacement procedure (which is suitable for all node types), that procedure will direct you to the next step for Gateway Node recovery.

[cols="1a,2a" options="header"]
|===
| Replacement platform| Procedure
|VMware
| link:all-node-types-replacing-vmware-node.html[Replace a VMware node]

|Linux
| link:all-node-types-replacing-linux-node.html[Replace a Linux node]

|Services appliances
| link:replacing-failed-node-with-services-appliance.html[Replace a services appliance]

|OpenStack
|NetApp-provided virtual machine disk files and scripts for OpenStack are no longer supported for recovery operations. If you need to recover a node running in an OpenStack deployment, download the files for your Linux operating system. Then, follow the procedure for link:all-node-types-replacing-linux-node.html[replacing a Linux node].
|===

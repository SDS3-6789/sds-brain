---
id: "storagegrid-118-18bc7ee9fb3c1eec"
title: "StorageGRID 11.8 Replace Gateway Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/replacing-gateway-node.adoc"
source_sha256: "1e7bc8b1a77bbc48d04fbedc1c176caf7bc30c8c36115a76051e5a285c9fc6bf"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/replacing-gateway-node.adoc"
---

# StorageGRID 11.8 Replace Gateway Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/replacing-gateway-node.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Replace Gateway Node
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

---
id: "storagegrid-119-0ed6d13f450c0fc1"
title: "StorageGRID 11.9 Warnings for recovering appliance Storage Nodes"
area: "storagegrid"
type: "import"
applies_to: ["11.9", "storagegrid-11.9"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg119-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-119"
repository_commit: "aa58c9affae3bb1994d6bd2e525851e3fd088517"
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/recovering-storagegrid-appliance-storage-node.adoc"
source_sha256: "d103fc55121c643f0021eff406f70786d8aa8e64aa865d2ada0eb37edf3421f4"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/recovering-storagegrid-appliance-storage-node.adoc"
---

# StorageGRID 11.9 Warnings for recovering appliance Storage Nodes

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/recovering-storagegrid-appliance-storage-node.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Warnings for recovering appliance Storage Nodes
:icons: font
:imagesdir: ../media/

[.lead]
The procedure for recovering a failed StorageGRID appliance Storage Node is the same whether you are recovering from the loss of the system drive or from the loss of storage volumes only.

CAUTION: If more than one Storage Node has failed (or is offline), contact technical support. Don't perform the following recovery procedure. Data loss could occur.

CAUTION: If this is the second Storage Node failure in less than 15 days after a Storage Node failure or recovery, contact technical support. Rebuilding Cassandra on two or more Storage Nodes within 15 days can result in data loss.

NOTE: If more than one Storage Node at a site has failed, a site recovery procedure might be required. See link:how-site-recovery-is-performed-by-technical-support.html[How technical support recovers a site].

CAUTION: If ILM rules are configured to store only one replicated copy and the copy exists on a storage volume that has failed, you will not be able to recover the object.

NOTE: For hardware maintenance procedures, such as instructions for replacing a controller or reinstalling SANtricity OS, see the https://docs.netapp.com/us-en/storagegrid-appliances/commonhardware/index.html[maintenance instructions for your storage appliance^].

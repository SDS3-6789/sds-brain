---
id: "storagegrid-119-82af8be81941dfa7"
title: "StorageGRID 11.9 Replace failed node with services appliance"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/replacing-failed-node-with-services-appliance.adoc"
source_sha256: "1cc9c7da962ea60a88817bc3d60d3a9fddaf2f03361c66a8743eba002fd6bac9"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/replacing-failed-node-with-services-appliance.adoc"
---

# StorageGRID 11.9 Replace failed node with services appliance

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/replacing-failed-node-with-services-appliance.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Replace failed node with services appliance
:icons: font
:imagesdir: ../media/

[.lead]
You can use a services appliance to recover a failed Gateway Node, a failed non-primary Admin Node, or a failed primary Admin Node that was hosted on VMware, a Linux host, or a services appliance. This procedure is one step of the grid node recovery procedure.

.Before you begin

* You have determined that one of the following situations is true:
 ** The virtual machine hosting the node can't be restored.
 ** The physical or virtual Linux host for the grid node has failed, and must be replaced.
 ** The services appliance hosting the grid node must be replaced.
* You have confirmed that the StorageGRID Appliance Installer version on the services appliance matches the software version of your StorageGRID system. See https://docs.netapp.com/us-en/storagegrid-appliances/installconfig/verifying-and-upgrading-storagegrid-appliance-installer-version.html[Verify and upgrade StorageGRID Appliance Installer version^].

NOTE: Don't deploy both an SG110 and an SG1100 services appliance or an SG100 and an SG1000 services appliance in the same site. Unpredictable performance might result.

.About this task

You can use a services appliance to recover a failed grid node in the following cases:

* The failed node was hosted on VMware or Linux (link:installing-services-appliance-platform-change-only.html[platform change])
* The failed node was hosted on a services appliance (link:preparing-appliance-for-reinstallation-platform-replacement-only.html[platform replacement])

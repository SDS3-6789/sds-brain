---
id: "storagegrid-118-60291e3a76eb1882"
title: "StorageGRID 11.8 Reset Archive Node connection to the cloud"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/resetting-archive-node-connection-to-cloud.adoc"
source_sha256: "8a618a8d9a3b86ea8587d4bfaca0b77c42c349041cdacc6fd4aecf5b8247b4ae"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/resetting-archive-node-connection-to-cloud.adoc"
---

# StorageGRID 11.8 Reset Archive Node connection to the cloud

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/resetting-archive-node-connection-to-cloud.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Reset Archive Node connection to the cloud
:icons: font
:imagesdir: ../media/

[.lead]
After you recover an Archive Node that targets the cloud through the S3 API, you need to modify configuration settings to reset connections. An Outbound Replication Status (ORSU) alarm is triggered if the Archive Node is unable to retrieve object data.

NOTE: If your Archive Node connects to external storage through TSM middleware, then the node resets itself automatically and you don't need to reconfigure.

.Before you begin

You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.Steps

. Select *SUPPORT* > *Tools* > *Grid topology*.
. Select *Archive Node* > *ARC* > *Target*.
. Edit the *Access Key* field by entering an incorrect value and click *Apply Changes*.
. Edit the *Access Key* field by entering the correct value and click *Apply Changes*.

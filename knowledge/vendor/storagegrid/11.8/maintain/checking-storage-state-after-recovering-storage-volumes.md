---
id: "storagegrid-118-53d0ccf47d903352"
title: "StorageGRID 11.8 Check storage state after recovering storage volumes"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/checking-storage-state-after-recovering-storage-volumes.adoc"
source_sha256: "b3888a0f417c40f43e5c61701e5b92f57a2e9f0264d74af8ab7408c255a0ea13"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/checking-storage-state-after-recovering-storage-volumes.adoc"
---

# StorageGRID 11.8 Check storage state after recovering storage volumes

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/checking-storage-state-after-recovering-storage-volumes.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Check storage state after recovering storage volumes
:icons: font
:imagesdir: ../media/

[.lead]
After recovering storage volumes, you must verify that the desired state of the Storage Node is set to online and ensure that the state will be online by default whenever the Storage Node server is restarted.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* The Storage Node has been recovered, and data recovery is complete.

.Steps

. Select *SUPPORT* > *Tools* > *Grid topology*.
. Check the values of *Recovered Storage Node* > *LDR* > *Storage* > *Storage State -- Desired* and *Storage State -- Current*.
+
The value of both attributes should be Online.

. If the Storage State -- Desired is set to Read-only, complete the following steps:
 .. Click the *Configuration* tab.
 .. From the *Storage State -- Desired* drop-down list, select *Online*.
 .. Click *Apply Changes*.
 .. Click the *Overview* tab and confirm that the values of *Storage State -- Desired* and *Storage State -- Current* are updated to Online.

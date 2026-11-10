---
id: "storagegrid-119-b3be7df9e3801fff"
title: "StorageGRID 11.9 Check storage state after recovering appliance Storage Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/checking-storage-state-after-recovering-sga.adoc"
source_sha256: "5b7877437d11f26de54db704b9221e769ffeb6b33a6858732fc2add2d4adba84"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/checking-storage-state-after-recovering-sga.adoc"
---

# StorageGRID 11.9 Check storage state after recovering appliance Storage Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/checking-storage-state-after-recovering-sga.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Check storage state after recovering appliance Storage Node
:icons: font
:imagesdir: ../media/

[.lead]
After recovering an appliance Storage Node, you must verify that the desired state of the appliance Storage Node is set to online and ensure that the state will be online by default whenever the Storage Node server is restarted.

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

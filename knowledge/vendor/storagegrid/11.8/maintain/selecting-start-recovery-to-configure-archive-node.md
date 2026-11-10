---
id: "storagegrid-118-18d765cf86af44b0"
title: "StorageGRID 11.8 Select Start Recovery to configure Archive Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/selecting-start-recovery-to-configure-archive-node.adoc"
source_sha256: "71f8ae846b0d5bd30b128f865f0cab9f445e30f094a1117218a101f5712fd08b"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/selecting-start-recovery-to-configure-archive-node.adoc"
---

# StorageGRID 11.8 Select Start Recovery to configure Archive Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/selecting-start-recovery-to-configure-archive-node.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Select Start Recovery to configure Archive Node
:icons: font
:imagesdir: ../media/

[.lead]
After replacing an Archive Node, you must select Start Recovery in the Grid Manager to configure the new node as a replacement for the failed node.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:../admin/admin-group-permissions.html[Maintenance or Root access permission].
* You have the provisioning passphrase.
* You have deployed and configured the replacement node.

.Steps

. From the Grid Manager, select *MAINTENANCE* > *Tasks* > *Recovery*.
. Select the grid node you want to recover in the Pending Nodes list.
+
Nodes appear in the list after they fail, but you can't select a node until it has been reinstalled and is ready for recovery.

. Enter the *Provisioning Passphrase*.
. Click *Start Recovery*.
+
image::../media/4b_select_recovery_node.png[screenshot showing the Maintenance > Recovery page]

. Monitor the progress of the recovery in the Recovering Grid Node table.
+
NOTE: While the recovery procedure is running, you can click *Reset* to start a new recovery. A dialog box appears, indicating that the node will be left in an indeterminate state if you reset the procedure.
+
image::../media/recovery_reset_warning.gif[screenshot showing the reset recovery warning dialog box]
+
If you want to retry the recovery after resetting the procedure, you must restore the node to a pre-installed state, as follows:

 ** *VMware*: Delete the deployed virtual grid node. Then, when you are ready to restart the recovery, redeploy the node.
 ** *Linux*: Restart the node by running this command on the Linux host: `storagegrid node force-recovery _node-name_`

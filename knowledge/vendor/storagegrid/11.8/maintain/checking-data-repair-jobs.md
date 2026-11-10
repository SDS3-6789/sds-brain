---
id: "storagegrid-118-30caae57da963b48"
title: "StorageGRID 11.8 Check data repair jobs"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/checking-data-repair-jobs.adoc"
source_sha256: "afe1cc810e26e3f9de9274ee81f52a4566a9479be83cb89ba17106272ec3dfa6"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/checking-data-repair-jobs.adoc"
---

# StorageGRID 11.8 Check data repair jobs

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/checking-data-repair-jobs.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Check data repair jobs
:icons: font
:imagesdir: ../media/

[.lead]
Before decommissioning a grid node, you must confirm that no data repair jobs are active. If any repairs have failed, you must restart them and allow them to complete before performing the decommission procedure.

.About this task
If you need to decommission a disconnected Storage Node, you will also complete these steps after the decommission procedure completes to ensure the data repair job has completed successfully. You must ensure that any erasure-coded fragments that were on the removed node have been restored successfully.

These steps only apply to systems that have erasure-coded objects.

.Steps

. Log in to the primary Admin Node:

.. Enter the following command: `ssh admin@_grid_node_IP_`
.. Enter the password listed in the `Passwords.txt` file.
.. Enter the following command to switch to root: `su -`
.. Enter the password listed in the `Passwords.txt` file.
+
When you are logged in as root, the prompt changes from `$` to `#`.

. Check for running repairs: `repair-data show-ec-repair-status`
** If you have never run a data repair job, the output is `No job found`. You don't need to restart any repair jobs.
** If the data repair job was run previously or is running currently, the output lists information for the repair. Each repair has a unique repair ID.
+
image::../media/repair-data-status.png[Repair data status]

+
TIP: Optionally, you can use the Grid Manager to monitor restoration processes in progress and display a restoration history. See 
link:../maintain/restoring-volume.html[Restore object data using Grid Manager].

. If the State for all repairs is `Completed`, you don't need to restart any repair jobs.
. If the State for any repair is `Stopped`, you must restart that repair.
 .. Obtain the repair ID for the failed repair from the output.
 .. Run the `repair-data start-ec-node-repair` command.
+
Use the `--repair-id` option to specify the Repair ID. For example, if you want to retry a repair with repair ID 949292, run this command: `repair-data start-ec-node-repair --repair-id 949292`

 .. Continue to track the status of EC data repairs until the State for all repairs is `Completed`.

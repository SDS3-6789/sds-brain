---
id: "storagegrid-118-c1765ed8e88625e3"
title: "StorageGRID 11.8 Recover Storage Node down more than 15 days"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/recovering-storage-node-that-has-been-down-more-than-15-days.adoc"
source_sha256: "dceba8f1f435b920c9e648a615aba42ef02e6b62308578577e287d6a776c5a37"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/recovering-storage-node-that-has-been-down-more-than-15-days.adoc"
---

# StorageGRID 11.8 Recover Storage Node down more than 15 days

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/recovering-storage-node-that-has-been-down-more-than-15-days.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Recover Storage Node down more than 15 days
:icons: font
:imagesdir: ../media/

[.lead]
If a single Storage Node has been offline and not connected to other Storage Nodes for more than 15 days, you must rebuild Cassandra on the node.

.Before you begin

* You have checked that a Storage Node decommissioning is not in progress, or you have paused the node decommission procedure. (In the Grid Manager, select *MAINTENANCE* > *Tasks* > *Decommission*.)
* You have checked that an expansion is not in progress. (In the Grid Manager, select *MAINTENANCE* > *Tasks* > *Expansion*.)

.About this task

Storage Nodes have a Cassandra database that includes object metadata. If a Storage Node has not been able to communicate with other Storage Nodes for more than 15 days, StorageGRID assumes that node's Cassandra database is stale. The Storage Node can't rejoin the grid until Cassandra has been rebuilt using information from other Storage Nodes.

Use this procedure to rebuild Cassandra only if a single Storage Node is down. Contact technical support if additional Storage Nodes are offline or if Cassandra has been rebuilt on another Storage Node within the last 15 days; for example, Cassandra might have been rebuilt as part of the procedures to recover failed storage volumes or to recover a failed Storage Node.

CAUTION: If more than one Storage Node has failed (or is offline), contact technical support. Don't perform the following recovery procedure. Data loss could occur.

CAUTION: If this is the second Storage Node failure in less than 15 days after a Storage Node failure or recovery, contact technical support. Don't perform the following recovery procedure. Data loss could occur.

NOTE: If more than one Storage Node at a site has failed, a site recovery procedure might be required. See link:how-site-recovery-is-performed-by-technical-support.html[How technical support recovers a site].

.Steps

. If necessary, power on the Storage Node that needs to be recovered.
. Log in to the grid node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.
+
When you are logged in as root, the prompt changes from `$` to `#`.+
+
NOTE: If you are unable to log in to the grid node, the system disk might not be intact. Go to the procedure for  link:recovering-from-system-drive-failure.html[recovering from system drive failure].

. Perform the following checks on the Storage Node:
 .. Issue this command: `nodetool status`
+
The output should be `Connection refused`

 .. In the Grid Manager, select *SUPPORT* > *Tools* > *Grid topology*.
 .. Select *_Site_* > *Storage Node* > *SSM* > *Services*. Verify that the Cassandra service displays `Not Running`.
 .. Select *Storage Node* > *SSM* > *Resources*. Verify that there is no error status in the Volumes section.
 .. Issue this command: `grep -i Cassandra /var/local/log/servermanager.log`
+
You should see the following message in the output:
+
----
Cassandra not started because it has been offline for more than 15 day grace period - rebuild Cassandra
----
. Issue this command, and monitor the script output: `check-cassandra-rebuild`
 ** If the Cassandra service depending on volume 0 is running, you will be prompted to stop it. Enter: *y*
+
NOTE: If the Cassandra service is already stopped, you aren't prompted. The Cassandra service is stopped only for volume 0.
 ** Review the warnings in the script. If none of them apply, confirm that you want to rebuild Cassandra. Enter: *y*
+
NOTE: Some StorageGRID recovery procedures use Reaper to handle Cassandra repairs. Repairs occur automatically as soon as the related or required services have started. You might notice script output that mentions "reaper" or "Cassandra repair." If you see an error message indicating the repair has failed, run the command indicated in the error message.

. After the rebuild completes, perform the following checks:
 .. In the Grid Manager, select *SUPPORT* > *Tools* > *Grid topology*.
 .. Select *_Site_* > *recovered Storage Node* > *SSM* > *Services*.
 .. Confirm that all services are running.
 .. Select *DDS* > *Data Store*.
 .. Confirm that the *Data Store Status* is "Up" and the *Data Store State* is "Normal."

---
id: "storagegrid-120-c6537b0f54146c0e"
title: "StorageGRID 12.0 Restore StorageGRID Admin Node database when recovering non-primary Admin Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/restoring-admin-node-database-non-primary-admin-node.adoc"
source_sha256: "561f25b22f6adf82b71007e21f822c289e7f17742bc2519fe249d202af00a2a5"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/restoring-admin-node-database-non-primary-admin-node.adoc"
---

# StorageGRID 12.0 Restore StorageGRID Admin Node database when recovering non-primary Admin Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/restoring-admin-node-database-non-primary-admin-node.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Restore StorageGRID Admin Node database when recovering non-primary Admin Node
:icons: font
:imagesdir: ../media/

[.lead]
If you want to retain the historical information about attributes and alerts on a non-primary Admin Node that has failed, you can restore the Admin Node database from the primary Admin Node.

.Before you begin

* The recovered Admin Node is installed and running.
* The StorageGRID system includes at least two Admin Nodes.
* You have the `Passwords.txt` file.
* You have the provisioning passphrase.

.About this task

If an Admin Node fails, the historical information stored in its Admin Node database is lost. This database includes the following information:

* Alert history
* Historical attribute data, which is used in in legacy-style charts on the Nodes page

When you recover an Admin Node, the software installation process creates an empty Admin Node database on the recovered node. However, the new database only includes information for servers and services that are currently part of the system or added later.

If you restored a non-primary Admin Node, you can restore the historical information by copying the Admin Node database from the primary Admin Node (the _source Admin Node_) to the recovered node.

NOTE: Copying the Admin Node database might take several hours. Some Grid Manager features will be unavailable while services are stopped on the source node.

.Steps

. Log in to the source Admin Node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.

. Run the following command from the source Admin Node. Then, enter the provisioning passphrase if prompted. `recover-access-points`

. From the source Admin Node, stop the MI service: `service mi stop`

. From the source Admin Node, stop the Management Application Program Interface (mgmt-api) service: `service mgmt-api stop`

. Complete the following steps on the recovered Admin Node:
 .. Log in to the recovered Admin Node:
  ... Enter the following command: `ssh admin@_grid_node_IP_`
  ... Enter the password listed in the `Passwords.txt` file.
  ... Enter the following command to switch to root: `su -`
  ... Enter the password listed in the `Passwords.txt` file.
 .. Stop the MI service: `service mi stop`
 .. Stop the mgmt-api service: `service mgmt-api stop`
 .. Add the SSH private key to the SSH agent. Enter:``ssh-add``
 .. Enter the SSH Access Password listed in the `Passwords.txt` file.
 .. Copy the database from the source Admin Node to the recovered Admin Node: `/usr/local/mi/bin/mi-clone-db.sh Source_Admin_Node_IP`
 .. When prompted, confirm that you want to overwrite the MI database on the recovered Admin Node.
+
The database and its historical data are copied to the recovered Admin Node. When the copy operation is done, the script starts the recovered Admin Node.

 .. When you no longer require passwordless access to other servers, remove the private key from the SSH agent. Enter:``ssh-add -D``
 
. Restart the services on the source Admin Node: `service servermanager start`

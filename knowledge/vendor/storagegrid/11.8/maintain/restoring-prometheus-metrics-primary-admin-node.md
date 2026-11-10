---
id: "storagegrid-118-4a1378ba4f61cb46"
title: "StorageGRID 11.8 Restore Prometheus metrics when recovering primary Admin Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/restoring-prometheus-metrics-primary-admin-node.adoc"
source_sha256: "c5744c8b309b1899865882fcdb9f4634fa4eb9133c0a7a23d1b08f71f99f70e1"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/restoring-prometheus-metrics-primary-admin-node.adoc"
---

# StorageGRID 11.8 Restore Prometheus metrics when recovering primary Admin Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/restoring-prometheus-metrics-primary-admin-node.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Restore Prometheus metrics when recovering primary Admin Node
:icons: font
:imagesdir: ../media/

[.lead]
Optionally, you can retain the historical metrics maintained by Prometheus on a primary Admin Node that has failed. The Prometheus metrics can only be restored if your StorageGRID system includes another Admin Node.

.Before you begin

* The recovered Admin Node is installed and running.
* The StorageGRID system includes at least two Admin Nodes.
* You have the `Passwords.txt` file.
* You have the provisioning passphrase.

.About this task

If an Admin Node fails, the metrics maintained in the Prometheus database on the Admin Node are lost. When you recover the Admin Node, the software installation process creates a new Prometheus database. After the recovered Admin Node is started, it records metrics as if you had performed a new installation of the StorageGRID system.

If you restored a primary Admin Node and your StorageGRID system has another Admin Node, you can restore the historical metrics by copying the Prometheus database from a non-primary Admin Node (the _source Admin Node_) to the recovered primary Admin Node. If your system has only a primary Admin Node, you can't restore the Prometheus database.

NOTE: Copying the Prometheus database might take an hour or more. Some Grid Manager features will be unavailable while services are stopped on the source Admin Node.

.Steps

. Log in to the source Admin Node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.
. From the source Admin Node, stop the Prometheus service: `service prometheus stop`
. Complete the following steps on the recovered Admin Node:
 .. Log in to the recovered Admin Node:
  ... Enter the following command: `ssh admin@_grid_node_IP_`
  ... Enter the password listed in the `Passwords.txt` file.
  ... Enter the following command to switch to root: `su -`
  ... Enter the password listed in the `Passwords.txt` file.
 .. Stop the Prometheus service: `service prometheus stop`
 .. Add the SSH private key to the SSH agent. Enter:``ssh-add``
 .. Enter the SSH Access Password listed in the `Passwords.txt` file.
 .. Copy the Prometheus database from the source Admin Node to the recovered Admin Node: `/usr/local/prometheus/bin/prometheus-clone-db.sh Source_Admin_Node_IP`
 .. When prompted, press *Enter* to confirm that you want to destroy the new Prometheus database on the recovered Admin Node.
+
The original Prometheus database and its historical data are copied to the recovered Admin Node. When the copy operation is done, the script starts the recovered Admin Node. The following status appears:
+
Database cloned, starting services

 .. When you no longer require passwordless access to other servers, remove the private key from the SSH agent. Enter:``ssh-add -D``
. Restart the Prometheus service on the source Admin Node.`service prometheus start`

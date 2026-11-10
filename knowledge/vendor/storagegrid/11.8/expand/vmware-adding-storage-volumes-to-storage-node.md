---
id: "storagegrid-118-0fe291a0aa91fb89"
title: "StorageGRID 11.8 VMware: Add storage volumes to Storage Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/vmware-adding-storage-volumes-to-storage-node.adoc"
source_sha256: "61f25a6be15d32d046a87781ae32c9b09a798734bd04af13b998625d30e68046"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "expand/vmware-adding-storage-volumes-to-storage-node.adoc"
---

# StorageGRID 11.8 VMware: Add storage volumes to Storage Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/vmware-adding-storage-volumes-to-storage-node.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# VMware: Add storage volumes to Storage Node
:icons: font
:imagesdir: ../media/

[.lead]
If a Storage Node includes fewer than 16 storage volumes, you can increase its capacity by using VMware vSphere to add volumes.

.Before you begin
* You have access to the instructions for installing StorageGRID for VMware deployments.
** link:../vmware/index.html[Install StorageGRID on VMware]

* You have the `Passwords.txt` file.
* You have link:../admin/admin-group-permissions.html[specific access permissions].

CAUTION: Don't attempt to add storage volumes to a Storage Node while a software upgrade, recovery procedure, or another expansion procedure is active.

.About this task

The Storage Node is unavailable for a brief time when you add storage volumes. You should perform this procedure on one Storage Node at a time to avoid impacting client-facing grid services.

.Steps

. If necessary, install new storage hardware and create new VMware datastores.
. Add one or more hard disks to the virtual machine for use as storage (object stores).
 .. Open VMware vSphere Client.
 .. Edit the virtual machine settings to add one or more additional hard disks.

+
The hard disks are typically configured as Virtual Machine Disks (VMDKs). VMDKs are more commonly used and are easier to manage, while RDMs might provide better performance for workloads that use larger object sizes (for example, greater than 100 MB). For more information about adding hard disks to virtual machines, see the VMware vSphere documentation.
. Restart the virtual machine by using the *Restart Guest OS* option in the VMware vSphere Client, or by entering the following command in an ssh session to the virtual machine:``sudo reboot``
+
NOTE: Don't use *Power Off* or *Reset* to restart the virtual machine.

. Configure the new storage for use by the Storage Node:
 .. Log in to the grid node:
  ... Enter the following command: `ssh admin@_grid_node_IP_`
  ... Enter the password listed in the `Passwords.txt` file.
  ... Enter the following command to switch to root: `su -`
  ... Enter the password listed in the `Passwords.txt` file.
When you are logged in as root, the prompt changes from `$` to `#`.
 .. Configure the new storage volumes:
+
`sudo add_rangedbs.rb`
+
This script finds any new storage volumes and prompts you to format them.

 .. Enter *y* to accept the formatting.
 .. If any of the volumes have previously been formatted, decide if you want to reformat them.
  *** Enter *y* to reformat.
  *** Enter *n* to skip reformatting.

+
The `setup_rangedbs.sh` script runs automatically.
. Check that the services start correctly:
 .. View a list of the status of all services on the server:
+
`sudo storagegrid-status`
+
The status is updated automatically.

 .. Wait until all services are Running or Verified.
 .. Exit the status screen:
+
`Ctrl+C`
. Verify that the Storage Node is online:
 .. Sign in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
 .. Select *SUPPORT* > *Tools* > *Grid topology*.
 .. Select *_site_* > *_Storage Node_* > *LDR* > *Storage*.
 .. Select the *Configuration* tab and then the *Main* tab.
 .. If the *Storage State - Desired* drop-down list is set to Read-only or Offline, select *Online*.
 .. Select *Apply Changes*.
. To see the new object stores:
 .. Select *NODES* > *_site_* > *_Storage Node_* > *Storage*.
 .. View the details in the *Object Stores* table.

.Result
You can use the expanded capacity of the Storage Nodes to save object data.

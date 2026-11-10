---
id: "storagegrid-120-70cbb2f18e5b9987"
title: "StorageGRID 12.0 Prepare StorageGRID appliance Storage Node for reinstallation"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/preparing-appliance-storage-node-for-reinstallation.adoc"
source_sha256: "89704d493e3e27683c0e6ba08a1e30fe647a74297107d88b5dd12d5d26b77bce"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/preparing-appliance-storage-node-for-reinstallation.adoc"
---

# StorageGRID 12.0 Prepare StorageGRID appliance Storage Node for reinstallation

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/preparing-appliance-storage-node-for-reinstallation.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Prepare StorageGRID appliance Storage Node for reinstallation
:icons: font
:imagesdir: ../media/

[.lead]
When recovering an appliance Storage Node, you must first prepare the appliance for reinstallation of StorageGRID software.

.Steps

. Log in to the failed Storage Node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.

+
When you are logged in as root, the prompt changes from `$` to `#`.
. Prepare the appliance Storage Node for the installation of StorageGRID software. `sgareinstall`
. When prompted to continue, enter: `y`
+
The appliance reboots, and your SSH session ends. It usually takes about 5 minutes for the StorageGRID Appliance Installer to become available, although in some cases you might need to wait up to 30 minutes.
+
CAUTION: Don't attempt to accelerate the reboot by cycling power or otherwise resetting the appliance. You might interrupt automatic BIOS, BMC, or other firmware upgrades.
+
The StorageGRID appliance Storage Node is reset, and data on the Storage Node is no longer accessible. IP addresses configured during the original installation process should remain intact; however, it is recommended that you confirm this when the procedure completes.
+
After executing the `sgareinstall` command, all StorageGRID-provisioned accounts, passwords, and SSH keys are removed, and new host keys are generated.

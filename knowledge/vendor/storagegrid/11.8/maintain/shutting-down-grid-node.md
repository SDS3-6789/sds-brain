---
id: "storagegrid-118-f30f0abc84c9e77f"
title: "StorageGRID 11.8 Shut down grid node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/shutting-down-grid-node.adoc"
source_sha256: "f5a596b8609e395f1c7bf871a2ccdbaee767effe378859c6a55c629fdcce290c"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/shutting-down-grid-node.adoc"
---

# StorageGRID 11.8 Shut down grid node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/shutting-down-grid-node.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Shut down grid node
:icons: font
:imagesdir: ../media/

[.lead]
You can shut down a grid node from the node's command shell.

.Before you begin

* You have the `Passwords.txt` file.

.About this task

Before performing this procedure, review these considerations:

* In general, you should not shut down more than one node at a time to avoid disruptions.
* Don't shut down a node during a maintenance procedure unless explicitly instructed to do so by the documentation or by technical support.
* The shutdown process is based on where the node is installed, as follows:
 ** Shutting down a VMware node shuts down the virtual machine.
 ** Shutting down a Linux node shuts down the container.
 ** Shutting down a StorageGRID appliance node shuts down the compute controller.
* If you plan to shut down more than one Storage Node at a site, stop ingesting objects at that site for approximately one hour before shutting down the nodes.
+
If any ILM rule uses the *Dual commit* ingest option (or if a rule uses the *Balanced* option and all required copies can't be created immediately), StorageGRID immediately commits any newly ingested objects to two Storage Nodes on the same site and evaluates ILM later. If more than one Storage Node at a site is shut down, you might not be able to access newly ingested objects for the duration of the shutdown. Write operations might also fail if too few Storage Nodes remain available at the site. See link:../ilm/index.html[Manage objects with ILM].

.Steps

. Log in to the grid node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.

+
When you are logged in as root, the prompt changes from `$` to `#`.
. Stop all services: `service servermanager stop`
+
Services can take up to 15 minutes to shut down, and you might want to log in to the system remotely to monitor the shutdown process.
. If the node is running on a VMware virtual machine or it is an appliance node, issue the shutdown command: `shutdown -h now`
+
Perform this step regardless of the outcome of the `service servermanager stop` command.
+
NOTE: After you issue the `shutdown -h now` command on an appliance node, you must power cycle the appliance to restart the node.
+
For the appliance, this command shuts down the controller, but the appliance is still powered on. You must complete the next step.

. If you are powering down an appliance node, follow the steps for your appliance.
+
[role="tabbed-block"]
#### .SG6160
--

.. Turn off the power to the SG6100-CN storage controller.
.. Wait for the blue power LED on the SG6100-CN storage controller to turn off.
--

.SGF6112
--

.. Turn off the power to the appliance.
.. Wait for the blue power LED to turn off.
--

.SG6000
--

.. Wait for the green Cache Active LED on the back of the storage controllers to turn off.
+
This LED is on when cached data needs to be written to the drives. You must wait for this LED to turn off before you turn off power.

.. Turn off the power to the appliance, and wait for the blue power LED to turn off.
--

.SG5800
--
.. Wait for the green Cache Active LED on the back of the storage controller to turn off.
+
This LED is on when cached data needs to be written to the drives. You must wait for this LED to turn off before you turn off power.
.. From the home page of SANtricity System Manager, select *View Operations in Progress*.
.. Confirm that all operations have completed before continuing with the next step.
.. Turn off both power switches on the controller shelf, and wait for all LEDs on the controller shelf to turn off.
--

.SG5700
--

.. Wait for the green Cache Active LED on the back of the storage controller to turn off.
+
This LED is on when cached data needs to be written to the drives. You must wait for this LED to turn off before you turn off power.

.. Turn off the power to the appliance, and wait for all LED and seven-segment display activity to stop.

--

.SG100 or SG1000
--

.. Turn off the power to the appliance.
.. Wait for the blue power LED to turn off.

--
####

---
id: "storagegrid-120-2fd0cc01fc127171"
title: "StorageGRID 12.0 Migrate a StorageGRID node to a new Linux host"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/linux-migrating-grid-node-to-new-host.adoc"
source_sha256: "6b61c6c97128c8612b95326ab28b7e4a09fc21e50ecccd18fbe32104c1798eb2"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/linux-migrating-grid-node-to-new-host.adoc"
---

# StorageGRID 12.0 Migrate a StorageGRID node to a new Linux host

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/linux-migrating-grid-node-to-new-host.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Migrate a StorageGRID node to a new Linux host
:icons: font
:imagesdir: ../media/

[.lead]
You can migrate one or more StorageGRID nodes from one Linux host (the _source host_) to another Linux host (the _target host_) to perform host maintenance without impacting the functionality or availability of your grid.

For example, you might want to migrate a node to perform OS patching and reboot. 
 
.Before you begin

* You planned your StorageGRID deployment to include migration support. See link:../swnodes/node-container-migration-requirements.html[Node container migration requirements].

* The target host is already prepared for StorageGRID use.

* Shared storage is used for all per-node storage volumes
* Network interfaces have consistent names across hosts.

[NOTE]
#### In a production deployment, don't run more than one Storage Node on a single host. Using a dedicated host for each Storage Node provides an isolated failure domain.

Other types of nodes, such as Admin Nodes or Gateway Nodes, can be deployed on the same host. However, if you have multiple nodes of the same type (two Gateway Nodes, for example), don't install all instances on the same host.
#### ## Export node from source host

As a first step, shut down the grid node and export it from the source Linux host.

Run the following commands on the _source host_. 

.Steps

. Obtain the status of all nodes currently running on the source host.
+
`sudo storagegrid node status all`
+
Example output:
+
----
Name Config-State Run-State
DC1-ADM1 Configured Running
DC1-ARC1 Configured Running
DC1-GW1 Configured Running
DC1-S1 Configured Running
DC1-S2 Configured Running
DC1-S3 Configured Running
----

. Identify the name of the node you want to migrate, and stop it if its Run-State is Running.
+
`sudo storagegrid node stop DC1-S3`
+
Example output:
+
----
Stopping node DC1-S3
Waiting up to 630 seconds for node shutdown
----

. Export the node from the source host.
+
`sudo storagegrid node export DC1-S3`
+
Example output:
+
----
Finished exporting node DC1-S3 to /dev/mapper/sgws-dc1-s3-var-local. 
Use 'storagegrid node import /dev/mapper/sgws-dc1-s3-var-local' if you
want to import it again.
----

. Make note of the `import` command suggested in the output.
+
You will run this command on the target host in the next step.

## Import node on target host

After exporting the node from the source host, you import and validate the node on the target host. Validation confirms that the node has access to the same block storage and network interface devices as it had on the source host.


Run the following commands on the _target host_.

.Steps

. Import the node on the target host.
+
`sudo storagegrid node import /dev/mapper/sgws-dc1-s3-var-local`
+
Example output:
+
----
Finished importing node DC1-S3 from /dev/mapper/sgws-dc1-s3-var-local.
You should run 'storagegrid node validate DC1-S3'
----

. Validate the node configuration on the new host.
+
`sudo storagegrid node validate DC1-S3`
+
Example output:
+
----
Confirming existence of node DC1-S3... PASSED
Checking configuration file /etc/storagegrid/nodes/DC1-S3.conf for node DC1-S3... PASSED
Checking for duplication of unique values... PASSED
----

. If any validation errors occur, address them before starting the migrated node.
+
For troubleshooting information, see the StorageGRID link:../swnodes/index.html[installation instructions] for your Linux operating system.

## Start migrated node

After you validate the migrated node, you start the node by running a command on the _target host_.

.Steps

. Start the node on the new host.
+
`sudo storagegrid node start DC1-S3`

. Sign in to the Grid Manager and verify that the status of the node is green with no alert.
+
CAUTION: Verifying that the status of the node is green ensures that the migrated node has fully restarted and rejoined the grid. If the status is not green, don't migrate any additional nodes so that you will not have more than one node out of service.

. If you are unable to access the Grid Manager, wait for 10 minutes, then run the following command:
+
`sudo storagegrid node status _node-name`
+
Confirm that the migrated node has a Run-State of Running.

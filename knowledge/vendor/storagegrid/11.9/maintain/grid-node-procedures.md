---
id: "storagegrid-119-f9afcaf877df3b56"
title: "StorageGRID 11.9 Node maintenance procedures"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/grid-node-procedures.adoc"
source_sha256: "ca44384bc73ff32d839332dd70e7fb926ab2ebe3a001611d241becb5e1f4cf94"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/grid-node-procedures.adoc"
---

# StorageGRID 11.9 Node maintenance procedures

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/grid-node-procedures.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Node maintenance procedures
:icons: font
:imagesdir: ../media/

[.lead]
You might need to perform maintenance procedures related to specific grid nodes or node services.

Server Manager procedures::
Server Manager runs on every grid node to supervise the starting and stopping of services and to ensure that services gracefully join and leave the StorageGRID system. Server Manager also monitors the services on every grid node and will automatically attempt to restart any services that report faults.
+
To perform Server Manager procedures, you typically need to access the node's command line.
+
NOTE: You should access Server Manager only if technical support has directed you to do so.
+
NOTE: You must close the current command shell session and log out after you are finished with Server Manager. Enter: `exit`

Node reboot, shut down, and power procedures::

You use these procedures to reboot one or more nodes, to shut down and restart nodes, or to power nodes off and power them back on. 

Port remap procedures::

You can use the port remap procedures to remove the port remaps from a node, for example, if you want to configure a load balancer endpoint using a port that was previously remapped.

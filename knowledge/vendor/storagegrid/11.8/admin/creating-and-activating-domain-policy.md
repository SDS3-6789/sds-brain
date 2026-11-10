---
id: "storagegrid-118-9310cea0f9ddfd75"
title: "StorageGRID 11.8 Create and activate the domain policy"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/creating-and-activating-domain-policy.adoc"
source_sha256: "d6430213411bf4cc06e40dfa689aa60efdbcfd2ebda27fcf57dd1015fd4c6938"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/creating-and-activating-domain-policy.adoc"
---

# StorageGRID 11.8 Create and activate the domain policy

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/creating-and-activating-domain-policy.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Create and activate the domain policy
:icons: font
:imagesdir: ../media/

[.lead]
You must create a domain policy and then activate it to configure the TSM server to save data sent from the Archive Node.

.Steps

. Create a domain policy.
+
`copy domain standard tsm-domain`

. If you aren't using an existing management class, enter one of the following:
+
`define policyset tsm-domain standard`
+
`define mgmtclass tsm-domain standard _default_`
+
`_default_` is the default management class for the deployment.

. Create a copygroup to the appropriate storage pool. Enter (on one line):
+
`define copygroup tsm-domain standard _default_ type=archive destination=SGWSDiskPool retinit=event retmin=0 retver=0`
+
`_default_` is the default Management Class for the Archive Node. The values of `retinit`, `retmin`, and `retver` have been chosen to reflect the retention behavior currently used by the Archive Node
+
NOTE: Don't set `retinit` to `retinit=create`. Setting `retinit=create` blocks the Archive Node from deleting content, because retention events are used to remove content from the TSM server.

. Assign the management class to be the default.
+
`assign defmgmtclass _tsm-domain_ standard _default_`

. Set the new policy set as active.
+
`activate policyset tsm-domain standard`
+
Ignore the "no backup copy group" warning that appears when you enter the activate command.

. Register a node to use the new policy set on the TSM server. On the TSM server, enter (on one line):
+
`register node arc-user arc-password passexp=0 domain=tsm-domain MAXNUMMP=number-of-sessions`
+
arc-user and arc-password are same client node name and password as you define on the Archive Node, and the value of MAXNUMMP is set to the number of tape drives reserved for Archive Node store sessions.
+
NOTE: By default, registering a node creates an administrative user ID with client owner authority, with the password defined for the node.

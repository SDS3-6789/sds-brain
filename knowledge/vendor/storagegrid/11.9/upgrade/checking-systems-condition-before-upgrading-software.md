---
id: "storagegrid-119-20b0f34368862742"
title: "StorageGRID 11.9 Check the system's condition"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/upgrade/checking-systems-condition-before-upgrading-software.adoc"
source_sha256: "b473aa3adcc554b9de633a31336f3c5377c110591cb0e4e6fecb6c917feaffa1"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "upgrade/checking-systems-condition-before-upgrading-software.adoc"
---

# StorageGRID 11.9 Check the system's condition

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/upgrade/checking-systems-condition-before-upgrading-software.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Check the system's condition
:icons: font
:imagesdir: ../media/

[.lead]
Before upgrading a StorageGRID system, verify the system is ready to accommodate the upgrade. Ensure that the system is running normally and that all grid nodes are operational.

.Steps
. Sign in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
. Check for and resolve any active alerts.

. Confirm that no conflicting grid tasks are active or pending.
 .. Select *SUPPORT* > *Tools* > *Grid topology*.
 .. Select *_site_* > *_primary Admin Node_* > *CMN* > *Grid Tasks* > *Configuration*.
+
Information lifecycle management evaluation (ILME) tasks are the only grid tasks that can run concurrently with the software upgrade.

 .. If any other grid tasks are active or pending, wait for them to finish or release their lock.
+
NOTE: Contact technical support if a task does not finish or release its lock.

. Refer to link:../network/internal-grid-node-communications.html[Internal grid node communications] and link:../network/external-communications.html[External communications] to ensure that all required ports for StorageGRID 11.9 are opened before you upgrade.
+
NOTE: No additional ports are required when upgrading to StorageGRID 11.9.
+
The following required port was added in StorageGRID 11.7. Make sure it's available before you upgrade to StorageGRID 11.9.
+
[cols="1a,2a" options=header] 
|===
| Port| Description

| 18086 
| TCP port used for S3 requests from the StorageGRID load balancer to LDR and the new LDR service.

Before upgrading, confirm that this port is open from all grid nodes to all Storage Nodes.  

Blocking this port will cause S3 service interruptions after upgrade to StorageGRID 11.9.
|===

CAUTION: If you have opened any custom firewall ports, you are notified during the upgrade precheck. You must contact technical support before proceeding with the upgrade.

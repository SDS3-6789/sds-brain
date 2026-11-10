---
id: "storagegrid-118-12de54038bc9ab00"
title: "StorageGRID 11.8 Check system's condition before applying hotfix"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/checking-systems-condition-before-applying-hotfix.adoc"
source_sha256: "a9ec6dfb388534dd1093890d8ee91e6f6fc6d0aebb5e94c0639a4cfd0430fb6d"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/checking-systems-condition-before-applying-hotfix.adoc"
---

# StorageGRID 11.8 Check system's condition before applying hotfix

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/checking-systems-condition-before-applying-hotfix.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Check system's condition before applying hotfix
:icons: font
:imagesdir: ../media/

[.lead]
You must verify the system is ready to accommodate the hotfix.

. Sign in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

. If possible, ensure that the system is running normally and that all grid nodes are connected to the grid.
+
Connected nodes have green check marks image:../media/icon_alert_green_checkmark.png[icon alert green check mark] on the Nodes page.

. Check for and resolve any current alerts, if possible.

. Ensure no other maintenance procedures are in progress, such as an upgrade, recovery, expansion, or decommission procedure.
+
You should wait for any active maintenance procedures to complete before applying a hotfix.
+
You can't apply a StorageGRID hotfix when another maintenance procedure is running. For example, you can't apply a hotfix while a decommission, expansion, or recovery procedure is running.
+
NOTE: If a node or site link:pausing-and-resuming-decommission-process-for-storage-nodes.html[decommission procedure is paused], you can safely apply a hotfix. In addition, you might be able to apply a hotfix during the final stages of a StorageGRID upgrade procedure. See the instructions for link:../upgrade/index.html[upgrading StorageGRID software].

---
id: "storagegrid-119-f9740c39d538f105"
title: "StorageGRID 11.9 Recover from non-primary Admin Node failures"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/recovering-from-non-primary-admin-node-failures.adoc"
source_sha256: "d3876ce9855fdf0d35c514fd6a86d7e05de220914eec8ad04333314537fb684c"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/recovering-from-non-primary-admin-node-failures.adoc"
---

# StorageGRID 11.9 Recover from non-primary Admin Node failures

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/recovering-from-non-primary-admin-node-failures.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Recover from non-primary Admin Node failures
:icons: font
:imagesdir: ../media/

[.lead]
You must complete the following tasks to recover from a non-primary Admin Node failure. One Admin Node hosts the Configuration Management Node (CMN) service and is known as the primary Admin Node. Although you can have multiple Admin Nodes, each StorageGRID system includes only one primary Admin Node. All other Admin Nodes are non-primary Admin Nodes.

Follow these high-level steps to recover a non-primary Admin Node:
 
. link:copying-audit-logs-from-failed-non-primary-admin-node.html[Copy audit logs from the failed non-primary Admin Node]
. link:replacing-non-primary-admin-node.html[Replace the non-primary Admin Node]
. link:selecting-start-recovery-to-configure-non-primary-admin-node.html[Select Start Recovery to configure the non-primary Admin Node]
. link:restoring-audit-log-on-recovered-non-primary-admin-node.html[Restore the audit log on a recovered non-primary Admin Node]
. link:restoring-admin-node-database-non-primary-admin-node.html[Restore the Admin Node database when recovering a non-primary Admin Node]
. link:restoring-prometheus-metrics-non-primary-admin-node.html[Restore Prometheus metrics when recovering a non-primary Admin Node]

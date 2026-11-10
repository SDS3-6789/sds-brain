---
id: "storagegrid-119-629f7df3d67edd96"
title: "StorageGRID 11.9 Recover from primary Admin Node failures"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/recovering-from-primary-admin-node-failures.adoc"
source_sha256: "0446f58bdd3a1003f30dc2ce91839d8ce38e420d9cc33c9b44f336fe04b5f875"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/recovering-from-primary-admin-node-failures.adoc"
---

# StorageGRID 11.9 Recover from primary Admin Node failures

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/recovering-from-primary-admin-node-failures.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Recover from primary Admin Node failures
:icons: font
:imagesdir: ../media/

[.lead]
You must complete a specific set of tasks to recover from a primary Admin Node failure. The primary Admin Node hosts the Configuration Management Node (CMN) service for the grid.

CAUTION: You must repair or replace a failed primary Admin Node promptly or the grid might lose its ability to ingest new objects. The exact time period depends on your rate of object ingest: if you need a more accurate assessment of the time frame for your grid, contact technical support.

The Configuration Management Node (CMN) service on the primary Admin Node is responsible for issuing blocks of object identifiers for the grid. These identifiers are assigned to objects as they are ingested. New objects can't be ingested unless there are identifiers available. Object ingest can continue while the CMN is unavailable because approximately one month's supply of identifiers is cached in the grid. However, after cached identifiers are exhausted, no new objects can be added.

Follow these high-level steps to recover a primary Admin Node:

. link:copying-audit-logs-from-failed-primary-admin-node.html[Copy audit logs from failed primary Admin Node]
. link:replacing-primary-admin-node.html[Replace the primary Admin Node]
. link:configuring-replacement-primary-admin-node.html[Configure the replacement primary Admin Node]
. link:assess-hotfix-requirement-during-primary-admin-node-recovery.html[Determine if there is a hotfix requirement for the recovered primary Admin Node]
. link:restoring-audit-log-on-recovered-primary-admin-node.html[Restore the audit log on the recovered primary Admin Node]
. link:restoring-admin-node-database-primary-admin-node.html[Restore the Admin Node database when recovering a primary Admin Node]
. link:restoring-prometheus-metrics-primary-admin-node.html[Restore Prometheus metrics when recovering a primary Admin Node]

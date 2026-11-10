---
id: "storagegrid-120-de922ca2ebaf694f"
title: "StorageGRID 12.0 Upgrade StorageGRID software"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/upgrade/index.adoc"
source_sha256: "6cf96e20ca075f994086a01ce7a80c1527ef0a0406c719fb17d316ff8d1d6090"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "upgrade/index.adoc"
---

# StorageGRID 12.0 Upgrade StorageGRID software

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/upgrade/index.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Upgrade StorageGRID software
:icons: font
:imagesdir: ../media/

[.lead]
Use these instructions to upgrade a StorageGRID system to a new release.

When you perform the upgrade, all nodes in your StorageGRID system are upgraded.

CAUTION: Do not start the upgrade if you urgently need to expand your storage to increase capacity (if your storage is almost full). Complete the upgrade procedure in a timely manner. If a recovery is required, contact technical support.

## Before you upgrade
Review these topics to learn about the new features and enhancements in StorageGRID 12.0, determine whether any features have been deprecated or removed, and find out about changes to StorageGRID APIs.

* link:how-your-system-is-affected-during-upgrade.html[How your system is affected during the upgrade]
* link:../release-notes/whats-new.html[What's new in StorageGRID 12.0]
* link:../release-notes/removed-or-deprecated-features.html[Removed or deprecated features]
* link:../release-notes/changes-to-grid-management-api.html[Changes to the Grid Management API]
* link:../release-notes/changes-to-tenant-management-api.html[Changes to the Tenant Management API]

// 2025 APR 16, SGWS-34284

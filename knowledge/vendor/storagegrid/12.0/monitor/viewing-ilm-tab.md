---
id: "storagegrid-120-21541310ff9e80cd"
title: "StorageGRID 12.0 View the StorageGRID ILM tab"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/viewing-ilm-tab.adoc"
source_sha256: "68e4ca51fee519cfdba8bcbeee14d716371d34dbe7c42721fd340a044b4eaadf"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/viewing-ilm-tab.adoc"
---

# StorageGRID 12.0 View the StorageGRID ILM tab

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/monitor/viewing-ilm-tab.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View the StorageGRID ILM tab
:icons: font
:imagesdir: ../media/

[.lead]
The ILM tab provides information about information lifecycle management (ILM) operations.

The ILM tab is shown for each Storage Node, each site, and the entire grid. For each site and the grid, the ILM tab shows a graph of the ILM queue over time. For the grid, this tab also provides the estimated time to complete a full ILM scan of all objects.

For Storage Nodes, the ILM tab provides details about ILM evaluation and background verification for erasure-coded objects.

image:nodes_page_ilm_tab.png[Nodes page ILM tab]

.Related information

* link:monitoring-information-lifecycle-management.html[Monitor information lifecycle management]

* link:../admin/index.html[Administer StorageGRID]

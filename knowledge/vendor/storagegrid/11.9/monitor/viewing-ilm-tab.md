---
id: "storagegrid-119-21541310ff9e80cd"
title: "StorageGRID 11.9 View the ILM tab"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/viewing-ilm-tab.adoc"
source_sha256: "dcfb1971cbca1a30d52edab9486699f1b188e58ec174501a2e4c523d257c32c2"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/viewing-ilm-tab.adoc"
---

# StorageGRID 11.9 View the ILM tab

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/viewing-ilm-tab.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View the ILM tab
:icons: font
:imagesdir: ../media/

[.lead]
The ILM tab provides information about information lifecycle management (ILM) operations.

The ILM tab is shown for each Storage Node, each site, and the entire grid. For each site and the grid, the ILM tab shows a graph of the ILM queue over time. For the grid, this tab also provides the estimated time to complete a full ILM scan of all objects.

For Storage Nodes, the ILM tab provides details about ILM evaluation and background verification for erasure-coded objects.

image::../media/nodes_page_ilm_tab.png[Nodes page ILM tab]

.Related information

* link:monitoring-information-lifecycle-management.html[Monitor information lifecycle management]

* link:../admin/index.html[Administer StorageGRID]

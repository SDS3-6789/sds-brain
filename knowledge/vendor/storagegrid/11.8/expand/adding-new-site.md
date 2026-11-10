---
id: "storagegrid-118-9d772bd20c8ce377"
title: "StorageGRID 11.8 Add a new site"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/adding-new-site.adoc"
source_sha256: "f5f768a7b2c8f1a3823ba88fe6a48e770dc5bc5e888d1b77d96695517c1872a7"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "expand/adding-new-site.adoc"
---

# StorageGRID 11.8 Add a new site

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/expand/adding-new-site.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Add a new site
:icons: font
:imagesdir: ../media/

[.lead]
You can expand your StorageGRID system by adding a new site.

## Guidelines for adding a site

Before adding a site, review the following requirements and limitations:

* You can only add one site per expansion operation.
* You can't add grid nodes to an existing site as part of the same expansion.
* All sites must include at least three Storage Nodes.
* Adding a new site does not automatically increase the number of objects you can store. The total object capacity of a grid depends on the amount of available storage, the ILM policy, and the metadata capacity at each site.
* When sizing a new site, you must ensure that it includes enough metadata capacity.
+
StorageGRID keeps a copy of all object metadata at every site. When you add a new site, you must ensure that it includes enough metadata capacity for the existing object metadata and enough metadata capacity for growth.
+
For more information, see the following:

** link:../admin/managing-object-metadata-storage.html[Manage object metadata storage]

** link:../monitor/monitoring-storage-capacity.html#monitor-object-metadata-capacity-for-each-storage-node[Monitor object metadata capacity for each Storage Node]

* You must consider the available network bandwidth between sites, and the level of network latency. Metadata updates are continually replicated between sites even if all objects are stored only at the site where they are ingested.
* Because your StorageGRID system remains operational during the expansion, you must review ILM rules before starting the expansion procedure. You must ensure that object copies aren't stored to the new site until the expansion procedure is complete.
+
For example, before you begin the expansion, determine if any rules use the default storage pool (All Storage Nodes). If they do, you must create a new storage pool that contains the existing Storage Nodes and update your ILM rules to use the new storage pool. Otherwise, objects will be copied to the new site as soon as the first node at that site becomes active.
+
For more information about changing ILM when adding a new site, see the link:../ilm/example-6-changing-ilm-policy.html[example for changing an ILM policy].

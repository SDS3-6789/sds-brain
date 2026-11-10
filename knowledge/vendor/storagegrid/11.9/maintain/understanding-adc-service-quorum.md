---
id: "storagegrid-119-dd18e10e83c42ab9"
title: "StorageGRID 11.9 What is the ADC quorum?"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/understanding-adc-service-quorum.adoc"
source_sha256: "97143a462bc563b002d630ad685c014962dbeb7a6589cd3a8739afb5b78c7bbd"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/understanding-adc-service-quorum.adoc"
---

# StorageGRID 11.9 What is the ADC quorum?

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/understanding-adc-service-quorum.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# What is the ADC quorum?
:icons: font
:imagesdir: ../media/

[.lead]
You might not be able to decommission certain Storage Nodes at a site if too few Administrative Domain Controller (ADC) services would remain after the decommissioning.

The ADC service, which is found on some Storage Nodes, maintains grid topology information and provides configuration services to the grid. The StorageGRID system requires a quorum of ADC services to be available at each site and at all times.

You can't decommission a Storage Node if removing the node would cause the ADC quorum to no longer be met. To satisfy the ADC quorum during a decommissioning, a minimum of three Storage Nodes at each site must have the ADC service. If a site has more than three Storage Nodes with the ADC service, a simple majority of those nodes must remain available after the decommissioning: `((0.5 * _Storage Nodes with ADC_) + 1)`

CAUTION: Use caution when you decommission Storage Nodes in a grid containing software-based metadata-only nodes. If you decommission all nodes configured to store _both_ objects and metadata, the ability to store objects is removed from the grid. See link:../primer/what-storage-node-is.html#types-of-storage-nodes[Types of Storage Nodes] for more information about metadata-only Storage Nodes.

For example, suppose a site currently includes six Storage Nodes with ADC services and you want to decommission three Storage Nodes. Because of the ADC quorum requirement, you must complete two decommission procedures, as follows:

* In the first decommission procedure, you must ensure that four Storage Nodes with ADC services remain available: `((0.5 * 6) + 1)`. This means that you can only decommission two Storage Nodes initially.
* In the second decommission procedure, you can remove the third Storage Node because the ADC quorum now only requires three ADC services to remain available: `((0.5 * 4) + 1)`.

If you need to decommission a Storage Node but are unable to because of the ADC quorum requirement, add a new Storage Node in an link:../expand/index.html[expansion] and specify that it should have an ADC service. Then, decommission the existing Storage Node.

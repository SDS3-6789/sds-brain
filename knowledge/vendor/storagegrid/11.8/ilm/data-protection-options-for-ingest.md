---
id: "storagegrid-118-f804a01750496408"
title: "StorageGRID 11.8 Ingest options"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/data-protection-options-for-ingest.adoc"
source_sha256: "d38311c87daf4e03bc65d3cd6dcd0ca21acad58a02ddef6a886b0db65ec4e194"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/data-protection-options-for-ingest.adoc"
---

# StorageGRID 11.8 Ingest options

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/data-protection-options-for-ingest.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Ingest options
:icons: font
:imagesdir: ../media/

[.lead]
When you create an ILM rule, you specify one of three options for protecting objects at ingest: Dual commit, Strict, or Balanced.

Depending on your choice, StorageGRID makes interim copies and queues the objects for ILM evaluation later, or it uses synchronous placement and immediately makes copies to meet ILM requirements.

## Flowchart of ingest options

The flowchart shows what happens when objects are matched by an ILM rule that uses each of the three ingest options.

image::../media/ingest_object_lifecycle.png[Diagram showing how object ingest occurs for each ingest option]

## Dual commit

When you select the Dual commit option, StorageGRID immediately makes interim object copies on two different Storage Nodes and returns an "ingest successful" message to the client. The object is queued for ILM evaluation, and copies that meet the rule's placement instructions are made later. If the ILM policy can't be processed immediately after the dual commit, site-loss protection could take time to achieve.

Use the Dual commit option in either of these cases:

* You are using multi-site ILM rules and client ingest latency is your primary consideration. When using Dual commit, you must ensure your grid can perform the additional work of creating and removing the dual-commit copies if they don't satisfy ILM. Specifically:
 ** The load on the grid must be low enough to prevent an ILM backlog.
 ** The grid must have excess hardware resources (IOPS, CPU, memory, network bandwidth, and so on).
* You are using multi-site ILM rules and the WAN connection between the sites usually has high latency or limited bandwidth. In this scenario, using the Dual commit option can help prevent client timeouts. Before choosing the Dual commit option, you should test the client application with realistic workloads.

## Balanced (default)

When you select the Balanced option, StorageGRID also uses synchronous placement on ingest and immediately makes all copies specified in the rule's placement instructions. In contrast with the Strict option, if StorageGRID can't immediately make all copies, it uses Dual commit instead. If the ILM policy uses placements on multiple sites and immediate site-loss protection can't be achieved, the *ILM placement unachievable* alert is triggered.

Use the Balanced option to achieve the best combination of data protection, grid performance, and ingest success. Balanced is the default option in the Create ILM rule wizard.

## Strict

When you select the Strict option, StorageGRID uses synchronous placement on ingest and immediately makes all object copies specified in the rule's placement instructions. Ingest fails if StorageGRID can't create all copies, for example, because a required storage location is temporarily unavailable. The client must retry the operation.

Use the Strict option if you have an operational or regulatory requirement to immediately store objects only in the locations outlined in the ILM rule. For example, to satisfy a regulatory requirement, you might need to use the Strict option and a Location Constraint advanced filter to guarantee that objects are never stored at certain data centers.

See link:example-5-ilm-rules-and-policy-for-strict-ingest-behavior.html[Example 5: ILM rules and policy for Strict ingest behavior].

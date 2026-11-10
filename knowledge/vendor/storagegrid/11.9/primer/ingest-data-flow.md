---
id: "storagegrid-119-c7b573d20c3b5827"
title: "StorageGRID 11.9 Ingest data flow"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/primer/ingest-data-flow.adoc"
source_sha256: "48bcbdca7aeb7347f0443d8d9c4a6b29e371076a4d38eb70f536b77eaf59ded7"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "primer/ingest-data-flow.adoc"
---

# StorageGRID 11.9 Ingest data flow

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/primer/ingest-data-flow.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Ingest data flow
:icons: font
:imagesdir: ../media/

[.lead]
An ingest, or save, operation consists of a defined data flow between the client and the StorageGRID system.

## Data flow

When a client ingests an object to the StorageGRID system, the LDR service on Storage Nodes processes the request and stores the metadata and data to disk.

image::../media/ingest_data_flow.png[Ingest with synchronous placement]

. The client application creates the object and sends it to the StorageGRID system through an HTTP PUT request.
. The object is evaluated against the system's ILM policy.
. The LDR service saves the object data as a replicated copy or as an erasure-coded copy. (The diagram shows a simplified version of storing a replicated copy to disk.)
. The LDR service sends the object metadata to the metadata store.
. The metadata store saves the object metadata to disk.
. The metadata store propagates copies of object metadata to other Storage Nodes. These copies are also saved to disk.
. The LDR service returns an HTTP 200 OK response to the client to acknowledge that the object has been ingested.

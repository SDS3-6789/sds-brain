---
id: "storagegrid-120-c7b573d20c3b5827"
title: "StorageGRID 12.0 How StorageGRID handles object ingest"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/primer/ingest-data-flow.adoc"
source_sha256: "6cc6496b4cc86349ba3f7d9deb624cf654a5c7c775622fc3680d71a3e814f0b0"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "primer/ingest-data-flow.adoc"
---

# StorageGRID 12.0 How StorageGRID handles object ingest

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/primer/ingest-data-flow.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# How StorageGRID handles object ingest
:icons: font
:imagesdir: ../media/

[.lead]
An ingest, or save, operation consists of a defined data flow between the client and the StorageGRID system.

## Data flow

When a client ingests an object to the StorageGRID system, the LDR service on Storage Nodes processes the request and stores the metadata and data to disk.

image:ingest_data_flow.png[Ingest with synchronous placement]

. The client application creates the object and sends it to the StorageGRID system through an HTTP PUT request.
. The object is evaluated against the system's ILM policy.
. The LDR service saves the object data as a replicated copy or as an erasure-coded copy. (The diagram shows a simplified version of storing a replicated copy to disk.)
. The LDR service sends the object metadata to the metadata store.
. The metadata store saves the object metadata to disk.
. The metadata store propagates copies of object metadata to other Storage Nodes. These copies are also saved to disk.
. The LDR service returns an HTTP 200 OK response to the client to acknowledge that the object has been ingested.

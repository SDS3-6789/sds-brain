---
id: "storagegrid-120-484112eef80eced4"
title: "StorageGRID 12.0 consistency descriptions"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/_include/consistency-descriptions.adoc"
source_sha256: "e62157e6d4630ca1a0f2b3a1ec1d5d17e7133426e52cc4f73c3aca1aee47590d"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/consistency-descriptions.adoc"
---

# StorageGRID 12.0 consistency descriptions

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/_include/consistency-descriptions.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

// used in /s3/consistency.adoc and /ilm/advantages-disadvantages-of-ingest-options.html
* *All*: All nodes receive object metadata immediately or the request will fail.
* *Strong-global*: Guarantees read-after-write consistency for all client requests across all sites. When Quorum semantics are configured, the following behaviors apply:
** Allows for site failure tolerance for client requests when grids have three or more sites. Two-site grids won't have site failure tolerance.
** The following S3 operations won't succeed with one site down:
*** DeleteBucketEncryption
*** PutBucketBranch
*** PutBucketEncryption
*** PutBucketVersioning
*** PutObjectLegalHold
*** PutObjectLockConfiguration
*** PutObjectRetention

+
If needed, you can https://kb.netapp.com/hybrid/StorageGRID/Object_Mgmt/Configuring_StorageGRID_quorum_semantics_for_strong-global_consistency[configure StorageGRID Quorum semantics for strong-global consistency^].
* *Strong-site*: Object metadata is immediately distributed to other nodes at the site. Guarantees read-after-write consistency for all client requests within a site.
* *Read-after-new-write*: Provides read-after-write consistency for new objects and eventual consistency for object updates. Offers high availability and data protection guarantees. Recommended for most cases.
* *Available*: Provides eventual consistency for both new objects and object updates. For S3 buckets, use only as required (for example, for a bucket that contains log values that are rarely read, or for HEAD or GET operations on keys that don't exist). Not supported for S3 FabricPool buckets.

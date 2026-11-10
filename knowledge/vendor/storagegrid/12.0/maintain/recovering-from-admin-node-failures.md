---
id: "storagegrid-120-03006294acb072c8"
title: "StorageGRID 12.0 Primary or non-primary Admin Node recovery in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/recovering-from-admin-node-failures.adoc"
source_sha256: "60bf3044c14c93d32ec9bb4066cf3ba3a23facd6e3ed77222934fcfd7871b47d"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/recovering-from-admin-node-failures.adoc"
---

# StorageGRID 12.0 Primary or non-primary Admin Node recovery in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/recovering-from-admin-node-failures.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Primary or non-primary Admin Node recovery in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
The recovery process for an Admin Node depends on whether it is the primary Admin Node or a non-primary Admin Node.

The high-level steps for recovering a primary or non-primary Admin Node are the same, although the details of the steps differ.

Always follow the correct recovery procedure for the Admin Node you are recovering. The procedures look the same at a high level, but differ in the details.

.Choices

* link:recovering-from-primary-admin-node-failures.html[Recover from primary Admin Node failures]
* link:recovering-from-non-primary-admin-node-failures.html[Recover from non-primary Admin Node failures]

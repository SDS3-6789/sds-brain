---
id: "storagegrid-120-aae54355146fd41e"
title: "StorageGRID 12.0 Per-site delivery of StorageGRID platform services messages"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/per-site-delivery-of-platform-services-messages.adoc"
source_sha256: "0fa81bbc2f4478bb42f7478ebee9b0291220c0a9c021bd5b92b05496d817f064"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/per-site-delivery-of-platform-services-messages.adoc"
---

# StorageGRID 12.0 Per-site delivery of StorageGRID platform services messages

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/per-site-delivery-of-platform-services-messages.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Per-site delivery of StorageGRID platform services messages
:icons: font
:imagesdir: ../media/

[.lead]
All platform services operations are performed on a per-site basis.

That is, if a tenant uses a client to perform an S3 API Create operation on an object by connecting to a Gateway Node at Data Center Site 1, the notification about that action is triggered and sent from Data Center Site 1.

image:notification_multiple_sites.gif[Diagram showing that action on object at site 1 triggers notification from site 1]

If the client subsequently performs an S3 API Delete operation on that same object from Data Center Site 2, the notification about the delete action is triggered and sent from Data Center Site 2.

image:notifications_site_2.gif[diagram showing action on object from site 2 triggers notifications from site 2]

Make sure that the networking at each site is configured such that platform services messages can be delivered to their destinations.

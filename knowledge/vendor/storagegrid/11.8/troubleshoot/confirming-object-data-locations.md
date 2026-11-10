---
id: "storagegrid-118-7c731dd1e415acf7"
title: "StorageGRID 11.8 Confirm object data locations"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/confirming-object-data-locations.adoc"
source_sha256: "431da2a79211d22c89d0b7f751e5a3126ca7a6d5218330cdcca7c6576a031d1d"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "troubleshoot/confirming-object-data-locations.adoc"
---

# StorageGRID 11.8 Confirm object data locations

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/confirming-object-data-locations.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Confirm object data locations
:icons: font
:imagesdir: ../media/

[.lead]
Depending on the problem, you might want to link:../audit/object-ingest-transactions.html[confirm where object data is being stored]. For example, you might want to verify that the ILM policy is performing as expected and object data is being stored where intended.

.Before you begin
* You must have an object identifier, which can be one of:
 ** *UUID*: The object's Universally Unique Identifier. Enter the UUID in all uppercase.
 ** *CBID*: The object's unique identifier within StorageGRID . You can obtain an object's CBID from the audit log. Enter the CBID in all uppercase.
 ** *S3 bucket and object key*: When an object is ingested through the link:../s3/operations-on-objects.html[S3 interface], the client application uses a bucket and object key combination to store and identify the object.
 ** *Swift container and object name*: When an object is ingested through the link:../swift/object-operations.html[Swift interface], the client application uses a container and object name combination to store and identify the object.

.Steps
. Select *ILM* > *Object metadata lookup*.
. Type the object's identifier in the *Identifier* field.
+
You can enter a UUID, CBID, S3 bucket/object-key, or Swift container/object-name.

. If you want to look up a specific version of the object, enter the version ID (optional).
+
image::../media/object_lookup.png[Object Lookup page]

. Select *Look Up*.
+
The link:../ilm/verifying-ilm-policy-with-object-metadata-lookup.html[object metadata lookup results] appear. This page lists the following types of information:

 ** System metadata, including the object ID (UUID), the version ID (optional), the object name, the name of the container, the tenant account name or ID, the logical size of the object, the date and time the object was first created, and the date and time the object was last modified.
 ** Any custom user metadata key-value pairs associated with the object.
 ** For S3 objects, any object tag key-value pairs associated with the object.
 ** For replicated object copies, the current storage location of each copy.
 ** For erasure-coded object copies, the current storage location of each fragment.
 ** For object copies in a Cloud Storage Pool, the location of the object, including the name of the external bucket and the object's unique identifier.
 ** For segmented objects and multipart objects, a list of object segments including segment identifiers and data sizes. For objects with more than 100 segments, only the first 100 segments are shown.
 ** All object metadata in the unprocessed, internal storage format. This raw metadata includes internal system metadata that is not guaranteed to persist from release to release.
+
The following example shows the object metadata lookup results for an S3 test object that is stored as two replicated copies.

+
image::../media/object_lookup_results.png[Object Lookup Results]

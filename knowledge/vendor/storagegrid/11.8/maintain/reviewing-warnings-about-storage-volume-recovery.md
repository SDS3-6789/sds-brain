---
id: "storagegrid-118-c0fb5894862d9aa7"
title: "StorageGRID 11.8 Warnings for storage volume recovery"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/reviewing-warnings-about-storage-volume-recovery.adoc"
source_sha256: "88b9e6f51c2d19fa5b698f181622dc189a02f43b69e58730f1ca20e58a8c2282"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/reviewing-warnings-about-storage-volume-recovery.adoc"
---

# StorageGRID 11.8 Warnings for storage volume recovery

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/reviewing-warnings-about-storage-volume-recovery.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Warnings for storage volume recovery
:icons: font
:imagesdir: ../media/

[.lead]
Before recovering failed storage volumes for a Storage Node, review the following warnings.

The storage volumes (or rangedbs) in a Storage Node are identified by a hexadecimal number, which is known as the volume ID. For example, 0000 is the first volume and 000F is the sixteenth volume. The first object store (volume 0) on each Storage Node uses up to 4 TB of space for object metadata and Cassandra database operations; any remaining space on that volume is used for object data. All other storage volumes are used exclusively for object data.

If volume 0 fails and needs to be recovered, the Cassandra database might be rebuilt as part of the volume recovery procedure. Cassandra might also be rebuilt in the following circumstances:

* A Storage Node is brought back online after having been offline for more than 15 days.
* The system drive and one or more storage volumes fails and is recovered.

When Cassandra is rebuilt, the system uses information from other Storage Nodes. If too many Storage Nodes are offline, some Cassandra data might not be available. If Cassandra has been rebuilt recently, Cassandra data might not yet be consistent across the grid. Data loss can occur if Cassandra is rebuilt when too many Storage Nodes are offline or if two or more Storage Nodes are rebuilt within 15 days of each other.

CAUTION: If more than one Storage Node has failed (or is offline), contact technical support. Don't perform the following recovery procedure. Data loss could occur.

CAUTION: If this is the second Storage Node failure in less than 15 days after a Storage Node failure or recovery, contact technical support. Rebuilding Cassandra on two or more Storage Nodes within 15 days can result in data loss.

NOTE: If more than one Storage Node at a site has failed, a site recovery procedure might be required. See link:how-site-recovery-is-performed-by-technical-support.html[How technical support recovers a site].

CAUTION: If ILM rules are configured to store only one replicated copy and the copy exists on a storage volume that has failed, you will not be able to recover the object.

NOTE: If you encounter a Services: Status - Cassandra (SVST) alarm during recovery, see link:../maintain/recovering-failed-storage-volumes-and-rebuilding-cassandra-database.html[Recover failed storage volumes and rebuild Cassandra database]. After Cassandra is rebuilt, alarms should clear. If alarms don't clear, contact technical support.

.Related information

link:warnings-and-considerations-for-grid-node-recovery.html[Warnings and considerations for grid node recovery]

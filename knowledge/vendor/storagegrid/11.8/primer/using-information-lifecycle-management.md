---
id: "storagegrid-118-4aac345bb5241f99"
title: "StorageGRID 11.8 Use information lifecycle management"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/primer/using-information-lifecycle-management.adoc"
source_sha256: "6e87f0f805a06387ae27037fc4618c3941e9e9423ecd70806c141b4ef7ad033a"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "primer/using-information-lifecycle-management.adoc"
---

# StorageGRID 11.8 Use information lifecycle management

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/primer/using-information-lifecycle-management.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Use information lifecycle management
:icons: font
:imagesdir: ../media/

[.lead]
You use information lifecycle management (ILM) to control the placement, duration, and ingest behavior for all objects in your StorageGRID system. ILM rules determine how StorageGRID stores objects over time. You configure one or more ILM rules and then add them to an ILM policy.

A grid has only one active policy at a time. A policy can contain multiple rules.

ILM rules define:

* Which objects should be stored. A rule can apply to all objects, or you can specify filters to identify which objects a rule applies to. For example, a rule can apply only to objects associated with certain tenant accounts, specific S3 buckets or Swift containers, or specific metadata values.
* The storage type and location. Objects can be stored on Storage Nodes, in Cloud Storage Pools, or on Archive Nodes.
* The type of object copies made. Copies can be replicated or erasure-coded.
* For replicated copies, the number of copies made.
* For erasure-coded copies, the erasure-coding scheme used.
* The changes over time to an object's storage location and type of copies.
* How object data is protected as objects are ingested into the grid (synchronous placement or dual commit).

Note that object metadata is not managed by ILM rules. Instead, object metadata is stored in a Cassandra database in what is known as a metadata store. Three copies of object metadata are automatically maintained at each site to protect the data from loss.

## Example ILM rule

As an example, an ILM rule could specify the following:

* Apply only to the objects belonging to Tenant A.
* Make two replicated copies of those objects and store each copy at a different site.
* Retain the two copies "forever," which means that StorageGRID will not automatically delete them. Instead, StorageGRID will retain these objects until they are deleted by a client delete request or by the expiration of a bucket lifecycle.
* Use the Balanced option for ingest behavior: the two-site placement instruction is applied as soon as Tenant A saves an object to StorageGRID, unless it is not possible to immediately make both required copies.
+
For example, if Site 2 is unreachable when Tenant A saves an object, StorageGRID will make two interim copies on Storage Nodes at Site 1. As soon as Site 2 becomes available, StorageGRID will make the required copy at that site.

## How an ILM policy evaluates objects

The active ILM policies for your StorageGRID system control the placement, duration, and ingest behavior of all objects.

When clients save objects to StorageGRID, the objects are evaluated against the ordered set of ILM rules in the active policy, as follows:

. If the filters for the first rule in the policy match an object, the object is ingested according to that rule's ingest behavior and stored according to that rule's placement instructions.
. If the filters for the first rule don't match the object, the object is evaluated against each subsequent rule in the policy until a match is made.
. If no rules match an object, the ingest behavior and placement instructions for the default rule in the policy are applied. The default rule is the last rule in a policy and can't use any filters. It must apply to all tenants, all buckets, and all object versions.

## Example ILM policy

As an example, an ILM policy could contain three ILM rules that specify the following:

* *Rule 1: Replicated copies for Tenant A*
** Match all objects belonging to Tenant A.
** Store these objects as three replicated copies at three sites.
** Objects belonging to other tenants aren't matched by Rule 1, so they are evaluated against Rule 2.

* *Rule 2: Erasure coding for objects greater than 1 MB*
** Match all objects from other tenants, but only if they are greater than 1 MB. These larger objects are stored using 6+3 erasure coding at three sites.
** Does not match objects 1 MB or smaller, so these objects are evaluated against Rule 3.

* *Rule 3: 2 copies 2 data centers* (default)
** Is the last and default rule in the policy. Does not use filters.
** Make two replicated copies of all objects not matched by Rule 1 or Rule 2 (objects not belonging to Tenant A that are 1 MB or smaller).

image::../media/ilm_policy_and_rules.png[ILM Policy and Rules]

.Related information

* link:../ilm/index.html[Manage objects with ILM]

---
id: "storagegrid-120-0d9b77593e38c158"
title: "StorageGRID 12.0 ILM rules and policy for basic object protection and retention in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/example-1-ilm-rules-and-policy-for-object-storage.adoc"
source_sha256: "7ae9d5002ab6f478d6d59320b04b25315473a503fac301784bbdac3357187208"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/example-1-ilm-rules-and-policy-for-object-storage.adoc"
---

# StorageGRID 12.0 ILM rules and policy for basic object protection and retention in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/ilm/example-1-ilm-rules-and-policy-for-object-storage.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# ILM rules and policy for basic object protection and retention in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
You can use the following example rules and policy as a starting point when defining an ILM policy to meet your object protection and retention requirements.

CAUTION: The following ILM rules and policy are only examples. There are many ways to configure ILM rules. Before activating a new policy, simulate it to confirm it will work as intended to protect content from loss.

## ILM rule 1 for example 1: Copy object data to two sites

This example ILM rule copies object data to storage pools in two sites.

[cols="1a,2a" options="header"]
|===
| Rule definition| Example value
| One-site storage pools
| Two storage pools, each containing different sites, named Site 1 and Site 2.

| Rule name
| Two Copies Two Sites

| Reference time
| Ingest time

| Placements
| On Day 0 to forever, keep one replicated copy at Site 1 and one replicated copy at Site 2.
|===

The Rule analysis section of the Retention diagram states:

* StorageGRID site-loss protection will apply for the duration of this rule.
* Objects processed by this rule will not be deleted by ILM.

image:ilm_rule_two_copies_two_data_centers.png[ILM rule 1 for example 1: Copy object data to two sites]

## ILM rule 2 for example 1: Erasure-coding profile with bucket matching

This example ILM rule uses an erasure-coding profile and an S3 bucket to determine where and how long the object is stored.

[cols="1a,2a" options="header"]
|===
| Rule definition| Example value
|  Storage pool with multiple sites
|
* One storage pool across three sites (Sites 1, 2, 3)
* Use 6+3 erasure-coding scheme

| Rule name
| S3 Bucket finance-records

| Reference time
| Ingest time

| Placements
| For objects in the S3 bucket named finance-records, create one erasure-coded copy in the pool specified by the erasure-coding profile. Keep this copy forever.
|===

image:ilm_rule_ec_for_s3_bucket_finance_records.png[ILM rule 2 for example 1: erasure-coding profile with bucket matching]

## ILM policy for example 1

In practice, most ILM policies are simple, even though the StorageGRID system allows you to design sophisticated and complex ILM policies.

A typical ILM policy for a multi-site grid might include ILM rules such as the following:

* At ingest, store all objects belonging to the S3 bucket named `finance-records` in a storage pool that contains three sites. Use 6+3 erasure coding.
* If an object does not match the first ILM rule, use the policy's default ILM rule, Two Copies Two Data Centers, to store one copy of that object in Site 1, and one copy in Site 2.
+
image:policy_1_configured_policy.png[ILM policy for example 1]

.Related information

* link:ilm-policy-overview.html[Use ILM policies]
* link:creating-ilm-policy.html[Create ILM policies]

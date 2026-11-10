---
id: "storagegrid-118-9c114d36d3e23d34"
title: "StorageGRID 11.8 Example 2: ILM rules and policy for EC object size filtering"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/example-2-ilm-rules-and-policy-for-ec-object-size-filtering.adoc"
source_sha256: "64a2135dafaaab481772b6f4ebb0858890e210a1b80acba84d620b6761406446"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/example-2-ilm-rules-and-policy-for-ec-object-size-filtering.adoc"
---

# StorageGRID 11.8 Example 2: ILM rules and policy for EC object size filtering

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/example-2-ilm-rules-and-policy-for-ec-object-size-filtering.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Example 2: ILM rules and policy for EC object size filtering
:icons: font
:imagesdir: ../media/

[.lead]
You can use the following example rules and policy as starting points to define an ILM policy that filters by object size to meet recommended EC requirements.

CAUTION: The following ILM rules and policy are only examples. There are many ways to configure ILM rules. Before activating a new policy, simulate it to confirm it will work as intended to protect content from loss.

## ILM rule 1 for example 2: Use EC for objects greater than 1 MB 

This example ILM rule erasure codes objects that are greater than 1 MB.

NOTE: Erasure coding is best suited for objects greater than 1 MB. Don't use erasure coding for objects smaller than 200 KB to avoid the overhead of managing very small erasure-coded fragments.

[cols="2a,2a" options="header"]
|===
| Rule definition| Example value

| Rule name
| EC Only Objects > 1 MB

| Reference time
| Ingest time

| Advanced filter for Object size
| Object size greater than 1 MB

| Placements
| Create a 2+1 erasure-coded copy using three sites
|===

image::../media/policy_2_rule_1_ec_objects_adv_filtering.png[ILM rule 1 for example 2: Use EC for all objects greater than 1 MB]

## ILM rule 2 for example 2: Two replicated copies

This example ILM rule creates two replicated copies and does not filter by object size. This rule is the default rule for the policy. Because the first rule filters out all objects greater than 1 MB, this rule only applies to objects that are 1 MB or smaller.

[cols="1a,2a" options="header"]
|===
| Rule definition| Example value

| Rule name
| Two Replicated Copies

| Reference time
| Ingest time

| Advanced filter for Object size
| None

| Placements
| On Day 0 to forever, keep one replicated copy at Site 1 and one replicated copy at Site 2.
|===

## ILM policy for example 2: Use EC for objects greater than 1 MB

This example ILM policy includes two ILM rules:

* The first rule erasure codes all objects that are greater than 1 MB.
* The second (default) ILM rule creates two replicated copies. Because objects greater than 1 MB have been filtered out by rule 1, rule 2 only applies to objects that are 1 MB or smaller.

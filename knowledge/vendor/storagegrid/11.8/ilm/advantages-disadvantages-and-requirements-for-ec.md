---
id: "storagegrid-118-6bdf63f2558eeb1b"
title: "StorageGRID 11.8 Advantages, disadvantages, and requirements for erasure coding"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/advantages-disadvantages-and-requirements-for-ec.adoc"
source_sha256: "ab3b1ac5e6aee0eddc39fc24faf4cbdc4541b070108424965c90b7d22d59f91f"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/advantages-disadvantages-and-requirements-for-ec.adoc"
---

# StorageGRID 11.8 Advantages, disadvantages, and requirements for erasure coding

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ilm/advantages-disadvantages-and-requirements-for-ec.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Advantages, disadvantages, and requirements for erasure coding
:icons: font
:imagesdir: ../media/

[.lead]
Before deciding whether to use replication or erasure coding to protect object data from loss, you should understand the advantages, disadvantages, and the requirements for erasure coding.

## Advantages of erasure coding

When compared to replication, erasure coding offers improved reliability, availability, and storage efficiency.

* *Reliability*: Reliability is gauged in terms of fault tolerance--that is, the number of simultaneous failures that can be sustained without loss of data. With replication, multiple identical copies are stored on different nodes and across sites. With erasure coding, an object is encoded into data and parity fragments and distributed across many nodes and sites. This dispersal provides both site and node failure protection. When compared to replication, erasure coding provides improved reliability at comparable storage costs.
* *Availability*: Availability can be defined as the ability to retrieve objects if Storage Nodes fail or become inaccessible. When compared to replication, erasure coding provides increased availability at comparable storage costs.
* *Storage efficiency*: For similar levels of availability and reliability, objects protected through erasure coding consume less disk space than the same objects would if protected through replication. For example, a 10 MB object that is replicated to two sites consumes 20 MB of disk space (two copies), while an object that is erasure-coded across three sites with a 6+3 erasure-coding scheme only consumes 15 MB of disk space.
+
NOTE: Disk space for erasure-coded objects is calculated as the object size plus the storage overhead. The storage overhead percentage is the number of parity fragments divided by the number of data fragments.

## Disadvantages of erasure coding

When compared to replication, erasure coding has the following disadvantages:

* An increased number of Storage Nodes and sites is recommended, depending on the erasure-coding scheme. In contrast, if you replicate object data, you need only one Storage Node for each copy. See link:what-erasure-coding-schemes-are.html#erasure-coding-schemes-for-storage-pools-containing-three-or-more-sites[Erasure-coding schemes for storage pools containing three or more sites] and link:what-erasure-coding-schemes-are.html#erasure-coding-schemes-for-one-site-storage-pools[Erasure-coding schemes for one-site storage pools].
* Increased cost and complexity of storage expansions. To expand a deployment that uses replication, you add storage capacity in every location where object copies are made. To expand a deployment that uses erasure coding, you must consider both the erasure-coding scheme in use and how full existing Storage Nodes are. For example, if you wait until existing nodes are 100% full, you must add at least `k+m` Storage Nodes, but if you expand when existing nodes are 70% full, you can add two nodes per site and still maximize usable storage capacity. For more information, see link:../expand/adding-storage-capacity-for-erasure-coded-objects.html[Add storage capacity for erasure-coded objects].
* There are increased retrieval latencies when you use erasure coding across geographically distributed sites. The object fragments for an object that is erasure-coded and distributed across remote sites take longer to retrieve over WAN connections than an object that is replicated and available locally (the same site to which the client connects).
* When you use erasure coding across geographically distributed sites, there is higher WAN network traffic usage for retrievals and repairs, especially for frequently retrieved objects or for object repairs over WAN network connections.
* When you use erasure coding across sites, the maximum object throughput declines sharply as network latency between sites increases. This decrease is due to the corresponding decrease in TCP network throughput, which affects how quickly the StorageGRID system can store and retrieve object fragments.
* Higher usage of compute resources.

## When to use erasure coding

Erasure coding is best suited for the following requirements:

* Objects greater than 1 MB in size.
+
NOTE: Erasure coding is best suited for objects greater than 1 MB. Don't use erasure coding for objects smaller than 200 KB to avoid the overhead of managing very small erasure-coded fragments.

* Long-term or cold storage for infrequently retrieved content.
* High data availability and reliability.
* Protection against complete site and node failures.
* Storage efficiency.
* Single-site deployments that require efficient data protection with only a single erasure-coded copy rather than multiple replicated copies.
* Multiple-site deployments where the inter-site latency is less than 100 ms.

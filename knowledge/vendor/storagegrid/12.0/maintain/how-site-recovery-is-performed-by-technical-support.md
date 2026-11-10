---
id: "storagegrid-120-79c84869c08908ab"
title: "StorageGRID 12.0 How technical support recovers a StorageGRID site"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/how-site-recovery-is-performed-by-technical-support.adoc"
source_sha256: "d0bf35df38f9d9f0ac80d5ee3cea2a62ac3dd03d44aee9086d0173d18388dbb2"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/how-site-recovery-is-performed-by-technical-support.adoc"
---

# StorageGRID 12.0 How technical support recovers a StorageGRID site

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/how-site-recovery-is-performed-by-technical-support.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# How technical support recovers a StorageGRID site
:icons: font
:imagesdir: ../media/

[.lead]
If an entire StorageGRID site fails or if multiple Storage Nodes fail, you must contact technical support. Technical support will assess your situation, develop a recovery plan, and then recover the failed nodes or site in a way that meets your business objectives, optimizes recovery time, and prevents unnecessary data loss.

CAUTION: Site recovery can only be performed by technical support.

StorageGRID systems are resilient to a wide variety of failures, and you can successfully perform many recovery and maintenance procedures yourself. However, it is difficult to create a simple, generalized site recovery procedure because the detailed steps depend on factors that are specific to your situation. For example:

* *Your business objectives*: After the complete loss of a StorageGRID site, you should evaluate how best to meet your business objectives. For example, do you want to rebuild the lost site in-place? Do you want to replace the lost StorageGRID site in a new location? Every customer's situation is different, and your recovery plan must be designed to address your priorities.
* *Exact nature of the failure*: Before beginning a site recovery, establish if any nodes at the failed site are intact or if any Storage Nodes contain recoverable objects. If you rebuild nodes or storage volumes that contain valid data, unnecessary data loss could occur.
* *Active ILM policies*: The number, type, and location of object copies in your grid is controlled by your active ILM policies. The specifics of your ILM policies can affect the amount of recoverable data, as well as the specific techniques required for recovery.
+
CAUTION: If a site contains the only copy of an object and the site is lost, the object is lost.

* *Bucket (or container) consistency*: The consistency applied to a bucket (or container) affects whether StorageGRID fully replicates object metadata to all nodes and sites before telling a client that object ingest was successful. If the consistency value allows for eventual consistency, some object metadata might have been lost in the site failure. This can affect the amount of recoverable data and potentially the details of the recovery procedure.
* *History of recent changes*: The details of your recovery procedure can be affected by whether any maintenance procedures were in progress at the time of the failure or whether any recent changes were made to your ILM policies. Technical support must assess the recent history of your grid as well as its current situation before beginning a site recovery.

CAUTION: Site recovery can only be performed by technical support.

This is a general overview of the process that technical support uses to recover a failed site:

. Technical support:
.. Makes a detailed assessment of the failure.
.. Works with you to review your business objectives.
.. Develops a recovery plan tailored for your situation.

. If the primary Admin Node if it has failed, technical support recovers it.

. Technical support recovers all Storage Nodes, following this outline:
 .. Replace Storage Node hardware or virtual machines as required.
 .. Restore object metadata to the failed site.
 .. Restore object data to the recovered Storage Nodes.
+
CAUTION: Data loss will occur if the recovery procedures for a single failed Storage Node are used.
+
NOTE: When an entire site has failed, technical support uses specialized commands to successfully restore objects and object metadata.

. Technical support recovers other failed nodes.
+
After object metadata and data have been recovered, technical support uses standard procedures to recover failed Gateway Nodes or non-primary Admin Nodes.

.Related information

link:site-decommissioning.html[Site decommission]

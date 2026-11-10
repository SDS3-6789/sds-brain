---
id: "storagegrid-119-608596bcfc51a715"
title: "StorageGRID 11.9 Create a traffic classification policy for FabricPool"
area: "storagegrid"
type: "import"
applies_to: ["11.9", "storagegrid-11.9"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg119-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-119"
repository_commit: "aa58c9affae3bb1994d6bd2e525851e3fd088517"
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/fabricpool/creating-traffic-classification-policy-for-fabricpool.adoc"
source_sha256: "909280624547844f6422cec31be5733631d2b8b8f2fa4b5205eb4fc9c3f7ecd7"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "fabricpool/creating-traffic-classification-policy-for-fabricpool.adoc"
---

# StorageGRID 11.9 Create a traffic classification policy for FabricPool

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/fabricpool/creating-traffic-classification-policy-for-fabricpool.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Create a traffic classification policy for FabricPool
:icons: font
:imagesdir: ../media/

[.lead]
You can optionally design a StorageGRID traffic classification policy to optimize quality of service for the FabricPool workload.

For details about this task, see link:../admin/managing-traffic-classification-policies.html[Manage traffic classification policies]. To use the FabricPool setup wizard to complete this task, go to link:use-fabricpool-setup-wizard-steps.html[Access and complete the FabricPool setup wizard].

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:../admin/admin-group-permissions.html[Root access permission].

.About this task
The best practices for creating a traffic classification policy for FabricPool depend on the workload, as follows:

* If you plan to tier FabricPool primary workload data to StorageGRID, you should ensure that the FabricPool workload has most of the bandwidth. You can create a traffic classification policy to limit all other workloads.
+
NOTE: In general, FabricPool read operations are more important to prioritize than write operations.
+
For example, if other S3 clients use this StorageGRID system, you should create a traffic classification policy. You can limit network traffic for the other buckets, tenants, IP subnets, or load balancer endpoints.

* Generally, you should not impose quality of service limits on any FabricPool workload; you should only limit the other workloads.

* The limits placed on other workloads should account for the behavior of those workloads. The limits imposed will also vary based on the sizing and capabilities of your grid and what the expected amount of utilization is.

.Steps
. Select *CONFIGURATION* > *Network* > *Traffic classification*.
. Select *Create*.
. Enter a name and a description (optional) for the policy and select *Continue*.

. For the Add matching rules step, add at least one rule.
 .. Select *Add rule* 
 .. For Type, select *Load balancer endpoint*, and select the load balancer endpoint you created for FabricPool.
+
You can also select the FabricPool tenant account or bucket.

 .. If you want this traffic policy to limit traffic for the other endpoints, select *Inverse match*.

. Optionally, add one or more limits to control the network traffic matched by the rule.
+
NOTE: StorageGRID collects metrics even if you don't add any limits, so you can understand traffic trends.

 .. Select *Add a limit*.
 .. Select the type of traffic you want to limit and the limit to apply.

. Select *Continue*.

. Read and review the Traffic classification policy. Use the *Previous* button to go back and make changes as required. When you are satisfied with the policy, select *Save and continue*.

.After your finish

link:../admin/viewing-network-traffic-metrics.html[View network traffic metrics] to verify that the polices are enforcing the traffic limits you expect.

---
id: "rb-rgw-multisite-lag"
title: "RGW multisite lag investigation"
area: "ceph"
type: "runbook"
applies_to: ["rhcs-7.1", "rhcs-8.1"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhcs-8-multisite", "ceph-squid-multisite", "ibm-ceph-multisite", "ibm-ceph-deployment", "rhcs-8-release"]
---

# RGW multisite lag investigation

## Confirm the topology and expectation

Use this runbook only when the customer actually uses RGW multisite. Confirm source and destination clusters, their FSIDs, the selected realm, zonegroup and zones, and the policy that should copy the affected bucket. Multiple RGW instances behind one endpoint do not alone prove a multisite configuration.

The vendor and upstream multisite guides distinguish realms, zonegroups and zones. Treat source-to-destination synchronization as a specific direction. A healthy status for a different zone, realm or bucket is not evidence that the reported object should already be present.

This is a read-only, documented template; none of its commands have been executed on the user's infrastructure. Use an already-approved administrative session for each explicitly selected cluster and a verified local zone context. Do not switch the CLI's default realm or modify configuration to make the checks run.

## Collect synchronization state

In the correctly scoped RGW administrative context:

```bash
radosgw-admin sync status
radosgw-admin metadata sync status
```

Use the local command's help and exact vendor guide to add explicit realm/zone parameters where needed. Do not guess an identifier from a display name. Record the cluster, local zone, source zone, timestamp and returned status together.

For a data-sync investigation, read the installed command help before preparing `radosgw-admin data sync status --source-zone <SOURCE_ZONE_ID>`. The source-zone identifier must come from the customer's verified topology. Avoid collecting full zone configuration because it can expose system-user credentials.

## Decide what the evidence means

Distinguish metadata synchronization from data synchronization. A metadata issue can affect knowledge of users or buckets while an object data transfer has its own progress and error evidence. Compare a bounded second snapshot to establish whether the lag is shrinking, growing or stationary. Retain failure codes and source/destination identity; do not reduce the result to a single global "sync healthy" statement.

Correlate the lag with the two clusters' health, destination capacity, RGW daemon availability and network/TLS events. Compare the failure time to policy changes or upgrades. Where policy intentionally excludes a bucket or destination, absent data may be consistent with configuration; verify the expectation with the owner.

IBM's deployment guidance helps interpret geographic/site design, but it is not evidence of this customer's actual topology. The IBM multi-site considerations source was available through search results and direct retrieval was blocked; use the fully opened Red Hat/upstream sources for the initial procedure.

## Keep recovery decisions separate

Do not promote a zone, commit a new period, reinitialize sync, trim logs, modify policy or replay a write. These can alter data movement or authority. If a known issue seems relevant, compare its stated affected/fixed versions to both sides of the deployment and preserve uncertainty until the conditions match.

The handoff should identify the failed direction, metadata versus data symptom, impacted scope, observed progress, relevant patch levels and proposed next evidence. If the owner cannot supply the topology or expected policy, stop at that gap rather than inventing a replication relationship.

## Sources

- [RHCS 8 Multi-site configuration and administration](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/object_gateway_guide/multisite-configuration-and-administration)
- [Ceph Squid RGW multi-site](https://docs.ceph.com/en/squid/radosgw/multisite/)
- [IBM Storage Ceph 8.1 Multi-site considerations](https://www.ibm.com/docs/en/storage-ceph/8.1.0?topic=gateway-multi-site-considerations)
- [IBM Storage Ceph 8.1 RGW deployment guidelines](https://www.ibm.com/docs/en/storage-ceph/8.1.0?topic=gateway-deployment-guidelines)
- [Red Hat Ceph Storage 8.1 Release Notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/8.1_release_notes/8.1_release_notes)

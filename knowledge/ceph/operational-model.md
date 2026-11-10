---
id: "ceph-operational-model"
title: "Ceph RGW operational model and evidence routing"
area: "ceph"
type: "knowledge"
applies_to: ["rhcs-7.1", "rhcs-8.1"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["ibm-ceph-architecture", "rhcs-8-rgw", "ceph-squid-rgw-admin", "ceph-squid-s3"]
---

# Ceph RGW operational model and evidence routing

## Scope

This brain initially targets the owner's cephadm-managed RGW deployments. RBD and CephFS references are discoverable as background; their use in the actual fleet has not been established.

Treat a storage incident as evidence from several connected layers: client request, endpoint/load balancer, RGW daemon, RADOS pool/placement group, OSD, host and physical infrastructure. A symptom at one layer does not identify the cause. The IBM architecture reference describes these Ceph components; the routing below is an operational investigation method proposed for this repository.

| Symptom | First evidence | Follow-up |
|---|---|---|
| Cluster health warning | Exact health identifiers, FSID, time and client impact | Health baseline, then the relevant OSD/PG or daemon runbook |
| S3 403 or signature error | Operation, request ID, endpoint, timestamp, identity alias | Backend policy, clock, addressing and SDK behavior |
| Elevated S3 latency | Latency by operation and RGW, error rate, workload change | RADOS health, OSD/host pressure and network path |
| Missing object at another site | Source/destination zone and expected sync policy | Multisite status and lag; distinguish metadata from data |
| Failed daemon | Orchestrator state and service events | Host systemd/container state and bounded logs |

## Identity boundary

A CephX identity authorizes cluster operations. An RGW S3 user is a separate object-storage identity. The word "account" also has product-specific meanings: the owner says Objectify provisions an RGW user or a StorageGRID tenant. Do not substitute newer upstream RGW account semantics for that internal contract.

The RGW administrative interface can return key material when inspecting a user. Prefer an Objectify response projection that exposes only approved metadata. If a human runs a direct inspection, project the response to required non-secret fields before supplying it to the assistant. Never store raw credentials in incident or knowledge pages.

## Compatibility boundary

Ceph documents S3 compatibility and a feature support table. This supports using S3 as the shared API vocabulary, while testing actual operations against the installed backend and patch level. Record endpoint, region, addressing style, SDK version and options with a reported compatibility issue. AWS service behavior alone does not prove what RHCS supports.

## What becomes durable knowledge

Keep the observed symptom, scoped build, investigation results, source references and final outcome. Separate confirmed facts from possible explanations. A reusable note should explain which observation would falsify its conclusion. Customer data and private topology belong only in the appropriately restricted customer workspace.

## Sources

- [IBM Storage Ceph Concepts and Architecture Guide REDP-5721](https://www.redbooks.ibm.com/redpapers/pdfs/redp5721.pdf)
- [Red Hat Ceph Storage 8 Object Gateway Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/object_gateway_guide/index)
- [Ceph Squid RGW administration](https://docs.ceph.com/en/squid/radosgw/admin/)
- [Ceph Squid S3 API and feature support](https://docs.ceph.com/en/squid/radosgw/s3/)

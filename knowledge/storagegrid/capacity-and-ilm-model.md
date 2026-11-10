---
id: storagegrid-capacity-ilm-model
title: StorageGRID capacity, tenant usage, and ILM are different measurements
area: storagegrid
type: knowledge
applies_to: [storagegrid-11.9]
confidence: documented
last_verified: 2026-11-09
sources: [netapp-sg119-capacity, netapp-sg119-metadata, netapp-sg119-ilm, netapp-sg119-ilm-policies, netapp-sg119-ilm-lifecycle, netapp-sg119-tenant-dashboard, netapp-sg119-object-lock, netapp-sg119-search-integration]
---

# StorageGRID capacity, tenant usage, and ILM are different measurements

Use this model to choose evidence; confirm the matching chapters before applying it to 11.8 or an unconfirmed 12.x deployment.

| Measurement | Question it answers | Common misinterpretation to prevent |
|---|---|---|
| Tenant logical usage/quota | How much object data is attributed to this tenant? | Treating it as the physical cost of all protected copies |
| Physical object-data space | Which nodes/sites can accept protected object data? | Assuming grid-wide free space guarantees every placement is feasible |
| Allowed metadata usage | How much room remains for metadata under the supported limit? | Treating all filesystem free space as usable metadata capacity |
| ILM work and placement | Is the grid evaluating and meeting required placement? | Equating a completed scan with completed protection |

StorageGRID distinguishes object-data storage from metadata storage. Its capacity documentation identifies separate views and metrics. Preserve the node/site dimension rather than relying on an aggregate dashboard. [Capacity](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-storage-capacity.html). Metadata has an allowed allocation and space reserved for essential database work; exceeding the allowed amount is not simply a cosmetic alarm. [Metadata troubleshooting](https://docs.netapp.com/us-en/storagegrid-119/troubleshoot/troubleshooting-metadata-issues.html).

ILM rules describe the protection and placement of copies over time. Resolve the bucket's policy tag to its assigned active policy before selecting the matching rule: 11.9 can have multiple active policies, and untagged buckets use the Default tag's policy. [ILM policy selection](https://docs.netapp.com/us-en/storagegrid-119/ilm/ilm-policy-overview.html). Separate policy design from the observed current placement. [ILM](https://docs.netapp.com/us-en/storagegrid-119/ilm/index.html) and [object lifecycle](https://docs.netapp.com/us-en/storagegrid-119/ilm/how-ilm-operates-throughout-objects-life.html).

Tenant quota usage is estimated logical object data. It excludes the physical cost of copies and metadata. Preserve the calculation time when comparing Objectify, Tenant Manager, and monitoring values. [Tenant dashboard](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-tenant-manager-dashboard.html).

Retention is a separate axis: Object Lock can constrain deletion of versions even when capacity is tight. The agent must collect retention and legal-hold status without removing protection. [StorageGRID Object Lock](https://docs.netapp.com/us-en/storagegrid-119/ilm/managing-objects-with-s3-object-lock.html).

## Elasticsearch is not automatically the object inventory authority

StorageGRID search integration asynchronously exports object metadata to an external endpoint. If the user's Elasticsearch receives this feed, its state can lag object operations. The user has not confirmed that this is their Elasticsearch topology; it might instead contain operational logs or a different dataset. Obtain the index mapping and ingestion path before using counts or search misses as evidence of object loss. [Search integration](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-search-integration-service.html).

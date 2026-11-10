---
id: runbook-storagegrid-ilm-backlog
title: Investigate StorageGRID ILM queues and placement pressure
area: storagegrid
type: runbook
applies_to: [storagegrid-11.9]
confidence: documented
last_verified: 2026-11-09
sources: [netapp-sg119-ilm-monitor, netapp-sg119-ilm, netapp-sg119-ilm-policies, netapp-sg119-bucket-operations, netapp-sg119-ilm-lifecycle, netapp-sg119-object-lock, netapp-sg119-consistency]
---

# Investigate StorageGRID ILM queues and placement pressure

## Establish the incident

Bind the investigation to one customer and grid. Record software build, affected sites, bucket/tenant aliases where authorized, the first observed symptom, and a UTC comparison window. Ask whether the concern is growing evaluation backlog, inability to place copies, ingest failures, or concern about an individual object's protection. Those are different questions.

This procedure observes state. It does not activate an ILM policy, change ingest behavior, reduce protection, trigger repair, or edit object retention. Confirm equivalent documentation before applying the 11.9 interface steps to another release.

## Read the evidence

1. View the Grid Manager ILM dashboard and grid ILM view. Record queue size, client-driven arrivals, all-operation arrivals, scan rate, and evaluation rate over the same time window. Temporary spikes can occur; a continuing rise that does not drain deserves investigation. A completed scan alone does not prove ILM has been applied to every object. [ILM monitoring](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-information-lifecycle-management.html).
2. Resolve the affected bucket's current ILM policy tag to its assigned active policy. StorageGRID 11.9 supports multiple active policies; the Default tag's policy applies to an untagged bucket. Read the selected bucket's existing tag and policy mapping through the approved management view or read API, and stop placement conclusions if the mapping is unresolved. Preserve the mapped policy identity, rule order, matching object attributes, placement targets, copy type and retention stages. [ILM policy selection](https://docs.netapp.com/us-en/storagegrid-119/ilm/ilm-policy-overview.html). The S3 bucket-operation reference identifies the `NTAP-SG-ILM-BUCKET-TAG` tag when a non-default policy is assigned; inspect it without changing or deleting it. [Bucket operations](https://docs.netapp.com/us-en/storagegrid-119/s3/operations-on-buckets.html).
3. Correlate placement targets with observed site/node availability, capacity pressure, and existing network telemetry. Treat a recent policy change, workload change, recovery, or site event as a hypothesis to test against the timestamped evidence. Do not infer causation from a coincident alert alone.
4. For one approved sample object, use existing metadata/placement views to compare intended lifecycle stage with recorded placement. Record the sample's version and observation time. Avoid a broad object scan or retrieving the payload. [Object lifecycle](https://docs.netapp.com/us-en/storagegrid-119/ilm/how-ilm-operates-throughout-objects-life.html).

## Interpret carefully

Separate metadata consistency from copy placement. StorageGRID documents an interaction between consistency settings and ILM ingest behavior; one successful S3 response is not a universal proof of the protection assumptions made by an application. Retrieve the version-matched settings before offering a resilience conclusion. [Consistency](https://docs.netapp.com/us-en/storagegrid-119/s3/consistency-controls.html).

If retention affects the proposed response, inspect Object Lock configuration and the relevant version's retention/legal-hold state. Do not propose expiration or removal of protection as an automatic capacity fix. [Object Lock](https://docs.netapp.com/us-en/storagegrid-119/ilm/managing-objects-with-s3-object-lock.html).

## Exit criteria

Return the evidence for whether the queue is draining, stable, or growing; which placements appear constrained; and what remains unknown. Escalate when data protection cannot be established or placement constraints persist. A change proposal must specify affected customers/sites, expected protection before/after, validation, and rollback separately from this read-only report.

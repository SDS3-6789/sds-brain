---
id: runbook-s3-latency-5xx
title: Investigate S3 latency and server errors
area: s3
type: runbook
applies_to: [aws-s3-reference, ceph-rgw, storagegrid]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-performance, aws-s3-errors, netapp-sg119-lb-monitor, netapp-sg119-monitor, netapp-sg119-troubleshoot]
---

# Investigate S3 latency and server errors

## Define what is slow

Select one customer and cluster/grid plus a bounded UTC incident interval and an appropriate baseline. Identify the operation mix, object-size bands, concurrency, client/SDK version, retry behavior, and whether latency means total application time, time to first byte, server processing time, or multipart completion. Keep successful and failed requests separate.

This workflow uses existing telemetry and narrowly approved reads. It does not generate benchmark traffic, upload diagnostic objects, change concurrency, restart gateways, or modify storage recovery parameters. If telemetry is insufficient, propose a bounded test for separate approval.

## Correlate

1. Compare request counts, error counts, latency distribution, bytes, and retries over the same interval. A percentile from one dashboard cannot be combined with a different time range or operation mix. Preserve the query, datasource, labels, aggregation, and sample interval.
2. Examine DNS/connect/TLS/client-transfer evidence separately from backend service time. AWS's performance guidance calls out network/CPU/memory measurements and HTTP timing, along with observing 503 responses. Its AWS-specific placement or acceleration options are not automatic advice for an on-premises backend. [AWS performance guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html).
3. Classify the exact provider error. AWS lists `SlowDown` as a 503 response, but a proxy-generated 503 or a different backend's 503 needs its own evidence. Preserve request ID and source component before claiming throttling. [AWS errors](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/ErrorResponses.html).
4. For StorageGRID, examine traffic distribution and HA roles on the actual S3 path. Compare active nodes and do not treat an expected standby's low traffic as a failure. [Load-balancing observations](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-load-balancing-operations.html).
5. Correlate node/site health, storage, ILM, and resources with the same request interval. For Ceph RGW, continue into the Ceph health/slow-operations runbooks with the verified cluster context; frontend symptoms alone do not identify an OSD root cause. [StorageGRID monitoring categories](https://docs.netapp.com/us-en/storagegrid-119/monitor/index.html).

## Use a hypothesis table

For each candidate cause, show observed evidence, contradictory evidence, and one next read. Examples include a client retry storm, one degraded gateway path, a workload-size shift, a backend placement constraint, or an unavailable datasource. Mark these as hypotheses until evidence discriminates between them.

Capture the timeline of application, network, certificate, maintenance, and storage changes. NetApp recommends framing the problem and impact with baselines and recent changes; this repository turns that into a customer-scoped evidence record. [Troubleshooting overview](https://docs.netapp.com/us-en/storagegrid-119/troubleshoot/index.html).

## Exit

Return the affected operation/population, timing layer, measured regression, uncertainty, and next scoped evidence request. Do not recommend more retries or concurrency blindly: that is a change proposal whose load impact must be evaluated.

---
id: runbook-storagegrid-capacity
title: Diagnose StorageGRID object-data and metadata capacity
area: storagegrid
type: runbook
applies_to: [storagegrid-11.9]
confidence: documented
last_verified: 2026-11-09
sources: [netapp-sg119-capacity, netapp-sg119-metadata, netapp-sg119-monitor, netapp-sg119-troubleshoot]
---

# Diagnose StorageGRID object-data and metadata capacity

## Scope and prerequisites

This is a read-only triage procedure, reviewed against 11.9 documentation and not tested on the user's grid. Confirm the actual release/hotfix, customer, grid, site, and UTC interval. For 11.8 or 12.x, resolve the corresponding version's chapter before following interface labels or thresholds. Use Grid Manager visibility or a scoped monitoring connection; a broad administrator credential is unnecessary for routine evidence gathering.

## Collect

1. Record current and resolved capacity alerts, affected nodes/sites, onset, and whether clients report failed ingest, failed reads, or only reduced headroom. Preserve the alert severity and the rule definition actually deployed.
2. In the dashboard and node storage views, inspect **object data and metadata separately**. Capture used/available values by site and node, plus trend and last sample time. NetApp notes that aggregate totals omit nodes that have not reported metrics for at least five minutes; an apparently improved aggregate can reflect missing telemetry. [Capacity guide](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-storage-capacity.html).
3. For metadata, compare used bytes with **allowed** metadata bytes. Do not substitute filesystem capacity or actual reserved space for the documented denominator. In 11.9, relevant metrics include `storagegrid_storage_utilization_metadata_bytes` and `storagegrid_storage_utilization_metadata_allowed_bytes`. Discover the real labels and attach the customer/grid selector before querying. [Capacity guide](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-storage-capacity.html).
4. Correlate the same interval with node availability, recent ingest changes, object-size distribution, ILM activity, and maintenance. Distinguish missing observations from a measured zero. NetApp's monitoring guide separately covers health, storage, ILM, resource use, tenant activity, and load balancing. [Monitoring](https://docs.netapp.com/us-en/storagegrid-119/monitor/index.html).

## Interpret and escalate

Metadata capacity can be the limiting factor even when object-data space remains. The 11.9 metadata guidance identifies 70%, 90%, and 100% of allowed space as minor, major, and critical thresholds. Check the installed alert rule rather than treating these numbers as a universal exporter threshold. A major/critical metadata condition requires prompt escalation and a reviewed capacity response. The read-only agent must not delete database files, run a repair, or start an expansion. [Metadata troubleshooting](https://docs.netapp.com/us-en/storagegrid-119/troubleshoot/troubleshooting-metadata-issues.html).

Compute a trend estimate only when samples are reliable and the workload is sufficiently stable. State the observation window and uncertainty. Do not promise a safe number of days based on one sample or assume that free space in a different site satisfies the active ILM placement.

## Output

Return a table of customer/grid/site/node, metric, value, timestamp, denominator, trend, and alert. Separate **capacity pressure**, **placement constraints**, and **missing telemetry** as hypotheses. Include the smallest next evidence request and a timeline of recent changes. NetApp's troubleshooting method emphasizes a defined problem, impact, baselines, and recent changes. [Troubleshooting overview](https://docs.netapp.com/us-en/storagegrid-119/troubleshoot/index.html).

---
id: dashboard-to-evidence
title: Trace a Grafana alert or panel to trustworthy evidence
area: observability
type: runbook
applies_to: [Grafana-version-unconfirmed, custom-exporter]
confidence: documented
last_verified: 2026-11-09
sources: [grafana-dashboard-export, grafana-es-query, grafana-service-accounts, prometheus-api, prometheus-functions]
---

# Trace a Grafana alert or panel to trustworthy evidence

## Entry conditions

Use this when a dashboard reports S3 latency, storage pressure, failures or missing data. Obtain the customer/cluster alias, dashboard and panel identifiers, datasource UID, UTC incident interval and the operator's reported impact. Existing backend access must already be limited to the intended customer.

## Read-only procedure

1. Inspect the dashboard definition or a reviewed export. Record the panel expression, selected variables, transformations, unit, time override and query datasource. Do not change or save the dashboard. [Grafana dashboard export/share documentation](https://grafana.com/docs/grafana/latest/visualizations/dashboards/share-dashboards-panels/) is the interface reference; do not create a public snapshot.
2. Check whether the datasource is Elasticsearch, Prometheus or another system. Do not assume a custom exporter means Prometheus. Confirm its UID in the approved inventory; a display name alone is insufficient when duplicate names exist.
3. Preserve the exact selectors and run the same expression over a short interval around the event. Record the requested interval, returned timestamps and sampling step. Start with one affected cluster/panel, not every customer or the entire retention period.
4. Compare the raw result with the displayed panel. A transformation, repeated panel, aggregation or time shift can explain the difference. For Elasticsearch, verify timestamp fields and query syntax against the installed editor: [query editor reference](https://grafana.com/docs/grafana/latest/datasources/elasticsearch/query-editor/).
5. If Prometheus is confirmed, inspect metadata for the selected metric before applying a function. Use counter rates over a suitable range rather than reading a cumulative counter as a current request rate. Account for resets and missing samples. References: [HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/) and [query functions](https://prometheus.io/docs/prometheus/latest/querying/functions/).
6. Correlate the same interval with the appropriate Ceph or StorageGRID runbook. If the dashboard cannot establish backend health, mark it as an observation gap rather than concluding the backend is healthy.

## Interpret and close

Separate four cases: actual service degradation, stale/failed collection, a query/label mismatch, or a visualization calculation. Record which evidence distinguishes them. Minimum handoff: context, panel/datasource, interval, actual expression, series count, units, collection freshness, backend observations and remaining hypotheses.

Use a least-privilege service account that can access only the relevant material; [Grafana service accounts](https://grafana.com/docs/grafana/latest/administration/service-accounts/) explains the identity mechanism. A successful query is not proof that the account cannot reach other customers. Validate that property independently before enabling automation.

Escalate when monitoring cannot establish whether a durability or availability incident is occurring. Do not silence the alert, widen access, change collection intervals or restart exporters through this first-release workflow.

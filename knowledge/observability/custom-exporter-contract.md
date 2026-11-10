---
id: custom-exporter-contract
title: Establish the custom exporter and dashboard contract
area: observability
type: knowledge
applies_to: [Grafana-version-unconfirmed, exporter-version-unconfirmed]
confidence: documented
last_verified: 2026-11-09
sources: [user-intake-2026-11-09, grafana-elasticsearch, grafana-prometheus, grafana-es-query, prometheus-exporters, prometheus-exposition, prometheus-naming, prometheus-histograms]
---

# Establish the custom exporter and dashboard contract

The user confirmed Grafana, a custom exporter and Elasticsearch. The exporter format, storage backend and metric names were not supplied. Prometheus is a candidate integration only. Elasticsearch might contain application logs, exporter output, object metadata, or several of these; establish its actual role before querying.

## Minimum evidence packet

Request one reviewed dashboard JSON and a small schema sample. Record dashboard UID/version, datasource UID/type, panel ID/title, query text, variables, units, transformations, time overrides and refresh interval. Map each datasource to the customer and cluster in the restricted inventory. A dashboard that looks like a cluster dashboard may still query several backends.

For every useful exporter field record its original name, human meaning, type, unit, labels, scope, collection interval, update timestamp, expected cardinality and empty-value behavior. Keep cumulative counters distinct from current gauges. Check whether latency is seconds or milliseconds and whether size is bytes or a displayed conversion. Confirm whether quota means logical tenant usage, bucket usage, provisioned limit or protected physical capacity. These are proposed local schema fields, not a description of Objectify's existing response.

If it is Prometheus-compatible, `HELP`/`TYPE` and the sample exposition are starting evidence for metric semantics. Inspect the deployed exporter code/version or team documentation when these are absent or misleading. [Exposition formats](https://prometheus.io/docs/instrumenting/exposition_formats/) and [exporter guidance](https://prometheus.io/docs/instrumenting/writing_exporters/) supply the format and design references.

## Use queries only after discovery

Do not fabricate metric names such as an imagined RGW latency or Objectify quota gauge. Translate the existing panel's verified expression into a bounded query first. Preserve its customer/cluster selector, then compare the raw data with the rendered value. Note transformations or unit conversions before attributing a discrepancy to the underlying system.

For a Prometheus backend, determine whether the observation is a counter, gauge, classic/native histogram or summary before choosing a function. Percentiles of independently computed summaries cannot be casually combined into a fleet percentile. [Metric naming](https://prometheus.io/docs/practices/naming/) and [histograms and summaries](https://prometheus.io/docs/practices/histograms/) support that review. Do not assume dashboard percentages are computed over the same population as an API quota.

For Elasticsearch, record the permitted index/alias, timestamp field, field types, request-ID field and exact customer/cluster field names. A query against a string field and the corresponding keyword field may behave differently; inspect the mapping. Use the installed Grafana query editor's supported syntax. [Grafana Elasticsearch reference](https://grafana.com/docs/grafana/latest/datasources/elasticsearch/) and [query editor](https://grafana.com/docs/grafana/latest/datasources/elasticsearch/query-editor/) are discovery references; latest features may not exist in the installed release.

## No-data and timing

Distinguish zero, null, absent series, stale scrape, exporter failure and datasource failure. Preserve source timestamps and timezone. Compare the same time interval across dashboards, Objectify, RGW and Grid Manager. A status collected ten minutes ago is not simultaneous with an incident that started two minutes ago. Annotate sampling and lag before concluding that systems disagree.

Store the approved metric map using `templates/metric-contract.json`. Keep customer-specific labels and index names in private storage. Validate a small known-good and known-bad example with the exporter owner before promoting an interpretation to verified knowledge.

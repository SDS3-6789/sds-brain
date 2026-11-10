---
id: elasticsearch-correlation
title: Correlate S3 request failures in authorized Elasticsearch data
area: observability
type: runbook
applies_to: [Elasticsearch-version-unconfirmed]
confidence: documented
last_verified: 2026-11-09
sources: [elastic-search-api, elastic-health-api, grafana-elasticsearch, user-intake-2026-11-09]
---

# Correlate S3 request failures in authorized Elasticsearch data

## Establish the data contract

Confirm that the intended index actually contains gateway/application events for the selected customer and cluster. The presence of Elasticsearch does not prove it is a log platform or a StorageGRID metadata integration. Obtain the permitted index alias, timestamp field, exact-match customer/cluster fields, request-ID field, event status and duration units. Start with a known request ID supplied by the operator.

The [Elasticsearch Search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search) supports bounded reads against a specified index and requires index read access. Use a scoped backend identity; do not rely exclusively on a filter in the query. Confirm the installed API version before using the current reference.

## Investigation

1. Resolve the datasource UID and index alias from the private context. Reject `_all`, a global wildcard or a cross-customer alias. Keep the investigation's UTC interval narrow.
2. Reuse the existing working dashboard query or an approved query template. Request only fields needed for correlation. Keep result size small, disable full hit counting when not needed and record partial results/timeouts.
3. Filter by the exact request ID where available; otherwise combine the authorized customer, cluster, time and observed error. A short identifier may not be globally unique.
4. Match gateway events with client request time and the storage backend's observed state. Compare retries, upstream response time and timeout stages. Preserve differing request IDs created by retries rather than collapsing them into one event.
5. If there are no hits, check index/time mapping and collection delay before widening the query. Do not search every index to compensate for a missing mapping.

## Template only — replace with reviewed field names

The following JSON is a design template, not an executable Objectify request or a verified query for your exporter:

```json
{
  "size": 20,
  "timeout": "5s",
  "track_total_hits": false,
  "_source": ["VERIFIED_TIMESTAMP", "VERIFIED_REQUEST_ID", "VERIFIED_STATUS"],
  "query": {
    "bool": {
      "filter": [
        {"term": {"VERIFIED_CUSTOMER_FIELD": "ACTIVE_CUSTOMER"}},
        {"term": {"VERIFIED_CLUSTER_FIELD": "ACTIVE_CLUSTER"}},
        {"term": {"VERIFIED_REQUEST_ID_FIELD": "KNOWN_REQUEST_ID"}},
        {"range": {"VERIFIED_TIMESTAMP": {"gte": "START_UTC", "lte": "END_UTC"}}}
      ]
    }
  }
}
```

Use mappings to select keyword/exact-match fields. Exclude raw messages and arbitrary `_source` payloads unless reviewed for credentials and personal information. Some API reads use POST; classify operations by documented semantics and a strict path/body allowlist, not by the verb alone. This package does not implement a generic Elasticsearch HTTP proxy.

## Separate the search platform from the storage service

An Elasticsearch health issue may explain missing incident evidence without proving Ceph or StorageGRID failure. The [cluster health API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-health) distinguishes shard allocation states and requires cluster monitoring privileges. Do not grant cluster-wide visibility to a customer-only diagnostic session without an approved boundary.

Handoff: context, query/index, time window, field map, returned count, timeout/partial flags, representative redacted request events and their relationship to backend observations. If the necessary fields are absent, document a schema gap and use the product's own read-only evidence path.

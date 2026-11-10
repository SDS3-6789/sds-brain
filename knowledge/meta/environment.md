---
id: environment-intake
title: Environment inventory and unresolved details
area: meta
type: knowledge
applies_to: [reported-fleet]
confidence: user-reported
last_verified: 2026-11-09
sources: [user-intake-2026-11-09, hpe-xl420-apollo, hpe-xl170r, hpe-xl190r, hpe-dl385]
---

# Environment inventory and unresolved details

The intake states: containerized Ceph RGW managed by cephadm; RHCS releases 7.1z7, 8.1z3 and 8.1z6–z9; NetApp StorageGRID 11.8, 11.9 and 12; RHEL 9.6/9.8; Grafana, a custom exporter and Elasticsearch; HPE hardware described as exel420, exel170, exel190 and DL385. Multiple customers have multiple clusters. Objectify creates Ceph RGW users and StorageGRID tenants through an internal API. Its first integration must be read-only.

These statements describe the fleet collectively. No customer aliases, cluster FSIDs, endpoint addresses, installed daemon digests, Grafana datasource UIDs, metric schema, dashboard exports, Confluence spaces or Red Hat document exports have been provided. Do not populate any of them from memory or inference.

## Hardware interpretation

HPE documents the XL420 name within the Apollo 4200 family: [Apollo 4200 Gen10 Plus QuickSpecs](https://www.hpe.com/int/en/collaterals/collateral.a50002573enw.html). XL170r and XL190r are plausible interpretations of the other reported names: [XL170r product reference](https://support.hpe.com/hpesc/public/docDisplay?docId=a00027628en_us), [XL190r manual index](https://support.hpe.com/connect/s/product?kmpmoid=1010192754&language=en_CA&tab=manuals). This is a candidate mapping. The exact generation of every model, including DL385, remains unknown. The [DL385 Gen11 guide](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00002188en_us&docLocale=en_US) is a discovery reference, not a claim that Gen11 is installed.

## Information that unlocks live integration

1. Objectify `/openapi.json`, authentication scheme, safe response schema and one redacted successful response per approved read operation.
2. One example customer/cluster inventory and the identity boundaries enforced by each backend.
3. One reviewed dashboard export, datasource mapping and exporter sample showing names, labels, types and units. Confirm whether Prometheus is present.
4. Exact StorageGRID 12 minor/build, server generations/iLO firmware and installed Grafana/Elasticsearch versions.
5. Confluence Cloud versus Data Center and a reviewed export of permitted pages. The user's full Red Hat documentation can be imported after its release and permitted audience are identified.

Use `config/context.example.json` as the private inventory template. Keep actual context files in the restricted customer environment.

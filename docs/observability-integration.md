# Grafana, Elasticsearch and the custom exporter

## Grafana MCP inside the internal network

The integration uses the official [Grafana MCP v2.2.0](https://github.com/grafana/mcp-grafana/tree/v2.2.0). Its release archives travel with this repository in `mcp/grafana/vendor/`, and `mcp/grafana/launch.py` selects and verifies the local archive for the current operating system and CPU. No GitHub access, package manager, container pull or runtime download is needed inside the internal network. The launcher does not fetch a missing archive or substitute an unpinned program from `PATH`.

This follows the reference brain's [vendored-server approach](https://github.com/team-redbull/redbull-brain/blob/main/mcp/README.md), adapted to the SDS stack. The SDS release remains pinned to v2.2.0; it does not copy the reference team's older pin or assume that their Prometheus/Loki layout exists here. Archive provenance, sizes and SHA-256 values are recorded in `mcp/grafana/release-manifest.json`. Local verification results and remaining acceptance requirements are recorded in `docs/VALIDATION.md`.

The archive set covers Linux x86-64, Linux ARM64, macOS ARM64 and Windows x86-64. Follow [the local Grafana setup](../mcp/grafana/README.md) for the offline check, internal URL/token setup, CA handling and connected-host refresh procedure. An unsupported platform or missing/mismatched archive must be corrected in the transferred package before use.

The upstream v2.2.0 README requires **Grafana 9.0 or later for full functionality**; earlier versions can lack datasource APIs. Obtain the installed Grafana and Elasticsearch/plugin versions before enabling this integration. That minimum does not prove every tool is compatible with the installed versions or permissions.

## Fixed tools and outbound behavior

The local launcher forces stdio, read-only mode and these tool categories: `search`, `datasource`, `dashboard`, `elasticsearch`. Prometheus remains excluded until its deployment is confirmed. There is no HTTP MCP listener and no online documentation tool in this profile. Keep raw API, SQL, rendering, plugin installation, assistant and write categories outside this first-release configuration.

Anonymous usage reporting is disabled with the upstream flag and environment settings. The launcher removes inherited `OTEL_*` configuration so an unrelated shell's trace/log exporter is not carried into this customer process. It also clears inherited `GRAFANA_*` configuration before setting the selected endpoint/token, and clears ambient HTTP/HTTPS/ALL proxy variables. This is a direct-connection profile: a deployment that requires a proxy needs a deliberately reviewed launcher adaptation. Do not work around this by bypassing the launcher. The upstream usage-statistics switch alone does not disable separately configured OpenTelemetry exporters. These launch settings are distinct from a network firewall: enforce the organization's outbound policy in the internal runtime as well.

The upstream [v2.2.0 transport implementation](https://github.com/grafana/mcp-grafana/blob/v2.2.0/cmd/mcp-grafana/main.go) initializes the stdio Grafana context once from process configuration. Its request-selected `X-Grafana-URL` mechanism belongs to HTTP middleware and is not installed in the stdio path. The SDS profile does not enable dynamic per-call organization selection. These facts support the configured endpoint behavior; they do not replace datasource authorization or establish a general network sandbox.

The packaged server still needs an authorized route to the selected **internal Grafana**. Grafana in turn must reach its approved internal datasources. Vendoring the executable does not supply a Grafana instance, credentials, a datasource map or the model/client connection. No connection to the user's Grafana or Elasticsearch has been performed during this build.

## Bind access to a customer

Use a dedicated service account and datasource permissions whose real backend reach is limited to the active customer. Depending on the Grafana edition and layout, this can require separate organizations/instances or an approved authorization gateway. A dashboard folder, variable, query selector or datasource display name is not the access boundary. Inspect the actual token and datasource capabilities with the platform owner.

Set `SDS_GRAFANA_URL` and `SDS_GRAFANA_TOKEN` through the approved runtime mechanism. The launcher requires the explicit HTTPS endpoint and token, then maps them to the upstream process's connection variables. Do not depend on an ambient Grafana URL, token, extra header or alternate authentication setting from another customer's shell. Use the host's trusted CA store or set `SDS_GRAFANA_CA_FILE` to an existing approved PEM CA bundle; the launcher passes it through the supported `--tls-ca-file` option. Never disable certificate verification. Inspect returned datasource UIDs and map them to the active customer and cluster before querying. Start a fresh client session when changing customer.

## Elasticsearch

Use the reviewed datasource UID and customer-scoped index alias. Confirm installed Elasticsearch/plugin versions, timestamp field, field mappings and the purpose of the data. Scope queries to a small interval and return only approved fields. Backend authorization must prevent cross-customer reads even when a query is malformed. If the official server exposes more than the approved boundary, leave the integration disabled and use reviewed exports or a narrowly constrained internal gateway.

Elasticsearch is not assumed to be the repository's vector store, a Prometheus substitute or StorageGRID search integration. The user has not supplied that architecture. Use `knowledge/observability/custom-exporter-contract.md` and the correlation runbook to establish it. Do not invent metric, index or label names.

## Internal acceptance

In an approved non-production context, verify the selected identity, list permitted datasources, read one known dashboard, execute one bounded known Elasticsearch query and confirm cross-customer access is denied. Inspect output for credentials and sensitive content. Record binary version/hash, client version, Grafana/plugin version, datasource IDs, query window, outcome and reviewer in the private validation record.

Only after those checks classify the integration as environment-tested. The optional JSON under `config/` is a merge example: add it to the selected customer's explicit local MCP profile after setting the internal connection. A local archive check or tool-list handshake does not establish backend authorization or live query correctness.

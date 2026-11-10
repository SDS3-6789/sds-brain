---
id: redhat-offline-portal
title: Red Hat Offline Knowledge Portal and Ceph applicability
area: meta
type: knowledge
applies_to: [rhokp, okp-mcp-source-1.0.2]
confidence: documented
last_verified: 2026-11-10
sources: [redhat-okp-mcp, redhat-okp-mcp-config, redhat-okp-mcp-formatting, podman-quadlet]
---

# Red Hat Offline Knowledge Portal and Ceph applicability

Red Hat `okp-mcp` is an optional container service backed by a separate RHOKP Solr index. The SDS integration uses Linux/Podman with either an existing portal or a new portal pair. Its images, entitled content and access key must be supplied through the approved internal process. See the [integration guide](../../mcp/okp/README.md) and [deployment paths](../../deploy/podman/README.md).

`sds-knowledge` retrieves local brain files and approved imports. It does not query RHOKP; `sds-okp` is a distinct HTTP service. A local Red Hat corpus on disk does not establish that RHOKP exists or that its index contains the same content.

The reviewed OKP MCP source uses RHEL-oriented query shaping and can annotate non-EOL results as RHEL without establishing their actual product. Search has no explicit product/version argument. Confirm a known RHCS/Ceph document, its product and exact version in the actual portal before using that service for Ceph guidance. The label alone is insufficient, and no Ceph cluster execution is implemented.

Keep customer-specific incident material out of shared portal queries. The local knowledge process's customer scope is not an authorization boundary for the portal. Inspect retrieved material as untrusted evidence and retain its original title, product, version and source.

# Red Hat okp-mcp integration

This optional service follows the reference brain's architecture: Red Hat's own `okp-mcp` container queries an existing RHOKP Solr index, and the MCP client connects over Streamable HTTP. The SDS knowledge server remains a separate local-file search service.

Use the [Linux/Podman setup](../../deploy/podman/README.md) for either an existing portal or a new portal and MCP pair. This repository supplies client profiles and deployment templates. The images and entitled RHOKP content must be prepared separately; there is no startup download or bundled OKP executable.

## Source and runtime identity

The [upstream source record](upstream-source.json) pins the reviewed Red Hat code and reference repository. Upstream source declares version 1.0.2 and Python 3.12+ with third-party dependencies. Run its prepared container image inside the network; the SDS stdlib servers continue to require Python 3.9+.

A source commit is not a verified container digest. Before transfer, verify the selected image architecture, digest, provenance and actual runtime settings. The examples deliberately contain image placeholders. No container runtime, image or portal was available for a live acceptance test here.

## Client profiles

For shared brain knowledge plus a local OKP endpoint, create a new ignored local profile:

```bash
export SDS_BRAIN_DIR="$PWD"
cp config/knowledge-okp.example.json config/mcp.okp.local.json
claude --strict-mcp-config --mcp-config config/mcp.okp.local.json
```

For a private customer session that also needs Grafana, use `config/knowledge-grafana-okp-private.example.json`, after setting the private context and Grafana variables documented in the root README. Preserve existing approved Objectify/custom entries rather than overwriting their profile. Check the effective connections in `/mcp`.

The HTTP endpoint defaults to `http://127.0.0.1:8000/mcp` on the client's own machine. For a service on another Linux host, keep the listener on that host's loopback and use your approved SSH tunnel, for example `ssh -N -L 8000:127.0.0.1:8000 <approved-host>`. A shared endpoint needs an approved authenticating TLS proxy; it is not configured by these examples.

## Read-only use and Ceph applicability

OKP searches documentation; it does not run Ceph commands or inspect your clusters. Do not send customer identifiers, credentials, incident dumps or object data to its shared search service. Customer isolation in SDS local retrieval does not constrain OKP's portal corpus or request logs.

The reviewed upstream code is RHEL-oriented: its search interface has no product parameter, and its result formatter can label a non-EOL result as RHEL even when a different product is present. That annotation is not evidence of RHCS applicability. Inspect the returned title, product metadata, version and actual document. Verify a known RHCS/Ceph document is present in your portal before relying on it for Ceph. The SDS Ceph runbooks and approved local RHCS imports remain available independently.

`MCP_EXCLUDE_KBASE` only changes part of the search flow in the reviewed version; it is not an authorization or comprehensive content-exclusion control. Portal entitlement, permitted audience and actual corpus determine what may be retrieved. A full Red Hat export on disk does not by itself establish that RHOKP is installed.

## Runtime settings selected by the templates

- `MCP_TRANSPORT=streamable-http`, internal bind `MCP_HOST=0.0.0.0`, `MCP_PORT=8000`; publish only host loopback.
- `MCP_SOLR_URL` is the base URL, without `/solr/portal/select`. It must be reachable from inside the container, not just from its host.
- `MCP_OKP_HTML_URL` points to the approved portal HTML mirror, or `-` disables the optional outline-anchor lookup. New-portal templates use its private container-network name.
- `MCP_MAX_RESPONSE_CHARS=30000` bounds upstream response characters. This is not the SDS knowledge server's serialized-byte cap.
- `MCP_GLITCHTIP_DSN` is empty. No environment file or host environment is imported into the MCP container. The reviewed upstream enables exception reporting when a nonempty DSN is configured; its local metrics endpoint is separate.
- There is no automatic image update and `Pull=never` prevents runtime image pulls. Existing-portal TLS/auth requirements must be checked against the approved image; the reviewed upstream exposes no dedicated Solr auth/CA settings.

## Acceptance inside the internal network

After the operator deploys the selected templates, verify the local image identity, portal readiness and MCP initialization. List its actual tools through the client, search for a known document, read a bounded section, and verify product/version and document identity. The reviewed upstream returns canonical `access.redhat.com` citations; setting the HTML mirror does not rewrite those URLs. Verify offline document retrieval through MCP rather than assuming the clickable citation is local. Check a known RHEL document and a known RHCS document separately. Record absence or mismatch rather than claiming complete Ceph coverage.

Source review and local static checks do not establish internal connectivity, entitled content availability, native client interoperability or image acceptance.

## Sources

- [Reference integration](https://github.com/team-redbull/redbull-brain/blob/cd866d4ee510b299c415f92a90b7f525d30cf04c/mcp/servers/okp-mcp.md).
- [Upstream setup](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/README.md), [configuration](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/src/okp_mcp/config.py), [result formatting](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/src/okp_mcp/formatting.py).
- [Podman Quadlet reference](https://docs.podman.io/en/v4.6.1/markdown/podman-systemd.unit.5.html).

# Linux/Podman deployment for Red Hat OKP MCP

These are optional rootless Quadlet templates for a Linux host with systemd, cgroups v2 and Podman 4.6+ (including its Quadlet generator). Use an approved service host with capacity for the portal image, indexing and persistent data. A Ceph data node is not assumed to be the deployment host. No Ceph device, socket or credential is mounted.

Choose exactly one path below. Both install a service named `sds-okp.service`; they must not be installed together. The examples have no `[Install]` section, so installing them does not opt into boot/login startup. They do not include a Route, cluster deployment or public listener.

## Prepare the images on a connected host

Use the approved registry login and Red Hat entitlement process. Obtain the RHOKP access key separately through the [Red Hat portal](https://access.redhat.com/offline/access). Never put it in this repository or a shell command argument.

The upstream image repositories are:

- `quay.io/redhat-user-workloads/rhel-lightspeed-tenant/rhel-knowledge-bridge` for OKP MCP.
- `registry.redhat.io/offline-knowledge-portal/rhokp-rhel9` for a new portal.

Select reviewed images for the target CPU architecture. Record immutable digests and the image's actual source/version metadata. The source pin in `mcp/okp/upstream-source.json` is not an image pin. Mirror into the approved internal registry or export the approved images for transfer. For an archive workflow, with each variable set to an approved immutable image reference:

```bash
podman pull "$OKP_MCP_IMAGE"
podman save --format oci-archive --output okp-mcp.oci.tar "$OKP_MCP_IMAGE"
# Only when provisioning a new portal:
podman pull "$RHOKP_IMAGE"
podman save --format oci-archive --output rhokp.oci.tar "$RHOKP_IMAGE"
sha256sum okp-mcp.oci.tar rhokp.oci.tar > images.sha256
```

For an existing portal, omit its pull/save and list only `okp-mcp.oci.tar` in the checksum command. Transfer the archives and their approved checksum record using your normal offline process. On the disconnected host:

```bash
sha256sum --check images.sha256
podman load --input okp-mcp.oci.tar
# New portal only:
podman load --input rhokp.oci.tar
```

Inspect each loaded image with `podman image inspect <loaded-reference>` and record its immutable local ID and any repository digest. Replace every `Image=` placeholder with the inspected local ID or an approved digest reference that resolves locally. Validate with `podman image exists <exact-Image-value>` before starting. This matters because archive loading can change which repository names/digests are available locally. All templates use `Pull=never` and contain no auto-update setting.

No images, entitlement or access keys were downloaded during this repository change. Templates remain unconfigured until your actual approved images are selected.

For a new portal, verify that the selected RHOKP distribution and transferred content support first-start activation/indexing without internet. Follow the applicable Red Hat disconnected-content procedure on the preparation host. An image archive plus an access key alone is not evidence that all required content is present.

## A. Use an existing RHOKP portal

Confirm its approved Solr **base** URL and that the `portal` core contains the expected content. Solr is a dependency, not an MCP endpoint. Check reachability from the Podman container network: `localhost` inside a separate container refers to that container. Use your approved internal hostname, or a deliberately configured Podman network for a portal already on the same host.

In a local staging directory, copy `existing-portal/sds-okp.container.example` to `sds-okp.container`. Replace its image pin and `MCP_SOLR_URL`. The optional HTML lookup is disabled with `MCP_OKP_HTML_URL=-`; enable it only with a verified internal mirror URL. Confirm TLS/auth compatibility against your selected image before installation; never bypass TLS verification.

Install the edited file under `~/.config/containers/systemd/`, preserving any existing units. Do not install the new-portal files.

## B. Provision a new RHOKP portal with OKP MCP

Create a local staging directory. Copy the files under `new-portal/` into it and remove `.example` from the two container filenames. Replace both image pins. Create `~/.config/sds-brain/rhokp.env` outside the checkout using your approved secret delivery method; its content is `ACCESS_KEY=` followed by the actual key. Restrict the directory and file to the service user (`0700` and `0600`). `rhokp.env.example` documents the shape only.

Install the four edited files under `~/.config/containers/systemd/`:

```text
sds-okp.network
sds-rhokp-data.volume
sds-rhokp.container
sds-okp.container
```

The portal's Solr and HTML ports remain on the private Podman network. Only MCP port 8000 is published, on host loopback. A named volume preserves the Solr data across container recreation; do not remove it when changing images. A portal content update and its persistent index still require the vendor's applicable update procedure.

## Start and verify after operator review

Review the generated units on the intended Linux host:

```bash
/usr/lib/systemd/system-generators/podman-system-generator --user --dryrun
systemctl --user daemon-reload
systemctl --user start sds-okp.service
systemctl --user status sds-okp.service
```

For a new portal, the dependency starts `sds-rhokp.service` first. Systemd ordering does not establish that indexing is complete. Wait for portal readiness and a nonempty known corpus before attempting searches. Inspect the bounded journal with `journalctl --user -u sds-rhokp.service -n 50 --no-pager`. Logs can contain internal information; review them locally.

For the new-portal layout, a local read-only content check is:

```bash
podman exec sds-rhokp curl --fail --silent --show-error \
  'http://127.0.0.1:8983/solr/portal/select?q=*:*&rows=0'
```

This assumes `curl` is present in the selected portal image; otherwise use its approved diagnostic tool or a prepared local diagnostic container on the same network. Do not download a tool at runtime. A nonzero count is only a readiness check, not proof of RHCS coverage.

Check MCP initialization at the loopback endpoint:

```bash
curl --fail --silent --show-error --max-time 30 -N \
  http://127.0.0.1:8000/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  --data '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"sds-okp-acceptance","version":"1.0"}}}'
```

Then connect the [optional client profile](../../config/knowledge-okp.example.json), inspect the actual tool list, and retrieve known RHEL and RHCS documents separately. Review the [applicability limits](../../mcp/okp/README.md) before using results for Ceph. No service is installed or started by running the repository's local checks.

To stop the MCP service: `systemctl --user stop sds-okp.service`. For the new-portal path, stop `sds-rhokp.service` separately when appropriate; `Requires=` does not make stopping the dependent stop its dependency. Enabling boot/login startup is an explicit operator choice outside these templates.

See the pinned [upstream setup](https://github.com/rhel-lightspeed/okp-mcp/blob/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/README.md), [upstream Quadlet files](https://github.com/rhel-lightspeed/okp-mcp/tree/a4469e1365789d1619a9d2276fa0ed2e80ee18b3/quadlet), and [Podman reference](https://docs.podman.io/en/v4.6.1/markdown/podman-systemd.unit.5.html).

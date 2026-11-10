# Offline Grafana MCP

This directory carries the official Grafana MCP **v2.2.0** release archives and an SDS launcher. Transfer this directory with the rest of the repository into the internal network. The internal launch path uses only local files and the approved internal Grafana endpoint.

The reference project's [Grafana guide](https://github.com/team-redbull/redbull-brain/blob/main/mcp/servers/grafana.md) also ships archives with a platform-selecting Python launcher. SDS uses its own launcher and a newer, separately pinned official release, with Elasticsearch enabled and Prometheus left conditional.

## Contents

| Path | Purpose |
|---|---|
| `launch.py` | Select the current platform, verify the archive and extracted executable, and run the fixed read-only stdio profile |
| `release-manifest.json` | Official release identity, asset filenames, byte sizes, hashes and recorded verification evidence |
| `vendor/` | Actual release archives transported with the repository |
| `LICENSE.upstream` | Apache-2.0 license copied from the pinned official upstream release |
| `../../scripts/vendor_grafana.py` | Verify the complete local archive set; download the pinned set only when explicitly requested on a connected staging host |

The included platforms are Linux x86-64, Linux ARM64, macOS ARM64 and Windows x86-64. CPU aliases such as `amd64`/`x86_64` and `aarch64`/`arm64` are normalized by the launcher. The macOS archive requires Apple Silicon; it is not an Intel macOS binary. No fallback download or arbitrary executable on `PATH` is used.

The two included Python MCPs and this launcher require Python 3.9 or newer. The shell examples use `python3`; on native Windows, use your approved Python executable and set the MCP entry's `command` accordingly (for example `python` or its absolute path). The Grafana server itself is a compiled executable. The upstream README specifies Grafana 9.0 or later for full functionality; confirm the installed server/plugin versions during acceptance.

## Inside the internal network

1. Transfer and extract the complete SDS repository through the normal approved process. Preserve the archives as binary files. Do not transfer only the JSON manifest or source-code files.
2. Run the local checks from the repository root:

   ```bash
   python3 scripts/vendor_grafana.py --check
   python3 mcp/grafana/launch.py --check
   ```

   These check local material without contacting Grafana or a public website. The vendor check covers the archive set; the launcher check selects the current platform. A missing archive, wrong platform or checksum mismatch is a packaging problem; correct the transferred files before continuing.
3. Have the operator supply `SDS_GRAFANA_URL` (the selected customer's HTTPS Grafana URL) and `SDS_GRAFANA_TOKEN` (a read-only service-account token) through the approved runtime mechanism. The optional MCP configuration contains no credential value. Do not put a real token into shell history, a committed file or a shared incident note.
4. Use the host's approved CA trust. When a private CA is not already trusted, set `SDS_GRAFANA_CA_FILE` to the existing approved PEM CA bundle. The launcher passes the file through upstream's `--tls-ca-file`; it never disables certificate verification.
5. For a new profile, copy `config/knowledge-grafana-private.example.json` to `config/mcp.private.local.json`; it contains the bound knowledge server plus the local Grafana launcher. For an existing profile, merge the `sds-grafana` entry from `config/mcp-integrations.example.json` and preserve approved local entries. Keep `SDS_BRAIN_DIR`, `SDS_CUSTOMER` and `SDS_CLUSTER` set to the selected restricted checkout/context. Enable Objectify only after its separate contract acceptance.
6. Start a fresh Claude session with that explicit local profile, inspect `/mcp`, then perform the small internal acceptance sequence in `docs/observability-integration.md`.

The MCP entry calls `python3 mcp/grafana/launch.py` through an absolute repository path. The normal launch takes no passthrough flags: it fixes stdio, read-only mode and the selected categories. `--check` validates local files without starting the upstream server. The launcher caches the verified executable under the operating system's user cache; it does not modify the transferred archive.

The profile includes only dashboard search/read, datasource discovery and Elasticsearch query categories. It disables writes and anonymous usage reporting, removes inherited `OTEL_*` settings, and replaces inherited `GRAFANA_*` settings with the explicit SDS connection. Ambient HTTP/HTTPS/ALL proxy variables are cleared. It connects directly to the selected internal Grafana; a required proxy must be added through a reviewed launcher adaptation, not an untracked environment override. The official server can still return sensitive dashboard or search content: customer-scoped backend permissions and reviewed query fields remain necessary.

The pinned upstream stdio implementation reads its Grafana configuration once when the process starts. Its HTTP `X-Grafana-URL` override middleware is not used on that path, and the SDS profile does not enable dynamic per-call organization selection. See [the upstream transport implementation](https://github.com/grafana/mcp-grafana/blob/v2.2.0/cmd/mcp-grafana/main.go). This is a configured process boundary, not a substitute for network or backend access controls.

## Verification boundaries

Checksums establish that the packaged archive matches the pinned release bytes. A local startup/tool-discovery test establishes only that the executable can start and expose the expected local interface on the tested platform. Neither proves that an internal CA, credential, Grafana API, Elasticsearch plugin or datasource authorization works.

Consult `docs/VALIDATION.md` and the manifest for the observed verification results. Do not classify an unexecuted platform as runtime-tested. No live customer Grafana or Elasticsearch query is part of this build's validation.

## Refresh on a connected staging host

Updates are prepared outside the internal runtime. The launcher never checks for or downloads an update.

1. Select an exact upstream release and review its changes, license, required Grafana version and command-line flags. The pinned source for this package is [Grafana MCP v2.2.0](https://github.com/grafana/mcp-grafana/releases/tag/v2.2.0).
2. For the currently pinned release, use the explicit connected-host download command:

   ```bash
   python3 scripts/vendor_grafana.py --download
   python3 scripts/vendor_grafana.py --check
   ```

   Public internet access is needed only for the download step. A different version requires a reviewed manifest update first; this command is not an automatic upgrade to the latest release.
3. When changing the version, update `release-manifest.json`, the archive set and accompanying upstream license material together. Match the official release filenames, byte sizes and SHA-256 values. Preserve any additional manifest fields required by the launcher, including the extracted executable hashes. Generate those hashes from the newly verified archives, not from an unrelated installed executable.
4. Run the launcher's checks and meaningful regression tests. On each available platform, start the binary with the fixed SDS profile, inspect stderr, complete local MCP initialization and list the tools. Check that writes, public documentation lookup and unexpected categories remain absent. Record which platforms were only byte-verified.
5. Regenerate the repository's package manifest and archive through the release process. Transfer the complete updated package into the internal network and repeat scoped internal acceptance before team rollout.

Preserve `LICENSE.upstream` and the upstream notices when redistributing the archives. The reference project's vendoring layout is architectural guidance; it is not a reason to copy its credentials, deployment assumptions or unrelated MCP servers.

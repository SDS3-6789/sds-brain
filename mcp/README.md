# MCP integration map

| Integration | Implementation | Client configuration | Deployment |
|---|---|---|---|
| SDS knowledge | [Local stdlib server](knowledge/server.py) | [Default shared profile](../.mcp.json), [private profile](../config/knowledge-private.example.json) | Started by the MCP client |
| team-brain plugin | [Local Claude package](../docs/PLUGIN.md), same canonical SDS knowledge server | `plugins/team-brain/.mcp.json`, explicit `SDS_BRAIN_DIR` and optional fixed aliases | Optional client plugin; no live service enabled by default |
| Grafana | [Verified offline launcher](grafana/README.md) and bundled archives | [Knowledge + Grafana private profile](../config/knowledge-grafana-private.example.json) | Local stdio executable |
| Objectify | [Restricted adapter](../docs/objectify-integration.md), disabled until reviewed | [Optional integration entries](../config/mcp-integrations.example.json) | Local stdio adapter; internal API access only after acceptance |
| Red Hat okp-mcp | [Upstream container service](okp/README.md), optional | [Knowledge + OKP](../config/knowledge-okp.example.json), [knowledge + Grafana + OKP private](../config/knowledge-grafana-okp-private.example.json) | [Linux/Podman templates](../deploy/podman/README.md) |

The default `.mcp.json` starts only shared local retrieval. Optional services must be selected explicitly in a local client profile. Preserve existing approved entries when updating a profile. The client starts neither Podman nor RHOKP automatically.

`sds-knowledge` indexes local files and the source catalog; it does not query RHOKP. `sds-okp` is a separate HTTP connection to the upstream Red Hat service. Knowledge-server customer filters do not apply to that service, Grafana, other tools or conversation history.

The added [SQLite document snapshot](../docs/SQLITE.md) has its own offline CLI/direct SQL interface. It is not an additional MCP service and the current knowledge MCP does not read it automatically.

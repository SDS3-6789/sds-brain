---
id: "rb-cephadm-daemon-triage"
title: "Cephadm daemon and container failure triage"
area: "ceph"
type: "runbook"
applies_to: ["rhcs-7.1", "rhcs-8.1", "rhel-9.6", "rhel-9.8"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["ceph-squid-cephadm", "rhcs-8-operations", "rhel-9-containers", "rhcs-8-installation", "rhcs-8-upgrade", "podman-container-inspect", "ceph-squid-rgw-service"]
---

# Cephadm daemon and container failure triage

## Scope and prerequisites

Use this for an observed daemon failure, unexpected restart or discrepancy between the orchestrator and host. Select the customer, cluster and FSID, then identify the exact service, daemon and host. Read-only mode applies to both the cluster and host. This template is documented but has not been run on the owner's systems.

The commands below presume an existing approved session and installed tools. Creating a new troubleshooting container, installing a utility or logging into another host are separate connection actions. A host may contain remnants from another cluster; never treat every local container as belonging to the selected FSID.

## Compare control-plane and host evidence

Set `BRAIN_SERVICE` and `BRAIN_DAEMON_ID` from the already verified incident inventory. Check the installed CLI's supported filters; if either identity is unknown, stop at the inventory gap instead of listing unrelated services.

```bash
ceph fsid
ceph orch status
ceph orch ls --service_name="$BRAIN_SERVICE"
ceph orch ps --service-name "$BRAIN_SERVICE" --daemon-id "$BRAIN_DAEMON_ID" --format json
```

Record the chosen daemon's reported host, state, version, image and event timestamps. Use the plain service summary here; do not export full service specifications, which can contain inline TLS private keys. Cephadm's troubleshooting documentation describes per-service and per-daemon events and host/container inspection. An orchestrator snapshot can be stale relative to the host; retain both observation times.

On the identified host, select the exact existing systemd unit into `BRAIN_UNIT`; derive it from observed inventory, not a guessed naming pattern. Set `BRAIN_CONTAINER_ID` to the selected daemon's exact container ID from the scoped orchestrator evidence, and verify its host and FSID mapping. If the ID is absent or ambiguous, stop rather than inspecting every host container. Limit returned properties:

```bash
systemctl show "$BRAIN_UNIT" -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts
podman container inspect "$BRAIN_CONTAINER_ID" --format '{{.ID}} {{.Name}} {{.Image}} {{.State.Status}}'
journalctl -u "$BRAIN_UNIT" --since "$BRAIN_SINCE" --until "$BRAIN_UNTIL" --no-pager -n 200
```

Set `BRAIN_SINCE` and `BRAIN_UNTIL` to the incident's approved interval. Inspect any output locally for credentials or private customer content before sharing. Podman's formatted inspection selects the listed fields only; never omit the format or return the complete container environment/configuration. Verify these fields in the installed Podman manual before use.

## Work through concrete explanations

| Observed failure | Evidence to seek |
|---|---|
| Process exits repeatedly | Exit status, first relevant error, crash time and resource pressure |
| Image cannot start or be fetched | Approved image reference/digest, registry reachability and runtime error |
| Orchestrator cannot manage host | Host identity, SSH/connectivity errors and placement events |
| Service exists on unexpected host | Inventory, deployment spec history and change record |
| Failure begins during upgrade | Stage, mixed daemon versions, image and supported upgrade path |

Use the RHEL container guide for runtime behavior. Match image/package architecture and installed runtime version before treating a public issue as the same failure. The vendor installation and upgrade guides are background for prerequisites; they do not authorize reinstalling or upgrading during this investigation.

## Completion and escalation

Create a timeline connecting the last known healthy state, triggering event, first error and latest observation. State whether the host process is dead, the container is missing, or only the management view reports failure. If those observations disagree, explain the discrepancy as unresolved.

Do not restart, redeploy, remove or reconfigure daemons, pause orchestration, pull images, or rerun deployment. Preserve a small evidence bundle and propose the narrowest next diagnostic or a separate reviewed recovery plan. If other services share the affected host or failure domain, include that potential scope without assuming that they have also failed.

## Sources

- [Ceph Squid cephadm troubleshooting](https://docs.ceph.com/en/squid/cephadm/troubleshooting/)
- [Red Hat Ceph Storage 8 Operations Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/operations_guide/index)
- [RHEL 9 Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/index)
- [Red Hat Ceph Storage 8 Installation Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/installation_guide/index)
- [Red Hat Ceph Storage 8 Upgrade Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/upgrade_guide/index)
- [Podman container inspect reference](https://docs.podman.io/en/latest/markdown/podman-container-inspect.1.html)
- [Ceph Squid RGW service specifications and TLS](https://docs.ceph.com/en/squid/cephadm/services/rgw/)

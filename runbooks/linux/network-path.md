---
id: "rb-linux-network-path"
title: "RHEL storage network and endpoint path triage"
area: "linux"
type: "runbook"
applies_to: ["rhel-9.6", "rhel-9.8"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhel-9-networking", "rhel-9-tls", "rhel-9-performance", "rhcs-8-configuration", "rhcs-8-hardware"]
---

# RHEL storage network and endpoint path triage

## Identify the failing path

Choose the customer, cluster, host and destination before issuing a query. Separate the S3 client path, RGW-to-RADOS path, inter-OSD traffic, and management/monitoring path. Confirm whether the endpoint is a load balancer, direct daemon address or DNS alias. This is a documented read-only template and has not been validated against the user's networks.

Record the failure interval, direction, protocol and port. A successful request from the engineer's workstation does not prove connectivity from the affected RGW host. Use an already-approved session in the relevant network namespace.

## Inspect local state

```bash
ip -brief address
ip route show
ip -s link
nmcli device status
nmcli connection show --active
ss -s
chronyc tracking
chronyc sources -v
```

These outputs can expose internal topology; keep them scoped to the customer. NetworkManager's active profile is configuration evidence, while interface counters and socket summaries provide current operating evidence. Read the RHEL networking guide and local tool help for the installed versions.

For the observed interface, inspect its driver and statistics:

```bash
ethtool -i "$BRAIN_IFACE"
ethtool -S "$BRAIN_IFACE"
```

`BRAIN_IFACE` must be an interface observed on this host. Collect two bounded samples if deltas are needed; a lifetime error counter does not show whether errors are occurring now. Hardware-specific counters require the NIC/driver documentation to interpret. For bonds, inspect the selected bond's existing status and correlate its members with switch-side evidence.

## Follow the evidence

| Failure pattern | Next read-only question |
|---|---|
| Name resolves differently across clients | Which resolver, search path and returned address did each client use? |
| Timeout from one source path | Which route, interface, firewall and load-balancer path applies there? |
| TLS handshake failure | Which certificate chain, SNI hostname and protocol policy were presented? |
| Intermittent retransmission/error bursts | Do host and switch counters change during the same UTC interval? |
| Signature or monitor clock warnings | Do the relevant hosts show time synchronization issues? |
| Large transfers fail but small requests work | Is there evidence of MTU/path constraints, proxy limits or different operations? |

The Ceph configuration and hardware guides are references for intended networks. Compare the customer design to observation; do not assume all clusters use identical ports, VLANs, MTUs or NICs. The TLS guide supplies certificate and crypto background, not proof that this customer's chain is trusted.

## Bound active checks

DNS queries, TCP/TLS handshakes and HTTP HEAD requests are usually observational but still generate traffic. Prepare an endpoint-specific bounded check only when the relevant path is authorized. Avoid scanning subnets, broad packet capture, unlimited polling or bypassing certificate verification. If packet evidence is essential, define a separate narrow capture scope and protect captured data.

Finish with the failing path, observation point, evidence timestamps and unresolved layer. Do not bounce a bond, restart NetworkManager, flush rules, change MTU/offloads, renew addressing or edit DNS here. Hand a precise path and time window to the network/hardware owner when switch-side information is needed.

## Sources

- [RHEL 9 Configuring and managing networking](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/index)
- [RHEL 9 Securing networks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/index)
- [RHEL 9 Monitoring and managing system status and performance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/index)
- [Red Hat Ceph Storage 8 Configuration Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/configuration_guide/index)
- [Red Hat Ceph Storage 8 Hardware Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/hardware_guide/index)

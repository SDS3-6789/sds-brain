---
id: runbook-storagegrid-connectivity
title: Diagnose StorageGRID S3 connectivity and load-balancer paths
area: storagegrid
type: runbook
applies_to: [storagegrid-11.9]
confidence: documented
last_verified: 2026-11-09
sources: [netapp-sg119-client-connections, netapp-sg119-client-ports, netapp-sg119-lb-endpoints, netapp-sg119-lb-monitor, netapp-sg119-network, netapp-sg119-logs]
---

# Diagnose StorageGRID S3 connectivity and load-balancer paths

## Scope

Use one named customer, grid, application path, and UTC interval. Identify the exact FQDN, approved port, TLS hostname, endpoint type, and release/hotfix from authorized inventory. Do not scan all grid addresses. Interface labels and port assumptions must be checked against the installed release.

## Trace the path

1. Draw the actual route in the incident record: client resolver → approved VIP/load balancer → StorageGRID endpoint → storage service. Include an external proxy/load balancer only if inventory establishes that it exists. Compare the application's configured hostname/port/certificate trust with the intended connection values. [Client connection requirements](https://docs.netapp.com/us-en/storagegrid-119/admin/configuring-client-connections.html).
2. Read endpoint settings: protocol, port, binding mode, tenant restrictions if configured, certificate name/expiry, and the chosen HA group. Endpoints are configuration objects; merely reaching an Admin Node does not establish that the desired S3 endpoint is reachable. [Endpoint configuration reference](https://docs.netapp.com/us-en/storagegrid-119/admin/configuring-load-balancer-endpoints.html).
3. Read the HA group's current roles and correlate a role transition with the failure interval. An active-backup group's backup member need not show normal request traffic. Compare request distribution across active load-balancing nodes using existing charts. [Load-balancing monitoring](https://docs.netapp.com/us-en/storagegrid-119/monitor/monitoring-load-balancing-operations.html).
4. Check existing network observations for the named path: DNS answer, route/interface, connection establishment, certificate validation, and packet loss/retransmission evidence where available. The network guide distinguishes StorageGRID network roles; do not substitute a reachable management path for the application path. [Networking guide](https://docs.netapp.com/us-en/storagegrid-119/network/index.html).

## Do not bypass the path accidentally

NetApp documents load-balancer connections and direct LDR connections separately. The documented direct-LDR defaults are not a recommendation to bypass the supported customer path. Use the inventory's assigned endpoint port. A direct-node comparison requires an explicitly approved diagnostic plan because it can change the failure domain and application behavior. [Connection and port reference](https://docs.netapp.com/us-en/storagegrid-119/admin/summary-ip-addresses-and-ports-for-client-connections.html).

For one approved metadata-only request, correlate the client timestamp/status with existing endpoint access logs. Retain the source node and request identifier where provided. A TLS failure occurs before S3 authorization; an S3 error response demonstrates a different point of progress through the path. [Log reference](https://docs.netapp.com/us-en/storagegrid-119/monitor/logs-files-reference.html).

## Output

Report the last confirmed working layer and first unconfirmed/failing layer. State whether evidence supports DNS, transport, TLS, endpoint binding, HA, request distribution, or backend-service investigation. Do not change DNS, certificates, routes, HA priority, endpoint bindings, or firewall rules during this read-only workflow. Include the exact scoped next read, not a generic request for every log.

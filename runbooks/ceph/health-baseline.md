---
id: "rb-ceph-health-baseline"
title: "Ceph health warning baseline"
area: "ceph"
type: "runbook"
applies_to: ["rhcs-7.1", "rhcs-8.1"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["ceph-squid-monitoring", "ceph-reef-health", "ceph-squid-health", "rhcs-7-troubleshooting", "rhcs-8-troubleshooting"]
---

# Ceph health warning baseline

## Purpose and boundary

Identify the scope and urgency of a Ceph warning without changing cluster state. This is a documented investigation template; it has not been executed on the owner's clusters. It does not establish a connection or grant an agent shell access.

Select one customer and cluster in the private inventory. Use that cluster's already-open, approved administrative session. Confirm the expected FSID; stop if it differs, is missing, or the command cannot reach monitors. Do not fall back to another cluster's default configuration. Starting a new cephadm shell may create a local container and is outside the command block below.

## Collect an initial status snapshot

```bash
ceph fsid
ceph -s --format json
ceph health detail --format json
ceph versions
ceph quorum_status --format json
ceph osd stat
ceph pg stat
ceph df --format json
```

Save the timestamp and required fields in the customer's incident workspace. These commands inspect cluster status, daemon versions, monitor quorum, OSD/PG state and capacity. They do not impose hard response-size, execution-time or backend-work limits; keep full output local and share only reviewed relevant fields. Prefer existing telemetry if the cluster is overloaded. Use the monitoring reference for output meaning and the installed product's guide for version differences. Avoid continuous polling until a useful interval and duration have been agreed.

## Triage the actual health identifiers

Ceph health checks have distinct identifiers. Record all returned identifiers and associated affected daemons or PGs. Distinguish the aggregate severity from observed client impact; a green S3 health probe is limited evidence about that endpoint and operation.

| Evidence | Investigation route |
|---|---|
| Monitor unavailable, clock issue, command timeout | Establish quorum/time/network evidence before OSD recovery analysis |
| Down OSD, slow requests or recovery warnings | `slow-ops-and-recovery.md` |
| PG inconsistency, incomplete state or unfound objects | Preserve PG/OSD evidence and escalate to the storage owner/vendor |
| RGW failures with healthy RADOS | `rgw-request-triage.md` |
| Failed cephadm daemon | `cephadm-daemon-triage.md` |
| Capacity-related identifiers | Compare per-OSD and relevant pool capacity before proposing any action |

The health-check references explain the conditions associated with individual flags. Use the matching Reef/Squid family only after build selection; downstream guides and advisories remain authoritative for the vendor deployment.

## Turn the snapshot into an investigation

Ask when the customer first observed impact, which operations fail, and whether a maintenance or workload change preceded it. Compare the current state with a recent healthy interval from the same cluster. Record discrepancies between metrics, logs and CLI status instead of choosing the most convenient source.

Do not mute the warning, acknowledge a crash, adjust full ratios, mark OSDs out, start repair or initiate recovery here. A warning can disappear because a condition cleared, because monitoring lost visibility, or because someone muted it; verify which happened.

## Expected result

Produce a short incident update with verified customer/cluster scope, health identifiers, affected services, current client impact, a UTC timeline, evidence links and the next diagnostic question. Mark cause as unknown unless independent evidence supports it. If quorum is unavailable, data may be inaccessible, or redundancy is severely reduced, involve the storage owner immediately and retain the original outputs.

## Sources

- [Ceph Squid cluster monitoring](https://docs.ceph.com/en/squid/rados/operations/monitoring/)
- [Ceph Reef health checks](https://docs.ceph.com/en/reef/rados/operations/health-checks/)
- [Ceph Squid health checks](https://docs.ceph.com/en/squid/rados/operations/health-checks/)
- [Red Hat Ceph Storage 7 Troubleshooting Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html/troubleshooting_guide/index)
- [Red Hat Ceph Storage 8 Troubleshooting Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/troubleshooting_guide/index)

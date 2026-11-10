---
id: "rb-ceph-slow-ops"
title: "Ceph slow operations, PG recovery and backfill triage"
area: "ceph"
type: "runbook"
applies_to: ["rhcs-7.1", "rhcs-8.1"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhcs-8-osd-troubleshooting", "rhcs-8-pg-troubleshooting", "ibm-ceph-recovery", "ibm-ceph-throttling", "ceph-squid-mclock", "ceph-squid-configuration", "ceph-reef-pg-json", "ceph-squid-pg-json"]
---

# Ceph slow operations, PG recovery and backfill triage

## Start conditions

Run the health baseline first and retain its verified FSID. Work in the same selected customer/cluster session. This procedure is read-only and has not been validated on the user's production systems. Its goal is to distinguish a busy cluster from a stalled recovery path or underlying fault.

## Locate affected resources

Use the already-installed `jq` to project selected fields and cap returned samples. Reef and Squid's own QA clients read `dump_stuck` results from the `stuck_pg_stats` array inside a JSON object. Check that the installed release returns that structure; a schema/projection error is an evidence gap, not an empty healthy result.

```bash
set -o pipefail
ceph osd tree --format json | jq -e '{reported_nodes:(.nodes|length),sample:(.nodes[0:40]|map({id,name,type,status}))}'
ceph osd df --format json | jq -e '{reported_nodes:(.nodes|length),sample:(.nodes[0:40]|map({id,name,status,kb,kb_used,kb_avail,utilization}))}'
ceph osd perf | sed -n '1,41p'
ceph pg stat
ceph pg dump_stuck inactive --format json | jq -e 'if type == "object" and (.stuck_pg_stats|type) == "array" then .stuck_pg_stats | {reported:length,sample:(.[0:20]|map({pgid,state,up,acting}))} else error("Unexpected PG schema; inspect locally") end'
ceph pg dump_stuck stale --format json | jq -e 'if type == "object" and (.stuck_pg_stats|type) == "array" then .stuck_pg_stats | {reported:length,sample:(.[0:20]|map({pgid,state,up,acting}))} else error("Unexpected PG schema; inspect locally") end'
ceph pg dump_stuck unclean --format json | jq -e 'if type == "object" and (.stuck_pg_stats|type) == "array" then .stuck_pg_stats | {reported:length,sample:(.[0:20]|map({pgid,state,up,acting}))} else error("Unexpected PG schema; inspect locally") end'
```

These caps apply after the cluster returns the full result; they limit disclosure/output size, not backend work or response time. Samples are incomplete when reported counts exceed their limits. If the cluster is overloaded or inventory is very large, prefer existing telemetry and one PG already identified by health evidence. Take a second snapshot only after agreeing an observation interval. Compare recovery progress rather than assuming every non-clean state is permanently stuck. Red Hat documents the stuck-PG inspection commands.

For one PG identified in the output, an engineer can inspect its detailed query using `ceph pg <PG_ID> query`; replace the placeholder only after matching the selected cluster. Keep returned object and topology details in the customer's private incident record.

## Test competing explanations

| Observation | Follow-up evidence |
|---|---|
| Many affected OSDs share a host, rack or switch | Host pressure and physical/network event timeline |
| One OSD has abnormal latency | Disk/controller errors, workload and device identity |
| Backfill is capacity-blocked | Destination OSD fullness and applicable pool placement |
| Recovery is progressing while client latency rises | Workload versus background-recovery contention |
| PG cannot become active, incomplete/unfound data | Vendor escalation with exact PG state and acting set |

Red Hat's OSD guide identifies hardware, networking and system load as slow-request investigation areas. A slow OSD can be waiting for another OSD; the reporting daemon is not automatically the faulty device. Compare all members implicated by the evidence before proposing replacement.

## Separate recovery from tuning

IBM distinguishes recovery driven by available PG log history from backfill comparison. Use the distinction to understand progress; do not force one method by changing log retention. Some IBM operational articles cover broad release ranges. Their legacy throttle examples are not automatic recommendations for this fleet.

Inspect the Monitor configuration database/default values for a single implicated OSD:

```bash
ceph config get osd.OSD_ID osd_op_queue
ceph config get osd.OSD_ID osd_mclock_profile
```

Replace `OSD_ID` with the observed numeric ID. `config get` reports Monitor database or compiled-in default values; local files, command-line options, and runtime overrides can make the running daemon differ. Do not label these results effective runtime configuration. If effective settings are needed, prepare a narrowly selected read using the installed vendor's running-configuration interface. If a key is unavailable, retain that result and consult the exact release. The upstream mClock reference explains why scheduler profiles matter before proposing tuning.

## Stop and report

Do not change recovery rates, OSD flags, CRUSH weights, PG counts, full ratios or scrub settings. Do not run repair, purge, zap, benchmark or object deletion. Capture which hypothesis is supported, what would disprove it, and the next safe observation. Escalation should include scoped versions, PG/OSD IDs, capacity and latency evidence, recent changes and whether recovery is improving or stalled.

## Sources

- [RHCS 8 Troubleshooting Ceph OSDs](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/troubleshooting_guide/troubleshooting-ceph-osds)
- [RHCS 8 Troubleshooting Ceph placement groups](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/troubleshooting_guide/troubleshooting-ceph-placement-groups)
- [Differences between backfill, recovery and peering](https://www.ibm.com/support/pages/node/7176025)
- [Managing backfill, recovery and rebalancing throttles](https://www.ibm.com/support/pages/node/6963280)
- [Ceph Squid mClock configuration reference](https://docs.ceph.com/en/squid/rados/configuration/mclock-config-ref/)
- [Ceph configuration sources and inspection commands](https://docs.ceph.com/en/squid/rados/configuration/ceph-conf/)
- [Ceph Reef QA client: `get_stuck_pgs` JSON handling](https://github.com/ceph/ceph/blob/reef/qa/tasks/ceph_manager.py)
- [Ceph Squid QA client: `get_stuck_pgs` JSON handling](https://github.com/ceph/ceph/blob/squid/qa/tasks/ceph_manager.py)

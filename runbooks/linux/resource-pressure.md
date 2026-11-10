---
id: "rb-linux-resource-pressure"
title: "RHEL CPU, memory and storage latency triage"
area: "linux"
type: "runbook"
applies_to: ["rhel-9.6", "rhel-9.8"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhel-9-performance-overview", "rhel-9-performance", "rhel-9-kernel", "rhel-9-storage", "rhel-9-containers"]
---

# RHEL CPU, memory and storage latency triage

## Scope

Select one customer, cluster and host. Confirm the incident interval and which RGW/OSD or other service is affected. This is a short, read-only evidence procedure, not a benchmark or tuning recipe. It has not been run on the owner's hosts.

Start with existing Grafana data for the failing interval. A current command can show present pressure but cannot reconstruct a past spike by itself. Use available PCP or sysstat history if it already exists; do not enable a persistent recorder during this first pass.

## Identify the host and collect a short sample

```bash
cat /etc/redhat-release
uname -r
rpm -q kernel-core podman procps-ng sysstat
uptime
free -h
vmstat 1 5
iostat -xz 1 5
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,MODEL
```

`vmstat` and `iostat` are documented RHEL monitoring tools; a missing package is an evidence gap, not permission to install it. Check installed man pages for options. Their first report may summarize the period since boot, so separate that row from interval samples. Record units and sample duration.

Set `BRAIN_PIDS` to a verified, comma-separated list of the selected service's host PIDs. If the mapping is missing, obtain it from the approved inventory first. Inspect those processes without collecting arguments or environment, returning at most twenty rows:

```bash
set -o pipefail
ps -p "$BRAIN_PIDS" -o pid,ppid,comm,%cpu,%mem --sort=-%cpu | sed -n '1,21p'
journalctl -k --since "$BRAIN_SINCE" --until "$BRAIN_UNTIL" --no-pager -n 200
```

The process sample is not a complete host inventory. Its line cap limits returned output after `ps` has produced it, not collection cost. The kernel journal may contain device identifiers or other customer information; retain it in the private incident context. Set both journal time variables to the agreed incident interval before running the block.

## Interpret several signals together

| Hypothesis | Evidence needed before accepting it |
|---|---|
| CPU contention | Busy cores/run queue during the failing interval and implicated service workload |
| Memory pressure | Available memory, reclaim/swap behavior, process/cgroup limits and relevant kernel events |
| Block-device bottleneck | Per-device latency, queue/workload evidence and correlation with service delay |
| Hardware/device errors | Kernel/controller event timeline and verified device-to-OSD mapping |
| Container-specific limit | Service/container scope and host metrics that explain the difference |

A busy-device percentage, high load average or low free-memory value is not sufficient alone to identify a cause. Compare against a healthy interval on this host and, if appropriate, a similar peer with the same role and hardware. Record alternative explanations when the available samples cannot discriminate among them.

## Host, package and device boundaries

Keep the full RHEL kernel build with every suspected kernel issue; Red Hat's backports make an upstream version prefix insufficient. The container shares the host kernel, but its resource limits and process state can differ from host-wide availability. The storage guide's persistent identifiers help avoid equating a changing device path with a physical replacement slot.

The result should name the constrained layer, observed evidence, uncertainty and next diagnostic. Do not drop caches, kill processes, run filesystem repair, trigger SMART tests, change cgroup limits, tune kernel parameters or generate I/O load. A remediation proposal must explicitly account for other services and OSDs on the host.

## Sources

- [RHEL 9 Overview of performance monitoring options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/overview-of-performance-monitoring-options)
- [RHEL 9 Monitoring and managing system status and performance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/index)
- [RHEL 9 Managing, monitoring, and updating the kernel](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/index)
- [RHEL 9 Managing storage devices](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/index)
- [RHEL 9 Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/index)

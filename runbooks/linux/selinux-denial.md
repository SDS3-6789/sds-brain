---
id: "rb-linux-selinux-denial"
title: "RHEL SELinux denial investigation"
area: "linux"
type: "runbook"
applies_to: ["rhel-9.6", "rhel-9.8"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhel-9-selinux", "rhel-9-selinux-troubleshooting", "rhcs-8-hardening", "rhel-9-containers"]
---

# RHEL SELinux denial investigation

## Establish the symptom

Use this when a service or application has an access failure and an SELinux denial is a plausible explanation. Select the customer/cluster/host and record the operation and its UTC timestamp. A permissions error alone does not prove SELinux is responsible. This is a documented diagnostic procedure; it has not been exercised on the owner's hosts.

Keep the selected host and relevant container/service scope explicit. Do not reproduce an application write merely to provoke a denial in the initial read-only phase. Prefer existing events from the actual failure.

## Read the existing evidence

Set `BRAIN_PID` to the process observed at the incident time. If that identity cannot be established, stop and request an operator-selected Audit event rather than querying every process. The Audit output below is for local operator inspection and is capped at 120 lines:

```bash
set -o pipefail
getenforce
sestatus
systemctl is-active auditd
ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -p "$BRAIN_PID" -ts recent -i | sed -n '1,120p'
journalctl -t setroubleshoot --since "$BRAIN_SINCE" --until "$BRAIN_UNTIL" --no-pager -n 100
```

Red Hat's troubleshooting guide identifies Audit events and the journal as diagnostic sources. `recent` is relative to collection time; it may not cover an older incident. For an older failure, prepare an explicit start/end interval using the installed `ausearch` syntax. The output cap can split an event and does not bound Audit search cost or prove completeness. Companion Audit records can contain process arguments; return only the redacted fields listed below after local inspection. An empty sample does not prove that no denial exists.

For a specific observed path and process, inspect only the required labels:

```bash
ls -Zd -- "$BRAIN_PATH"
ps -p "$BRAIN_PID" -o pid,comm,label
matchpathcon -V "$BRAIN_PATH"
```

Use a path and PID from the incident, not a recursive filesystem search. The process may have exited or the PID may have been reused; match timestamps before associating it with the failure.

## Interpret the denial

Record the denied permission, source context, target context, object class and application/path alias. Compare the observed label with the expected policy label. Also consider ordinary file permissions, ownership, mount behavior and application configuration. Red Hat recommends examining labeling and configuration before generating a local policy exception.

For a container, identify the corresponding host path and security context through the approved runtime inventory. Do not expose the complete container environment or assume that disabling confinement is an acceptable diagnostic shortcut. Use the RHEL container documentation and the vendor's security guidance for the actual deployment.

## What the report should say

Separate three outcomes: a relevant denial was found; a denial was found but its relationship to the incident is uncertain; or the available logs do not establish a denial. Explain the time coverage and any missing logs. A proposed fix should state which label, boolean, application setting or policy behavior appears relevant and why; it remains a proposal in this phase.

Do not change enforcement, disable dontaudit rules, relabel files, generate/install an allow module, change booleans or restart services. These are state changes even when a vendor troubleshooting page demonstrates them. If additional logging is needed, describe its effect and scope as a separate change. Preserve only the minimal redacted evidence and link the incident to the relevant policy source.

## Sources

- [RHEL 9 Using SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/index)
- [RHEL 9 Troubleshooting problems related to SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/troubleshooting-problems-related-to-selinux_using-selinux)
- [Red Hat Ceph Storage 8 Data Security and Hardening Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/data_security_and_hardening_guide/index)
- [RHEL 9 Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/index)

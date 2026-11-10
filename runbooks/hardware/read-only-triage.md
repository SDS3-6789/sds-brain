---
id: hpe-readonly-triage
title: Correlate HPE hardware evidence with Ceph symptoms
area: hardware
type: runbook
applies_to: [HPE-generation-unconfirmed, RHEL-9]
confidence: documented
last_verified: 2026-11-09
sources: [hpe-ilorest-usage, hpe-redfish-concepts, hpe-redfish-services, linux-upstream-admin, hpe-apollo-utilities]
---

# Correlate HPE hardware evidence with Ceph symptoms

## Scope first

Establish the customer/cluster and affected host, exact HPE model/generation, Ceph daemon or OSD, RHEL/kernel build and incident interval. Obtain an approved mapping between host alias, physical system and management controller. Keep serials and management addresses in private evidence.

## Read-only evidence sequence

1. Inspect existing host and iLO health information. Record the system/controller/drive/NIC firmware identifiers before selecting a support document. Use the matching [HPE service reference](https://servermanagementportal.ext.hpe.com/docs/redfishservices).
2. From an approved host session, collect narrowly scoped existing information. Typical inspection commands are shown below; they are suggestions for the operator, not an automated shell integration:

```bash
cat /etc/redhat-release
uname -r
lsblk -o NAME,TYPE,SIZE,MODEL
lspci -nn
```

Device/model details can still identify infrastructure. Review outputs before importing them into shared knowledge. The [Linux administration guide](https://docs.kernel.org/admin-guide/index.html) is background; RHEL documentation governs supported tooling and backports.

3. Read the relevant existing kernel journal interval and correlate storage transport errors, link resets, ECC/machine-check events, filesystem I/O errors and device timeouts with the Ceph symptom. Choose bounded journal selectors from the RHEL runbook. Absence of an error is not proof the hardware is healthy.
4. For iLO, discover the Redfish service root and follow returned resource links. Do not assume `/Systems/1` or a fixed storage-controller resource across generations. Read only the relevant inventory, health and existing event records; no Redfish Actions. Reference: [Redfish concepts](https://servermanagementportal.ext.hpe.com/docs/concepts).
5. If approved iLOrest is available, choose the documented read-only inventory functions for that version and account. Do not enable debug output that could capture authentication. Reference: [iLOrest usage](https://servermanagementportal.ext.hpe.com/docs/redfishclients/ilorest-userguide/usage).
6. Map the affected Ceph device to a physical bay using both Ceph/OS device evidence and the controller's inventory. Record disagreements and stop before proposing replacement if the mapping is ambiguous.

## Hypotheses to separate

Drive/media failure, transport/backplane error, controller/cache behavior, network retransmissions, memory errors, thermal/power constraints and storage recovery load can all present as poor application performance. Compare their timestamps and scope. One hot OSD versus every OSD on a host suggests different next checks; it does not by itself establish a root cause.

## Stop and escalate

Escalate active data-loss risk, repeated device disappearances, uncorrected memory errors, power/thermal alarms or inability to map the device safely. Prepare a reviewed support packet with model/generation, firmware, affected components, bounded events and the exact cluster state. Existing AHS/IML evidence may help the hardware owner; support bundles must be reviewed before sharing. [Apollo utility reference](https://support.hpe.com/hpesc/public/docDisplay?docId=a00066162en_us&docLocale=en_US).

Do not start drive self-tests, destructive diagnostics, firmware updates, controller reconfiguration, power cycling or an OSD replacement through this runbook. Keep any proposed remediation separate with a maintenance plan and recovery impact assessment.

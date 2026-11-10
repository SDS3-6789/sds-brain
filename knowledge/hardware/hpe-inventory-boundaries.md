---
id: hpe-inventory-boundaries
title: HPE model, generation and device identity boundaries
area: hardware
type: knowledge
applies_to: [XL420-candidate, XL170r-candidate, XL190r-candidate, DL385-generation-unconfirmed]
confidence: documented
last_verified: 2026-11-09
sources: [hpe-xl420-apollo, hpe-xl170r, hpe-xl190r, hpe-dl385, hpe-ilorest, hpe-redfish-services, hpe-apollo-utilities]
---

# HPE model, generation and device identity boundaries

The reported family names are sufficient for documentation discovery, not firmware selection. The XL420 board name appears within HPE's Apollo 4200 family; it is important to capture the actual system product name and generation. [HPE QuickSpecs](https://www.hpe.com/int/en/collaterals/collateral.a50002573enw.html). XL170r, XL190r and DL385 likewise require generation-specific manuals and support evidence.

The local inventory should record the product/model, generation, CPU platform, iLO generation/firmware, system ROM, storage controller, operating mode, drive model/firmware and network adapter/firmware. Keep serial numbers and management addresses private. Select the appropriate [HPE Redfish service reference](https://servermanagementportal.ext.hpe.com/docs/redfishservices) after inventory; do not assign an iLO generation based solely on a familiar server name.

Use approved read access to iLO and the host to compare independent layers. An OSD daemon ID maps to a logical storage device, which maps to a physical drive and bay through controller/backplane information. A Linux path such as a changing sdX name is insufficient evidence for replacement. If the controller hides physical disks, escalate to the hardware owner for a verified mapping before proposing service work.

For performance investigations, correlate errors, queueing, temperatures, power state and network link evidence with the incident interval. Controller cache state, firmware issues and transport errors are different hypotheses; none follows automatically from high disk utilization. Avoid tests that generate load or exercise failing media during a production incident.

The [iLOrest overview](https://servermanagementportal.ext.hpe.com/docs/redfishclients/ilorest-userguide) describes tooling across iLO generations; the [Apollo utilities reference](https://support.hpe.com/hpesc/public/docDisplay?docId=a00066162en_us&docLocale=en_US) identifies relevant diagnostic families. The catalog also contains model-specific manuals. Some HPE pages were visible only through their official indexed summaries; acquire the exact guide through your support access before hardware service.

This release provides an inventory and triage procedure. It does not deploy an iLO MCP, download firmware, change a controller mode, flash a system, reset iLO or power-cycle a server.

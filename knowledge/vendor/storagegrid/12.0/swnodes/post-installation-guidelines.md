---
id: "storagegrid-120-0a4f45e5d88bd752"
title: "StorageGRID 12.0 Network and DHCP requirements after installing StorageGRID"
area: "storagegrid"
type: "import"
applies_to: ["12.0", "storagegrid-12.0"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg120-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-120"
repository_commit: "92a3f4cb2ac43fd5f151e410f99e7b9d4b019938"
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/post-installation-guidelines.adoc"
source_sha256: "5f78fac1ca5d6be5b0868bbc7ca41feea170294b02f39abe49a0b88e8e050fe6"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "swnodes/post-installation-guidelines.adoc"
---

# StorageGRID 12.0 Network and DHCP requirements after installing StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/post-installation-guidelines.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Network and DHCP requirements after installing StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
After completing grid node deployment and configuration, follow these guidelines for DHCP addressing and network configuration changes.

* If DHCP was used to assign IP addresses, configure a DHCP reservation for each IP address on the networks being used.
+
You can only set up DHCP during the deployment phase. You can't set up DHCP during configuration.
+
NOTE: Nodes reboot when the Grid Network configuration is changed by DHCP, which can cause outages if a DHCP change affects multiple nodes at the same time.

* You must use the Change IP procedures if you want to change IP addresses, subnet masks, and default gateways for a grid node. See link:../maintain/configuring-ip-addresses.html[Configure IP addresses].
* If you make networking configuration changes, including routing and gateway changes, client connectivity to the primary Admin Node and other grid nodes might be lost. Depending on the networking changes applied, you might need to reestablish these connections.

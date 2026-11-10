---
id: "storagegrid-119-3fd434f72d724f3a"
title: "StorageGRID 11.9 Post-installation guidelines"
area: "storagegrid"
type: "import"
applies_to: ["11.9", "storagegrid-11.9"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg119-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-119"
repository_commit: "aa58c9affae3bb1994d6bd2e525851e3fd088517"
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/ubuntu/post-installation-guidelines.adoc"
source_sha256: "eb78d67f0490b7fc94ebee7df2ff6753755d2673c3965c5959738ba1b24c92ab"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ubuntu/post-installation-guidelines.adoc"
---

# StorageGRID 11.9 Post-installation guidelines

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/ubuntu/post-installation-guidelines.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Post-installation guidelines
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

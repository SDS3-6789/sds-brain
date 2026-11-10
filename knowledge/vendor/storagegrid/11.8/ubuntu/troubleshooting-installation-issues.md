---
id: "storagegrid-118-0d22aab5335e4c85"
title: "StorageGRID 11.8 Troubleshoot installation issues"
area: "storagegrid"
type: "import"
applies_to: ["11.8", "storagegrid-11.8"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg118-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-118"
repository_commit: "9066339be246ef04b60100d49a31f887c58e7ae0"
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ubuntu/troubleshooting-installation-issues.adoc"
source_sha256: "eb9f3a1f3aa3a8ae017719998cec122126b77e8cfa928875dae5551964525821"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ubuntu/troubleshooting-installation-issues.adoc"
---

# StorageGRID 11.8 Troubleshoot installation issues

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/ubuntu/troubleshooting-installation-issues.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Troubleshoot installation issues
:icons: font
:imagesdir: ../media/

[.lead]
If any problems occur while installing your StorageGRID system, you can access the installation log files. Technical support might also need to use the installation log files to resolve issues.

The following installation log files are available from the container that is running each node:

* `/var/local/log/install.log` (found on all grid nodes)
* `/var/local/log/gdu-server.log` (found on the primary Admin Node)

The following installation log files are available from the host:

* `/var/log/storagegrid/daemon.log`
* `/var/log/storagegrid/nodes/<node-name>.log`

To learn how to access the log files, see link:../monitor/collecting-log-files-and-system-data.html[Collect log files and system data]. 

.Related information
link:../troubleshoot/index.html[Troubleshoot a StorageGRID system]

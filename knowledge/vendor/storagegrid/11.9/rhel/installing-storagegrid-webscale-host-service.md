---
id: "storagegrid-119-53803cf574f239fd"
title: "StorageGRID 11.9 Install StorageGRID host services"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/rhel/installing-storagegrid-webscale-host-service.adoc"
source_sha256: "aa9a96da248802a573aa57e2f83d19656b3aa347d0fe7bca75e9a3acb701cf46"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "rhel/installing-storagegrid-webscale-host-service.adoc"
---

# StorageGRID 11.9 Install StorageGRID host services

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/rhel/installing-storagegrid-webscale-host-service.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Install StorageGRID host services
:icons: font
:imagesdir: ../media/

[.lead]
You use the StorageGRID RPM package to install the StorageGRID host services.

.About this task

These instructions describe how to install the host services from the RPM packages. As an alternative, you can use the DNF repository metadata included in the installation archive to install the RPM packages remotely. See the DNF repository instructions for your Linux operating system.

.Steps

. Copy the StorageGRID RPM packages to each of your hosts, or make them available on shared storage.
+
For example, place them in the `/tmp` directory, so you can use the example command in the next step.

. Log in to each host as root or using an account with sudo permission, and run the following commands in the order specified:
+
----
sudo dnf --nogpgcheck localinstall /tmp/StorageGRID-Webscale-Images-version-SHA.rpm
----
+
----
sudo dnf --nogpgcheck localinstall /tmp/StorageGRID-Webscale-Service-version-SHA.rpm
----
+
CAUTION: You must install the Images package first, and the Service package second.
+
NOTE: If you placed the packages in a directory other than `/tmp`, modify the command to reflect the path you used.

// 2024 SEP 16, SGRIDDOC-95

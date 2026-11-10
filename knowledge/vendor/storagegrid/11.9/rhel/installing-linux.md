---
id: "storagegrid-119-ea2540ab7982c5cd"
title: "StorageGRID 11.9 Install Linux"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/rhel/installing-linux.adoc"
source_sha256: "76d23ecd51595cdf8ef6e11a6c6731510d7c7a39d09062a442f132843851ac73"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "rhel/installing-linux.adoc"
---

# StorageGRID 11.9 Install Linux

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/rhel/installing-linux.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Install Linux
:icons: font
:imagesdir: ../media/

[.lead]
You must install StorageGRID on all Red Hat Enterprise Linux grid hosts. For a list of supported versions, use the NetApp Interoperability Matrix Tool.

.Before you begin

Ensure your operating system meets StorageGRID's minimum kernel version requirements, as listed below. Use the command `uname -r` to get your operating system's kernel version, or consult with your OS vendor.

[cols="1a,2a,2a" options="header"]
|===
| Red Hat Enterprise Linux version| Minimum kernel version| Kernel package name

| 8.8 (deprecated)
| 4.18.0-477.10.1.el8_8.x86_64
| kernel-4.18.0-477.10.1.el8_8.x86_64

| 8.10
| 4.18.0-553.el8_10.x86_64
| kernel-4.18.0-553.el8_10.x86_64

| 9.0 (deprecated)
| 5.14.0-70.22.1.el9_0.x86_64
| kernel-5.14.0-70.22.1.el9_0.x86_64

| 9.2 (deprecated)
| 5.14.0-284.11.1.el9_2.x86_64
| kernel-5.14.0-284.11.1.el9_2.x86_64

| 9.4
| 5.14.0-427.18.1.el9_4.x86_64
| kernel-5.14.0-427.18.1.el9_4.x86_64

| 9.6
| 5.14.0-570.18.1.el9_6.x86_64
| kernel-5.14.0-570.18.1.el9_6.x86_64
|===

.Steps

. Install Linux on all physical or virtual grid hosts according to the distributor's instructions or your standard procedure.
+
NOTE: If you are using the standard Linux installer, select the "compute node" software configuration, if available, or "minimal install" base environment. Don't install any graphical desktop environments.

. Ensure that all hosts have access to package repositories, including the Extras channel.
+
You might need these additional packages later in this installation procedure.

. If swap is enabled:
 .. Run the following command: `$ sudo swapoff --all`
 .. Remove all swap entries from `/etc/fstab` to persist the settings.

+
NOTE: Failing to disable swap entirely can severely lower performance.

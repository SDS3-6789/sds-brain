---
id: "storagegrid-118-5521b2a8d1b963a8"
title: "StorageGRID 11.8 Audit log file rotation"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/audit-log-file-rotation.adoc"
source_sha256: "2ace306ad41f9b07de4098f107e145a0b2ced4787b8ec7298f540eff57caf9a7"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/audit-log-file-rotation.adoc"
---

# StorageGRID 11.8 Audit log file rotation

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/audit/audit-log-file-rotation.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Audit log file rotation
:icons: font
:imagesdir: ../media/

[.lead]
Audit logs files are saved to an Admin Node's `/var/local/log` directory. The active audit log files are named `audit.log`.

NOTE: Optionally, you can change the destination of audit logs and send audit information to an external syslog server. Local logs of audit records continue to be generated and stored when an external syslog server is configured. See link:../monitor/configure-audit-messages.html[Configure audit messages and log destinations].

Once a day, the active `audit.log` file is saved, and a new `audit.log` file is started. The name of the saved file indicates when it was saved, in the format `_yyyy-mm-dd.txt_`. If more than one audit log is created in a single day, the file names use the date the file was saved, appended by a number, in the format `_yyyy-mm-dd.txt.n_`. For example, `2018-04-15.txt` and `2018-04-15.txt.1` are the first and second log files created and saved on 15 April 2018.

After a day, the saved file is compressed and renamed, in the format `_yyyy-mm-dd.txt.gz_`, which preserves the original date. Over time, this results in the consumption of storage allocated for audit logs on the Admin Node. A script monitors the audit log space consumption and deletes log files as necessary to free space in the `/var/local/log` directory. Audit logs are deleted based on the date they were created, with the oldest being deleted first. You can monitor the script's actions in the following file: `/var/local/log/manage-audit.log`.

This example shows the active `audit.log` file, the previous day's file (`2018-04-15.txt`), and the compressed file for the prior day (`2018-04-14.txt.gz`).

----
audit.log
2018-04-15.txt
2018-04-14.txt.gz
----

---
id: "storagegrid-118-70fc20de08968759"
title: "StorageGRID 11.8 Troubleshoot delivery of platform services messages (SMTT alarm)"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/troubleshooting-delivery-platform-services-messages.adoc"
source_sha256: "fd337a89fdaf87edd8036462e0dd66c6080b34ab548d760750381f06aba5ba5e"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "troubleshoot/troubleshooting-delivery-platform-services-messages.adoc"
---

# StorageGRID 11.8 Troubleshoot delivery of platform services messages (SMTT alarm)

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/troubleshoot/troubleshooting-delivery-platform-services-messages.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Troubleshoot delivery of platform services messages (SMTT alarm)
:icons: font
:imagesdir: ../media/


[.lead]
The Total Events (SMTT) alarm is triggered in the Grid Manager if a platform service message is delivered to an destination that can't accept the data.

.About this task
For example, an S3 multipart upload can succeed even though the associated replication or notification message can't be delivered to the configured endpoint. Or, a message for CloudMirror replication can fail to be delivered if the metadata is too long.

The SMTT alarm contains a Last Event message that says, `Failed to publish notifications for _bucket-name object key_` for the last object whose notification failed.

Event messages are also listed in the `/var/local/log/bycast-err.log` log file. See the link:../monitor/logs-files-reference.html[Log files reference].

For additional information, see the link:../admin/troubleshooting-platform-services.html[Troubleshoot platform services]. You might need to link:../tenant/signing-in-to-tenant-manager.html[access the tenant from the Tenant Manager] to debug a platform service error.

.Steps
. To view the alarm, select *NODES* > *_site_* > *_grid node_* > *Events*.
. View Last Event at the top of the table.
+
Event messages are also listed in `/var/local/log/bycast-err.log`.

. Follow the guidance provided in the SMTT alarm contents to correct the issue.
. Select *Reset event counts*.
. Notify the tenant of the objects whose platform services messages have not been delivered.
. Instruct the tenant to trigger the failed replication or notification by updating the object's metadata or tags.

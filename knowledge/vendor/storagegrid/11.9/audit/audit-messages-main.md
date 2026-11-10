---
id: "storagegrid-119-6ef5c5b54e031786"
title: "StorageGRID 11.9 Audit message descriptions"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/audit-messages-main.adoc"
source_sha256: "d0e3f707b5b9331ac230bee9d6b1806b62a6f454367986a074bfd7e12f078e50"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/audit-messages-main.adoc"
---

# StorageGRID 11.9 Audit message descriptions

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/audit-messages-main.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Audit message descriptions
:icons: font
:imagesdir: ../media/

[.lead]
Detailed descriptions of audit messages returned by the system are listed in the following sections. Each audit message is first listed in a table that groups related messages by the class of activity that the message represents. These groupings are useful both for understanding the types of activities that are audited, and for selecting the desired type of audit message filtering.

The audit messages are also listed alphabetically by their four-character codes. This alphabetic list enables you to find information about specific messages.

The four-character codes used throughout this chapter are the ATYP values found in the audit messages as shown in the following example message:

[subs="specialcharacters,quotes"]
----
2014-07-17T03:50:47.484627
\[AUDT:[RSLT(FC32):VRGN][AVER(UI32):10][ATIM(UI64):1405569047484627][*ATYP\(FC32\):SYSU*][ANID(UI32):11627225][AMID(FC32):ARNI][ATID(UI64):9445736326500603516]]
----

For information about setting audit message levels, changing log destinations, and using an external syslog server for your audit information, see link:../monitor/configure-audit-messages.html[Configure audit messages and log destinations]

---
id: "storagegrid-119-0ccdc8a19daa9422"
title: "StorageGRID 11.9 SYSU: Node Start"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/sysu-node-start.adoc"
source_sha256: "dfa8b6ae4a1048ff668040acb0cf80788d3a53058364a553c3771f9dae2fbcc8"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/sysu-node-start.adoc"
---

# StorageGRID 11.9 SYSU: Node Start

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/sysu-node-start.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# SYSU: Node Start
:icons: font
:imagesdir: ../media/

[.lead]
When a service is restarted, this message is generated to indicate if the previous shutdown was clean (commanded) or disorderly (unexpected).

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
RSLT
a|
Clean Shutdown
a|
The nature of the shutdown:

SUCS: System was cleanly shut down.

DSDN: System was not cleanly shut down.

VRGN: System was started for the first time after server installation (or re-installation).

|===
The message does not indicate if the host server was started, only the reporting service. This message can be used to:

* Detect discontinuity in the audit trail.
* Determine if a service is failing during operation (as the distributed nature of the StorageGRID system can mask these failures). Server Manager restarts a failed service automatically.

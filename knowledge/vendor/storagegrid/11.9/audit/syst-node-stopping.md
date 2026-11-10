---
id: "storagegrid-119-0b498b0fb601f391"
title: "StorageGRID 11.9 SYST: Node Stopping"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/syst-node-stopping.adoc"
source_sha256: "d41da7b0542bc896ac5ee3274be755ed9f10f97c1e972c7a42ccfb3f88e95cf3"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/syst-node-stopping.adoc"
---

# StorageGRID 11.9 SYST: Node Stopping

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/syst-node-stopping.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# SYST: Node Stopping
:icons: font
:imagesdir: ../media/

[.lead]
When a service is gracefully stopped, this message is generated to indicate the shutdown was requested and that the service has initiated its shutdown sequence. SYST can be used to determine if the shutdown was requested, before the service is restarted (unlike SYSD, which is typically sent after the service restarts.)

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
RSLT
a|
Clean Shutdown
a|
The nature of the shutdown:

SUCS: System was cleanly shutdown.

|===
The message does not indicate if the host server is being stopped, only the reporting service. The RSLT code of a SYST message can't indicate a "dirty" shutdown, because the message is generated only by "clean" shutdowns.

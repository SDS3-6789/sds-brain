---
id: "storagegrid-118-3f0c4ff851723036"
title: "StorageGRID 11.8 View legacy alarms"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/monitor/viewing-legacy-alarms.adoc"
source_sha256: "4cc42adc74413f5ab8dc6c5c148fc859a82be14154792187ad35d88e3b3c341a"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/viewing-legacy-alarms.adoc"
---

# StorageGRID 11.8 View legacy alarms

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/monitor/viewing-legacy-alarms.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View legacy alarms
:icons: font
:imagesdir: ../media/

[.lead]
Alarms (legacy system) are triggered when system attributes reach alarm threshold values. You can view the currently active alarms from the Current Alarms page.

NOTE: While the legacy alarm system continues to be supported, the alert system offers significant benefits and is easier to use.

.Before you begin
* You must be signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.Steps
. Select *SUPPORT* > *Alarms (legacy)* > *Current alarms*.
+
image::../media/current_alarms_page.png[Current Alarms Page]
+
The alarm icon indicates the severity of each alarm, as follows:
+
[cols="1a,1a,1a,3a" options="header"]
|===
| Icon| Color| Alarm severity| Meaning
|image:../media/icon_alarm_yellow_notice.gif[yellow square icon]
|Yellow
|Notice
|The node is connected to the grid, but an unusual condition exists that does not affect normal operations.

|image:../media/icon_alert_yellow_minor.png[light orange diamond icon]
|Light Orange
|Minor
|The node is connected to the grid, but an abnormal condition exists that could affect operation in the future. You should investigate to prevent escalation.

|image:../media/icon_alert_orange_major.png[dark orange diamond icon]
|Dark Orange
|Major
|The node is connected to the grid, but an abnormal condition exists that currently affects operation. This requires prompt attention to prevent escalation.

|image:../media/icon_alert_red_critical.png[red x icon]
|Red
|Critical
|The node is connected to the grid, but an abnormal condition exists that has stopped normal operations. You should address the issue immediately.
|===
+
. To learn about the attribute that caused the alarm to be triggered, right click the attribute name in the table.
. To view additional details about an alarm, click the service name in the table.
+
The Alarms tab for the selected service appears (*SUPPORT* > *Tools* > *Grid topology* > *_Grid Node_* > *_Service_* > *Alarms*).
+
image::../media/alarms_acknowledging.png[Alarms Acknowledging]

. If you want to clear the count of current alarms, you can optionally do the following:
 ** Acknowledge the alarm. An acknowledged alarm is no longer included in the count of legacy alarms unless it is triggered at the next severity level or it is resolved and occurs again.
 ** Disable a particular Default alarm or Global Custom alarm for the entire system to prevent it from being triggered again.

.Related information

link:alarms-reference.html[Alarms reference (legacy system)]

link:managing-alarms.html[Acknowledge current alarms (legacy system)]

link:managing-alarms.html[Disable alarms (legacy system)]

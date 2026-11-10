---
id: "storagegrid-118-bb3cd27b4f058ee7"
title: "StorageGRID 11.8 Remove custom alert rules"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/monitor/removing-custom-alert-rules.adoc"
source_sha256: "d1dedbd96043dfe3a4deef95f3e8884b3bf324f6095c60eb0ae49ed6b95897da"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/removing-custom-alert-rules.adoc"
---

# StorageGRID 11.8 Remove custom alert rules

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/monitor/removing-custom-alert-rules.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Remove custom alert rules
:icons: font
:imagesdir: ../media/

[.lead]
You can remove a custom alert rule if you no longer want to use it.

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:../admin/admin-group-permissions.html[Manage alerts or Root access permission].

.Steps
. Select *ALERTS* > *Rules*.
+
The Alert Rules page appears.

. Select the radio button for the custom alert rule you want to remove.
+
You can't remove a default alert rule.

. Select *Remove custom rule*.
+
A confirmation dialog box appears.

. Select *OK* to remove the alert rule.
+
Any active instances of the alert will be resolved within 10 minutes.

---
id: "storagegrid-118-5221eb1dbfe17489"
title: "StorageGRID 11.8 View StorageGRID license information"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/viewing-storagegrid-license-information.adoc"
source_sha256: "c292eb0a44718537f7b46f960ddb7800256263efe20035a994afe37381044bf2"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/viewing-storagegrid-license-information.adoc"
---

# StorageGRID 11.8 View StorageGRID license information

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/viewing-storagegrid-license-information.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View StorageGRID license information
:icons: font
:imagesdir: ../media/

[.lead]
You can view the license information for your StorageGRID system, such as the maximum storage capacity of your grid, whenever necessary.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.About this task
If there is an issue with the software license for this StorageGRID system, the Health status card on the dashboard includes a License status icon and a *License* link. The number indicates the number of license-related issues.

image::../media/dashboard_health_panel_license_status.png[Dashboard Health Status Card License Status]

.Steps

. Access the License page by doing one of the following:

* Select *MAINTENANCE* > *System* > *License*.
* From the Health status card on the dashboard, select the License status icon or the *License* link.
+
This link appears only if there is an issue with the license.

. View the read-only details for the current license:
+
* StorageGRID system ID, which is the unique identification number for this StorageGRID installation
* License serial number
* License type, either *Perpetual* or *Subscription*
* Licensed storage capacity of the grid
* Supported storage capacity
* License end date. *N/A* appears for a perpetual license.
* Support end date
+
This date is read from the current license file and might be out of date if you extended or renewed the support service contract after obtaining the license file. To update this value, see link:updating-storagegrid-license-information.html[Update StorageGRID license information]. You can also view the actual contract end date using Active IQ.

* Contents of the license text file

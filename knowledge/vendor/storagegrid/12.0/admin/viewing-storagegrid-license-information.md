---
id: "storagegrid-120-5221eb1dbfe17489"
title: "StorageGRID 12.0 View StorageGRID license information"
area: "storagegrid"
type: "import"
applies_to: ["12.0", "storagegrid-12.0"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg120-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-120"
repository_commit: "92a3f4cb2ac43fd5f151e410f99e7b9d4b019938"
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/viewing-storagegrid-license-information.adoc"
source_sha256: "68c111618c567317b3b02a05478076fda72c1d0eb1d19010a800f46fc83451d3"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/viewing-storagegrid-license-information.adoc"
---

# StorageGRID 12.0 View StorageGRID license information

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/viewing-storagegrid-license-information.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View StorageGRID license information
:icons: font
:imagesdir: ../media/

[.lead]
You can view the license information for your StorageGRID system, such as the maximum storage capacity of your grid, whenever necessary.

.Before you begin

You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.About this task
If there is an issue with the software license for this StorageGRID system, the Health status card on the dashboard includes a License status icon and a *License* link. The number indicates the number of license-related issues.

image:dashboard_health_panel_license_status.png[Dashboard Health Status Card License Status]

.Steps

. Access the License page by doing one of the following:

* Select *Maintenance* > *System* > *License*.
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

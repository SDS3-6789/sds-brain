---
id: "storagegrid-118-c277ba54802bbb3e"
title: "StorageGRID 11.8 Specify the StorageGRID license information"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/specifying-storagegrid-license-information.adoc"
source_sha256: "4e289b4707ceac88577c5bf0e57d4178c2b854ef46c24eab1ca7998fd07c7059"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "vmware/specifying-storagegrid-license-information.adoc"
---

# StorageGRID 11.8 Specify the StorageGRID license information

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/specifying-storagegrid-license-information.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Specify the StorageGRID license information
:icons: font
:imagesdir: ../media/

[.lead]
You must specify the name for your StorageGRID system and upload the license file provided by NetApp.

.Steps

. On the License page, enter a meaningful name for your StorageGRID system in the *Grid Name* field.
+
After installation, the name is displayed at the top of the Nodes menu.

. Select *Browse*, locate the NetApp license file (`NLF-_unique-id_.txt`), and select *Open*.
+
The license file is validated, and the serial number is displayed.
+
NOTE: The StorageGRID installation archive includes a free license that does not provide any support entitlement for the product. You can update to a license that offers support after installation.
+
image::../media/2_gmi_installer_license_page.png[StorageGRID  installer license page]

. Select *Next*.

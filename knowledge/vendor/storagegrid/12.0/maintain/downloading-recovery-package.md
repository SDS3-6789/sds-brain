---
id: "storagegrid-120-9adc3472ffe27f31"
title: "StorageGRID 12.0 Download the StorageGRID recovery package"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/downloading-recovery-package.adoc"
source_sha256: "3b8798adfb01fee04bfea2046366c960038fe5633cf3efe16034cb76695969b8"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/downloading-recovery-package.adoc"
---

# StorageGRID 12.0 Download the StorageGRID recovery package

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/downloading-recovery-package.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Download the StorageGRID recovery package
:icons: font
:imagesdir: ../media/

[.lead]
The recovery package file allows you to restore the StorageGRID system if a failure occurs.

.Before you begin

* From any Admin Node, you are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the provisioning passphrase.
* You have link:../admin/admin-group-permissions.html[specific access permissions].

Download the current recovery package file before making grid topology changes to the StorageGRID system or before upgrading software. Then, download a new copy of the recovery package after making grid topology changes or after upgrading software.

.Steps

. Select *Maintenance* > *System* > *Recovery package*.
. Enter the provisioning passphrase, and select *Start download*.
+
The download starts immediately.

. When the download completes, open the `.zip` file and confirm that you can access the contents, including the `Passwords.txt` file.
. Copy the downloaded recovery package file (`.zip`) to two safe, secure, and separate locations.
+
CAUTION: The recovery package file must be secured because it contains encryption keys and passwords that can be used to obtain data from the StorageGRID system.

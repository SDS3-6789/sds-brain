---
id: "storagegrid-120-4deccfd5cea359cc"
title: "StorageGRID 12.0 Navigate to the StorageGRID Grid Manager"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/navigating-to-grid-manager.adoc"
source_sha256: "5f380aafd43b8bb52f42e4bd272ed36f68d2885a7739209776c0e33e78e4590f"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "swnodes/navigating-to-grid-manager.adoc"
---

# StorageGRID 12.0 Navigate to the StorageGRID Grid Manager

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/swnodes/navigating-to-grid-manager.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Navigate to the StorageGRID Grid Manager
:icons: font
:imagesdir: ../media/

[.lead]
You use the Grid Manager to define all of the information required to configure your StorageGRID system.

.Before you begin

The primary Admin Node must be deployed and have completed the initial startup sequence.

.Steps

. Open your web browser and navigate to:
+
`https://_primary_admin_node_ip_`
+
Alternatively, you can access the Grid Manager on port 8443:
+
`https://_primary_admin_node_ip_:8443`
+
You can use the IP address for the primary Admin Node IP on the Grid Network or on the Admin Network, as appropriate for your network configuration. You might need to use the security/advanced option in your browser to navigate to an untrusted certificate.

. Manage a temporary installer password as needed:

* If a password has already been set using one of these methods, enter the password to proceed.
 
**	A user set the password while accessing the installer previously
**	For Linux, the password was automatically imported from the node config file at `/etc/storagegrid/nodes/_<node_name>_.conf`
**  For VMware, the SSH/console password was automatically imported from the OVF properties

* If a password has not been set, optionally set a password to secure the StorageGRID installer.

. Select *Install a StorageGRID system*.
+
The page used to configure a StorageGRID grid appears.
+
image:gmi_installer_first_screen.gif[StorageGRID installer first screen]

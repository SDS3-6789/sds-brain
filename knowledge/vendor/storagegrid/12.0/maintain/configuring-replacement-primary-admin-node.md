---
id: "storagegrid-120-bc85544a136cc124"
title: "StorageGRID 12.0 Configure a replacement primary Admin Node in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/configuring-replacement-primary-admin-node.adoc"
source_sha256: "bf1384c32778000596c415b3f1855e608497a6b4b39eddc2e1a884babdc2055d"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/configuring-replacement-primary-admin-node.adoc"
---

# StorageGRID 12.0 Configure a replacement primary Admin Node in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/configuring-replacement-primary-admin-node.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Configure a replacement primary Admin Node in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
The replacement node must be configured as the primary Admin Node for your StorageGRID system.

.Before you begin

* For primary Admin Nodes hosted on virtual machines, the virtual machine has been deployed, powered on, and initialized.
* For primary Admin Nodes hosted on a services appliance, you have replaced the appliance and have installed software. See the https://docs.netapp.com/us-en/storagegrid-appliances/installconfig/index.html[installation instructions for your appliance^].
* You have the latest backup of the recovery package file (`sgws-recovery-package-_id-revision_.zip`).
* You have the provisioning passphrase.

.Steps

. Open your web browser and navigate to `\https://primary_admin_node_ip`.

. Manage a temporary installer password as needed:

* If a password has already been set using one of these methods, enter the password to proceed.
 
**	A user set the password while accessing the installer previously
**	For bare metal systems, the password was automatically imported from the node config file at `/etc/storagegrid/nodes/_<node_name>_.conf`
** For VMs, the SSH/console password was automatically imported from the OVF properties

* If a password has not been set, optionally set a password to secure the StorageGRID installer.

. Click *Recover a failed primary Admin Node*.
+
image:install_or_recover_primary_admin_node.png[Install or recover Primary Admin Node]

. Upload the most recent backup of the recovery package:
 .. Click *Browse*.
 .. Locate the most recent recovery package file for your StorageGRID system, and click *Open*.
. Enter the provisioning passphrase.
. Click *Start Recovery*.
+
The recovery process begins. The Grid Manager might become unavailable for a few minutes as the required services start. When the recovery is complete, the sign in page is displayed.

. If single sign-on (SSO) is enabled for your StorageGRID system and the relying party trust for the Admin Node you recovered was configured to use the default management interface certificate, update (or delete and recreate) the node's relying party trust in Active Directory Federation Services (AD FS). Use the new default server certificate that was generated during the Admin Node recovery process.
+
NOTE: To configure a relying party trust, see link:../admin/configure-sso.html[Configure single sign-on]. To access the default server certificate, log in to the command shell of the Admin Node. Go to the `/var/local/mgmt-api` directory, and select the `server.crt` file.

CAUTION: After recovering a primary admin node, link:assess-hotfix-requirement-during-primary-admin-node-recovery.html[determine if you need to apply a hotfix].

---
id: "storagegrid-118-97d4a2396e839d54"
title: "StorageGRID 11.8 Monitor StorageGRID appliance installation"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/monitoring-storagegrid-appliance-installation-sn.adoc"
source_sha256: "923d380bdb2e824bb6ae7428859eb996e38d1247ab477766e2c64979dbf5eaa9"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/monitoring-storagegrid-appliance-installation-sn.adoc"
---

# StorageGRID 11.8 Monitor StorageGRID appliance installation

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/monitoring-storagegrid-appliance-installation-sn.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Monitor StorageGRID appliance installation
:icons: font
:imagesdir: ../media/

[.lead]
The StorageGRID Appliance Installer provides status until installation is complete. When the software installation is complete, the appliance is rebooted.

.Steps

. To monitor the installation progress, click *Monitor Installation* from the menu bar.
+
The Monitor Installation page shows the installation progress.
+
image::../media/monitor_installation_configure_storage.gif[This image is explained by the surrounding text.]
+
The blue status bar indicates which task is currently in progress. Green status bars indicate tasks that have completed successfully.
+
NOTE: The installer ensures that tasks completed in a previous install aren't re-run. If you are re-running an installation, any tasks that don't need to be re-run are shown with a green status bar and a status of "Skipped."

. Review the progress of first two installation stages.
 ** *1. Configure storage*
+
During this stage, the installer connects to the storage controller, clears any existing configuration, communicates with SANtricity OS to configure volumes, and configures host settings.

 ** *2. Install OS*
+
During this stage, the installer copies the base operating system image for StorageGRID to the appliance.
. Continue monitoring the installation progress until the *Install StorageGRID* stage pauses and a message appears on the embedded console prompting you to approve this node on the Admin Node using the Grid Manager.
+
image::../media/monitor_installation_install_sgws.gif[This image is explained by the surrounding text.]

. Go to link:selecting-start-recovery-to-configure-appliance-storage-node.html[Select Start Recovery to configure appliance Storage Node].

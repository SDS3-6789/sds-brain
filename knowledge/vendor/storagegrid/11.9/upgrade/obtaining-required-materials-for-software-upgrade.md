---
id: "storagegrid-119-edc2673fdc8571cd"
title: "StorageGRID 11.9 Obtain the required materials for a software upgrade"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/upgrade/obtaining-required-materials-for-software-upgrade.adoc"
source_sha256: "fd01638b918dfbbc3a3f13b6bef19fcad3cbf5d824ae29cbe9c7a3e62f3abe10"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "upgrade/obtaining-required-materials-for-software-upgrade.adoc"
---

# StorageGRID 11.9 Obtain the required materials for a software upgrade

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/upgrade/obtaining-required-materials-for-software-upgrade.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Obtain the required materials for a software upgrade
:icons: font
:imagesdir: ../media/

[.lead]
Before you begin the software upgrade, obtain all required materials.

[cols="1a,3a" options="header"]
|===
| Item| Notes

|Service laptop
|The service laptop must have:

* Network port
* SSH client (for example, PuTTY)

| link:../admin/web-browser-requirements.html[Supported web browser]
|Browser support typically changes for each StorageGRID release. Make sure your browser is compatible with the new StorageGRID version.

|Provisioning passphrase
|The passphrase is created and documented when the StorageGRID system is first installed. The provisioning passphrase is not listed in the `Passwords.txt` file.

|Linux RPM or DEB archive
|If any nodes are deployed on Linux hosts, you must link:linux-installing-rpm-or-deb-package-on-all-hosts.html[download and install the RPM or DEB package on all hosts] before you start the upgrade.

Ensure your operating system meets StorageGRID's minimum kernel version requirements:

* link:../rhel/installing-linux.html[Install StorageGRID on Red Hat Enterprise Linux hosts]
* link:../ubuntu/installing-linux.html[Install StorageGRID on Ubuntu or Debian hosts]
    
|StorageGRID documentation
|* link:../release-notes/index.html[Release notes] for StorageGRID 11.9 (sign in required). Be sure to read these carefully before starting the upgrade. 
* https://kb.netapp.com/hybrid/StorageGRID/Maintenance/StorageGRID_11.9_software_upgrade_resolution_guide[StorageGRID software upgrade resolution guide^] for the major version you are upgrading to (sign in required)

* Other https://docs.netapp.com/us-en/storagegrid-family/index.html[StorageGRID documentation^], as required.
|===

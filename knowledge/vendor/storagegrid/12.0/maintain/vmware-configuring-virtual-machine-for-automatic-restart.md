---
id: "storagegrid-120-5d44dbe14c58a0be"
title: "StorageGRID 12.0 Configure a VMware virtual machine for automatic restart in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/vmware-configuring-virtual-machine-for-automatic-restart.adoc"
source_sha256: "524df63cd5304c3aa202075a4e43bebcc3c3aaeac20e87a511e036d457289f6d"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/vmware-configuring-virtual-machine-for-automatic-restart.adoc"
---

# StorageGRID 12.0 Configure a VMware virtual machine for automatic restart in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/vmware-configuring-virtual-machine-for-automatic-restart.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Configure a VMware virtual machine for automatic restart in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
If the virtual machine does not restart after VMware vSphere Hypervisor is restarted, you might need to configure the virtual machine for automatic restart.

You should perform this procedure if you notice that a virtual machine does not restart while you are recovering a grid node or performing another maintenance procedure.

.Steps

. In the VMware vSphere Client tree, select the virtual machine that is not started.
. Right-click the virtual machine, and select *Power on*.
. Configure VMware vSphere Hypervisor to restart the virtual machine automatically in future.

---
id: "storagegrid-119-5d44dbe14c58a0be"
title: "StorageGRID 11.9 VMware: Configure virtual machine for automatic restart"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/vmware-configuring-virtual-machine-for-automatic-restart.adoc"
source_sha256: "233f3651efcbe3f3d1353896f3811012419ede5a4565c69ad9a12fa9c36367ba"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/vmware-configuring-virtual-machine-for-automatic-restart.adoc"
---

# StorageGRID 11.9 VMware: Configure virtual machine for automatic restart

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/vmware-configuring-virtual-machine-for-automatic-restart.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# VMware: Configure virtual machine for automatic restart
:icons: font
:imagesdir: ../media/

[.lead]
If the virtual machine does not restart after VMware vSphere Hypervisor is restarted, you might need to configure the virtual machine for automatic restart.

You should perform this procedure if you notice that a virtual machine does not restart while you are recovering a grid node or performing another maintenance procedure.

.Steps

. In the VMware vSphere Client tree, select the virtual machine that is not started.
. Right-click the virtual machine, and select *Power on*.
. Configure VMware vSphere Hypervisor to restart the virtual machine automatically in future.

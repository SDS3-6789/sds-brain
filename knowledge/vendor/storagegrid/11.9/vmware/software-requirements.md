---
id: "storagegrid-119-838b38af787a4a14"
title: "StorageGRID 11.9 Software requirements for VMware"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/vmware/software-requirements.adoc"
source_sha256: "f55fdf6afb8c38acde1e5be1e119ab43ca56e6fcf17770620acad67ac32b36ea"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "vmware/software-requirements.adoc"
---

# StorageGRID 11.9 Software requirements for VMware

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/vmware/software-requirements.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Software requirements for VMware
:icons: font
:imagesdir: ../media/

[.lead]
You can use a virtual machine to host any type of StorageGRID node. You need one virtual machine for each grid node.

## VMware vSphere Hypervisor

You must install VMware vSphere Hypervisor on a prepared physical server. The hardware must be configured correctly (including firmware versions and BIOS settings) before you install VMware software.

* Configure networking in the hypervisor as required to support networking for the StorageGRID system you are installing.
+
link:../network/index.html[Networking guidelines]

* Ensure that the datastore is large enough for the virtual machines and virtual disks that are required to host the grid nodes.
* If you create more than one datastore, name each datastore so that you can easily identify which datastore to use for each grid node when you create virtual machines.

## ESX host configuration requirements

CAUTION: You must properly configure the network time protocol (NTP) on each ESX host. If the host time is incorrect, negative effects, including data loss, could occur.

## VMware configuration requirements

You must install and configure VMware vSphere and vCenter before deploying StorageGRID nodes.

For supported versions of VMware vSphere Hypervisor and VMware vCenter Server software, see the https://imt.netapp.com/matrix/#welcome[NetApp Interoperability Matrix Tool^].

For the steps required to install these VMware products, see the VMware documentation.

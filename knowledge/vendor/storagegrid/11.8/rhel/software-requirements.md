---
id: "storagegrid-118-1aade0cd18a1ed42"
title: "StorageGRID 11.8 Software requirements for Red Hat Enterprise Linux"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/rhel/software-requirements.adoc"
source_sha256: "e77a9f136a7f8c9ca6812870616c7d00e8ba0244497ccd5d47bce8e44a8027cf"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "rhel/software-requirements.adoc"
---

# StorageGRID 11.8 Software requirements for Red Hat Enterprise Linux

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/rhel/software-requirements.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Software requirements for Red Hat Enterprise Linux
:icons: font
:imagesdir: ../media/

[.lead]
You can use a virtual machine to host any type of StorageGRID node. You need one virtual machine for each grid node.

To install StorageGRID on Red Hat Enterprise Linux (RHEL), you must install some third-party software packages. Some supported Linux distributions don't contain these packages by default. The software package versions that StorageGRID installations are tested on include those listed on this page. 

NOTE: If you select a Linux distribution and container runtime installation option that requires any of these packages, and they are not installed automatically by the Linux distribution, install one of the versions listed here if available from your provider or the supporting vendor for your Linux distribution. Otherwise, use the default package versions available from your vendor.

NOTE: All installation options require either Podman or Docker. Do not install both packages. Install only the package required by your installation option.

## Python versions tested

* 3.5.2-2
* 3.6.8-2
* 3.6.8-38
* 3.6.9-1
* 3.7.3-1
* 3.8.10-0
* 3.9.2-1
* 3.9.10-2
* 3.9.16-1
* 3.10.6-1
* 3.11.2-6

## Podman versions tested

* 3.2.3-0
* 3.4.4+ds1
* 4.1.1-7
* 4.2.0-11
* 4.3.1+ds1-8+b1
* 4.4.1-8
* 4.4.1-12

## Docker versions tested

IMPORTANT: Docker support is deprecated and will be removed in a future release.

* Docker-CE 20.10.7
* Docker-CE 20.10.20-3
* Docker-CE 23.0.6-1
* Docker-CE 24.0.2-1
* Docker-CE 24.0.4-1
* Docker-CE 24.0.5-1
* Docker-CE 24.0.7-1
* 1.5-2

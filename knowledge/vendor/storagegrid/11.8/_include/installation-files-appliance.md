---
id: "storagegrid-118-6f7dfff5ab04ef19"
title: "StorageGRID 11.8 installation files appliance"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/_include/installation-files-appliance.adoc"
source_sha256: "e7a813a6ed67c52e246d94af382b092e83559fb3fd4893ef918f35e8d4b4428d"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/installation-files-appliance.adoc"
---

# StorageGRID 11.8 installation files appliance

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/_include/installation-files-appliance.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

//installation files for appliances - used in expand and maintain

[cols="1a,1a" options="header"]
|===
| Path and file name| Description

m|./debs/storagegrid-webscale-images-version-SHA.deb
|
DEB package for installing the StorageGRID node images on your appliances.

m|./debs/storagegrid-webscale-images-version-SHA.deb.md5
|
MD5 checksum for the file `/debs/storagegridwebscale-
images-version-SHA.deb`.
|===

NOTE: For appliance installation, these files are only required if you need to avoid network traffic. The appliance can download the required files from the primary Admin Node.

---
id: "storagegrid-119-6f7dfff5ab04ef19"
title: "StorageGRID 11.9 installation files appliance"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/installation-files-appliance.adoc"
source_sha256: "e7a813a6ed67c52e246d94af382b092e83559fb3fd4893ef918f35e8d4b4428d"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/installation-files-appliance.adoc"
---

# StorageGRID 11.9 installation files appliance

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/installation-files-appliance.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

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

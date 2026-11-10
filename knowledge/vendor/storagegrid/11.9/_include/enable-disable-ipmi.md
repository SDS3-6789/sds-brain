---
id: "storagegrid-119-f01e67e2dbe1dbd8"
title: "StorageGRID 11.9 enable disable ipmi"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/enable-disable-ipmi.adoc"
source_sha256: "865856a643445cf254bbed3b77e1c08f85a82380ef3fdc6d55178ed3fb0e5356"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/enable-disable-ipmi.adoc"
---

# StorageGRID 11.9 enable disable ipmi

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/enable-disable-ipmi.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

//This is the shared note on how to enable or disable the IPMI//

//ALSO UPDATE IN OTHER REPO//

NOTE: You can enable or disable remote IPMI access for all appliances containing a BMC. The remote IPMI interface allows low-level hardware access to your StorageGRID appliances by anyone with a BMC account and password. If you do not need remote IPMI access to the BMC, disable this option using one of the following methods: +
In Grid Manager, go to *CONFIGURATION* > *Security* > *Security settings* > *Appliances* and clear the *Enable remote IPMI access* checkbox. +
In the Grid management API, use the private endpoint: `PUT /private/bmc`.

//ALSO UPDATE IN OTHER REPO//

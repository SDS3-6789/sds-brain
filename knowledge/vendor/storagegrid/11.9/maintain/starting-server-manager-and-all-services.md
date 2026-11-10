---
id: "storagegrid-119-2b912587a0eadf3e"
title: "StorageGRID 11.9 Start Server Manager and all services"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/starting-server-manager-and-all-services.adoc"
source_sha256: "9ed1e190e6cfd7ea329a9cae94d13c022a5bb45aad9dd5a2e60b85a3f2a70318"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/starting-server-manager-and-all-services.adoc"
---

# StorageGRID 11.9 Start Server Manager and all services

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/starting-server-manager-and-all-services.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Start Server Manager and all services
:icons: font
:imagesdir: ../media/

[.lead]
You might need to start Server Manager, which also starts all services on the grid node.

.Before you begin

You have the `Passwords.txt` file.

.About this task

Starting Server Manager on a grid node where it is already running results in a restart of Server Manager and all services on the grid node.

.Steps

. Log in to the grid node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.

+
When you are logged in as root, the prompt changes from `$` to `#`.
. Start Server Manager: `service servermanager start`
. Log out of the command shell: `exit`

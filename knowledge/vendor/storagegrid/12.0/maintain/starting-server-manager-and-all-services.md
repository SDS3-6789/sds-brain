---
id: "storagegrid-120-2b912587a0eadf3e"
title: "StorageGRID 12.0 Start StorageGRID Server Manager and all services"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/starting-server-manager-and-all-services.adoc"
source_sha256: "167597336ed026f1b5ca6134dd2b81e52a2fa49e46e9c9326962cb5169fc1a53"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/starting-server-manager-and-all-services.adoc"
---

# StorageGRID 12.0 Start StorageGRID Server Manager and all services

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/starting-server-manager-and-all-services.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Start StorageGRID Server Manager and all services
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

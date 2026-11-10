---
id: "storagegrid-119-e3bab2edef7c0c76"
title: "StorageGRID 11.9 View Server Manager status and version"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/viewing-server-manager-status-and-version.adoc"
source_sha256: "05010e4d4027ba060b42d2211826c349c4b2648f03ceeacf52fffcfa3ad00c6e"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/viewing-server-manager-status-and-version.adoc"
---

# StorageGRID 11.9 View Server Manager status and version

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/viewing-server-manager-status-and-version.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View Server Manager status and version
:icons: font
:imagesdir: ../media/

[.lead]
For each grid node, you can view the current status and version of Server Manager running on that grid node. You can also obtain the current status of all services running on that grid node.

.Before you begin

You have the `Passwords.txt` file.

.Steps

. Log in to the grid node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.

+
When you are logged in as root, the prompt changes from `$` to `#`.
. View the current status of Server Manager running on the grid node: `*service servermanager status*`
+
The current status of Server Manager running on the grid node is reported (running or not). If Server Manager's status is `running`, the time it has been running since last it was started is listed. For example:
+
----
servermanager running for 1d, 13h, 0m, 30s
----

. View the current version of Server Manager running on a grid node: `*service servermanager version*`
+
The current version is listed. For example:
+
----
11.1.0-20180425.1905.39c9493
----

. Log out of the command shell: `*exit*`

---
id: "storagegrid-118-27ad26487cffbda9"
title: "StorageGRID 11.8 Force service to terminate"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/forcing-service-to-terminate.adoc"
source_sha256: "089abd2ab15b8148447aba5fb2d4190063cd4aea0b88c731eec4c1864c3a558b"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/forcing-service-to-terminate.adoc"
---

# StorageGRID 11.8 Force service to terminate

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/maintain/forcing-service-to-terminate.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Force service to terminate
:icons: font
:imagesdir: ../media/

[.lead]
If you need to stop a service immediately, you can use the `force-stop` command.

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
. Manually force the service to terminate: `service _servicename_ force-stop`
+
For example:
+
----
service ldr force-stop
----
+
The system waits 30 seconds before terminating the service.

. Log out of the command shell: `exit`

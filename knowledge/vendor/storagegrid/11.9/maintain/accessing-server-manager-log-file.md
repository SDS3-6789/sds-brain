---
id: "storagegrid-119-7c36035961f03efa"
title: "StorageGRID 11.9 Troubleshoot Server Manager"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/accessing-server-manager-log-file.adoc"
source_sha256: "4cbcf554830dcc90f950f0582ea53698ff1c2e0a0be71d90446fec1cdcb42899"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/accessing-server-manager-log-file.adoc"
---

# StorageGRID 11.9 Troubleshoot Server Manager

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/accessing-server-manager-log-file.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Troubleshoot Server Manager
:icons: font
:imagesdir: ../media/

[.lead]
If a problem arises when using Server Manager, check its log file.

Error messages related to Server Manager are captured in the Server Manager log file, which is located at: `/var/local/log/servermanager.log`

Check this file for error messages regarding failures. Escalate the issue to technical support if required. You might be asked to forward log files to technical support.

## Service with an error state

If you detect that a service has entered an error state, attempt to restart the service.

.Before you begin

You have the `Passwords.txt` file.

.About this task

Server Manager monitors services and restarts any that have stopped unexpectedly. If a service fails, Server Manager attempts to restart it. If there are three failed attempts to start a service within five minutes, the service enters an error state. Server Manager does not attempt another restart.

.Steps

. Log in to the grid node:
 .. Enter the following command: `ssh admin@_grid_node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.

+
When you are logged in as root, the prompt changes from `$` to `#`.
. Confirm the error state of the service: `service _servicename_ status`
+
For example:
+
----
service ldr status
----
+
If the service is in an error state, the following message is returned: `_servicename_ in error state`. For example:
+
----
ldr in error state
----
+
NOTE: If the service status is `disabled`, see the instructions for link:using-donotstart-file.html[removing a DoNotStart file for a service].

. Attempt to remove the error state by restarting the service: `service _servicename_ restart`
+
If the service fails to restart, contact technical support.

. Log out of the command shell: `exit`

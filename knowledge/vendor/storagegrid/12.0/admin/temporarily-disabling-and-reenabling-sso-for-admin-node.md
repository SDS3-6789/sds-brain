---
id: "storagegrid-120-e5ab908c8df81232"
title: "StorageGRID 12.0 Temporarily disable and reenable SSO for a StorageGRID Admin Node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/temporarily-disabling-and-reenabling-sso-for-admin-node.adoc"
source_sha256: "092ed1183733682a0b7c2d57858fb18967171a1880dd4757a539e2b7b89821ff"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/temporarily-disabling-and-reenabling-sso-for-admin-node.adoc"
---

# StorageGRID 12.0 Temporarily disable and reenable SSO for a StorageGRID Admin Node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/temporarily-disabling-and-reenabling-sso-for-admin-node.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Temporarily disable and reenable SSO for a StorageGRID Admin Node
:icons: font
:imagesdir: ../media/

[.lead]
You might not be able to sign in to the Grid Manager if the single sign-on (SSO) system goes down. In this case, you can temporarily disable and reenable SSO for one Admin Node. To disable and then reenable SSO, you must access the node's command shell.

.Before you begin

* You have link:admin-group-permissions.html[specific access permissions].
* You have the `Passwords.txt` file.
* You know the password for the local root user.

.About this task

After you disable SSO for one Admin Node, you can sign in to the Grid Manager as the local root user. To secure your StorageGRID system, you must use the node's command shell to reenable SSO on the Admin Node as soon as you sign out.

TIP: Disabling SSO for one Admin Node does not affect the SSO settings for any other Admin Nodes in the grid. The *Enable SSO* checkbox on the Single Sign-on page in the Grid Manager remains selected, and all existing SSO settings are maintained unless you update them.

.Steps

. Log in to an Admin Node:
 .. Enter the following command: `ssh admin@Admin_Node_IP`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.
+
When you are logged in as root, the prompt changes from `$` to `#`.
. Run the following command:``disable-saml``
+
A message indicates that the command applies to this Admin Node only.

. Confirm that you want to disable SSO.
+
A message indicates that single sign-on is disabled on the node.

. From a web browser, access the Grid Manager on the same Admin Node.
+
The Grid Manager sign-in page is now displayed because SSO has been disabled.

. Sign in with the username root and the local root user's password.
. If you disabled SSO temporarily because you needed to correct the SSO configuration:
 .. Select *Configuration* > *Access control* > *Single sign-on*.
 .. Change the incorrect or out-of-date SSO settings.
 .. Select *Save*.
+
Selecting *Save* from the Single Sign-on page automatically reenables SSO for the entire grid.
. If you disabled SSO temporarily because you needed to access the Grid Manager for some other reason:
 .. Perform whatever task or tasks you need to perform.
 .. Select *Sign out*, and close the Grid Manager.
 .. Reenable SSO on the Admin Node. You can perform either of the following steps:
  *** Run the following command: `enable-saml`
+
A message indicates that the command applies to this Admin Node only.
+
Confirm that you want to enable SSO.
+
A message indicates that single sign-on is enabled on the node.

  *** Reboot the grid node: `reboot`
. From a web browser, access the Grid Manager from the same Admin Node.
. Confirm that the StorageGRID Sign in page appears and that you must enter your SSO credentials to access the Grid Manager.

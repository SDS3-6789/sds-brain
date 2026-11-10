---
id: "storagegrid-120-e3e34d8282559138"
title: "StorageGRID 12.0 Learn about StorageGRID SSO"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/how-sso-works.adoc"
source_sha256: "9870666b2f00753ba34d4cfc4eb62731bd4c5cc1c88512817cd6328eb93132e7"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/how-sso-works.adoc"
---

# StorageGRID 12.0 Learn about StorageGRID SSO

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/how-sso-works.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Learn about StorageGRID SSO
:icons: font
:imagesdir: ../media/

[.lead]
When single sign-on (SSO) is enabled, users can access the Grid Manager, Tenant Manager, Grid Management API, or Tenant Management API only if their credentials are authorized using the SSO sign-in process implemented by your organization. Local users can't sign in to StorageGRID.

The StorageGRID system supports single sign-on (SSO) using the Security Assertion Markup Language 2.0 (SAML 2.0) standard.

Before enabling single sign-on (SSO), review how the StorageGRID sign-in and sign-out processes are affected when SSO is enabled.

## Sign in when SSO is enabled

When SSO is enabled and you sign in to StorageGRID, you are redirected to your organization's SSO page to validate your credentials.

.Steps

. Enter the fully qualified domain name or IP address of any StorageGRID Admin Node in a web browser.
+
The StorageGRID Sign in page appears.

** If this is the first time you have accessed the URL on this browser, you are prompted for an account ID.
** If you have previously accessed either the Grid Manager or the Tenant Manager, you are prompted to select a recent account or to enter an account ID.
+
NOTE: The StorageGRID Sign in page is not shown when you enter the complete URL for a tenant account (that is, a fully qualified domain name or IP address followed by `/?accountId=_20-digit-account-id_`). Instead, you are immediately redirected to your organization's SSO sign-in page, where you can <<signin_sso,sign in with your SSO credentials>>.

. Indicate whether you want to access the Grid Manager or the Tenant Manager:
 ** To access the Grid Manager, leave the *Account ID* field blank, enter *0* as the account ID, or select *Grid Manager* if it appears in the list of recent accounts.
 ** To access the Tenant Manager, enter the 20-digit tenant account ID or select a tenant by name if it appears in the list of recent accounts.
. Select *Sign in*
+
StorageGRID redirects you to your organization's SSO sign-in page. For example:

. [[signin_sso]]Sign in with your SSO credentials.
+
If your SSO credentials are correct:

 .. The identity provider (IdP) provides an authentication response to StorageGRID.
 .. StorageGRID validates the authentication response.
 .. If the response is valid and you belong to a federated group with StorageGRID access permissions, you are signed in to the Grid Manager or the Tenant Manager, depending on which account you selected.
+
NOTE: If the service account is inaccessible, you can still sign in, as long as you are an existing user that belongs to a federated group with StorageGRID access permissions.

. Optionally, access other Admin Nodes, or access the Grid Manager or the Tenant Manager, if you have adequate permissions.
+
You don't need to reenter your SSO credentials.

## Sign out when SSO is enabled

When SSO is enabled for StorageGRID, what happens when you sign out depends on what you are signed in to and where you are signing out from.

.Steps

. Locate the *Sign out* link in the top-right corner of the user interface.
. Select *Sign out*.
+
The StorageGRID Sign in page appears. The *Recent Accounts* drop-down is updated to include *Grid Manager* or the name of the tenant, so you can access these user interfaces more quickly in the future.
+
TIP: The table summarizes what happens when you sign out if you are using a single browser session. If you are signed in to StorageGRID across multiple browser sessions, you must sign out of all browser sessions separately.
+
[cols="1a,1a,1a" options="header"]
|===
| If you are signed in to...| And you sign out from...| You are signed out of...

| Grid Manager on one or more Admin Nodes
| Grid Manager on any Admin Node
| Grid Manager on all Admin Nodes

*Note:* If you use Entra ID for SSO, it might take a few minutes to be signed out of all Admin Nodes.
| Tenant Manager on one or more Admin Nodes
| Tenant Manager on any Admin Node
| Tenant Manager on all Admin Nodes

.2+| Both Grid Manager and Tenant Manager
| Grid Manager
| The Grid Manager only. You must also sign out of the Tenant Manager to sign out of SSO.
| Tenant Manager
| The Tenant Manager only. You must also sign out of the Grid Manager to sign out of SSO.
|===

// 2025 JUN 10, SGWS-33778

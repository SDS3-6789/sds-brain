---
id: "storagegrid-118-2b0f934a9c87328e"
title: "StorageGRID 11.8 Use identity federation"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/using-identity-federation.adoc"
source_sha256: "5377d8929cf92a8d950758af74a6f50dbefd549e4f78aece36af3b6723ed8185"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/using-identity-federation.adoc"
---

# StorageGRID 11.8 Use identity federation

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/using-identity-federation.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Use identity federation
:icons: font
:imagesdir: ../media/

[.lead]
Using identity federation makes setting up groups and users faster, and it allows users to sign in to StorageGRID using familiar credentials.

## Configure identity federation for Grid Manager

You can configure identity federation in the Grid Manager if you want admin groups and users to be managed in another system such as Active Directory, Azure Active Directory (Azure AD), OpenLDAP, or Oracle Directory Server.

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:admin-group-permissions.html[specific access permissions].
* You are using Active Directory, Azure AD, OpenLDAP, or Oracle Directory Server as the identity provider.
+
NOTE: If you want to use an LDAP v3 service that is not listed, contact technical support.
* If you plan to use OpenLDAP, you must configure the OpenLDAP server. See <<Guidelines for configuring an OpenLDAP server>>.
* If you plan to enable single sign-on (SSO), you have reviewed the link:requirements-for-sso.html[requirements and considerations for single sign-on].
* If you plan to use Transport Layer Security (TLS) for communications with the LDAP server, the identity provider is using TLS 1.2 or 1.3. See link:supported-ciphers-for-outgoing-tls-connections.html[Supported ciphers for outgoing TLS connections].

.About this task
You can configure an identity source for the Grid Manager if you want to import groups from another system such as Active Directory, Azure AD, OpenLDAP, or Oracle Directory Server. You can import the following types of groups:

* Admin groups. The users in admin groups can sign in to the Grid Manager and perform tasks, based on the management permissions assigned to the group.
* Tenant user groups for tenants that don't use their own identity source. Users in tenant groups can sign in to the Tenant Manager and perform tasks, based on the permissions assigned to the group in the Tenant Manager. See link:creating-tenant-account.html[Create tenant account] and link:../tenant/index.html[Use a tenant account] for details.

### Enter the configuration

.Steps

. Select *CONFIGURATION* > *Access control* > *Identity federation*.
include::../_include/identity_federation_configure_steps.adoc[]

## Force synchronization with the identity source
include::../_include/identity_federation_force_sync_steps.adoc[]

## Disable identity federation
include::../_include/identity_federation_disable_steps.adoc[]

## Guidelines for configuring an OpenLDAP server
include::../_include/identity_federation_openldap_guidelines.adoc[]

---
id: "storagegrid-120-d23a9d4269e6cd1a"
title: "StorageGRID 12.0 Use identity federation in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/using-identity-federation.adoc"
source_sha256: "c1e44aa1a500e6ea3f8f932c9c5493368385a93bf008d1d8137004c935342121"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/using-identity-federation.adoc"
---

# StorageGRID 12.0 Use identity federation in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/using-identity-federation.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Use identity federation in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
Using identity federation makes setting up tenant groups and users faster, and it allows tenant users to sign in to the tenant account using familiar credentials.

## Configure identity federation for Tenant Manager

You can configure identity federation for the Tenant Manager if you want tenant groups and users to be managed in another system such as Active Directory, Microsoft Entra ID, OpenLDAP, or Oracle Directory Server.

.Before you begin

* You're signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the link:tenant-management-permissions.html[Root access permission].
* You're using Active Directory, Microsoft Entra ID, OpenLDAP, or Oracle Directory Server as the identity provider.
+
NOTE: If you want to use an LDAP v3 service that isn't listed, contact technical support.

* If you plan to use OpenLDAP, you must configure the OpenLDAP server. See <<Guidelines for configuring OpenLDAP server>>.
* If you plan to use Transport Layer Security (TLS) for communications with the LDAP server, the identity provider must be using TLS 1.2 or 1.3. See link:../admin/supported-ciphers-for-outgoing-tls-connections.html[Supported ciphers for outgoing TLS connections].

.About this task

Whether you can configure an identity federation service for your tenant depends on how your tenant account was set up. Your tenant might share the identity federation service that was configured for the Grid Manager. If you see this message when you access the Identity Federation page, you can't configure a separate federated identity source for this tenant.

image:tenant_shares_identity_federation.png[Tenant Shares Identity Federation]

### Enter configuration

When you configure identify federation, you provide the values StorageGRID needs to connect to an LDAP service.

.Steps

. Select *Access Management* > *Identity federation*.
include::../_include/identity_federation_configure_steps.adoc[]

## Force synchronization with identity source
include::../_include/identity_federation_force_sync_steps.adoc[]

## Disable identity federation
include::../_include/identity_federation_disable_steps.adoc[]

## Guidelines for configuring OpenLDAP server
include::../_include/identity_federation_openldap_guidelines.adoc[]

// 2025 JUN 10, SGWS-33778

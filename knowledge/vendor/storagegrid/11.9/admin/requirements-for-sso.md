---
id: "storagegrid-119-e560d7ec4ece4935"
title: "StorageGRID 11.9 Requirements and considerations for single sign-on"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/requirements-for-sso.adoc"
source_sha256: "dad409365d0c8e06cd4f303e63f5b21cb35b042d62d9db4da5b17ab4223e6908"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/requirements-for-sso.adoc"
---

# StorageGRID 11.9 Requirements and considerations for single sign-on

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/requirements-for-sso.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Requirements and considerations for single sign-on
:icons: font
:imagesdir: ../media/

[.lead]
Before enabling single sign-on (SSO) for a StorageGRID system, review the requirements and considerations.

## Identity provider requirements

StorageGRID supports the following SSO identity providers (IdP):

* Active Directory Federation Service (AD FS)
* Azure Active Directory (Azure AD)
* PingFederate

You must configure identity federation for your StorageGRID system before you can configure an SSO identity provider. The type of LDAP service you use for identity federation controls which type of SSO you can implement.

[cols="1a,1a"]  
|===
| Configured LDAP service type |Options for SSO identity provider

| Active Directory
|* Active Directory
* Azure
* PingFederate

| Azure
| Azure

|===


### AD FS requirements
You can use any of the following versions of AD FS:

 * Windows Server 2022 AD FS
 * Windows Server 2019 AD FS
 * Windows Server 2016 AD FS

NOTE: Windows Server 2016 should be using the https://support.microsoft.com/en-us/help/3201845/cumulative-update-for-windows-10-version-1607-and-windows-server-2016[KB3201845 update^], or higher.

### Additional requirements

* Transport Layer Security (TLS) 1.2 or 1.3
* Microsoft .NET Framework, version 3.5.1 or higher

### Considerations for Azure

If you use Azure as the SSO type and users have user principal names that don't use the sAMAccountName as the prefix, login issues can occur if StorageGRID loses its connection with the LDAP server. To allow users to sign in, you must restore the connection to the LDAP server.

## Server certificate requirements

By default, StorageGRID uses a management interface certificate on each Admin Node to secure access to the Grid Manager, the Tenant Manager, the Grid Management API, and the Tenant Management API. When you configure relying party trusts (AD FS), enterprise applications (Azure), or service provider connections (PingFederate) for StorageGRID, you use the server certificate as the signature certificate for StorageGRID requests.

If you have not already link:configuring-custom-server-certificate-for-grid-manager-tenant-manager.html[configured a custom certificate for the management interface], you should do so now. When you install a custom server certificate, it is used for all Admin Nodes, and you can use it in all StorageGRID relying party trusts, enterprise applications, or SP connections.

NOTE: Using an Admin Node's default server certificate in a relying party trust, enterprise application, or SP connection is not recommended. If the node fails and you recover it, a new default server certificate is generated. Before you can sign in to the recovered node, you must update the relying party trust, enterprise application, or SP connection with the new certificate.

You can access an Admin Node's server certificate by logging in to the command shell of the node and going to the `/var/local/mgmt-api` directory. A custom server certificate is named `custom-server.crt`. The node's default server certificate is named `server.crt`.

## Port requirements

Single sign-on (SSO) is not available on the restricted Grid Manager or Tenant Manager ports. You must use the default HTTPS port (443) if you want users to authenticate with single sign-on. See link:controlling-access-through-firewalls.html[Control access at external firewall].

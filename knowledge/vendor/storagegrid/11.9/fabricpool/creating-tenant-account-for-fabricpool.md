---
id: "storagegrid-119-48199d85670f31f5"
title: "StorageGRID 11.9 Create a tenant account for FabricPool"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/fabricpool/creating-tenant-account-for-fabricpool.adoc"
source_sha256: "fabd8aeaebf4b266154308b009d2fca8e10552317134ed270d5e0ac59024ca48"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "fabricpool/creating-tenant-account-for-fabricpool.adoc"
---

# StorageGRID 11.9 Create a tenant account for FabricPool

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/fabricpool/creating-tenant-account-for-fabricpool.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Create a tenant account for FabricPool
:icons: font
:imagesdir: ../media/

[.lead]
You must create a tenant account in the Grid Manager for FabricPool use.

Tenant accounts allow client applications to store and retrieve objects on StorageGRID. Each tenant account has its own account ID, authorized groups and users, buckets, and objects.

For details about this task, see link:../admin/creating-tenant-account.html[Create tenant account]. To use the FabricPool setup wizard to complete this task, go to link:use-fabricpool-setup-wizard-steps.html[Access and complete the FabricPool setup wizard].


.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have link:../admin/admin-group-permissions.html[specific access permissions].

.Steps
. Select *TENANTS*.

. Select *Create*.

. For the Enter details steps, enter the following information.
+
[cols="1a,3a" options="header"]
|===
| Field | Description

| Name
| A name for the tenant account. Tenant names don't need to be unique. When the tenant account is created, it receives a unique, numeric account ID.

| Description (optional)
| A description to help identify the tenant.

| Client type
| Must be *S3* for FabricPool.

| Storage quota (optional)
| Leave this field blank for FabricPool.

|===

. For the Select permissions step:

.. Don't select *Allow platform services*. 
+
FabricPool tenants don't typically need to use platform services, such as CloudMirror replication.

.. Optionally, select *Use own identity source*.
.. Don't select *Allow S3 Select*. 
+
FabricPool tenants don't typically need to use S3 Select. 

.. Optionally, select *Use grid federation connection* to allow the tenant to use a link:../admin/grid-federation-overview.html[grid federation connection] for account clone and cross-grid replication. Then, select the grid federation connection to use.

. For the Define root access step, specify which user will have the initial Root access permission for the tenant account, based on whether your StorageGRID system uses link:../admin/using-identity-federation.html[identity federation], link:../admin/configuring-sso.html[single sign-on (SSO)], or both. 
+
[cols="1a,2a" options="header"]
|===
| Option 
| Do this

| If identity federation is not enabled 
| Specify the password to use when signing into the tenant as the local root user.

| If identity federation is enabled
| . Select an existing federated group to have Root access permission for the tenant.

. Optionally, specify the password to use when signing in to the tenant as the local root user.

| If both identity federation and single sign-on (SSO) are enabled
| Select an existing federated group to have Root access permission for the tenant. No local users can sign in.

|===

. Select *Create tenant*.

---
id: "storagegrid-118-017108c60f105d79"
title: "StorageGRID 11.8 Tenant management permissions"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/tenant-management-permissions.adoc"
source_sha256: "ede46f844279edb7e680bb82e747b674a93020aea86d2f7f46ed062d8df7fafa"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/tenant-management-permissions.adoc"
---

# StorageGRID 11.8 Tenant management permissions

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/tenant-management-permissions.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Tenant management permissions
:icons: font
:imagesdir: ../media/

[.lead]
Before you create a tenant group, consider which permissions you want to assign to that group. Tenant management permissions determine which tasks users can perform using the Tenant Manager or the Tenant Management API. A user can belong to one or more groups. Permissions are cumulative if a user belongs to multiple groups.

To sign in to the Tenant Manager or to use the Tenant Management API, users must belong to a group that has at least one permission. All users who can sign in can perform the following tasks:

* View the dashboard
* Change their own password (for local users)

For all permissions, the group's Access mode setting determines whether users can change settings and perform operations or whether they can only view the related settings and features.

NOTE: If a user belongs to multiple groups and any group is set to Read-only, the user will have read-only access to all selected settings and features.

You can assign the following permissions to a group. Note that S3 tenants and Swift tenants have different group permissions.

[cols="1a,3a,3a" options="header"]
|===
| Permission| Description| Details

| Root access
| Provides full access to the Tenant Manager and the Tenant Management API.
| Swift users must have Root access permission to sign in to the tenant account.

| Administrator
| Swift tenants only. Provides full access to the Swift containers and objects for this tenant account
| Swift users must have the Swift Administrator permission to perform any operations with the Swift REST API.

| Manage your own S3 credentials
| Allows users to create and remove their own S3 access keys.
| Users who don't have this permission don't see the *STORAGE (S3)* > *My S3 access keys* menu option.

| View all buckets
| 
*S3 tenants*: Allows users to view all buckets and bucket configurations.

*Swift tenants*: Allows Swift users to view all containers and container configurations using the Tenant Management API.
| 
Users who don't have either the View all buckets or the Manage all buckets permission don't see the *Buckets* menu option.

This permission is superseded by the Manage all buckets permission. It does not affect S3 bucket or group polices used by S3 clients or S3 Console.

You can only assign this permission to Swift groups from the Tenant Management API. You can't assign this permission to Swift groups using the Tenant Manager.

| Manage all buckets
|
*S3 tenants*: Allows users to use the Tenant Manager and the Tenant Management API to create and delete S3 buckets and to manage the settings for all S3 buckets in the tenant account, regardless of S3 bucket or group policies.

*Swift tenants*: Allows Swift users to control the consistency for Swift containers using the Tenant Management API.
| 
Users who don't have either the View all buckets or the Manage all buckets permission don't see the *Buckets* menu option.

This permission supersedes the View all buckets permission. It does not affect S3 bucket or group polices used by S3 clients or S3 Console.

You can only assign this permission to Swift groups from the Tenant Management API. You can't assign this permission to Swift groups using the Tenant Manager.

| Manage endpoints
| Allows users to use the Tenant Manager or the Tenant Management API to create or edit platform service endpoints, which are used as the destination for StorageGRID platform services.
| Users who don't have this permission don't see the *Platform services endpoints* menu option.

| Use S3 Console tab
| When combined with the View all buckets or Manage all buckets permission, allows users to view and manage objects from the S3 Console tab on the details page for a bucket.
| 
|===

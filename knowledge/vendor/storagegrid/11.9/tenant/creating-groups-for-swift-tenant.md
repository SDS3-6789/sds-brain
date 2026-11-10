---
id: "storagegrid-119-740981f770254fdf"
title: "StorageGRID 11.9 Create groups for a Swift tenant"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/creating-groups-for-swift-tenant.adoc"
source_sha256: "b6f362d54409adbebe0efca19ab5f0d48479eaec3f8498aa6c3a2f381a2b346b"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/creating-groups-for-swift-tenant.adoc"
---

# StorageGRID 11.9 Create groups for a Swift tenant

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/tenant/creating-groups-for-swift-tenant.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Create groups for a Swift tenant
:icons: font
:imagesdir: ../media/

[.lead]
You can manage access permissions for a Swift tenant account by importing federated groups or creating local groups. At least one group must have the Swift Administrator permission, which is required to manage the containers and objects for a Swift tenant account.

NOTE: Support for Swift client applications has been deprecated and will be removed in a future release.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].

* You belong to a user group that has the link:tenant-management-permissions.html[Root access permission].

* If you plan to import a federated group, you have link:using-identity-federation.html[configured identity federation], and the federated group already exists in the configured identity source.

## Access the Create group wizard

.Steps

As your first step, access the Create group wizard.

. Select *ACCESS MANAGEMENT* > *Groups*.

. Select *Create group*.

## Choose a group type

You can create a local group or import a federated group.

.Steps

. Select the *Local group* tab to create a local group, or select the *Federated group* tab to import a group from the previously configured identity source.
+
If single sign-on (SSO) is enabled for your StorageGRID system, users belonging to local groups will not be able to sign in to the Tenant Manager, although they can use client applications to manage the tenant's resources, based on group permissions.

. Enter the group's name.

 ** *Local group*: Enter both a display name and a unique name. You can edit the display name later.

 ** *Federated group*: Enter the unique name. For Active Directory, the unique name is the name associated with the `sAMAccountName` attribute. For OpenLDAP, the unique name is the name associated with the `uid` attribute.

. Select *Continue*.

## Manage group permissions

Group permissions control which tasks users can perform in the Tenant Manager and Tenant Management API.

.Steps

. For *Access mode*, select one of the following:
** *Read-write* (default): Users can sign in to Tenant Manager and manage the tenant configuration.
** *Read-only*: Users can only view settings and features. They can't make any changes or perform any operations in the Tenant Manager or Tenant Management API. Local read-only users can change their own passwords.
+
NOTE: If a user belongs to multiple groups and any group is set to Read-only, the user will have read-only access to all selected settings and features.

. Select the *Root access* checkbox if group users need to sign in to the Tenant Manager or Tenant Management API.

. Select *Continue*.

## Set Swift group policy
Swift users need administrator permission to authenticate into the Swift REST API to create containers and ingest objects.

. Select the *Swift administrator* checkbox if group users need to use the Swift REST API to manage containers and objects.


. If you are creating a local group, select *Continue*. If you are creating a federated group, select *Create group* and *Finish*.

## Add users (local groups only)

You can save the group without adding users, or you can optionally add any local users that already exist.

.Steps

. Optionally, select one or more local users for this group.
+
If you have not yet created local users, you can add this group to the user on the Users page. See link:../tenant/managing-local-users.html[Manage local users].

. Select *Create group* and *Finish*.
+
The group you created appears in the list of groups.

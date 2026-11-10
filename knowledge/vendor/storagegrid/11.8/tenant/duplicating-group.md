---
id: "storagegrid-118-4195405cdef5d0e7"
title: "StorageGRID 11.8 Duplicate group"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/duplicating-group.adoc"
source_sha256: "459f334a377ea3a87ee428d1bd4fc4e930198697a26090921e1b1d1512691623"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/duplicating-group.adoc"
---

# StorageGRID 11.8 Duplicate group

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/duplicating-group.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Duplicate group
:icons: font
:imagesdir: ../media/

[.lead]
You can create new groups more quickly by duplicating an existing group.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the Root access permission. See link:tenant-management-permissions.html[Tenant management permissions].

.Steps
. Select *ACCESS MANAGEMENT* > *Groups*.
. Select the checkbox for the group you want to duplicate.
. Select *Duplicate group*. For additional details on creating a group, see the instructions for creating groups for link:creating-groups-for-s3-tenant.html[an S3 tenant] or for link:creating-groups-for-swift-tenant.html[a Swift tenant].
. Select the *Local group* tab to create a local group, or select the *Federated group* tab to import a group from the previously configured identity source.
+
If single sign-on (SSO) is enabled for your StorageGRID system, users belonging to local groups will not be able to sign in to the Tenant Manager, although they can use client applications to manage the tenant's resources, based on link:tenant-management-permissions.html[group permissions].

. Enter the group's name.
 ** *Local group*: Enter both a display name and a unique name. You can edit the display name later.
 ** *Federated group*: Enter the unique name. For Active Directory, the unique name is the name associated with the `sAMAccountName` attribute. For OpenLDAP, the unique name is the name associated with the `uid` attribute.
. Select *Continue*.
. As needed, modify the permissions for this group.
. Select *Continue*.
. As needed, if you are duplicating a group for an S3 tenant, optionally select a different policy from the *Add S3 policy* radio buttons. If you selected a custom policy, update the JSON string as required.
. Select *Create group*.

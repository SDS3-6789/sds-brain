---
id: "storagegrid-118-6ba895592082b7fc"
title: "StorageGRID 11.8 What is account clone?"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/grid-federation-what-is-account-clone.adoc"
source_sha256: "4a3662b2cd2a1340bb5aab3f5b71e9d66fc9724ef57c385ba0764d30d9813ede"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/grid-federation-what-is-account-clone.adoc"
---

# StorageGRID 11.8 What is account clone?

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/grid-federation-what-is-account-clone.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# What is account clone?
:icons: font
:imagesdir: ../media/

[.lead]
Account clone is the automatic replication of a tenant account, tenant groups, tenant users, and, optionally, S3 access keys between the StorageGRID systems in a link:grid-federation-overview.html[grid federation connection]. 

Account clone is required for link:grid-federation-what-is-cross-grid-replication.html[cross-grid replication]. Cloning account information from a source StorageGRID system to a destination StorageGRID system ensures that tenant users and groups can access the corresponding buckets and objects on either grid.

## Workflow for account clone

The workflow diagram shows the steps that grid administrators and permitted tenants will perform to set up account clone. These steps are performed after the link:grid-federation-create-connection.html[grid federation connection is configured].

image::../media/grid-federation-account-clone-workflow.png[workflow for account clone]

## Grid admin workflow

The steps that grid admins perform depend on whether the StorageGRID systems in the link:grid-federation-overview.html[grid federation connection] use single sign-on (SSO) or identity federation.

### [[account-clone-sso]]Configure SSO for account clone (optional)

If either StorageGRID system in the grid federation connection uses SSO, both grids must use SSO. Before creating the tenant accounts for grid federation, the grid admins for the tenant's source and destination grids must perform these steps.

.Steps

. Configure the same identity source for both grids. See link:using-identity-federation.html[Use identity federation].

. Configure the same SSO identity provider (IdP) for both grids. See link:configuring-sso.html[Configure single sign-on].

. link:managing-admin-groups.html[Create the same admin group] on both grids by importing the same federated group.
+
When you create the tenant, you will select this group to have the initial Root access permission for both the source and destination tenant accounts. 
+
NOTE: If this admin group doesn't exist on both grids before you create the tenant, the tenant isn't replicated to the destination.

### [[account-clone-identity-federation]]Configure grid-level identity federation for account clone (optional)

If either StorageGRID system uses identity federation without SSO, both grids must use identity federation. Before creating the tenant accounts for grid federation, the grid admins for the tenant's source and destination grids must perform these steps.

.Steps

. Configure the same identity source for both grids. See link:using-identity-federation.html[Use identity federation].

. Optionally, if a federated group will have initial Root access permission for both the source and destination tenant accounts, link:managing-admin-groups.html[create the same admin group] on both grids by importing the same federated group.
+
NOTE: If you assign Root access permission to a federated group that doesn't exist on both grids, the tenant isn't replicated to the destination grid.

. If you don't want a federated group to have initial Root access permission for both accounts, specify a password for the local root user.

### Create permitted S3 tenant account

After optionally configuring SSO or identity federation, a grid admin performs these steps to determine which tenants can replicate bucket objects to other StorageGRID systems.

.Steps
. Determine which grid you want to be the tenant's source grid for account clone operations.
+
The grid where the tenant is originally created is known as the tenant's _source grid_. The grid where the tenant is replicated is known as the tenant's _destination grid_. 

. On that grid, create a new S3 tenant account or edit an existing account.

. Assign the *Use grid federation connection* permission.
. If the tenant account will manage its own federated users, assign the *Use own identity source* permission.
+
If this permission is assigned, both the source and destination tenant accounts must configure the same identity source before creating federated groups. Federated groups added to the source tenant can't be cloned to the destination tenant unless both grids use the same identity source.

. Select a specific grid federation connection.

. Save the new or modified tenant.
+
When a new tenant with the *Use grid federation connection* permission is saved, StorageGRID automatically creates a replica of that tenant on the other grid, as follows:

* Both tenant accounts have the same account ID, name, storage quota, and assigned permissions.
* If you selected a federated group to have Root access permission for the tenant, that group is cloned to the destination tenant.
* If you selected a local user to have Root access permission for the tenant, that user is cloned to the destination tenant. However, the password for that user is not cloned.

For details, see
link:grid-federation-manage-tenants.html[Manage permitted tenants for grid federation].

## Permitted tenant account workflow

After a tenant with the *Use grid federation connection* permission is replicated to the destination grid, permitted tenant accounts can perform these steps to clone tenant groups, users, and S3 access keys.

.Steps

. Sign in to the tenant account on the tenant's source grid.

. If permitted, configure identify federation on both the source and destination tenant accounts.

. Create groups and users on the source tenant.
+
When new groups or users are created on the source tenant, StorageGRID automatically clones them to the destination tenant, but no cloning occurs from the destination back to the source. 

. Create S3 access keys.

. Optionally, clone S3 access keys from the source tenant to the destination tenant. 

For details about the permitted tenant account workflow and to learn how groups, users, and S3 access keys are cloned, see link:../tenant/grid-federation-account-clone.html[Clone tenant groups and users] and link:../tenant/grid-federation-clone-keys-with-api.html[Clone S3 access keys using the API].

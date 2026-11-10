---
id: "storagegrid-118-80eb1d67136f5735"
title: "StorageGRID 11.8 Manage tenants: Overview"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/managing-tenants.adoc"
source_sha256: "1baaad3746984c4a0a32cba1a186ce74831904b14f8c20f437ec4297a12b6ed6"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/managing-tenants.adoc"
---

# StorageGRID 11.8 Manage tenants: Overview

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/managing-tenants.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Manage tenants: Overview
:icons: font
:imagesdir: ../media/

[.lead]
As a grid administrator, you create and manage the tenant accounts that S3 and Swift clients use to store and retrieve objects.

NOTE: Support for Swift client applications has been deprecated and will be removed in a future release.

## What are tenant accounts?

A tenant account allows you to use either the Simple Storage Service (S3) REST API or the Swift REST API to store and retrieve objects in a StorageGRID system.

Each tenant account has federated or local groups, users, S3 buckets or Swift containers, and objects.

Tenant accounts can be used to segregate stored objects by different entities. For example, multiple tenant accounts can be used for either of these use cases:

* *Enterprise use case:* If you are administering a StorageGRID system in an enterprise application, you might want to segregate the grid's object storage by the different departments in your organization. In this case, you could create tenant accounts for the Marketing department, the Customer Support department, the Human Resources department, and so on.
+
NOTE: If you use the S3 client protocol, you can use S3 buckets and bucket policies to segregate objects between the departments in an enterprise. You don't need to use tenant accounts. See instructions for implementing link:../s3/bucket-and-group-access-policies.html[S3 buckets and bucket policies] for more information.

* *Service provider use case:* If you are administering a StorageGRID system as a service provider, you can segregate the grid's object storage by the different entities that will lease the storage on your grid. In this case, you would create tenant accounts for Company A, Company B, Company C, and so on.

For more information, see link:../tenant/index.html[Use a tenant account].

## How do I create a tenant account?

When you create a tenant account, you specify the following information:

* Basic information including the tenant name, client type (S3 or Swift) and optional storage quota.

* Permissions for the tenant account, such as whether the tenant account can use S3 platform services, configure its own identity source, use S3 Select, or use a grid federation connection.

* The initial root access for the tenant, based on whether the StorageGRID system uses local groups and users, identity federation, or single sign-on (SSO).

In addition, you can enable the S3 Object Lock setting for the StorageGRID system if S3 tenant accounts need to comply with regulatory requirements. When S3 Object Lock is enabled, all S3 tenant accounts can create and manage compliant buckets.

## What is Tenant Manager used for?

After you create the tenant account, tenant users can sign in to the Tenant Manager to perform tasks such as the following:

* Set up identity federation (unless the identity source is shared with the grid)
* Manage groups and users
* Use grid federation for account clone and cross-grid replication
* Manage S3 access keys
* Create and manage S3 buckets
* Use S3 platform services
* Use S3 Select
* Monitor storage usage

TIP: While S3 tenant users can create and manage S3 access key and buckets with the Tenant Manager, they must use an S3 client application to ingest and manage objects. See link:../s3/index.html[Use S3 REST API] for details.

TIP: Swift users must have the Root access permission to access the Tenant Manager. However, the Root access permission does not allow users to authenticate into the Swift REST API to create containers and ingest objects. Users must have the Swift Administrator permission to authenticate into the Swift REST API.

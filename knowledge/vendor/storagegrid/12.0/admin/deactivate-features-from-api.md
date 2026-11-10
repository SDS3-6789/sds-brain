---
id: "storagegrid-120-b07c933845e8ccd1"
title: "StorageGRID 12.0 Deactivate StorageGRID features with the API"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/deactivate-features-from-api.adoc"
source_sha256: "f963256d94ee81d9ab6b99b3f879cdc45fe79e5c11ae7776af886a99bf62e0f3"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/deactivate-features-from-api.adoc"
---

# StorageGRID 12.0 Deactivate StorageGRID features with the API

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/deactivate-features-from-api.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Deactivate StorageGRID features with the API
:icons: font
:imagesdir: ../media/

[.lead]
You can use the Grid Management API to completely deactivate certain features in the StorageGRID system. When a feature is deactivated, no one can be assigned permissions to perform the tasks related to that feature.

.About this task
The Deactivated Features system allows you to prevent access to certain features in the StorageGRID system. Deactivating a feature is the only way to prevent the root user or users who belong to admin groups with *Root access* permission from being able to use that feature.

To understand how this functionality might be useful, consider the following scenario:

_Company A is a service provider who leases the storage capacity of their StorageGRID system by creating tenant accounts. To protect the security of their leaseholders' objects, Company A wants to ensure that its own employees can never access any tenant account after the account has been deployed._

_Company A can accomplish this goal by using the Deactivate Features system in the Grid Management API. By completely deactivating the *Change tenant root password* feature in the Grid Manager (both the UI and the API), Company A ensures that Admin users--including the root user and users belonging to groups with the *Root access* permission--can't change the password for any tenant account's root user._


.Steps

. Access the Swagger documentation for the Grid Management API. See link:using-grid-management-api.html[Use the Grid Management API].
. Locate the Deactivate Features endpoint.
. To deactivate a feature, such as Change tenant root password, send a body to the API like this:
+
`{ "grid": {"changeTenantRootPassword": true} }`
+
When the request is complete, the Change tenant root password feature is disabled. The *Change tenant root password* management permission no longer appears in the user interface, and any API request that attempts to change the root password for a tenant will fail with "403 Forbidden."

## Reactivate deactivated features

By default, you can use the Grid Management API to reactivate a feature that has been deactivated. However, if you want to prevent deactivated features from ever being reactivated, you can deactivate the *activateFeatures* feature itself.

CAUTION: The *activateFeatures* feature can't be reactivated. If you decide to deactivate this feature, be aware that you will permanently lose the ability to reactivate any other deactivated features. You must contact technical support to restore any lost functionality.

.Steps

. Access the Swagger documentation for the Grid Management API.
. Locate the Deactivate Features endpoint.
. To reactivate all features, send a body to the API like this:
+
`{ "grid": null }`
+
When this request is complete, all features, including the Change tenant root password feature, are reactivated. The *Change tenant root password* management permission now appears in the user interface, and any API request that attempts to change the root password for a tenant will succeed, assuming the user has the *Root access* or *Change tenant root password* management permission.

TIP: The previous example causes _all_ deactivated features to be reactivated. If other features have been deactivated that should remain deactivated, you must explicitly specify them in the PUT request. For example, to reactivate the Change tenant root password feature and continue to deactivate the storageAdmin management permission, send this PUT request: +
`{ "grid": {"storageAdmin": true} }`

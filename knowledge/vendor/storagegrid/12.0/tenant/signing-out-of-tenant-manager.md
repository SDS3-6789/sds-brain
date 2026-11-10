---
id: "storagegrid-120-3aed1c88214762ea"
title: "StorageGRID 12.0 Sign out of StorageGRID Tenant Manager"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/signing-out-of-tenant-manager.adoc"
source_sha256: "4d2eae75529986c698c021eea2fb698f2e23599ce3935f8dee6fd13fed8580d2"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/signing-out-of-tenant-manager.adoc"
---

# StorageGRID 12.0 Sign out of StorageGRID Tenant Manager

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/signing-out-of-tenant-manager.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Sign out of StorageGRID Tenant Manager
:icons: font
:imagesdir: ../media/

[.lead]
When you are done working with the Tenant Manager, you must sign out to ensure that unauthorized users can't access the StorageGRID system. Closing your browser might not sign you out of the system, based on browser cookie settings.

.Steps

. Locate the username drop-down in the top-right corner of the user interface.
+
image:tenant_user_sign_out.png[Sign out link]

. Select the username and then select *Sign out*.
+
* If SSO is not in use:
+
You are signed out of the Admin Node. The Tenant Manager sign in page is displayed.
+
NOTE: If you signed into more than one Admin Node, you must sign out of each node.

* If SSO is enabled:
+
You are signed out of all Admin Nodes you were accessing. The StorageGRID Sign in page is displayed. The name of the tenant account you just accessed is listed as the default in the *Recent Accounts* drop-down, and the tenant's *Account ID* is shown.
+
NOTE: If SSO is enabled and you are also signed in to the Grid Manager, you must also sign out of the Grid Manager to sign out of SSO.

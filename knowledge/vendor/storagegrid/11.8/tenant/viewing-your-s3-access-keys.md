---
id: "storagegrid-118-fd74c47f35c227e1"
title: "StorageGRID 11.8 View your S3 access keys"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/viewing-your-s3-access-keys.adoc"
source_sha256: "22507d51e0cea1127c5a10b1cd62b1fcb5c16ae80a1904a94bfd89b3c97f0c04"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/viewing-your-s3-access-keys.adoc"
---

# StorageGRID 11.8 View your S3 access keys

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/tenant/viewing-your-s3-access-keys.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View your S3 access keys
:icons: font
:imagesdir: ../media/

[.lead]
If you are using an S3 tenant and you have the link:tenant-management-permissions.html[appropriate permission], you can view a list of your S3 access keys. You can sort the list by expiration time, so you can determine which keys will expire soon. As needed, you can link:creating-your-own-s3-access-keys.html[create new keys] or link:deleting-your-own-s3-access-keys.html[delete keys] that you are no longer using.

CAUTION: The S3 buckets and objects belonging to your account can be accessed using the access key ID and secret access key displayed for your account in the Tenant Manager. For this reason, protect access keys as you would a password. Rotate access keys on a regular basis, remove any unused keys from your account, and never share them with other users.

.Before you begin

* You are signed in to the Tenant Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You belong to a user group that has the Manage your own S3 credentials link:tenant-management-permissions.html[permission].

.Steps

. Select *STORAGE (S3)* > *My access keys*.

. From the My access keys page, sort any existing access keys by *Expiration time* or *Access key ID*.

. As needed, create new keys or delete any keys that you are no longer using.
+
If you create new keys before the existing keys expire, you can begin using the new keys without temporarily losing access to the objects in the account.
+
Expired keys are removed automatically.

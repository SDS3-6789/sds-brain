---
id: "storagegrid-118-397bcbdec3c44b67"
title: "StorageGRID 11.8 Example group policies"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/s3/example-group-policies.adoc"
source_sha256: "fdf3c964095be35094d20eca684644e9376daad5537ff0d904dbcfb0438dbdb5"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/example-group-policies.adoc"
---

# StorageGRID 11.8 Example group policies

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/s3/example-group-policies.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Example group policies
:icons: font
:imagesdir: ../media/

[.lead]
Use the examples in this section to build StorageGRID access policies for groups.

Group policies specify the access permissions for the group that the policy is attached to. There is no `Principal` element in the policy because it is implicit. Group policies are configured using the Tenant Manager or the API.

## Example: Set group policy using Tenant Manager

When you add or edit a group in the Tenant Manager, you can select a group policy to determine which S3 access permissions the members of this group will have. See link:../tenant/creating-groups-for-s3-tenant.html[Create groups for an S3 tenant].

* *No S3 Access*: Default option. Users in this group don't have access to S3 resources, unless access is granted with a bucket policy. If you select this option, only the root user will have access to S3 resources by default.
* *Read Only Access*: Users in this group have read-only access to S3 resources. For example, users in this group can list objects and read object data, metadata, and tags. When you select this option, the JSON string for a read-only group policy appears in the text box. You can't edit this string.
* *Full Access*: Users in this group have full access to S3 resources, including buckets. When you select this option, the JSON string for a full-access group policy appears in the text box. You can't edit this string.

* *Ransomware Mitigation*: This sample policy applies to all buckets for this tenant. Users in this group can perform common actions, but can't permanently delete objects from buckets that have object versioning enabled.
+
Tenant Manager users who have the Manage all buckets permission can override this group policy. Limit the Manage all buckets permission to trusted users, and use Multi-Factor Authentication (MFA) where available.

* *Custom*: Users in the group are granted the permissions you specify in the text box.

## Example: Allow group full access to all buckets

In this example, all members of the group are permitted full access to all buckets owned by the tenant account unless explicitly denied by bucket policy.

----
{
  "Statement": [
    {
      "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::*"
    }
  ]
}
----

## Example: Allow group read-only access to all buckets

In this example, all members of the group have read-only access to S3 resources, unless explicitly denied by the bucket policy. For example, users in this group can list objects and read object data, metadata, and tags.

----
{
  "Statement": [
    {
      "Sid": "AllowGroupReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:ListBucket",
        "s3:ListBucketVersions",
        "s3:GetObject",
        "s3:GetObjectTagging",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionTagging"
      ],
      "Resource": "arn:aws:s3:::*"
    }
  ]
}
----

## Example: Allow group members full access to only their "folder" in a bucket

In this example, members of the group are only permitted to list and access their specific folder (key prefix) in the specified bucket. Note that access permissions from other group policies and the bucket policy should be considered when determining the privacy of these folders.

----
{
  "Statement": [
    {
      "Sid": "AllowListBucketOfASpecificUserPrefix",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::department-bucket",
      "Condition": {
        "StringLike": {
          "s3:prefix": "${aws:username}/*"
        }
      }
    },
    {
      "Sid": "AllowUserSpecificActionsOnlyInTheSpecificUserPrefix",
      "Effect": "Allow",
      "Action": "s3:*Object",
      "Resource": "arn:aws:s3:::department-bucket/${aws:username}/*"
    }
  ]
}
----

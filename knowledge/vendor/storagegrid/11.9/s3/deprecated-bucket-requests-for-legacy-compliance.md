---
id: "storagegrid-119-1610e85c1ad9cdd7"
title: "StorageGRID 11.9 Deprecated bucket requests for legacy Compliance"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/deprecated-bucket-requests-for-legacy-compliance.adoc"
source_sha256: "c4408203879f8d91befe43f44319623cf45ec4a2efe4ed13c30ec6af5f19a760"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/deprecated-bucket-requests-for-legacy-compliance.adoc"
---

# StorageGRID 11.9 Deprecated bucket requests for legacy Compliance

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/deprecated-bucket-requests-for-legacy-compliance.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Deprecated bucket requests for legacy Compliance
:icons: font
:imagesdir: ../media/

[.lead]
You might need to use the StorageGRID S3 REST API to manage buckets that were created using the legacy Compliance feature.

## Compliance feature deprecated

The StorageGRID Compliance feature that was available in previous StorageGRID versions is deprecated and has been replaced by S3 Object Lock.

If you previously enabled the global Compliance setting, the global S3 Object Lock setting is enabled in StorageGRID 11.6. You can no longer create new buckets with Compliance enabled; however, as required, you can use the StorageGRID S3 REST API to manage any existing legacy Compliant buckets.

* link:use-s3-api-for-s3-object-lock.html[Use S3 REST API to configure S3 Object Lock]

* link:../ilm/index.html[Manage objects with ILM]

* https://kb.netapp.com/Advice_and_Troubleshooting/Hybrid_Cloud_Infrastructure/StorageGRID/How_to_manage_legacy_Compliant_buckets_in_StorageGRID_11.5[NetApp Knowledge Base: How to manage legacy Compliant buckets in StorageGRID 11.5^]

Deprecated compliance requests: 

* link:../s3/deprecated-put-bucket-request-modifications-for-compliance.html[Deprecated - PUT Bucket request modifications for compliance]

+
The SGCompliance XML element is deprecated. Previously, you could include this StorageGRID custom element in the optional XML request body of PUT Bucket requests to create a Compliant bucket.

* link:../s3/deprecated-get-bucket-compliance-request.html[Deprecated - GET Bucket compliance]

+
The GET Bucket compliance request is deprecated. However, you can continue to use this request to determine the compliance settings currently in effect for an existing legacy Compliant bucket.

* link:../s3/deprecated-put-bucket-compliance-request.html[Deprecated - PUT Bucket compliance]

+
The PUT Bucket compliance request is deprecated. However, you can continue to use this request to modify the compliance settings for an existing legacy Compliant bucket. For example, you can place an existing bucket on legal hold or increase its retention period.

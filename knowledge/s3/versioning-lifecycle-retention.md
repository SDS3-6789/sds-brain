---
id: s3-versioning-lifecycle-retention
title: Keep versioning, lifecycle, and retention separate
area: s3
type: knowledge
applies_to: [aws-s3-reference, storagegrid-11.9, ceph-rgw]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-versioning, aws-s3-lifecycle, aws-s3-object-lock, netapp-sg119-object-lock]
---

# Keep versioning, lifecycle, and retention separate

These are distinct dimensions in a diagnosis. AWS provides the reference concepts below; confirm the actual backend's support and settings before applying them.

| Dimension | Evidence to collect | What the agent must not infer |
|---|---|---|
| Versioning | Bucket state and the exact object version involved | A current-key view includes every historical version |
| Lifecycle | Existing rules, filters, relevant ages, and status | A policy denial alone prevents lifecycle actions |
| Object retention | Retention mode and retain-until date for the specific version | New versions are prevented by the same retention setting |
| Legal hold | Hold status for the specific version | A fixed expiration date necessarily removes a legal hold |

AWS versioning can preserve multiple complete object versions; a normal deletion in a versioned bucket can insert a delete marker rather than remove the historical version. Inspect the version ID and delete-marker state before reporting object loss or reclaimed capacity. [Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

AWS lifecycle rules can transition or expire qualifying objects, including existing objects. Its documentation states that a bucket policy does not prevent lifecycle deletions or transitions. Do not recommend a policy change as proof that lifecycle is disabled. [Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

AWS Object Lock applies protection to object versions through retention and legal holds. A legal hold remains until removed and is separate from a retention period. Protected versions can coexist with newer versions or delete markers. [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

StorageGRID has its own Object Lock and ILM requirements. Read the version-specific settings rather than assuming all current AWS functionality is available. [SG 11.9 Object Lock](https://docs.netapp.com/us-en/storagegrid-119/ilm/managing-objects-with-s3-object-lock.html).

The first release is read-only. Produce an evidence summary for the authorized owner; do not delete a version, remove a legal hold, bypass governance, suspend versioning, or edit lifecycle rules. Capacity pressure does not itself authorize changing retention.

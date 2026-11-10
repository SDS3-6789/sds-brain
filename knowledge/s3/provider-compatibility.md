---
id: s3-provider-compatibility
title: AWS S3, Ceph RGW, and StorageGRID compatibility boundaries
area: s3
type: knowledge
applies_to: [aws-s3-reference, ceph-rgw, storagegrid-11.8, storagegrid-11.9, storagegrid-12-unconfirmed]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-consistency, netapp-sg118-consistency, netapp-sg119-consistency, netapp-sg118-s3, netapp-sg119-s3, netapp-sg120-s3, netapp-sg119-s3-quick-reference, netapp-sg119-object-operations, aws-s3-kms]
---

# AWS S3, Ceph RGW, and StorageGRID compatibility boundaries

AWS is a protocol and implementation reference in this repository. The user has not confirmed an AWS account or an AWS deployment. Every answer must name the actual target backend; an AWS article cannot establish support in Ceph RGW or StorageGRID.

| Concern | AWS reference | StorageGRID evidence | Ceph RGW decision |
|---|---|---|---|
| Object consistency | AWS documents strong object read-after-write and list consistency | 11.8/11.9 default read-after-new-write treats overwrites, metadata updates, and deletes differently | Check the installed vendor release and local/multisite context |
| Checksum behavior | Check the exact API, algorithm, SDK version, and headers | 11.9 documents added pre-calculated SHA-256 support for selected operations | Do not assume all algorithms or trailer formats are implemented |
| STS/session policy | AWS IAM/STS are their own services | 12.0 documents AssumeRole and session-policy additions | Verify RGW STS and identity configuration independently |
| API coverage | AWS documentation includes AWS-specific features | Use the versioned supported-operation table and operation caveats | Use the matching RHCS/IBM/upstream RGW documentation |
| Encryption | AWS SSE-KMS involves AWS KMS permissions and keys | Verify the installed backend's encryption choices | Verify actual key-management integration; AWS KMS behavior is not inherited |

Sources: [AWS consistency](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel), [SG 11.8 consistency](https://docs.netapp.com/us-en/storagegrid-118/s3/consistency-controls.html), [SG 11.9 consistency](https://docs.netapp.com/us-en/storagegrid-119/s3/consistency-controls.html), [11.8 S3 updates](https://docs.netapp.com/us-en/storagegrid-118/s3/index.html), [11.9 S3 updates](https://docs.netapp.com/us-en/storagegrid-119/s3/index.html), [12.0 S3 updates](https://docs.netapp.com/us-en/storagegrid-120/s3/index.html), [SG operation reference](https://docs.netapp.com/us-en/storagegrid-119/s3/quick-reference-support-for-aws-apis.html), and [AWS SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

## How to answer compatibility questions

Record the complete tuple: product build, request operation, request headers, SDK/CLI version, signature method, endpoint style, encryption mode, and object/bucket settings. Classify the answer as **documented**, **observed in this environment**, or **unverified**. A successful basic upload is insufficient evidence for multipart checksums, retention, lifecycle, policy conditions, or conditional writes.

Use a feature matrix with one row per exact operation/header combination. Include a source and a test result separately. Production writes are outside this release's read-only integration policy; compatibility tests requiring writes belong in a separately approved test plan and test bucket.

## Ownership is also provider-specific

The StorageGRID 11.9 object-operation reference states that objects in a bucket are owned by the bucket owner. Do not transplant an AWS cross-account ownership explanation into a StorageGRID incident without checking that provider's rules. [StorageGRID object operations](https://docs.netapp.com/us-en/storagegrid-119/s3/operations-on-objects.html).

Unknown support should produce a precise gap, such as "CRC32C trailer validation for this exact SG build is not yet verified," rather than "S3 compatible, therefore supported."

---
id: runbook-s3-multipart-checksums
title: Diagnose multipart completion and checksum errors
area: s3
type: runbook
applies_to: [aws-s3-reference, ceph-rgw, storagegrid]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-multipart, aws-s3-list-multipart, netapp-sg119-s3, netapp-sg119-s3-quick-reference, netapp-sg119-object-operations, aws-s3-errors]
---

# Diagnose multipart completion and checksum errors

## Capture the failed stage

Bind one customer/backend, cluster/grid, bucket alias, object alias, upload ID alias, and UTC interval. Identify whether failure occurred during initiation, a part upload, part listing, or completion. Record SDK/CLI versions, part size/count, retry behavior, checksum algorithm, and relevant header names. Do not copy the object body, signed headers, encryption keys, or full upload identifiers into a shared knowledge page.

AWS describes multipart upload as independent part transfers followed by completion. An initiated upload can persist until explicitly completed or stopped. The brain observes unfinished uploads; aborting or completing them is a write operation and is disabled in the first release. [AWS multipart guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html).

## Bound the inventory read

Use an already approved customer-specific profile, endpoint, region, bucket, and narrow prefix. Confirm that the backend supports the operation before running the example. It requests one returned page instead of automatically traversing all pages; SDK/CLI retries may still occur.

```bash
aws --profile "$SDS_S3_PROFILE" --endpoint-url "$SDS_S3_ENDPOINT" \
  --region "$SDS_S3_REGION" --cli-connect-timeout 5 --cli-read-timeout 10 \
  s3api list-multipart-uploads --bucket "$SDS_S3_BUCKET" \
  --prefix "$SDS_APPROVED_PREFIX" --max-uploads 20 --no-paginate \
  --query '{Truncated:IsTruncated,Uploads:Uploads[].{Key:Key,Started:Initiated}}'
```

The AWS CLI reference documents service-side limits and pagination markers. A truncated response is a sample, not proof that all unfinished uploads were examined. Object keys are customer data; keep this output within the authorized incident scope. [CLI reference](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-multipart-uploads.html).

## Match the implementation

StorageGRID 11.9 documents added pre-calculated SHA-256 support for selected object and multipart operations. Read the exact operation's supported header/body fields; do not infer that all AWS algorithms or streaming variants are supported. Check the selected product version before suggesting a client configuration change. [11.9 updates](https://docs.netapp.com/us-en/storagegrid-119/s3/index.html) and [API reference](https://docs.netapp.com/us-en/storagegrid-119/s3/quick-reference-support-for-aws-apis.html).

Use the client's recorded part identities and completion manifest, when safely available, to investigate missing/repeated parts, differing upload IDs, or algorithm mismatch. Treat an ETag as an opaque returned identifier unless the provider explicitly documents the relevant checksum semantics; avoid assuming it is always a whole-object MD5. Review the actual provider's operation semantics. [StorageGRID object operations](https://docs.netapp.com/us-en/storagegrid-119/s3/operations-on-objects.html).

Interpret `InvalidPart`, `BadDigest`, or other reported codes from the provider reference and retain the failed stage. [AWS errors](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/ErrorResponses.html). Finish with the evidence-supported compatibility or client-state hypothesis and the smallest next read. No abort, completion, object deletion, lifecycle edit, or new upload is performed.

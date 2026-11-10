---
id: runbook-s3-access-denied
title: Investigate S3 access denied without changing permissions
area: s3
type: runbook
applies_to: [aws-s3-reference, ceph-rgw, storagegrid]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-access-denied, aws-iam-policy-evaluation, aws-s3-head-object, aws-s3-head-bucket, aws-s3-kms, netapp-sg119-errors]
---

# Investigate S3 access denied without changing permissions

## Bind the request

Confirm one customer, backend, cluster/grid, principal alias, bucket alias, operation, and UTC interval. Record exact product and SDK/CLI versions. Use the credentials already authorized for that customer through the local credential mechanism; never ask the user to paste a secret key. Obtain the original HTTP status, provider error, and request ID before retrying.

For AWS, a 403 can come from implicit or explicit denial, and the troubleshooting guide includes bucket/IAM policy, ownership, encryption, endpoint, organization, and other applicable layers. Only investigate layers that exist in the identified deployment. [AWS 403 guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshoot-403-errors.html). StorageGRID has its own supported error response set. [SG errors](https://docs.netapp.com/us-en/storagegrid-119/s3/error-responses.html).

## Minimal authorized probes

If the operator has approved a known bucket and a non-sensitive diagnostic object, these examples issue metadata-only reads. Each `SDS_` variable must be explicitly set from the selected customer's inventory; none is a default endpoint.

```bash
aws --profile "$SDS_S3_PROFILE" --endpoint-url "$SDS_S3_ENDPOINT" \
  --region "$SDS_S3_REGION" --cli-connect-timeout 5 --cli-read-timeout 10 \
  s3api head-bucket --bucket "$SDS_S3_BUCKET"

aws --profile "$SDS_S3_PROFILE" --endpoint-url "$SDS_S3_ENDPOINT" \
  --region "$SDS_S3_REGION" --cli-connect-timeout 5 --cli-read-timeout 10 \
  s3api head-object --bucket "$SDS_S3_BUCKET" --key "$SDS_DIAGNOSTIC_KEY" \
  --query '{Length:ContentLength,Modified:LastModified,Version:VersionId}'
```

AWS documents generic errors for both HEAD operations. In particular, a missing object can produce 403 when the caller lacks `s3:ListBucket`; it need not prove that the object exists or that its encryption is at fault. Do not assume all backend details are identical. [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html), [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html).

## Inspect policy evidence

Read only the applicable scoped policy statements and resource/action match. In AWS, an explicit deny overrides an allow; boundaries and organization policies can further constrain access. Ask for a redacted policy excerpt if the integration cannot safely retrieve the required scope. [IAM evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

For an actual AWS SSE-KMS object, include the applicable key permissions and key state in the investigation. On RGW or StorageGRID, first establish the real encryption implementation; do not prescribe AWS KMS permissions by analogy. [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

## Deliver

Return the failing action/resource/principal aliases, evidence for the denial layer, and remaining uncertainty. Propose the narrowest correction only after identifying the cause. Do not attach administrator policies, make a bucket public, rotate keys, bypass TLS, or alter retention as a diagnostic shortcut.

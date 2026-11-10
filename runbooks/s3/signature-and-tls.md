---
id: runbook-s3-signature-tls
title: Diagnose S3 signature mismatch and TLS failures
area: s3
type: runbook
applies_to: [aws-s3-reference, ceph-rgw, storagegrid]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-sigv4, aws-s3-presigned, aws-s3-errors, netapp-sg119-client-connections, netapp-sg119-s3-quick-reference]
---

# Diagnose S3 signature mismatch and TLS failures

## Establish the layer

Record one customer/backend, endpoint alias, TLS hostname, approved port, SDK version, addressing style, request method, and UTC incident time. Separate DNS/connectivity/TLS failure from a provider's `SignatureDoesNotMatch` or another S3 response. A request that never establishes TLS has not yet reached S3 signature validation.

Use existing client and service evidence first. Do not collect a full signed URL, secret key, Authorization header, session token, or unrestricted debug trace. A signature mismatch investigation usually needs header names, canonicalization choices, timestamps, and endpoint settings, not credential values.

## Signature evidence

1. Compare the configured signing region/service and request timestamp with the actual endpoint contract. AWS SigV4 derives the signing key from credential material and date/region/service scope. Relevant request components are included in the signature, so proxy rewriting or encoding changes are candidates to examine. [AWS SigV4](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/sig-v4-authenticating-requests.html).
2. Check method, host, port treatment, path-style versus virtual-host addressing, URL encoding, query parameters, and signed header names in redacted client evidence. Do not hand-build a new signature as the first intervention; use a supported SDK with the same reviewed settings.
3. Record whether credentials are static or session-based and whether the client is supplying a session token when required. This is a metadata question; do not print the token. For Ceph/StorageGRID, verify that the deployed release and identity configuration support the method actually used.
4. For a presigned URL, record its method, expiry, generation time, and the issuing principal alias. AWS documents that the URL operates with the issuer's permissions and that credential lifetime can constrain validity. Do not paste or replay the entire URL in shared reports. [Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html).

## TLS and proxy evidence

Inspect the presented certificate's subject/SAN, validity interval, issuer chain, and the client's trust store using the organization's existing diagnostic method. In StorageGRID, the client connection settings include the hostname, endpoint port, and certificate. A successful connection by IP with certificate verification disabled does not validate the intended hostname path. [SG client requirements](https://docs.netapp.com/us-en/storagegrid-119/admin/configuring-client-connections.html).

Review the exact algorithm/header behavior against the provider's release-specific API reference, especially after an SDK upgrade. Do not infer support for a checksum, chunking mode, or trailer from generic S3 compatibility. [SG 11.9 supported APIs](https://docs.netapp.com/us-en/storagegrid-119/s3/quick-reference-support-for-aws-apis.html).

## Output

Separate evidence-supported TLS, clock/scope, canonicalization, credential-lifecycle, and compatibility hypotheses. Use the provider error reference for interpretation. [AWS error codes](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/ErrorResponses.html). Suggest a controlled comparison using one approved metadata request; no credential rotation or proxy/TLS change is performed by this runbook.

---
id: s3-incident-evidence-contract
title: Minimal customer-scoped S3 evidence
area: s3
type: knowledge
applies_to: [aws-s3-reference, ceph-rgw, storagegrid]
confidence: documented
last_verified: 2026-11-09
sources: [aws-s3-head-object, aws-s3-head-bucket, netapp-sg119-errors, netapp-sg119-logs]
---

# Minimal customer-scoped S3 evidence

This is a proposed SDS evidence contract. It is not an assertion that the required telemetry already exists.

Before diagnosing a request, bind the session to exactly one customer alias, cluster/grid alias, backend type, release, tenant/account alias, and UTC time interval. Store customer-specific mappings in that customer's approved scope. Do not send a cross-customer account listing to the model and then filter it afterward.

Collect the following fields when available:

| Field | Why it matters |
|---|---|
| Operation, status, provider error code | Separates transport, authentication, authorization, and service failure |
| Request/correlation ID and UTC timestamp | Joins client, load-balancer, backend, and monitoring evidence |
| Endpoint alias, SDK version, addressing style | Identifies the path actually used |
| Logical object size and multipart stage | Separates request latency from transfer/workload effects |
| Retry count and elapsed time | Distinguishes one slow operation from repeated failed attempts |
| Principal/tenant aliases and applicable scope | Establishes the authorization boundary |
| Version ID, if relevant | Prevents confusing current and historical object state |

Preserve the provider's error code. StorageGRID includes both applicable S3 errors and additional responses; the HTTP status alone is incomplete. [Error reference](https://docs.netapp.com/us-en/storagegrid-119/s3/error-responses.html).

## Metadata-first probes

Use one explicitly approved bucket/object. `HeadObject` returns metadata without the object body, but its error is generic and can depend on permissions. `HeadBucket` also returns generic errors. Neither is a universal proof of existence, key validity, or policy correctness. These are AWS-documented behaviors; verify the matching provider implementation. [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html), [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html).

Object names, user metadata, tenant names, presigned URLs, and signed headers may contain sensitive information. Return only fields required to diagnose the incident. Do not enable unrestricted CLI debug output, return object payloads, enumerate every bucket, or retrieve all users as a default diagnostic step.

For StorageGRID, select a bounded interval from the relevant existing endpoint or audit logs. Its documented log families distinguish management requests, S3 endpoints, and other services. Preserve the original event source in the evidence record. [Log reference](https://docs.netapp.com/us-en/storagegrid-119/monitor/logs-files-reference.html).

An answer should end with observed evidence, a ranked hypothesis, what would falsify it, and the next smallest authorized read. An absence of permission or telemetry is a gap, not evidence of healthy service.

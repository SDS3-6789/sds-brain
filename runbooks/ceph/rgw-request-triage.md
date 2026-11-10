---
id: "rb-rgw-request-triage"
title: "RGW S3 errors and latency triage"
area: "ceph"
type: "runbook"
applies_to: ["rhcs-7.1", "rhcs-8.1"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhcs-7-rgw", "rhcs-8-rgw", "ceph-squid-s3", "ceph-squid-s3-auth", "ceph-squid-rgw-admin", "ceph-squid-rgw-metrics", "ceph-squid-cephadm", "ceph-squid-multitenancy"]
---

# RGW S3 errors and latency triage

## Pin the request and backend

Select the customer, cluster, endpoint and RGW service before querying anything. Objectify's logical account must be mapped to the RGW user and this backend; the owner reports that Objectify may also point to a StorageGRID tenant. Do not diagnose a StorageGRID response using an assumed Ceph backend.

Collect the UTC failure interval, exact S3 operation, HTTP status, S3 error code, request ID, region setting, addressing style, SDK/CLI version and whether the request went through a proxy/load balancer. Use an object alias when the real key is sensitive. Do not request Authorization headers, secret keys, session tokens or complete signed URLs.

## Establish whether RADOS or RGW is affected

Use the previously verified FSID and health baseline. Set `RGW_SERVICE` and `RGW_DAEMON_ID` from the incident inventory; stop if either mapping is unresolved. With `jq` already available, inspect the selected daemon in that service and project only needed fields:

```bash
set -o pipefail
ceph orch ps --service-name "$RGW_SERVICE" --daemon-id "$RGW_DAEMON_ID" --format json |
  jq -e 'if type == "array" then .[0:5] | map({daemon_type,daemon_id,hostname,status_desc,version,container_id,last_refresh}) else error("Unexpected daemon schema") end'
```

Compare successful and failing requests by operation, endpoint and daemon over the same interval. Separate response errors from timeouts where no service response was received. A generic connectivity probe cannot prove that authentication, authorization or a particular S3 feature works.

## Follow the strongest evidence

| Evidence | Check next |
|---|---|
| Signature or authentication failure | Clock, selected credential identity, endpoint/region, addressing and request transformation |
| Access denied | User suspension, requested action, bucket policy/ACL, object ownership and any identity-specific restrictions |
| Failure appeared after SDK update | Installed SDK options, signing/checksum behavior and backend feature support |
| Only one RGW is slow | Daemon resource pressure, local network and service logs |
| Multiple RGWs degrade with OSD warnings | Correlate the RADOS slow-operation investigation |
| Only listing or one large bucket is slow | Operation-specific latency and bucket/index evidence |

Ceph's S3 and authentication references describe compatibility and signing; they do not imply complete AWS feature parity. Vendor patch notes decide whether a specific fix or behavior applies to the installed RHCS build.

## Inspect account metadata without exposing credentials

Prefer the restricted Objectify adapter after its schema and authorization are validated. For direct inspection, `RGW_UID_QUALIFIED` must be the exact user identity from the verified mapping: `tenant$user` for an explicitly named RGW tenant, or a plain UID only when the empty legacy tenant is confirmed. Preserve the dollar sign as literal data in the variable; never infer a global user from a display name. Unknown tenant mapping is a stop condition. An authorized engineer with `jq` already installed may project only selected fields:

```bash
set -o pipefail
radosgw-admin user info --uid="$RGW_UID_QUALIFIED" |
  jq -e '{user_id,tenant,suspended,max_buckets,user_quota,bucket_quota}'
```

Run only inside the verified cluster/realm context. Stop on a command or projection error. The unfiltered administrative response may contain secrets; never send or store it. A user record does not by itself prove that a request's signing key belongs to that user. Projection limits returned content after retrieval; it does not reduce the backend query's work.

## Interpret monitoring honestly

The RGW metrics reference documents operation counters and latency structures. The owner's custom exporter may rename or transform them. Inspect metric type, units, labels and reset behavior before constructing a query. Do not describe a mean calculated from a sum/count as p95 latency. Preserve the Grafana datasource UID and the customer/cluster selector with every chart.

Finish with the affected operation, confirmed backend/build, supported hypothesis, evidence gaps and a proposed next read. This stage does not regenerate keys, edit policy, reshard buckets, enable verbose logging or issue test writes.

## Sources

- [Red Hat Ceph Storage 7 Object Gateway Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html/object_gateway_guide/index)
- [Red Hat Ceph Storage 8 Object Gateway Guide](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/object_gateway_guide/index)
- [Ceph Squid S3 API and feature support](https://docs.ceph.com/en/squid/radosgw/s3/)
- [Ceph Squid S3 authentication and ACLs](https://docs.ceph.com/en/squid/radosgw/s3/authentication/)
- [Ceph Squid RGW administration](https://docs.ceph.com/en/squid/radosgw/admin/)
- [Ceph Squid RGW metrics](https://docs.ceph.com/en/squid/radosgw/metrics/)
- [Ceph Squid daemon selection](https://docs.ceph.com/en/squid/cephadm/troubleshooting/)
- [Ceph Squid RGW tenant-qualified identities](https://docs.ceph.com/en/squid/radosgw/multitenancy/)

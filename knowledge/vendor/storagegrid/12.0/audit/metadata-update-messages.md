---
id: "storagegrid-120-35a0af058fcd39d5"
title: "StorageGRID 12.0 Audit messages for S3 object metadata updates in StorageGRID"
area: "storagegrid"
type: "import"
applies_to: ["12.0", "storagegrid-12.0"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg120-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-120"
repository_commit: "92a3f4cb2ac43fd5f151e410f99e7b9d4b019938"
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/metadata-update-messages.adoc"
source_sha256: "7abb595234a1776e479238ac7061947177e86582a3ca58a0a3a794caa5b658f9"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/metadata-update-messages.adoc"
---

# StorageGRID 12.0 Audit messages for S3 object metadata updates in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/metadata-update-messages.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Audit messages for S3 object metadata updates in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
Audit messages are generated when an S3 client updates an object's metadata.

## S3 metadata update audit messages

[cols="1a,1a,2a,1a,2a" options=header] 
|===
| Code
| Name
| Description
| Trace
| See

| SUPD
| S3 Metadata Updated
| Generated when an S3 client updates the metadata for an ingested object.
| CBID, S3KY, HTRH
| link:supd-s3-metadata-updated.html[SUPD: S3 Metadata Updated]

|===

## Example: S3 metadata update

The example shows a successful transaction to update the metadata for an existing S3 object.

### SUPD: S3 Metadata Update

The S3 client makes a request (SUPD) to update the specified metadata (`x-amz-meta-\*`) for the S3 object (S3KY). In this example, request headers are included in the field HTRH because it has been configured as an audit protocol header (*Configuration* > *Monitoring* > *Audit and syslog server*). See link:../monitor/configure-log-management.html[Configure log management and external syslog server].

----
2017-07-11T21:54:03.157462 [AUDT:[RSLT(FC32):SUCS][TIME(UI64):17631][SAIP(IPAD):"10.96.100.254"]
[HTRH(CSTR):"{\"accept-encoding\":\"identity\",\"authorization\":\"AWS LIUF17FGJARQHPY2E761:jul/hnZs/uNY+aVvV0lTSYhEGts=\",
\"content-length\":\"0\",\"date\":\"Tue, 11 Jul 2017 21:54:03 GMT\",\"host\":\"10.96.99.163:18082\",
\"user-agent\":\"aws-cli/1.9.20 Python/2.7.6 Linux/3.13.0-119-generic botocore/1.3.20\",
\"x-amz-copy-source\":\"/testbkt1/testobj1\",\"x-amz-metadata-directive\":\"REPLACE\",\"x-amz-meta-city\":\"Vancouver\"}"]
[S3AI(CSTR):"20956855414285633225"][SACC(CSTR):"acct1"][S3AK(CSTR):"SGKHyyv9ZQqWRbJSQc5vI7mgioJwrdplShE02AUaww=="]
[SUSR(CSTR):"urn:sgws:identity::20956855414285633225:root"]
[SBAI(CSTR):"20956855414285633225"][SBAC(CSTR):"acct1"][S3BK(CSTR):"testbkt1"]
[S3KY(CSTR):"testobj1"][CBID(UI64):0xCB1D5C213434DD48][CSIZ(UI64):10][AVER(UI32):10]
[ATIM(UI64):1499810043157462][ATYP(FC32):SUPD][ANID(UI32):12258396][AMID(FC32):S3RQ]
[ATID(UI64):8987436599021955788]]
----

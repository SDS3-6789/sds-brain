---
id: "storagegrid-119-1657a313bfad3989"
title: "StorageGRID 11.9 S3SL: S3 Select request"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/s3-select-request.adoc"
source_sha256: "176f1d15528463f536ea324a27d1ad092c981123bae87a1b583d2f31e5c37b2b"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/s3-select-request.adoc"
---

# StorageGRID 11.9 S3SL: S3 Select request

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/audit/s3-select-request.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# S3SL: S3 Select request
:icons: font
:imagesdir: ../media/

[.lead]
This message logs a completion after an S3 Select request has been returned to the client. The S3SL message can include error message and error code details. The request might not have been successful.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
BYSC
a|
Bytes Scanned
a|
Number of bytes scanned (received) from Storage Nodes.

BYSC and BYPR are likely to be different if the object is compressed. If the object is compressed BYSC would have the compressed byte count and BYPR would be the bytes after decompression.
a|
BYPR
a|
Bytes Processed
a|
Number of bytes processed. Indicates how many bytes of "Bytes Scanned" were actually processed or acted upon by an S3 Select job.
a|
BYRT
a|
Bytes Returned
a|
Number of bytes that an S3 Select job returned to the client.
a|
REPR
a|
Records Processed
a|
Number of records or rows that an S3 Select job received from Storage Nodes.
a|
RERT
a|
Records Returned
a|
Number of records or rows an S3 Select job returned to the client.

a|
JOFI
a|
Job Finished
a|
Indicates if the S3 Select job finished processing or not. If this is false, then the job failed to finish and the error fields will likely have data in them. The client might have received partial results, or no results at all.

a|
REID
a|
Request ID	
a|
Identifier for the S3 Select request.

a|
EXTM
a|
Execution Time
a|
The time, in seconds, it took for the S3 Select Job to complete.

a|
ERMG
a|
Error Message	
a|
Error message that the S3 Select job generated.

a|
ERTY
a|
Error Type	
a|
Error type that the S3 Select job generated.

a|
ERST
a|
Error Stacktrace	
a|
Error Stacktrace that the S3 Select job generated.	

a|
S3BK
a|
S3 bucket	
a|
The S3 bucket name.	

a|
S3AK
a|
S3 Access Key ID (request sender)	
a|
The S3 access key ID for the user that sent the request.

a|
S3AI
a|
S3 tenant account ID (request sender)	
a|
The tenant account ID of the user who sent the request. 

a|
S3KY
a|
S3 Key
a|
The S3 key name, not including the bucket name.

|===

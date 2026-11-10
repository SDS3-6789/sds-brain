---
id: "storagegrid-120-9537a734085557a2"
title: "StorageGRID 12.0 Supported Amazon S3 Select operations in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/s3/use-s3-select.adoc"
source_sha256: "eb73e3f91a11a437cac95e2500dc91676e24957141efcbddc80fc8a13071ff00"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/use-s3-select.adoc"
---

# StorageGRID 12.0 Supported Amazon S3 Select operations in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/s3/use-s3-select.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Supported Amazon S3 Select operations in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
StorageGRID supports the following Amazon S3 Select clauses, data types, and operators for the link:select-object-content.html[SelectObjectContent command].

NOTE: Any items not listed aren't supported.

For syntax, see link:select-object-content.html[SelectObjectContent]. For more information about S3 Select, see the https://docs.aws.amazon.com/AmazonS3/latest/userguide/selecting-content-from-objects.html[AWS documentation for S3 Select^].

Only tenant accounts that have S3 Select enabled can issue SelectObjectContent queries. See the link:../admin/manage-s3-select-for-tenant-accounts.html[considerations and requirements for using S3 Select].

## Clauses

* SELECT list
* FROM clause
* WHERE clause
* LIMIT clause

## Data types

* bool
* integer
* string
* float
* decimal, numeric
* timestamp

## Operators

### Logical operators

* AND
* NOT
* OR

### Comparison operators

* <
* >
* &lt;=
* &gt;=
* =
* =
* <>
* !=
* BETWEEN
* IN

### Pattern matching operators

* LIKE
* _
* %

### Unitary operators

* IS NULL
* IS NOT NULL

### Math operators

* +
* -
* *
* /
* %

StorageGRID follows the Amazon S3 Select operator precedence.

## Aggregate functions

* AVG()
* COUNT(*)
* MAX()
* MIN()
* SUM()

## Conditional functions

* CASE
* COALESCE
* NULLIF

## Conversion functions

* CAST (for supported datatype)

## Date functions

* DATE_ADD
* DATE_DIFF
* EXTRACT
* TO_STRING
* TO_TIMESTAMP
* UTCNOW

## String functions

* CHAR_LENGTH, CHARACTER_LENGTH
* LOWER
* SUBSTRING
* TRIM
* UPPER

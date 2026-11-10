---
id: "storagegrid-120-6801b68573458e5b"
title: "StorageGRID 12.0 ETAF audit message for security authentication failures in StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/etaf-security-authentication-failed.adoc"
source_sha256: "9efccafacef97bb03ba0c788f88f6bdfb8b8c937ff1685a93c42d2e2447f4aad"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "audit/etaf-security-authentication-failed.adoc"
---

# StorageGRID 12.0 ETAF audit message for security authentication failures in StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/audit/etaf-security-authentication-failed.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# ETAF audit message for security authentication failures in StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
This message is generated when a connection attempt using Transport Layer Security (TLS) has failed.

[cols="1a,1a,4a" options="header"]
|===
| Code| Field| Description
a|
CNID
a|
Connection Identifier
a|
The unique system identifier for the TCP/IP connection over which the authentication failed.
a|
RUID
a|
User Identity
a|
A service dependent identifier representing the identity of the remote user.
a|
RSLT
a|
Reason Code
a|
The reason for the failure:

SCNI: Secure connection establishment failed.

CERM: Certificate was missing.

CERT: Certificate was invalid.

CERE: Certificate was expired.

CERR: Certificate was revoked.

CSGN: Certificate signature was invalid.

CSGU: Certificate signer was unknown.

UCRM: User credentials were missing.

UCRI: User credentials were invalid.

UCRU: User credentials were disallowed.

TOUT: Authentication timed out.

|===
When a connection is established to a secure service that uses TLS, the credentials of the remote entity are verified using the TLS profile and additional logic built into the service. If this authentication fails due to invalid, unexpected, or disallowed certificates or credentials, an audit message is logged. This enables queries for unauthorized access attempts and other security-related connection problems.

The message could result from a remote entity having an incorrect configuration, or from attempts to present invalid or disallowed credentials to the system. This audit message should be monitored to detect attempts to gain unauthorized access to the system.

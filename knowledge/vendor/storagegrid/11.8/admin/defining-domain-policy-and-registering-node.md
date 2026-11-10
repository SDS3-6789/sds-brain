---
id: "storagegrid-118-c5a5107d4ae9f75f"
title: "StorageGRID 11.8 Define a domain policy and register a node"
area: "storagegrid"
type: "import"
applies_to: ["11.8", "storagegrid-11.8"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg118-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-118"
repository_commit: "9066339be246ef04b60100d49a31f887c58e7ae0"
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/defining-domain-policy-and-registering-node.adoc"
source_sha256: "a5772bb6b3cf2da86fba623439a5120b91488f3f1cfa10526b5f445c7f6649e1"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/defining-domain-policy-and-registering-node.adoc"
---

# StorageGRID 11.8 Define a domain policy and register a node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/defining-domain-policy-and-registering-node.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Define a domain policy and register a node
:icons: font
:imagesdir: ../media/

[.lead]
You need to define a domain policy that uses the TSM management class for the data saved from the Archive Node, and then register a node to use this domain policy.

NOTE: Archive Node processes can leak memory if the client password for the Archive Node in Tivoli Storage Manager (TSM) expires. Ensure that the TSM server is configured so the client username/password for the Archive Node never expires.

When registering a node on the TSM server for the use of the Archive Node (or updating an existing node), you must specify the number of mount points that the node can use for write operations by specifying the MAXNUMMP parameter to the REGISTER NODE command. The number of mount points is typically equivalent to the number of tape drive heads allocated to the Archive Node. The number specified for MAXNUMMP on the TSM server must be at least as large as the value set for the *ARC* > *Target* > *Configuration* > *Main* > *Maximum Store Sessions* for the Archive Node, which is set to a value of 0 or 1, as concurrent store sessions aren't supported by the Archive Node.

The value of MAXSESSIONS set for the TSM server controls the maximum number of sessions that can be opened to the TSM server by all client applications. The value of MAXSESSIONS specified on the TSM must be at least as large as the value specified for *ARC* > *Target* > *Configuration* > *Main* > *Number of Sessions* in the Grid Manager for the Archive Node. The Archive Node concurrently creates at most one session per mount point plus a small number (< 5) of additional sessions.

The TSM node assigned to the Archive Node uses a custom domain policy `tsm-domain`. The `tsm-domain` domain policy is a modified version of the "standard" domain policy, configured to write to tape and with the archive destination set to be the StorageGRID system's storage pool (`_SGWSDiskPool_`).

NOTE: You must log in to the TSM server with administrative privileges and use the dsmadmc tool to create and activate the domain policy.

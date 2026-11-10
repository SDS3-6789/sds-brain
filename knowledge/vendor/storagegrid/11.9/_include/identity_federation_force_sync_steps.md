---
id: "storagegrid-119-bba16f9947b2dfa8"
title: "StorageGRID 11.9 identity_federation_force_sync_steps"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/identity_federation_force_sync_steps.adoc"
source_sha256: "a0419f53f710d3b9856ace827a2cf653b7c2ec22a4559c8ac5848da3cbb50d22"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/identity_federation_force_sync_steps.adoc"
---

# StorageGRID 11.9 identity_federation_force_sync_steps

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/identity_federation_force_sync_steps.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

//These are the shared steps for identity federation force sync in the tenant manager and the grid manager//

The StorageGRID system periodically synchronizes federated groups and users from the identity source. You can force synchronization to start if you want to enable or restrict user permissions as quickly as possible.

.Steps

. Go to the Identity federation page.
. Select *Sync server* at the top of the page.
+
The synchronization process might take some time depending on your environment.
+
NOTE: The *Identity federation synchronization failure* alert is triggered if there is an issue synchronizing federated groups and users from the identity source.

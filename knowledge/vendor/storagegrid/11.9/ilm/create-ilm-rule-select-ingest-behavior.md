---
id: "storagegrid-119-827addd611f09b30"
title: "StorageGRID 11.9 Step 3 of 3: Select ingest behavior"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/ilm/create-ilm-rule-select-ingest-behavior.adoc"
source_sha256: "a74f051db67b46ad486d7931803f105d9d6f9f090bcb0b482030d99e78995998"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "ilm/create-ilm-rule-select-ingest-behavior.adoc"
---

# StorageGRID 11.9 Step 3 of 3: Select ingest behavior

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/ilm/create-ilm-rule-select-ingest-behavior.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Step 3 of 3: Select ingest behavior
:icons: font
:imagesdir: ../media/

[.lead]
The *Select ingest behavior* step of the Create ILM Rule wizard allows you to choose how the objects filtered by this rule are protected as they are ingested.

.About this task

StorageGRID can make interim copies and queue the objects for ILM evaluation later, or it can make copies to meet the rule's placement instructions immediately.

.Steps

. Select the link:data-protection-options-for-ingest.html[ingest behavior] to use.
+
For more information, see link:advantages-disadvantages-of-ingest-options.html[Advantages, disadvantages, and limitations of the ingest options].
+
[NOTE]
#### You can't use the Balanced or Strict option if the rule uses one of these placements:

** A Cloud Storage Pool at day 0
** A Cloud Storage Pool when the rule uses a User defined creation time as a Reference time

See link:example-5-ilm-rules-and-policy-for-strict-ingest-behavior.html[Example 5: ILM rules and policy for Strict ingest behavior].
#### . Select *Create*.
+
The ILM rule is created. The rule does not become active until it is added to an link:creating-ilm-policy.html[ILM policy] and that policy is activated.
+
To view the details of the rule, select the rule's name on the ILM rules page.

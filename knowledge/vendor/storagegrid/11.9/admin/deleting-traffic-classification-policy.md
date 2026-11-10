---
id: "storagegrid-119-61936d387aace3a5"
title: "StorageGRID 11.9 Delete a traffic classification policy"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/deleting-traffic-classification-policy.adoc"
source_sha256: "0e33142d08aa3df2d6829ae9d4ef048bd40043e333b0faf43478a14774ed9023"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/deleting-traffic-classification-policy.adoc"
---

# StorageGRID 11.9 Delete a traffic classification policy

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/deleting-traffic-classification-policy.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Delete a traffic classification policy
:icons: font
:imagesdir: ../media/

[.lead]
You can delete a traffic classification policy if you no longer need it. Make sure you delete the right policy because a policy can't be retrieved when deleted.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:admin-group-permissions.html[Root access permission].

.Steps

. Select *CONFIGURATION* > *Network* > *Traffic classification*.
+
The Traffic classification policies page appears with the existing policies listed in a table.

. Delete the policy using the Actions menu or the details page. 
+
[role="tabbed-block"]
#### .Actions menu
--

.. Select the checkbox for the policy.
.. Select *Actions* > *Remove*.

--
.Policy details page
--

.. Select the policy name.
.. Select the *Remove* button beside the policy name.

--
#### . Select *Yes* to confirm that you want to delete the policy.
+
The policy is deleted.

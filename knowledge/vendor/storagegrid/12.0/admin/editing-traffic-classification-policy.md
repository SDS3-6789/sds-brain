---
id: "storagegrid-120-cbaeb23f573171fa"
title: "StorageGRID 12.0 Edit a StorageGRID traffic classification policy"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/editing-traffic-classification-policy.adoc"
source_sha256: "ac87ffd695eab97aa16351f0e8bca4860155a413f858fc18fffcb5e6e49e927c"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/editing-traffic-classification-policy.adoc"
---

# StorageGRID 12.0 Edit a StorageGRID traffic classification policy

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/editing-traffic-classification-policy.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Edit a StorageGRID traffic classification policy
:icons: font
:imagesdir: ../media/

[.lead]
You can edit a traffic classification policy to change its name or description, or to create, edit, or delete any rules or limits for the policy.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:admin-group-permissions.html[Root access permission].

.Steps

. Select *Configuration* > *Network* > *Traffic classification*.
+
The Traffic classification policies page appears and the existing policies are listed in a table.

. Edit the policy using the Actions menu or the details page. See link:../admin/creating-traffic-classification-policies.html[create traffic classification policies] for what to enter.
+
[role="tabbed-block"]
#### .Actions menu
--

.. Select the checkbox for the policy.
.. Select *Actions* > *Edit*.

--
.Details page
--

.. Select the policy name.
.. Select the *Edit* button beside the policy name.
--
#### . For the Enter policy name step, optionally edit the policy name or description, and select *Continue*.

. For the Add matching rules step, optionally add a rule or edit the *Type* and *Match value* of the existing rule, and select *Continue*. 

. For the Set limits step, optionally add, edit, or delete a limit, and select *Continue*.

. Review the updated policy, and select *Save and continue*.
+
The changes you made to the policy are saved, and network traffic is now handled according to the traffic classification policies. You can view traffic charts and verify that the polices are enforcing the traffic limits you expect.

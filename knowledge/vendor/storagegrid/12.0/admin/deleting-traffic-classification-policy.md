---
id: "storagegrid-120-61936d387aace3a5"
title: "StorageGRID 12.0 Delete a StorageGRID traffic classification policy"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/deleting-traffic-classification-policy.adoc"
source_sha256: "0dd5302cef30e9409853af24b90e6c64bf600ccd00a7ab9ffc0f7fa2d94bbefb"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/deleting-traffic-classification-policy.adoc"
---

# StorageGRID 12.0 Delete a StorageGRID traffic classification policy

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/deleting-traffic-classification-policy.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Delete a StorageGRID traffic classification policy
:icons: font
:imagesdir: ../media/

[.lead]
You can delete a traffic classification policy if you no longer need it. Make sure you delete the right policy because a policy can't be retrieved when deleted.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:admin-group-permissions.html[Root access permission].

.Steps

. Select *Configuration* > *Network* > *Traffic classification*.
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

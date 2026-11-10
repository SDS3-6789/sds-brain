---
id: "storagegrid-118-c9ee912cfa26f459"
title: "StorageGRID 11.8 Monitor object verification operations"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/monitor/monitoring-object-verification-operations.adoc"
source_sha256: "3e6dee003b79fbbf6d4d8f5992ade1be6b9f2c6aff1875d7e39d926b265ba965"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/monitoring-object-verification-operations.adoc"
---

# StorageGRID 11.8 Monitor object verification operations

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/monitor/monitoring-object-verification-operations.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Monitor object verification operations
:icons: font
:imagesdir: ../media/

[.lead]
The StorageGRID system can verify the integrity of object data on Storage Nodes, checking for both corrupt and missing objects.

.Before you begin
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:../admin/admin-group-permissions.html[Maintenance or Root access permission].

.About this task
Two link:../troubleshoot/verifying-object-integrity.html[verification processes] work together to ensure data integrity:

* *Background verification* runs automatically, continuously checking the correctness of object data.
+
Background verification automatically and continuously checks all Storage Nodes to determine if there are corrupt copies of replicated and erasure-coded object data. If problems are found, the StorageGRID system automatically attempts to replace the corrupt object data from copies stored elsewhere in the system. Background verification does not run on Archive Nodes or on objects in a Cloud Storage Pool.
+
NOTE: The *Unidentified corrupt object detected* alert is triggered if the system detects a corrupt object that can't be corrected automatically.

* *Object existence check* can be triggered by a user to more quickly verify the existence (although not the correctness) of object data.
+

Object existence check verifies whether all expected replicated copies of objects and erasure-coded fragments exist on a Storage Node. Object existence check provides a way to verify the integrity of storage devices, especially if a recent hardware issue could have affected data integrity.

You should review the results from background verifications and object existence checks regularly. Investigate any instances of corrupt or missing object data immediately to determine the root cause.

.Steps
. Review the results from background verifications:
.. Select *NODES* > *_Storage Node_* > *Objects*.
.. Check the verification results:
 ** To check replicated object data verification, look at the attributes in the Verification section.
+
image::../media/nodes_storage_node_object_verification.png[Nodes > Storage Node > Object > Verification]

 ** To check erasure-coded fragment verification, select *_Storage Node_* > *ILM* and look at the attributes in the Erasure coding verification section.
+
image::../media/nodes_storage_node_ilm_ec_verification.png[Nodes > Storage Node > ILM > EC Verification]
+
Select the question mark image:../media/icon_nms_question.png[question mark] next to an attribute's name to display help text.

. Review the results from object existence check jobs:
.. Select *MAINTENANCE* > *Object existence check* > *Job history*.
.. Scan the Missing object copies detected column. If any jobs resulted in 100 or more missing object copies and the *Objects lost* alert has been triggered, contact technical support.
+
image::../media/oec_job_history.png[Object existence check job history]

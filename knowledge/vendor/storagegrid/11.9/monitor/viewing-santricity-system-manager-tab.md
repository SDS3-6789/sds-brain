---
id: "storagegrid-119-995081e27b3e2a24"
title: "StorageGRID 11.9 View the SANtricity System Manager tab (E-Series only)"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/viewing-santricity-system-manager-tab.adoc"
source_sha256: "ff6aa48eb8a6c3468a1bd0c4d1b774dff26c1a73177578b6ea5f5184f532be06"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "monitor/viewing-santricity-system-manager-tab.adoc"
---

# StorageGRID 11.9 View the SANtricity System Manager tab (E-Series only)

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/monitor/viewing-santricity-system-manager-tab.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View the SANtricity System Manager tab (E-Series only)
:icons: font
:imagesdir: ../media/

[.lead]
The SANtricity System Manager tab enables you to access SANtricity System Manager without having to configure or connect the management port of the storage appliance. You can use this tab to review hardware diagnostic and environmental information as well as issues related to the drives.

CAUTION: Accessing SANtricity System Manager from the Grid Manager is generally meant only to monitor appliance hardware and configure E-Series AutoSupport. Many features and operations within SANtricity System Manager such as upgrading firmware don't apply to monitoring your StorageGRID appliance. To avoid issues, always follow the hardware maintenance instructions for your appliance. To upgrade SANtricity firmware, see the https://docs.netapp.com/us-en/storagegrid-appliances/landing-maintain-hdwr/index.html[Maintenance configuration procedures^] for your storage appliance. 

NOTE: The SANtricity System Manager tab is shown only for storage appliance nodes using E-Series hardware.

Using SANtricity System Manager, you can do the following:

* View performance data such as storage array level performance, I/O latency, storage controller CPU utilization, and throughput.
* Check hardware component status.
* Perform support functions including viewing diagnostic data, and configuring E-Series AutoSupport.
+
NOTE: To use SANtricity System Manager to configure a proxy for E-Series AutoSupport, see link:../admin/sending-eseries-autosupport-messages-through-storagegrid.html[Send E-Series AutoSupport packages through StorageGRID].

To access SANtricity System Manager through Grid Manager, you must have the link:../admin/admin-group-permissions.html[Storage appliance administrator or Root access permission].

NOTE: You must have SANtricity firmware 8.70 or higher to access SANtricity System Manager using the Grid Manager.

The tab displays the home page of SANtricity System Manager.

image::../media/nodes_page_santricity_tab.png[Nodes page SANtricity tab]

NOTE: You can use the SANtricity System Manager link to open the SANtricity System Manager in a new browser window for easier viewing.

To see details for storage array level performance and capacity usage, position your cursor over each graph.

For more details on viewing the information accessible from the SANtricity System Manager tab, see https://docs.netapp.com/us-en/e-series-family/index.html[NetApp E-Series and SANtricity documentation^].

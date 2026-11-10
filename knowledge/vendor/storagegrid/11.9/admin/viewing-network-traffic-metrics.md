---
id: "storagegrid-119-cab5fbbefe3e92e7"
title: "StorageGRID 11.9 View network traffic metrics"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/viewing-network-traffic-metrics.adoc"
source_sha256: "30c291cec546b16a243993b14375f5e0114607cd7c4638b1baaab084a6a50feb"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/viewing-network-traffic-metrics.adoc"
---

# StorageGRID 11.9 View network traffic metrics

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/viewing-network-traffic-metrics.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# View network traffic metrics
:icons: font
:imagesdir: ../media/

[.lead]
You can monitor network traffic by viewing the graphs that are available from the Traffic classification policies page.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:admin-group-permissions.html[Root access or Tenant accounts permission].

.About this task

For any existing traffic classification policy, you can view metrics for the load balancer service to determine if the policy is successfully limiting traffic across the network. The data in the graphs can help you determine if you need to adjust the policy.

Even if no limits are set for a traffic classification policy, metrics are collected and the graphs provide useful information for understanding traffic trends.

.Steps

. Select *CONFIGURATION* > *Network* > *Traffic classification*.
+

The Traffic classification policies page appears, and the existing policies are listed in the table.
+

. Select the traffic classification policy name for which you want to view metrics.
. Select the *Metrics* tab.
+
The traffic classification policy graphs appear. The graphs display metrics only for the traffic that matches the selected policy.
+

+
The following graphs are included on the page.

** Request rate: This graph provides the amount of bandwidth matching this policy handled by all load balancers. Received data includes request headers for all requests and body data size for responses that have body data. Sent includes response headers for all requests and response body data size for requests that include body data in the response.
+

NOTE: When requests are complete, this chart only shows bandwidth usage. For slow or large object requests the actual instantaneous bandwidth might differ from the values reported in this graph.
+

** Error response rate: This graph provides an approximate rate at which requests matching this policy are returning errors (HTTP status code >= 400) to clients.

** Average request duration (non-error): This graph provides an average duration of successful requests matching this policy.
+

** Policy bandwidth usage: This graph provides the amount of bandwidth matching this policy handled by all load balancers. Received data includes request headers for all requests and body data size for responses that have body data. Sent includes response headers for all requests and response body data size for requests that include body data in the response.

. Position the cursor over a line graph to see a pop-up of values on a specific part of the graph.

. Select *Grafana dashboard* right below the Metrics title to view all the graphs for a policy. In addition to the four graphs from the *Metrics* tab, you can view two more graphs: 
+

* Write request rate by object size: The rate for PUT/POST/DELETE requests matching this policy. Positioning on an individual cell shows per second rates. Rates shown in the hover view are truncated to integer counts and might report 0 when there are non-zero requests in the bucket.
* Read request rate by object size: The rate for GET/HEAD requests matching this policy. Positioning on an individual cell shows per second rates. Rates shown in the hover view are truncated to integer counts and might report 0 when there are non-zero requests in the bucket. 

. Alternatively, access the graphs from the *SUPPORT* menu.
 .. Select *SUPPORT* > *Tools* > *Metrics*.
 .. Select *Traffic Classification Policy* from the *Grafana* section.
 .. Select the policy from the menu on the upper left of the page.
 .. Position the cursor over a graph to see a pop-up that shows the date and time of the sample, object sizes that are aggregated into the count, and the number of requests per second during that time period.
+

Traffic classification policies are identified by their ID. Policy IDs are listed on the Traffic classification policies page.
. Analyze the graphs to determine how often the policy is limiting traffic and whether you need to adjust the policy.

---
id: "storagegrid-119-e46d9430ac5dacf5"
title: "StorageGRID 11.9 Configure storage proxy"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/configuring-storage-proxy-settings.adoc"
source_sha256: "17e0ea55d96829ebe09d050c687cc200b45ebbd234603fc7acb61788f9f9e536"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/configuring-storage-proxy-settings.adoc"
---

# StorageGRID 11.9 Configure storage proxy

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/configuring-storage-proxy-settings.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Configure storage proxy
:icons: font
:imagesdir: ../media/

[.lead]
If you are using platform services or Cloud Storage Pools, you can configure a non-transparent proxy between Storage Nodes and the external S3 endpoints. For example, you might need a non-transparent proxy to allow platform services messages to be sent to external endpoints, such as an endpoint on the internet. 

NOTE: Configured storage proxy settings do not apply to Kafka platform services endpoints.

.Before you begin

* You have link:admin-group-permissions.html[specific access permissions].
* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].

.About this task

You can configure the settings for a single storage proxy.

.Steps

. Select *CONFIGURATION* > *Security* > *Proxy settings*.


. On the *Storage* tab, select the *Enable storage proxy* checkbox.

. Select the protocol for the storage proxy.
. Enter the hostname or IP address of the proxy server.
. Optionally, enter the port used to connect to the proxy server.
+
Leave this field blank to use the default port for the protocol: 80 for HTTP or 1080 for SOCKS5.

. Select *Save*.
+
After the storage proxy is saved, new endpoints for platform services or Cloud Storage Pools can be configured and tested.
+
NOTE: Proxy changes can take up to 10 minutes to take effect.

. Check the settings of your proxy server to ensure that platform service-related messages from StorageGRID will not be blocked.

. If you need to disable a storage proxy, clear the checkbox, and select *Save*.

// 2023 SEP 15, SGWS-25330

---
id: "storagegrid-118-8c8fbeffbc7f7afc"
title: "StorageGRID 11.8 Overview of the installation REST API"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/overview-of-installation-rest-api.adoc"
source_sha256: "a43bf6b08a72b50bed301a257a64985bd08d452ecec045e8f25f09c3948a7a2a"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "vmware/overview-of-installation-rest-api.adoc"
---

# StorageGRID 11.8 Overview of the installation REST API

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/vmware/overview-of-installation-rest-api.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Overview of the installation REST API
:icons: font
:imagesdir: ../media/

[.lead]
StorageGRID provides the StorageGRID Installation API for performing installation tasks.

The API uses the Swagger open source API platform to provide the API documentation. Swagger allows both developers and non-developers to interact with the API in a user interface that illustrates how the API responds to parameters and options. This documentation assumes that you are familiar with standard web technologies and the JSON data format.

CAUTION: Any API operations you perform using the API Docs webpage are live operations. Be careful not to create, update, or delete configuration data or other data by mistake.

Each REST API command includes the API's URL, an HTTP action, any required or optional URL parameters, and an expected API response.

## StorageGRID Installation API

The StorageGRID Installation API is only available when you are initially configuring your StorageGRID system, and if you need to perform a primary Admin Node recovery. The Installation API can be accessed over HTTPS from the Grid Manager.

To access the API documentation, go to the installation web page on the primary Admin Node and select *Help* > *API documentation* from the menu bar.

The StorageGRID Installation API includes the following sections:

* *config* -- Operations related to the product release and versions of the API. You can list the product release version and the major versions of the API supported by that release.
* *grid* -- Grid-level configuration operations. You can get and update grid settings, including grid details, Grid Network subnets, grid passwords, and NTP and DNS server IP addresses.
* *nodes* -- Node-level configuration operations. You can retrieve a list of grid nodes, delete a grid node, configure a grid node, view a grid node, and reset a grid node's configuration.
* *provision* -- Provisioning operations. You can start the provisioning operation and view the status of the provisioning operation.
* *recovery* -- Primary Admin Node recovery operations. You can reset information, upload the Recover Package, start the recovery, and view the status of the recovery operation.
* *recovery-package* -- Operations to download the Recovery Package.
* *schemas* -- API schemas for advanced deployments
* *sites* -- Site-level configuration operations. You can create, view, delete, and modify a site.

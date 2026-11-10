---
id: "storagegrid-119-ab84b52e3f8e6873"
title: "StorageGRID 11.9 Configure DNS servers"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/configuring-dns-servers.adoc"
source_sha256: "238c0b5dfd69138211bf4ca5f5210abad18db4befad8df747ab774c7ce535fa9"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/configuring-dns-servers.adoc"
---

# StorageGRID 11.9 Configure DNS servers

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/maintain/configuring-dns-servers.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Configure DNS servers
:icons: font
:imagesdir: ../media/

[.lead]
You can add, update, and remove DNS servers, so that you can use fully qualified domain name (FQDN) hostnames rather than IP addresses.

To use fully qualified domain names (FQDNs) instead of IP addresses when specifying hostnames for external destinations, specify the IP address of each DNS server you will use. These entries are used for AutoSupport, alert emails, SNMP notifications, platform services endpoints, Cloud Storage Pools, and more.

.Before you begin

* You are signed in to the Grid Manager using a link:../admin/web-browser-requirements.html[supported web browser].
* You have the link:../admin/admin-group-permissions.html[Maintenance or Root access permission].
* You have the IP addresses of the DNS servers to configure.

.About this task

include::../_include/dns-server-restrictions.adoc[]

## Add a DNS server
Follow these steps to add a DNS server.

.Steps
. Select *MAINTENANCE* > *Network* > *DNS servers*.
. Select *Add another server* to add a DNS server.
. Select *Save*.

## Modify a DNS server
Follow these steps to modify a DNS server.

.Steps
. Select *MAINTENANCE* > *Network* > *DNS servers*.
. Select the IP address of the server name you want to edit and make the necessary changes.
. Select *Save*.

## Delete a DNS server
Follow these steps to delete an IP address of a DNS server.

.Steps
. Select *MAINTENANCE* > *Network* > *DNS servers*.
. Select the delete icon image:../media/icon-x-to-remove.png[delete icon] next to the IP address.
. Select *Save*.

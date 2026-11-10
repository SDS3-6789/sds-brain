---
id: "storagegrid-119-2c04fd6b8aa88c4d"
title: "StorageGRID 11.9 Specify DNS server information"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/vmware/specifying-domain-name-system-server-information.adoc"
source_sha256: "fffd7cba7bc42f3befd1f574b6fe97f99735a53571b11dfe0cf9247c4d14ca8e"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "vmware/specifying-domain-name-system-server-information.adoc"
---

# StorageGRID 11.9 Specify DNS server information

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/vmware/specifying-domain-name-system-server-information.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Specify DNS server information
:icons: font
:imagesdir: ../media/

[.lead]
You must specify DNS information for your StorageGRID system, so that you can access external servers using hostnames instead of IP addresses.

.About this task

Specifying https://docs.netapp.com/us-en/storagegrid-appliances/commonhardware/checking-dns-server-configuration.html[DNS server information^] allows you to use Fully Qualified Domain Name (FQDN) hostnames rather than IP addresses for email notifications and AutoSupport.

include::../_include/dns-server-restrictions.adoc[]

.Steps

. Specify the IPv4 address for at least one DNS server in the *Server 1* text box.
. If necessary, select the plus sign next to the last entry to add additional server entries.
+
image::../media/9_gmi_installer_dns_page.gif[This image is explained by the surrounding text.]
+
The best practice is to specify at least two DNS servers. You can specify up to six DNS servers.

. Select *Next*.

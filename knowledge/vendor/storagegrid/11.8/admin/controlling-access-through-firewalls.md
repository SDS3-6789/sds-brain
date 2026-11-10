---
id: "storagegrid-118-3086211c21c471f9"
title: "StorageGRID 11.8 Control access at external firewall"
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
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/controlling-access-through-firewalls.adoc"
source_sha256: "85004b0e9f2a32da05238fc43c7144c50a9782faf1af6711678aa44231b730fa"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/controlling-access-through-firewalls.adoc"
---

# StorageGRID 11.8 Control access at external firewall

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/controlling-access-through-firewalls.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Control access at external firewall
:icons: font
:imagesdir: ../media/

[.lead]
You can open or close specific ports at the external firewall.

You can control access to the user interfaces and APIs on StorageGRID Admin Nodes by opening or closing specific ports at the external firewall. For example, you might want to prevent tenants from being able to connect to the Grid Manager at the firewall, in addition to using other methods to control system access. 

If you want to configure the StorageGRID internal firewall, see link:../admin/configure-firewall-controls.html[Configure internal firewall].

[cols="1a,1a,2a" options="header"]
|===
| Port| Description| If port is open...
a|
443
a|
Default HTTPS port for Admin Nodes
a|
Web browsers and management API clients can access the Grid Manager, the Grid Management API, the Tenant Manager, and the Tenant Management API.

*Note:* Port 443 is also used for some internal traffic.

a|
8443
a|
Restricted Grid Manager port on Admin Nodes
a|

* Web browsers and management API clients can access the Grid Manager and the Grid Management API using HTTPS.
* Web browsers and management API clients can't access the Tenant Manager or the Tenant Management API.
* Requests for internal content will be rejected.

a|
9443
a|
Restricted Tenant Manager port on Admin Nodes
a|

* Web browsers and management API clients can access the Tenant Manager and the Tenant Management API using HTTPS.
* Web browsers and management API clients can't access the Grid Manager or the Grid Management API.
* Requests for internal content will be rejected.

|===

TIP: Single sign-on (SSO) is not available on the restricted Grid Manager or Tenant Manager ports. You must use the default HTTPS port (443) if you want users to authenticate with single sign-on.

.Related information

* link:signing-in-to-grid-manager.html[Sign in to the Grid Manager]

* link:creating-tenant-account.html[Create tenant account]

* link:../network/external-communications.html[External communications]

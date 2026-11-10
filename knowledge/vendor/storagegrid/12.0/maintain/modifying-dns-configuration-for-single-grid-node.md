---
id: "storagegrid-120-b9e794d55db45323"
title: "StorageGRID 12.0 Modify DNS configuration for single StorageGRID node"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/modifying-dns-configuration-for-single-grid-node.adoc"
source_sha256: "da71690a9b61e08581b89856de21547c1a66d5b112683d064d2e7d93d9df49f6"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "maintain/modifying-dns-configuration-for-single-grid-node.adoc"
---

# StorageGRID 12.0 Modify DNS configuration for single StorageGRID node

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/maintain/modifying-dns-configuration-for-single-grid-node.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Modify DNS configuration for single StorageGRID node
:icons: font
:imagesdir: ../media/

[.lead]
Rather than configure the DNS globally for the entire deployment, you can run a script to configure DNS differently for each grid node.

In general, you should use the *Maintenance* > *Network* > *DNS servers* option on the Grid Manager to configure DNS servers. Only use the following script if you need to use different DNS servers for different grid nodes.

.Steps
. External SSH access is blocked by default. If required, link:../admin/manage-external-ssh-access.html[temporarily allow access].
. Log in to the primary Admin Node:
 .. Enter the following command: `ssh admin@_primary_Admin_Node_IP_`
 .. Enter the password listed in the `Passwords.txt` file.
 .. Enter the following command to switch to root: `su -`
 .. Enter the password listed in the `Passwords.txt` file.
+
When you are logged in as root, the prompt changes from `$` to `#`.

 .. Add the SSH private key to the SSH agent. Enter: `ssh-add`
 .. Enter the SSH Access Password listed in the `Passwords.txt` file.
. [[log_in_to_node]]Log in to the node you want to update with a custom DNS configuration: `ssh _node_IP_address_`
. Run the DNS setup script: `setup_resolv.rb.`
+
The script responds with the list of supported commands.
+
----
Tool to modify external name servers

available commands:
  add search <domain>
               add a specified domain to search list
               e.g.> add search netapp.com
  remove search <domain>
               remove a specified domain from list
               e.g.> remove search netapp.com
  add nameserver <ip>
               add a specified IP address to the name server list
               e.g.> add nameserver 192.0.2.65
  remove nameserver <ip>
               remove a specified IP address from list
               e.g.> remove nameserver 192.0.2.65
  remove nameserver all
               remove all nameservers from list
  save         write configuration to disk and quit
  abort        quit without saving changes
  help         display this help message


Current list of name servers:
    192.0.2.64
Name servers inherited from global DNS configuration:
    192.0.2.126
    192.0.2.127
Current list of search entries:
    netapp.com

Enter command [`add search <domain>|remove search <domain>|add nameserver <ip>`]
              [`remove nameserver <ip>|remove nameserver all|save|abort|help`]
----

. Add the IPv4 address of a server that provides domain name service for your network: `add <nameserver IP_address>`
. Repeat the `add nameserver` command to add name servers.
. Follow instructions as prompted for other commands.
. Save your changes and exit the application: `save`
. [[close_cmd_shell]]Close the command shell on the server: `exit`
. For each grid node, repeat the steps from <<log_in_to_node,logging into the node>> through <<close_cmd_shell,closing the command shell>>.
. When you no longer require passwordless access to other servers, remove the private key from the SSH agent. Enter: `ssh-add -D`

. If you've allowed external SSH access, link:../admin/manage-external-ssh-access.html[block access] when you're finished modifying the DNS configuration.

// 2025 APR 30, SGWS-34284

---
id: "storagegrid-120-17255f2c837c7b0a"
title: "StorageGRID 12.0 installation files vmware"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/_include/installation-files-vmware.adoc"
source_sha256: "9ba45564706301fc0db5cfe3b2350e40f87ca9f1c6d3ce2d661afd849dcf7367"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/installation-files-vmware.adoc"
---

# StorageGRID 12.0 installation files vmware

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/_include/installation-files-vmware.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

//installation files for VMware - used in vmware, expand, maintain

[cols="1a,1a" options="header"]
|===
| Path and file name| Description
m|./vsphere/README
|A text file that describes all of the files contained in the StorageGRID download file.

m|./vsphere/NLF000000.txt
|A free license that does not provide any support entitlement for the product.

m|./vsphere/NetApp-SG-version-SHA.vmdk
|The virtual machine disk file that is used as a template for creating grid node virtual machines.

m|./vsphere/vsphere-primary-admin.ovf

./vsphere/vsphere-primary-admin.mf
|The Open Virtualization Format template file (`.ovf`) and manifest file (`.mf`) for deploying the primary Admin Node.

m|./vsphere/vsphere-non-primary-admin.ovf

./vsphere/vsphere-non-primary-admin.mf
|The template file (`.ovf`) and manifest file (`.mf`) for deploying non-primary Admin Nodes.

m|./vsphere/vsphere-gateway.ovf

./vsphere/vsphere-gateway.mf
|The template file (`.ovf`) and manifest file (`.mf`) for deploying Gateway Nodes.

m|./vsphere/vsphere-storage.ovf

./vsphere/vsphere-storage.mf
|The template file (`.ovf`) and manifest file (`.mf`) for deploying virtual machine-based Storage Nodes.

h|Deployment scripting tool h|Description
m|./vsphere/deploy-vsphere-ovftool.sh
|A Bash shell script used to automate the deployment of virtual grid nodes.

m|./vsphere/deploy-vsphere-ovftool-sample.ini
|An example configuration file for use with the `deploy-vsphere-ovftool.sh` script.

m|./vsphere/configure-storagegrid.py
|A Python script used to automate the configuration of a StorageGRID system.

m|./vsphere/configure-sga.py
|A Python script used to automate the configuration of StorageGRID appliances.

m|./vsphere/storagegrid-ssoauth.py
|An example Python script that you can use to sign in to the Grid Management API when single sign-on (SSO) is enabled. You can also use this script for Ping Federate integration.

m|./vsphere/configure-storagegrid.sample.json
|An example configuration file for use with the `configure-storagegrid.py` script.

m|./vsphere/configure-storagegrid.blank.json
|A blank configuration file for use with the `configure-storagegrid.py` script.

m|./vsphere/storagegrid-ssoauth-azure.py
|An example Python script that you can use to sign in to the Grid Management API when single sign-on (SSO) is enabled using Active Directory or Ping Federate.

m|./vsphere/storagegrid-ssoauth-azure.js
|A helper script called by the companion `storagegrid-ssoauth-azure.py` Python script to perform SSO interactions with Azure.   

m|./vsphere/extras/api-schemas
|API schemas for StorageGRID.

*Note*: Before you perform an upgrade, you can use these schemas to confirm that any code you have written to use StorageGRID management APIs will be compatible with the new StorageGRID release if you don't have a non-production StorageGRID environment for upgrade compatibility testing.

|===

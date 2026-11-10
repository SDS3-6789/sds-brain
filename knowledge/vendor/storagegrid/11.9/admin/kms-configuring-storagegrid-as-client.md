---
id: "storagegrid-119-019451b2a242f094"
title: "StorageGRID 11.9 Configure StorageGRID as a client in the KMS"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/kms-configuring-storagegrid-as-client.adoc"
source_sha256: "b39a96a445cb4a6fe78b4019ab440be6e5c7e0d7f2b153482c5bf522bcd417a6"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/kms-configuring-storagegrid-as-client.adoc"
---

# StorageGRID 11.9 Configure StorageGRID as a client in the KMS

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/admin/kms-configuring-storagegrid-as-client.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Configure StorageGRID as a client in the KMS
:icons: font
:imagesdir: ../media/

[.lead]
You must configure StorageGRID as a client for each external key management server or KMS cluster before you can add the KMS to StorageGRID.

NOTE: These instructions apply to Thales CipherTrust Manager and Hashicorp Vault. For a list of supported products and versions, use the https://imt.netapp.com/matrix/#welcome[NetApp Interoperability Matrix Tool (IMT)^].

.Steps

. From the KMS software, create a StorageGRID client for each KMS or KMS cluster you plan to use.
+
Each KMS manages a single encryption key for the StorageGRID appliances nodes at a single site or at a group of sites.

. [[create-key-with-kms-product]]Create a key using one of the following two methods:
+
* Use the key management page of your KMS product. Create an AES encryption key for each KMS or KMS cluster.
+
The encryption key must be 2,048 bits or more, and it must be exportable.

* Have StorageGRID create the key. You will be prompted when you test and save after link:kms-adding.html#sg-create-key[uploading client certificates].

. Record the following information for each KMS or KMS cluster.
+
You need this information when you add the KMS to StorageGRID:

* Host name or IP address for each server.
* KMIP port used by the KMS.
* Key alias for the encryption key in the KMS.

. For each KMS or KMS cluster, obtain a server certificate signed by a certificate authority (CA) or a certificate bundle that contains each of the PEM-encoded CA certificate files, concatenated in certificate chain order.
+
The server certificate allows the external KMS to authenticate itself to StorageGRID.

* The certificate must use the Privacy Enhanced Mail (PEM) Base-64 encoded X.509 format.
* The Subject Alternative Name (SAN) field in each server certificate must include the fully qualified domain name (FQDN) or IP address that StorageGRID will connect to.
+
NOTE: When you configure the KMS in StorageGRID, you must enter the same FQDNs or IP addresses in the *Hostname* field.

* The server certificate must match the certificate used by the KMIP interface of the KMS, which typically uses port 5696.

. Obtain the public client certificate issued to StorageGRID by the external KMS and the private key for the client certificate.
+
The client certificate allows StorageGRID to authenticate itself to the KMS.

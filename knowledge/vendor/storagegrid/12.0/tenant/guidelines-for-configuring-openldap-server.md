---
id: "storagegrid-120-d36307a4b8b7d94b"
title: "StorageGRID 12.0 Configure an OpenLDAP server for StorageGRID"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/guidelines-for-configuring-openldap-server.adoc"
source_sha256: "77407928f1b1d1f707ce926523edf9966c81519ab73000a48e1afbcee043e07d"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "tenant/guidelines-for-configuring-openldap-server.adoc"
---

# StorageGRID 12.0 Configure an OpenLDAP server for StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/tenant/guidelines-for-configuring-openldap-server.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Configure an OpenLDAP server for StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
If you want to use an OpenLDAP server for identity federation, you must configure specific settings on the OpenLDAP server.

## Memberof and refint overlays

The memberof and refint overlays should be enabled. For more information, see the instructions for reverse group membership maintenance in the _OpenLDAP Software Administrator's Guide_.

## Indexing

You must configure the following OpenLDAP attributes with the specified index keywords:

----
olcDbIndex: objectClass eq
olcDbIndex: uid eq,pres,sub
olcDbIndex: cn eq,pres,sub
olcDbIndex: entryUUID eq
----

In addition, ensure the fields mentioned in the help for Username are indexed for optimal performance.

See the information about reverse group membership maintenance in the _OpenLDAP Software Administrator's Guide_.

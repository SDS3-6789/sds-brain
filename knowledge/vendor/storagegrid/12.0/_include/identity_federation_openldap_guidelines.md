---
id: "storagegrid-120-99cd380d95c950b9"
title: "StorageGRID 12.0 identity_federation_openldap_guidelines"
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
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/_include/identity_federation_openldap_guidelines.adoc"
source_sha256: "0871f0a9afbdb9c56dda0a094f8b7e16c0c1ced602de3faffff9176c08c9d239"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/identity_federation_openldap_guidelines.adoc"
---

# StorageGRID 12.0 identity_federation_openldap_guidelines

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/_include/identity_federation_openldap_guidelines.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

//These are the shared steps for identity federation openldap guidelines in the tenant manager and the grid manager//


If you want to use an OpenLDAP server for identity federation, you must configure specific settings on the OpenLDAP server.

CAUTION: For identity sources that aren't Active Directory or Microsoft Entra ID, StorageGRID won't automatically block S3 access to users who are disabled externally. To block S3 access, delete any S3 keys for the user or remove the user from all groups.

### Memberof and refint overlays

The memberof and refint overlays should be enabled. For more information, see the instructions for reverse group membership maintenance in the 
http://www.openldap.org/doc/admin24/index.html[OpenLDAP documentation: Version 2.4 Administrator's Guide^].

### Indexing

You must configure the following OpenLDAP attributes with the specified index keywords:

* `olcDbIndex: objectClass eq`
* `olcDbIndex: uid eq,pres,sub`
* `olcDbIndex: cn eq,pres,sub`
* `olcDbIndex: entryUUID eq`

In addition, ensure the fields mentioned in the help for Username are indexed for optimal performance.

See the information about reverse group membership maintenance in the
http://www.openldap.org/doc/admin24/index.html[OpenLDAP documentation: Version 2.4 Administrator's Guide^].

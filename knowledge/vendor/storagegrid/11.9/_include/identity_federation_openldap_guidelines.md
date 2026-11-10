---
id: "storagegrid-119-99cd380d95c950b9"
title: "StorageGRID 11.9 identity_federation_openldap_guidelines"
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
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/identity_federation_openldap_guidelines.adoc"
source_sha256: "56c3d279a20fc676bef5f71d5ab4b87e5e616548b54e7c3d71883dbf509af8b0"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "_include/identity_federation_openldap_guidelines.adoc"
---

# StorageGRID 11.9 identity_federation_openldap_guidelines

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/_include/identity_federation_openldap_guidelines.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

//These are the shared steps for identity federation openldap guidelines in the tenant manager and the grid manager//


If you want to use an OpenLDAP server for identity federation, you must configure specific settings on the OpenLDAP server.

CAUTION: For identity sources that aren't ActiveDirectory or Azure, StorageGRID will not automatically block S3 access to users who are disabled externally. To block S3 access, delete any S3 keys for the user or remove the user from all groups.

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

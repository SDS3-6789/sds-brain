---
id: storagegrid-version-api-boundaries
title: StorageGRID versions and API boundaries
area: storagegrid
type: knowledge
applies_to: [storagegrid-11.8, storagegrid-11.9, storagegrid-12-unconfirmed]
confidence: documented
last_verified: 2026-11-09
sources: [netapp-sg118-docs, netapp-sg119-docs, netapp-sg120-docs, netapp-sg119-grid-api, netapp-sg119-tenant-api, netapp-sg119-tenant, netapp-sg119-release-notes, netapp-sg120-whats-new]
---

# StorageGRID versions and API boundaries

## Fleet evidence

The user reports StorageGRID **11.8, 11.9, and "12"** across multiple customers and clusters. This is inventory supplied by the user, not a live discovery result. Preserve `12-unconfirmed` until an authorized operator provides the exact minor release, build, and hotfix. Official version-specific documentation exists for [11.8](https://docs.netapp.com/us-en/storagegrid-118/), [11.9](https://docs.netapp.com/us-en/storagegrid-119/), and [12.0](https://docs.netapp.com/us-en/storagegrid-120/). The unversioned documentation currently points at a newer branch; it is not the default authority for this fleet.

For every incident, attach customer alias, grid alias, release/build/hotfix, site scope, observed time, and the documentation version used. A documentation availability check does not prove that a release is installed or that a particular appliance/OS combination is supported.

## Three interfaces, three purposes

| Interface | Purpose | Identity boundary |
|---|---|---|
| S3 data API | Object and bucket requests from applications | Access keys and applicable S3 policies |
| Grid Management API | Grid-wide administration and inventory | Grid Manager account and group permissions |
| Tenant Management API | Management within a tenant | Tenant identity and tenant permissions |

StorageGRID documents `/grid`, `/org`, and `/private` resource families. Private endpoints can change without notice and disregard the request's API version. The brain must not synthesize private API calls from an old incident. Obtain the installed grid's Swagger documentation and approve specific read operations. [Grid API](https://docs.netapp.com/us-en/storagegrid-119/admin/using-grid-management-api.html).

Tenant API authentication is separate from S3 access-key authentication. The tenant API documentation describes bearer-token authentication and an SSO caveat. The agent should consume an already authorized, scoped credential through its runtime configuration rather than printing credentials or creating login sessions on its own. [Tenant API](https://docs.netapp.com/us-en/storagegrid-119/tenant/understanding-tenant-management-api.html).

## Objectify mapping

The user's Objectify business object maps to a **StorageGRID tenant** on this backend, while its Ceph mapping is an **RGW user**. A StorageGRID tenant has its own users, groups, buckets, and objects; it is not interchangeable with one S3 key or one tenant user. Keep separate fields for Objectify account ID, backend kind, grid ID, tenant ID, and principal alias. These mappings require Objectify's real OpenAPI contract and customer-scoped authorization. [Tenant account model](https://docs.netapp.com/us-en/storagegrid-119/tenant/index.html).

## Documentation access and upgrade evidence

The public [11.9 release-notes landing page](https://docs.netapp.com/us-en/storagegrid-119/release-notes/index.html) links to a support-login PDF for fixed and known issues. The [12.0 feature page](https://docs.netapp.com/us-en/storagegrid-120/release-notes/whats-new.html) similarly directs readers to authenticated release notes. These full release notes have not been imported. Request the authorized export for the actual build before assessing a defect or an upgrade path.

Use the source catalog to find a versioned reference, then inspect the relevant chapter. A source URL in the catalog means it was researched, not that its entire manual is included offline.

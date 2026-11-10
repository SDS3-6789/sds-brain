# Ceph, Linux and IBM documentation research

Research date: **2026-11-09**. This report describes the evidence incorporated into the initial SDS brain. No customer system was accessed and no infrastructure command was executed. The runbooks are sourced investigation templates awaiting environment validation.

## Version findings

- [Red Hat Ceph Storage 7.1 release notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html-single/7.1_release_notes/index) explicitly include **7.1z7** and identify it as a container-only update.
- [Red Hat Ceph Storage 8.1 release notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/8.1_release_notes/8.1_release_notes) contain **8.1z3 and 8.1z6 through z9**. Product features and fixes can vary within the 8.1 stream.
- Official [RHEL 9.6](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/9.6_release_notes/index) and [RHEL 9.8](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index) release notes were opened. The reported OS versions are valid research targets.
- The opened [RHCS 8.1 compatibility matrix](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/compatibility_guide/compatibility-matrix-for-red-hat-ceph-storage-8.1) lists RHEL **9.6 and 9.8**. Cached search text contained a wider list, so the retrieved page takes precedence for this report. Recheck the matrix for a proposed upgrade.
- [IBM's release/package matrix](https://www.ibm.com/support/pages/what-are-red-hat-and-ibm-storage-ceph-releases-and-corresponding-ceph-package-versions) supplies Reef/Squid family references and distinguishes package versions from container tags. It also shows multiple image rebuilds within some z-streams. This does not establish the running Red Hat image digest.

## Coverage delivered

The source catalog includes official Red Hat guides for deployment, configuration, operations, administration, upgrades, compatibility, hardware, security, RGW, release notes and troubleshooting. IBM adds architecture, version mapping, support indexes and recovery explanations. Pinned Ceph upstream references cover health, cephadm, S3, RGW administration, multisite, metrics and mClock. RHEL coverage includes kernel, network, storage, containers, performance and SELinux.

The catalog records an opened reference separately from a search-verified reference. Opening a guide index confirms the reference exists; it is not a claim that every linked chapter was reviewed. Links and original summaries are included here, **not a complete offline mirror of the vendor manuals**.

## Investigation design

The eight runbooks cover the owner's priority incident paths plus the host-level evidence those investigations need. Each begins with customer/cluster selection and keeps production mutation outside the initial procedure. No SSH executor or generic shell permission is established by these text files. Commands are proposed for an already-approved, explicitly selected administrative context.

RGW user inspection is deliberately projected to non-secret metadata fields. Raw user responses can contain S3 key material, as shown in the [Ceph RGW administration reference](https://docs.ceph.com/en/squid/radosgw/admin/). The monitoring procedures require the actual custom exporter schema; a Prometheus deployment was not assumed.

## Remaining evidence gaps

1. Per-customer cluster FSIDs, daemon builds, image digests, hosts and OS pairings have not been supplied.
2. The owner's full Red Hat documentation corpus has not been supplied or imported. The same applies to internal Confluence runbooks, dashboards, exporter definitions and past incidents.
3. Subscription support material is not exhaustively collected. The catalog includes public pages and marks mixed-access indexes; support credentials were not requested or used.
4. One IBM multisite topic was search-verified but its direct retrieval returned HTTP 403. The status is recorded as such.
5. No behavior is labeled tested on this fleet. A relevant release-note entry is a candidate explanation until its prerequisites match the incident.

## Files in this contribution

| File | Words |
|---|---:|
| `knowledge/ceph/operational-model.md` | 475 |
| `knowledge/ceph/version-evidence.md` | 562 |
| `knowledge/linux/diagnostic-boundaries.md` | 433 |
| `runbooks/ceph/cephadm-daemon-triage.md` | 686 |
| `runbooks/ceph/health-baseline.md` | 562 |
| `runbooks/ceph/rgw-multisite-lag.md` | 555 |
| `runbooks/ceph/rgw-request-triage.md` | 709 |
| `runbooks/ceph/slow-ops-and-recovery.md` | 785 |
| `runbooks/linux/network-path.md` | 573 |
| `runbooks/linux/resource-pressure.md` | 609 |
| `runbooks/linux/selinux-denial.md` | 601 |

Source catalog: `sources/ceph-linux.json` — 55 unique records, 54 opened and 1 search-verified. The technical review added primary references for configuration-source precedence, scoped Podman inspection, RGW tenant identity service specification privacy and the Reef/Squid stuck-PG JSON envelope.

Validation performed: source JSON parses; IDs and URLs are unique; every cited source ID in this contribution resolves; required frontmatter parses; shell blocks contain no matched deployment, repair, tuning or restart actions. This is a static content check, not execution validation.

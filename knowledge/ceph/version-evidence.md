---
id: "ceph-version-evidence"
title: "Ceph and RHEL version evidence"
area: "ceph"
type: "knowledge"
applies_to: ["rhcs-7.1", "rhcs-8.1", "rhel-9.6", "rhel-9.8"]
confidence: "documented"
last_verified: "2026-11-09"
sources: ["rhcs-7-release", "rhcs-8-release", "rhcs-8-compat", "ibm-ceph-version-matrix", "rhel-96-release", "rhel-98-release"]
---

# Ceph and RHEL version evidence

## User inventory and documentation evidence

The environment owner reports containerized RGW managed by cephadm and the releases below. This establishes the research target. It does not establish which customer, cluster or host currently runs each build.

| Reported version | Evidence found on 2026-11-09 | Selection rule |
|---|---|---|
| RHCS 7.1z7 | Red Hat's 7.1 release notes explicitly include z7 and identify it as a container-only update. | Use RHCS 7.1 documentation and its exact errata, then verify the running image. |
| RHCS 8.1z3 | Listed in Red Hat's 8.1 release notes. | Inspect feature/fix introduction at the z-stream level. |
| RHCS 8.1z6, z7, z8, z9 | All appear in the current 8.1 release notes. | Preserve each patch as a separate inventory value. |
| RHEL 9.6 and 9.8 | Official release notes exist for both. | Record each host's release RPM, running kernel and architecture. |
| RHCS 8.1 with RHEL 9.6/9.8 | The opened compatibility matrix lists these host OS releases. | Recheck current matrix and subscription support before upgrade planning. |

These findings come from the linked vendor documents, rather than an assumption that a version is too new to exist. Product support is a separate question from documentation availability. A compatibility matrix for 8.1 is not blanket confirmation of every historic image, hardware revision or mixed cluster state.

## Vendor release, package and container are different fields

IBM's release/package matrix associates corresponding 7.1 releases with the Reef family and 8.1 releases with Squid. It also shows multiple image rebuilds associated with one z-stream. Use this to locate upstream background, while retaining the distinction between IBM and Red Hat image registries and support policies. Do not infer a Red Hat OCI digest from an IBM container tag.

For each cluster, the local inventory should contain customer alias, cluster alias, FSID, vendor distribution, declared z-stream, daemon-reported versions, container image reference and digest, host OS and kernel, and date checked. Keep real identifiers in the customer's private inventory.

Read-only evidence, in the explicitly selected cluster's existing administrative session:

```bash
ceph fsid
ceph versions
cat /etc/redhat-release
uname -r
rpm -q redhat-release kernel-core podman
```

Compare the FSID to the chosen inventory entry before interpreting any other result. For a daemon's image/container identity, use the service- and daemon-scoped procedure in [cephadm daemon triage](../../runbooks/ceph/cephadm-daemon-triage.md). The host commands describe the host on which they run; they do not inventory the fleet. An image tag is mutable unless your registry policy prevents it. Preserve the digest reported by the actual runtime when available.

## Documentation precedence

Prefer the deployed vendor's exact-release notes, current support matrix and applicable advisory. Use the vendor guide for operational procedure; use a pinned upstream release family for implementation explanations. Keep conflicting sources visible. Mark a fix as a hypothesis until its prerequisite conditions match the affected deployment. Neither a matching error string nor a newer upstream patch proves that an upgrade is the correct remedy.

## Sources

- [Red Hat Ceph Storage 7.1 Release Notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/7/html-single/7.1_release_notes/index)
- [Red Hat Ceph Storage 8.1 Release Notes](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/8.1_release_notes/8.1_release_notes)
- [RHCS 8.1 Compatibility Matrix](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html/compatibility_guide/compatibility-matrix-for-red-hat-ceph-storage-8.1)
- [Red Hat and IBM Storage Ceph releases and corresponding package versions](https://www.ibm.com/support/pages/what-are-red-hat-and-ibm-storage-ceph-releases-and-corresponding-ceph-package-versions)
- [RHEL 9.6 Release Notes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/9.6_release_notes/index)
- [RHEL 9.8 Release Notes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index)

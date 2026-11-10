---
name: hypershift-debug
description: Establish whether an explicitly reported HyperShift or OpenShift dependency is relevant to an SDS storage incident.
disable-model-invocation: true
---

# Optional platform dependency investigation

This is original SDS content. The legacy skill path is retained to match the reference hierarchy. HyperShift and Kubernetes are not reported as deployed SDS components and no Kubernetes MCP is enabled.

Read AGENT.md and confirm customer/cluster aliases, backend, exact storage and platform versions, UTC window and the operator-supplied dependency. If that dependency is unknown, continue with the Ceph/RGW or StorageGRID runbooks rather than inventing platform context.

Ask for the approved topology and bounded redacted evidence identifying the storage consumer, gateway/service endpoint and owning team. Search locally and verify product versions before applying guidance. Separate platform symptoms from gateway, storage backend, host and network evidence. Record one read-only discriminating check per hypothesis for the authorized platform operator.

Never assume a kubeconfig context, access Secrets, exec into pods, create debug workloads, drain nodes or change hosted control plane resources through this package. The bundled Kubernetes archives preserve the reference paths only; their presence grants no connectivity or authorization. Escalate with evidence and unresolved mappings.

The Apache license at third_party/openshift-hypershift/LICENSE is retained as part of the reference package structure. This skill and the SDS hcp-architect agent were written independently; upstream Hypershift troubleshooting prose was not copied.

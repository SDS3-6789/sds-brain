---
name: incident-report
description: Prepare a local, redacted SDS incident report from an explicitly scoped investigation.
disable-model-invocation: true
---

# Draft an incident report

Read AGENT.md. Confirm the customer/cluster aliases, backend, exact build, UTC incident window, impact and authorized evidence. A customer report belongs in that customer's restricted checkout with SDS_CUSTOMER and SDS_CLUSTER set.

Create the draft:

    bash "$CLAUDE_PLUGIN_ROOT/scripts/brain-git.sh" start incident concise-slug

Use the incident template under SDS_BRAIN_DIR/templates/ as the content guide. Record impact, timeline, evidence, hypotheses, discriminating checks, mitigation proposals, uncertainty and follow-up ownership. Label suggested commands separately from executed observations. Preserve request IDs and bounded timestamps while removing credentials and unnecessary identifiers.

Do not infer a root cause from correlated timing. Do not claim production checks or changes occurred without evidence. Present the draft for review before promotion, sharing or export. The helper does not create commits or publish anything.

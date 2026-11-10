---
name: brain-learn
description: Prepare a local evidence-based knowledge draft for human review after an SDS investigation.
disable-model-invocation: true
---

# Prepare a learning draft

Read AGENT.md and search existing knowledge first. Confirm the operator wants a draft and whether it contains shared knowledge or customer evidence. Use a separate restricted checkout with both SDS_CUSTOMER and SDS_CLUSTER set for customer data.

Create a draft through the plugin helper:

    bash "$CLAUDE_PLUGIN_ROOT/scripts/brain-git.sh" start learn concise-slug

The helper creates a new file exclusively in inbox/ for shared work, or private/<customer>/<cluster>/drafts/ for bound work. Existing files are never overwritten. Drafts are not indexed as approved knowledge.

Write scope, exact version/build, redacted observations, document/source citations, confidence, uncertainty, bounded proposed checks and a review owner/date. Distinguish a hypothesis from repeatable verification. Do not copy credentials, full transcripts, raw customer exports or another customer's evidence.

Present the draft path and the proposed destination using the repository templates. Human review must approve promotion into shared knowledge. Do not automatically stage, commit, push, open a merge request or publish.

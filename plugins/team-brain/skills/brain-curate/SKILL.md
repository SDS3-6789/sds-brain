---
name: brain-curate
description: Review SDS knowledge for duplicate, stale or conflicting evidence and prepare a local curation proposal.
disable-model-invocation: true
---

# Curate with a review trail

Read AGENT.md, search the topic and read the existing source pages before recommending changes. Use the canonical stale command to identify review candidates; age alone is not grounds to delete evidence:

    python3 "$SDS_BRAIN_DIR/scripts/brain.py" stale --days 90

Prepare a local draft with the plugin helper:

    bash "$CLAUDE_PLUGIN_ROOT/scripts/brain-git.sh" start curate concise-slug

Record document IDs, exact product applicability, conflicts, source provenance, owner, review date and a proposed edit or retirement reason. Preserve references required by older installed versions. Keep customer evidence inside its bound restricted checkout.

Present the proposed changes for human review. After approved edits run the canonical validator, index regeneration and relevant tests. Do not delete knowledge, alter source originals, promote unverified findings or automatically commit/push.

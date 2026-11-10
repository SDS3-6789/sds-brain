"""Expose declared citation edges only; no inferred dependencies or live topology."""
from __future__ import annotations


def citations(brain, document_id):
    if document_id not in brain.documents:
        raise ValueError("Unknown document id")
    document = brain.documents[document_id]
    known = {entry["id"] for entry in brain.sources}
    return {"document_id": document_id, "scope": document.scope,
            "relation": "declared_source_reference",
            "sources": [source for source in document.metadata.get("sources", [])
                        if source in known],
            "notice": "Citation edges are metadata, not verified infrastructure relationships."}

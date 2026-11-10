"""Use SDS's canonical bounded document index rather than a second corpus."""
from __future__ import annotations


def search(brain, query, area=None, version=None, limit=8):
    return brain.search(query, area=area, version=version, limit=limit)


def read(brain, document_id, offset=0, max_chars=12000):
    return brain.read(document_id, offset=offset, max_chars=max_chars)

"""Paginated metadata; catalog links do not imply document bodies are bundled."""
from __future__ import annotations


def records(brain, vendor=None, product=None, offset=0, limit=20):
    if type(offset) is not int or type(limit) is not int or offset < 0 or not 1 <= limit <= 30:
        raise ValueError("Invalid source pagination")
    matches = [entry for entry in brain.sources
               if (not vendor or vendor.lower() in entry["vendor"].lower())
               and (not product or product.lower() in entry["product"].lower())]
    return {"sources": matches[offset:offset + limit], "total": len(matches),
            "next_offset": offset + limit if offset + limit < len(matches) else None,
            "content_status": "reference_only"}

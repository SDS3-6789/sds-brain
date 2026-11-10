"""Bounded local retrieval. No network, shell execution, or model dependencies."""
from __future__ import annotations

import collections
import datetime
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PUBLIC_DIRS = ("knowledge", "runbooks", "docs")
PRIVATE_DIRS = ("knowledge", "runbooks", "incidents")
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_CORPUS_BYTES = 256 * 1024 * 1024
MAX_DOCUMENTS = 10000
MAX_CHUNKS = 100000
MAX_METADATA_BYTES = 8 * 1024
MAX_SOURCE_RECORD_BYTES = 8 * 1024
MAX_TITLE_CHARS = 512
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
TERMS = re.compile(r"[a-z0-9]+(?:[_.-][a-z0-9]+)*")


def frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Read the documented flat frontmatter subset, without executing YAML tags."""
    if not text.startswith("---\n"):
        return {}, text
    pieces = text.split("\n---\n", 1)
    if len(pieces) != 2:
        raise ValueError("Unterminated frontmatter")
    if len(pieces[0].encode("utf-8")) > MAX_METADATA_BYTES:
        raise ValueError("Frontmatter exceeds the 8 KiB metadata limit")
    meta: dict[str, Any] = {}
    for line in pieces[0][4:].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            raise ValueError("Only flat frontmatter is supported")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in meta:
            raise ValueError("Duplicate frontmatter key")
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except (json.JSONDecodeError, RecursionError) as exc:
                raise ValueError("Invalid quoted frontmatter value") from exc
            if not isinstance(value, str):
                raise ValueError("Quoted frontmatter values must be strings")
        elif value.startswith("[") and value.endswith("]"):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
            except RecursionError as exc:
                raise ValueError("Frontmatter arrays must contain only strings") from exc
            if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
                raise ValueError("Frontmatter arrays must contain only strings")
        else:
            value = value.strip("\"'")
        meta[key] = value
    return meta, pieces[1]


def tokens(text: str) -> list[str]:
    found = TERMS.findall(text.lower())
    # Both compound names and their parts help queries such as "slow ops" / "slow_ops".
    return found + [part for term in found if re.search(r"[_.-]", term)
                    for part in re.split(r"[_.-]", term) if part]


def load_catalog(root: Path) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    ids: set[str] = set()
    if (root / "sources").is_symlink():
        raise ValueError("Source catalog directory must not be a symlink")
    for path in sorted((root / "sources").glob("*.json")):
        if path.is_symlink() or path.stat().st_size > MAX_FILE_BYTES:
            raise ValueError("Unsafe or oversized source catalog")
        records = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(records, list):
            raise ValueError("Source files must contain arrays")
        for entry in records:
            required = {"id", "title", "url", "vendor", "product", "versions", "topics",
                        "access", "verification", "checked_on", "notes"}
            if not isinstance(entry, dict) or not required <= entry.keys():
                raise ValueError("Missing source metadata")
            if not isinstance(entry["id"], str) or not re.fullmatch(r"[a-z0-9][a-z0-9_.-]*", entry["id"]):
                raise ValueError("Invalid source id")
            if entry["id"] in ids:
                raise ValueError("Duplicate source id: " + str(entry["id"]))
            for field in ("title", "url", "vendor", "product", "access", "verification", "checked_on", "notes"):
                if not isinstance(entry[field], str):
                    raise ValueError("Source text fields must be strings")
            if not str(entry["url"]).startswith("https://"):
                raise ValueError("Catalog sources must be HTTPS references")
            if entry["verification"] not in {"opened", "search-verified", "unverified"}:
                raise ValueError("Unknown verification status")
            if entry["access"] not in {"public", "subscription", "mixed"}:
                raise ValueError("Unknown source access classification")
            for field in ("versions", "topics"):
                if not isinstance(entry[field], list) or not all(isinstance(v, str) for v in entry[field]):
                    raise ValueError("Source versions/topics must be string arrays")
            if len(entry["title"]) > MAX_TITLE_CHARS:
                raise ValueError("Source title exceeds the 512 character limit")
            if len(json.dumps(entry, ensure_ascii=True).encode("ascii")) > MAX_SOURCE_RECORD_BYTES:
                raise ValueError("Source record exceeds the 8 KiB limit")
            datetime.date.fromisoformat(entry["checked_on"])
            ids.add(entry["id"])
            result.append(entry)
    return result


@dataclass
class Document:
    id: str
    title: str
    body: str
    metadata: dict[str, Any]
    scope: str = "shared"


@dataclass
class Chunk:
    document: Document
    ordinal: int
    text: str
    counts: collections.Counter
    length: int


def safe_files(base: Path):
    """Do not follow links, including links in an ancestor of a candidate file."""
    if base.is_symlink():
        raise ValueError("Symbolic-link document directories are not allowed")
    if not base.exists():
        return
    # pathlib compares Windows paths without case, unlike POSIX paths. Sort
    # their portable relative spelling so generated indexes are reproducible.
    for path in sorted(base.rglob("*.md"), key=lambda item: item.relative_to(base).as_posix()):
        current = path
        while current != base:
            if current.is_symlink():
                raise ValueError("Symbolic links are not allowed in the corpus")
            current = current.parent
        if not path.is_file():
            continue
        if path.stat().st_size > MAX_FILE_BYTES:
            raise ValueError("Document exceeds the 4 MiB limit")
        yield path


class Brain:
    def __init__(self, root: Path, customer: str | None = None, cluster: str | None = None):
        self.root = root.resolve(strict=True)
        if (customer is None) != (cluster is None):
            raise ValueError("customer and cluster must be supplied together")
        if customer is not None and (not isinstance(customer, str) or not isinstance(cluster, str)
                                     or not SLUG.fullmatch(customer) or not SLUG.fullmatch(cluster)):
            raise ValueError("Invalid context identifier")
        self.customer, self.cluster = customer, cluster
        self.documents: dict[str, Document] = {}
        self.sources = load_catalog(self.root)
        self.chunks: list[Chunk] = []
        self._bytes = 0
        for area in PUBLIC_DIRS:
            for path in safe_files(self.root / area):
                if path == self.root / "docs" / "SOURCES.md":
                    continue  # Catalog entries are indexed separately, without duplicate table text.
                self._add_file(path, "shared")
        for name in ("README.md", "AGENT.md"):
            path = self.root / name
            if path.exists():
                if path.is_symlink():
                    raise ValueError("Symbolic links are not allowed")
                self._add_file(path, "shared")
        if customer:
            base = self.root / "private" / customer / cluster
            # Check every parent: a tenant directory may itself be a symlink.
            for component in (self.root / "private", base.parent, base):
                if component.is_symlink():
                    raise ValueError("Private context paths must not be symlinks")
            for area in PRIVATE_DIRS:
                for path in safe_files(base / area):
                    self._add_file(path, "private")
        for entry in self.sources:
            doc = Document("catalog:" + entry["id"], entry["title"],
                           json.dumps(entry, ensure_ascii=False, indent=2),
                           {"area": "sources", "applies_to": entry["versions"],
                            "source_id": entry["id"], "url": entry["url"],
                            "content_status": "reference_only", "topics": entry["topics"]})
            self._add(doc)
        self.df = collections.Counter()
        for chunk in self.chunks:
            self.df.update(chunk.counts.keys())
        self.average_length = sum(c.length for c in self.chunks) / max(1, len(self.chunks))

    def _add_file(self, path: Path, scope: str):
        relative = path.relative_to(self.root).as_posix()
        if path.stat().st_size > MAX_FILE_BYTES:
            raise ValueError("Document exceeds the 4 MiB limit")
        text = path.read_text(encoding="utf-8")
        meta, body = frontmatter(text)
        if scope == "private":
            if meta.get("customer") != self.customer or meta.get("cluster") != self.cluster:
                raise ValueError("Private document context is missing or mismatched: " + relative)
        elif "customer" in meta or "cluster" in meta:
            raise ValueError("Customer-specific documents belong under private/: " + relative)
        title = meta.get("title") or next((l.lstrip("# ") for l in body.splitlines()
                                           if l.startswith("# ")), path.stem)
        self._add(Document(relative, str(title), body, meta, scope))

    def _add(self, doc: Document):
        if len(doc.title) > MAX_TITLE_CHARS:
            raise ValueError("Document title exceeds the 512 character limit")
        metadata = json.dumps(doc.metadata, ensure_ascii=True).encode("ascii")
        if len(metadata) > MAX_METADATA_BYTES:
            raise ValueError("Document metadata exceeds the 8 KiB limit")
        self._bytes += len(doc.body.encode("utf-8")) + len(doc.title.encode("utf-8")) + len(metadata)
        if self._bytes > MAX_CORPUS_BYTES or len(self.documents) >= MAX_DOCUMENTS:
            raise ValueError("Corpus limit exceeded; partition the documentation by product/version")
        self.documents[doc.id] = doc
        paragraphs = re.split(r"\n\s*\n", doc.body)
        chunks, pending = [], ""
        for paragraph in paragraphs:
            if pending and len(pending) + len(paragraph) > 2200:
                chunks.append(pending)
                pending = ""
            if len(paragraph) > 5000:
                chunks.extend(paragraph[i:i + 2200] for i in range(0, len(paragraph), 2200))
            else:
                pending += ("\n\n" if pending else "") + paragraph
        if pending:
            chunks.append(pending)
        for ordinal, text in enumerate(chunks or [doc.title]):
            terms = tokens(doc.title + " " + doc.title + " " + text)
            self.chunks.append(Chunk(doc, ordinal, text, collections.Counter(terms), len(terms)))
            if len(self.chunks) > MAX_CHUNKS:
                raise ValueError("Corpus chunk limit exceeded")

    def check_context(self, arguments: dict[str, Any]):
        if self.customer:
            if arguments.get("customer") != self.customer or arguments.get("cluster") != self.cluster:
                raise ValueError("Requested context does not match this server's bound customer and cluster")
        elif arguments.get("customer") is not None or arguments.get("cluster") is not None:
            raise ValueError("This is a shared-reference server; start a context-bound process for private data")

    def search(self, query: str, area: str | None = None, version: str | None = None,
               limit: int = 6) -> list[dict[str, Any]]:
        if not isinstance(query, str) or not query.strip() or len(query) > 1000:
            raise ValueError("query must contain 1-1000 characters")
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 20:
            raise ValueError("limit must be between 1 and 20")
        terms = set(tokens(query))
        n = len(self.chunks)
        matches = []
        for chunk in self.chunks:
            doc = chunk.document
            if area and area != doc.metadata.get("area"):
                continue
            applies = doc.metadata.get("applies_to", [])
            if version and not any(version.lower() in str(v).lower() for v in applies):
                continue
            score = 0.0
            for term in terms & chunk.counts.keys():
                frequency = chunk.counts[term]
                inverse = math.log(1 + (n - self.df[term] + 0.5) / (self.df[term] + 0.5))
                denom = frequency + 1.5 * (0.25 + 0.75 * chunk.length / max(self.average_length, 1))
                score += inverse * frequency * 2.5 / denom
            if score:
                if doc.id.startswith("runbooks/"):
                    score *= 1.12
                if doc.id.startswith("catalog:"):
                    score *= 0.65
                matches.append((score, chunk))
        matches.sort(key=lambda item: (-item[0], item[1].document.id, item[1].ordinal))
        # Show distinct documents and explicitly identified documentation
        # families before repeating chunks or alternate editions of one page.
        # This changes result diversity, not scores or version applicability:
        # editions remain separate documents and version filtering ran above.
        preferred, deferred = [], []
        seen_documents, seen_families = set(), set()
        for match in matches:
            doc = match[1].document
            family, original = doc.metadata.get("source_family"), doc.metadata.get("original_path")
            family_key = ((doc.scope, family, original)
                          if doc.metadata.get("source_kind") == "pinned-vendor-documentation"
                          and isinstance(family, str) and family
                          and isinstance(original, str) and original else None)
            if doc.id in seen_documents or (family_key is not None and family_key in seen_families):
                deferred.append(match)
                continue
            preferred.append(match)
            seen_documents.add(doc.id)
            if family_key is not None:
                seen_families.add(family_key)
        result, per_document = [], collections.Counter()
        for score, chunk in preferred + deferred:
            if per_document[chunk.document.id] >= 2:
                continue
            per_document[chunk.document.id] += 1
            result.append({"id": chunk.document.id, "chunk": chunk.ordinal,
                           "title": chunk.document.title, "score": round(score, 4),
                           "scope": chunk.document.scope, "metadata": chunk.document.metadata,
                           "excerpt": chunk.text[:3000]})
            if len(result) >= limit:
                break
        return result

    def read(self, document_id: str, offset: int = 0, max_chars: int = 12000) -> dict[str, Any]:
        # Look up an already indexed ID. Never treat model-provided input as a filesystem path.
        if document_id not in self.documents:
            raise ValueError("Unknown or inaccessible document id; select an id returned by search")
        if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
            raise ValueError("offset must be a nonnegative integer")
        if isinstance(max_chars, bool) or not isinstance(max_chars, int) or not 1 <= max_chars <= 24000:
            raise ValueError("max_chars must be between 1 and 24000")
        doc = self.documents[document_id]
        end = min(len(doc.body), offset + max_chars)
        return {"id": doc.id, "title": doc.title, "scope": doc.scope,
                "metadata": doc.metadata, "text": doc.body[offset:end],
                "next_offset": end if end < len(doc.body) else None,
                "reference_material": True}

    def status(self) -> dict[str, Any]:
        vendor_documents = [d for d in self.documents.values()
                            if d.metadata.get("source_kind") in
                            ("public-vendor-snapshot", "pinned-vendor-documentation")]
        vendor_sources = {source for d in vendor_documents
                          for source in (d.metadata.get("sources", [])
                                         if isinstance(d.metadata.get("sources"), list) else [])
                          if isinstance(source, str) and source}
        repositories = {d.metadata["repository_url"] for d in vendor_documents
                        if isinstance(d.metadata.get("repository_url"), str)
                        and d.metadata["repository_url"].strip()}
        manuals_bundled = bool(repositories or any(d.metadata.get("snapshot_scope") == "pdf-book"
                                                  for d in vendor_documents))
        return {"server": "sds-knowledge", "version": "0.4.0", "network": "none",
                "customer": self.customer, "cluster": self.cluster,
                "documents": sum(not k.startswith("catalog:") for k in self.documents),
                "private_documents": sum(d.scope == "private" for d in self.documents.values()),
                "catalog_references": len(self.sources), "chunks": len(self.chunks),
                "vendor_snapshot_documents": len(vendor_documents),
                "vendor_snapshot_sources": len(vendor_sources),
                "vendor_documentation_repositories": len(repositories),
                "vendor_manuals_bundled": manuals_bundled,
                "notice": "Catalog references are metadata and links, separate from indexed vendor snapshots. Snapshot counts describe local pages, files, PDF books and repository documentation; they do not establish complete manual or product coverage. Private imports are indexed only in this process's exact context. Restart after changing corpus files."}

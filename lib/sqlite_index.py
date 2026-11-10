"""Self-contained public SQLite/FTS5 snapshot, built without a service or network."""
from __future__ import annotations

from contextlib import closing
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import mimetypes
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import xml.etree.ElementTree as ET
from zipfile import BadZipFile, ZipFile

from lib.brain import frontmatter, load_catalog

SCHEMA_VERSION = 1
APPLICATION_ID = 0x53445342
PACKAGE_VERSION = "0.4.0"
DEFAULT_DATABASE = "data/sds-brain.db"
MAX_TEXT_BYTES = 4 * 1024 * 1024
MAX_ASSET_BYTES = 32 * 1024 * 1024
MAX_TOTAL_BYTES = 384 * 1024 * 1024
MAX_INPUTS = 20000
EXCLUDED_DIRS = {".git", ".codex", ".agents", ".venv", "venv", ".cache", "__pycache__",
                 ".pytest_cache", "private", "exports", "dist", "work", "outputs", "node_modules",
                 "inbox", "drafts", "staging"}
EXCLUDED_NAMES = {"MANIFEST.sha256", "rhokp.env", "SQLITE_BUILD_REPORT.json", "SQLITE_INDEX_REPORT.json"}
EXCLUDED_SUFFIXES = {".zip", ".gz", ".tgz", ".tar", ".7z", ".xz", ".exe", ".dll", ".so", ".dylib",
                     ".db", ".sqlite", ".sqlite3", ".pem", ".key", ".p12", ".pfx", ".log", ".pyc"}
TEXT_SUFFIXES = {".md", ".rst", ".adoc", ".txt"}
CONFIG_SUFFIXES = {".json", ".yaml", ".yml", ".toml", ".ini", ".container", ".network", ".volume", ".example"}
CODE_SUFFIXES = {".py", ".sh", ".ps1", ".js", ".mjs", ".cjs"}
DOC_ASSET_SUFFIXES = TEXT_SUFFIXES | CONFIG_SUFFIXES | {".html", ".htm", ".pdf", ".docx", ".sha256"}

SCHEMA = """
CREATE TABLE index_info (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE sources (
 source_id TEXT PRIMARY KEY, title TEXT NOT NULL, url TEXT NOT NULL, vendor TEXT NOT NULL,
 product TEXT NOT NULL, versions_json TEXT NOT NULL, topics_json TEXT NOT NULL,
 access TEXT NOT NULL, verification TEXT NOT NULL, checked_on TEXT NOT NULL, notes TEXT NOT NULL,
 capture_status TEXT NOT NULL, acquisition_json TEXT NOT NULL
);
CREATE TABLE documents (
 doc_id INTEGER PRIMARY KEY, document_id TEXT NOT NULL UNIQUE, path TEXT NOT NULL UNIQUE,
 title TEXT NOT NULL, body TEXT NOT NULL, content TEXT NOT NULL, metadata_json TEXT NOT NULL,
 scope TEXT NOT NULL CHECK(scope='shared'), kind TEXT NOT NULL, area TEXT NOT NULL,
 sha256 TEXT NOT NULL, body_sha256 TEXT NOT NULL, file_bytes INTEGER NOT NULL, source_url TEXT, source_kind TEXT NOT NULL
);
CREATE TABLE document_sources (
 doc_id INTEGER NOT NULL REFERENCES documents(doc_id) ON DELETE CASCADE,
 source_id TEXT NOT NULL, PRIMARY KEY(doc_id, source_id)
);
CREATE TABLE document_versions (
 doc_id INTEGER NOT NULL REFERENCES documents(doc_id) ON DELETE CASCADE,
 version TEXT NOT NULL, PRIMARY KEY(doc_id, version)
);
CREATE TABLE assets (
 asset_id INTEGER PRIMARY KEY, path TEXT NOT NULL UNIQUE, media_type TEXT NOT NULL,
 sha256 TEXT NOT NULL, size_bytes INTEGER NOT NULL, linked_document_path TEXT,
 content BLOB NOT NULL
);
CREATE TABLE inputs (path TEXT PRIMARY KEY, sha256 TEXT NOT NULL, size_bytes INTEGER NOT NULL);
CREATE INDEX documents_area_kind ON documents(area, kind);
CREATE INDEX document_sources_source ON document_sources(source_id);
CREATE INDEX document_versions_value ON document_versions(version);
CREATE INDEX assets_linked_document ON assets(linked_document_path);
CREATE VIRTUAL TABLE documents_fts USING fts5(
 title, body, path, content='documents', content_rowid='doc_id',
 tokenize='unicode61 remove_diacritics 2'
);
CREATE VIRTUAL TABLE documents_fts_vocabulary USING fts5vocab(documents_fts, 'row');
"""


def _json(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True)


def _linked(path):
    return path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())


def _regular_path(root, path, require_exists=True):
    """Validate lexical containment and every linked ancestor before reading/writing."""
    try:
        path.relative_to(root)
    except ValueError as error:
        raise ValueError("Path leaves the selected project") from error
    for component in (path, *path.parents):
        if _linked(component):
            raise ValueError("SQLite snapshot paths must not follow links")
        if component == root:
            break
    if require_exists and not path.is_file():
        raise ValueError("Expected a regular input file")
    if require_exists and path.stat().st_nlink > 1:
        raise ValueError("Hard-linked public files are not SQLite snapshot inputs")


def public_inputs(root):
    """Yield only explicitly supported public text/document inputs, never private material."""
    root = Path(root).resolve(strict=True)
    count = 0
    for base, directories, filenames in os.walk(root, followlinks=False):
        base = Path(base)
        retained = []
        for name in sorted(directories):
            path = base / name
            relative = path.relative_to(root).as_posix().lower()
            if name.lower() in EXCLUDED_DIRS or relative in {"data", "docs/imported"}:
                continue
            if _linked(path):
                raise ValueError("Linked public directory is not an index input")
            retained.append(name)
        directories[:] = retained
        for name in sorted(filenames):
            path = base / name
            relative = path.relative_to(root).as_posix()
            lower_name, lower_relative = name.lower(), relative.lower()
            suffix = path.suffix.lower()
            if (lower_name in {value.lower() for value in EXCLUDED_NAMES} or suffix in EXCLUDED_SUFFIXES or lower_name.startswith(".env")
                    or ".local." in lower_name or lower_name.endswith((".env", "-wal", "-shm", "-journal"))
                    or (lower_relative.startswith("mcp/objectify/") and lower_name.startswith("openapi"))):
                continue
            supported = (suffix in TEXT_SUFFIXES | CONFIG_SUFFIXES | CODE_SUFFIXES | {".docx", ".pdf", ".html", ".htm", ".sha256"}
                         or name in {"NOTICE", "Makefile", ".gitignore", ".gitattributes"}
                         or name.startswith("LICENSE"))
            if not supported:
                continue
            _regular_path(root, path)
            count += 1
            if count > MAX_INPUTS:
                raise ValueError("Too many SQLite index inputs; partition the corpus")
            yield path


def _fingerprint(records):
    digest = hashlib.sha256()
    for path, checksum, size in sorted(records):
        digest.update(path.encode("utf-8") + b"\0" + checksum.encode("ascii") + b"\0" + str(size).encode("ascii") + b"\n")
    return digest.hexdigest()


def _vocabulary_checksum(connection):
    digest = hashlib.sha256()
    for row in connection.execute("SELECT term,doc,cnt FROM documents_fts_vocabulary ORDER BY term"):
        digest.update(_json(tuple(row)).encode("ascii") + b"\n")
    return digest.hexdigest()


def corpus_fingerprint(root):
    root = Path(root).resolve(strict=True)
    records, total = [], 0
    for path in public_inputs(root):
        data = path.read_bytes()
        total += len(data)
        if len(data) > MAX_ASSET_BYTES or total > MAX_TOTAL_BYTES:
            raise ValueError("SQLite snapshot input byte limit exceeded")
        records.append((path.relative_to(root).as_posix(), hashlib.sha256(data).hexdigest(), len(data)))
    return {"fingerprint": _fingerprint(records), "inputs": len(records), "input_bytes": total}


def _word_text(data):
    import io
    try:
        with ZipFile(io.BytesIO(data)) as archive:
            member = archive.getinfo("word/document.xml")
            if member.file_size > 16 * 1024 * 1024:
                raise ValueError("Word document XML exceeds the extraction bound")
            xml = ET.fromstring(archive.read(member))
    except (BadZipFile, ET.ParseError, KeyError) as error:
        raise ValueError("Invalid Word document for text extraction") from error
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    return "\n".join(
        "".join(node.text or "" for node in paragraph.findall(".//w:t", ns))
        for paragraph in xml.findall(".//w:p", ns))


class _HTMLText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip += 1
        elif not self.skip and tag in {"p", "div", "br", "li", "tr", "pre", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.skip:
            self.skip -= 1
        elif not self.skip and tag in {"td", "th"}:
            self.parts.append("\t")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def _document(root, path, data):
    relative = path.relative_to(root).as_posix()
    suffix = path.suffix.lower()
    metadata = {}
    if suffix == ".docx":
        content = body = _word_text(data)
        metadata = {"title": next((line.strip() for line in body.splitlines() if line.strip()), path.stem)[:512],
                    "source_kind": "word-document-text", "extraction": "Main Word document paragraphs and table text; original DOCX retained as an asset"}
        kind = "document"
    elif suffix == ".pdf":
        return None  # Exact PDF retained as an asset; reviewed extracted book text is already in knowledge/vendor.
    else:
        if len(data) > MAX_TEXT_BYTES:
            raise ValueError("Text index input exceeds the 4 MiB document limit: " + relative)
        content = data.decode("utf-8")
        body = content
        kind = "document" if suffix in TEXT_SUFFIXES or path.name.startswith("LICENSE") or path.name == "NOTICE" else "config" if suffix in CONFIG_SUFFIXES else "code"
        if suffix == ".md":
            normalized = content.removeprefix("\ufeff").replace("\r\n", "\n")
            template_metadata = None
            if relative == "templates/incident.md":
                candidate, _ = frontmatter(normalized)
                placeholder_fields = {"id": "replace-with-incident-id", "title": "Replace with incident title",
                                      "customer": "customer-a", "cluster": "cluster-a"}
                if all(candidate.get(key) == value for key, value in placeholder_fields.items()):
                    template_metadata = dict(candidate)
                    template_metadata["template_placeholders"] = {key: template_metadata.pop(key) for key in ("customer", "cluster")}
                    template_metadata.update(scope="shared", source_kind="incident-template")
            if normalized.startswith("---\n"):
                header = normalized.split("\n---\n", 1)[0]
                # Rich plugin YAML is preserved without a YAML dependency. Detect
                # scope declarations before fallback can discard their meaning,
                # including quoted, nested, flow-mapping and indented keys.
                declarations = re.finditer(r'''(?:^|[\s{,])['"]?(customer|cluster|scope)['"]?\s*:\s*([^\n,}]*)''', header, re.MULTILINE | re.IGNORECASE)
                for declaration in declarations:
                    key, value = declaration.group(1).lower(), declaration.group(2).strip().split(" #", 1)[0].strip("\"'")
                    if template_metadata is not None and key in {"customer", "cluster"}:
                        continue  # Exact reviewed public template placeholders only.
                    if key != "scope" or value != "shared":
                        raise ValueError("Customer-scoped material cannot enter a shared SQLite snapshot: " + relative)
            try:
                metadata, body = frontmatter(normalized)
            except ValueError:
                if not relative.startswith("plugins/"):
                    raise
                # Claude plugin frontmatter may be richer than the flat SDS corpus schema.
                # Preserve it verbatim rather than silently dropping fields.
                metadata = {"source_kind": "plugin-documentation", "frontmatter": "Preserved verbatim in content"}
                body = content
            if template_metadata is not None:
                metadata, kind = template_metadata, "config"
        elif suffix in {".html", ".htm"}:
            parser = _HTMLText()
            parser.feed(content)
            body, kind = "".join(parser.parts), "document"
    if any(key.lower() in {"customer", "cluster"} for key in metadata) or metadata.get("scope", "shared") != "shared":
        raise ValueError("Customer-scoped material cannot enter a shared SQLite snapshot: " + relative)
    title = str(metadata.get("title") or next((line.lstrip("#= ") for line in body.splitlines() if line.startswith(("# ", "= "))), path.stem))
    if len(title) > 512:
        title = title[:512]
    if len(_json(metadata).encode("ascii")) > 64 * 1024:
        raise ValueError("Document metadata exceeds the SQLite snapshot bound")
    return {"document_id": relative, "path": relative, "title": title, "body": body, "content": content,
            "metadata": metadata, "kind": kind, "area": str(metadata.get("area", "plugin" if relative.startswith("plugins/") else "meta")),
            "source_url": metadata.get("source_url") or metadata.get("url"),
            "source_kind": str(metadata.get("source_kind", "local-project-document")),
            "versions": metadata.get("applies_to", []) if isinstance(metadata.get("applies_to", []), list) else [],
            "sources": metadata.get("sources", []) if isinstance(metadata.get("sources", []), list) else []}


def _acquisition(root):
    statuses, links = {}, {}
    report = root / "docs/OFFLINE_KNOWLEDGE_REPORT.json"
    if report.is_file():
        _regular_path(root, report)
        value = json.loads(report.read_text(encoding="utf-8"))
        statuses = {entry["source_id"]: entry for entry in value.get("sources", [])}
        for entry in value.get("documents", []):
            links[entry["raw_file"]] = entry["indexed_file"]
    report = root / "docs/OFFLINE_STORAGEGRID_REPORT.json"
    if report.is_file():
        _regular_path(root, report)
        value = json.loads(report.read_text(encoding="utf-8"))
        for repository in value.get("repositories", []):
            for entry in repository.get("indexed", []):
                links[repository["raw_directory"] + "/source/" + entry["source_path"]] = entry["file"]
    return statuses, links


def build_database(root, database=None):
    """Rebuild into a new file and atomically replace only the selected database."""
    root = Path(root).resolve(strict=True)
    database = Path(database) if database is not None else root / DEFAULT_DATABASE
    if not database.is_absolute():
        database = root / database
    database = Path(os.path.abspath(database))
    _regular_path(root, database, require_exists=False)
    if database.exists() and not database.is_file():
        raise ValueError("Database destination must be a regular file")
    if database.suffix.lower() != ".db":
        raise ValueError("Use a .db destination inside the selected project")
    _regular_path(root, root / "sources", require_exists=False)
    for catalog in (root / "sources").glob("*.json"):
        _regular_path(root, catalog)
    sources = load_catalog(root)
    statuses, asset_links = _acquisition(root)
    database.parent.mkdir(parents=True, exist_ok=True)
    _regular_path(root, database, require_exists=False)
    descriptor, temporary_name = tempfile.mkstemp(prefix="." + database.name + ".", suffix=".tmp", dir=database.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    connection = None
    try:
        connection = sqlite3.connect(str(temporary))
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA journal_mode=DELETE")
        connection.execute("PRAGMA synchronous=FULL")
        connection.execute("PRAGMA application_id=" + str(APPLICATION_ID))
        connection.execute("PRAGMA user_version=" + str(SCHEMA_VERSION))
        connection.executescript(SCHEMA)
        with connection:
            for source in sources:
                capture = statuses.get(source["id"], {})
                connection.execute("INSERT INTO sources VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (source["id"], source["title"], source["url"], source["vendor"], source["product"],
                     _json(source["versions"]), _json(source["topics"]), source["access"], source["verification"],
                     source["checked_on"], source["notes"], capture.get("status", "reference_only"), _json(capture)))
            records, total = [], 0
            for path in public_inputs(root):
                relative = path.relative_to(root).as_posix()
                data = path.read_bytes()
                total += len(data)
                if len(data) > MAX_ASSET_BYTES or total > MAX_TOTAL_BYTES:
                    raise ValueError("SQLite snapshot input byte limit exceeded")
                checksum = hashlib.sha256(data).hexdigest()
                records.append((relative, checksum, len(data)))
                connection.execute("INSERT INTO inputs VALUES(?,?,?)", records[-1])
                raw_vendor = relative.lower().startswith("vendor-sources/")
                document = None if raw_vendor else _document(root, path, data)
                if document is not None:
                    values = (document["document_id"], relative, document["title"], document["body"], document["content"],
                              _json(document["metadata"]), "shared", document["kind"], document["area"], checksum,
                              hashlib.sha256(document["body"].encode("utf-8")).hexdigest(),
                              len(data), document["source_url"], document["source_kind"])
                    cursor = connection.execute("""INSERT INTO documents(document_id,path,title,body,content,metadata_json,scope,kind,area,sha256,body_sha256,file_bytes,source_url,source_kind)
                                                 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", values)
                    doc_id = cursor.lastrowid
                    for source_id in set(item for item in document["sources"] if isinstance(item, str)):
                        connection.execute("INSERT INTO document_sources VALUES(?,?)", (doc_id, source_id))
                    for version in set(item for item in document["versions"] if isinstance(item, str)):
                        connection.execute("INSERT INTO document_versions VALUES(?,?)", (doc_id, version))
                if raw_vendor or path.suffix.lower() in {".pdf", ".docx", ".html", ".htm"}:
                    connection.execute("INSERT INTO assets(path,media_type,sha256,size_bytes,linked_document_path,content) VALUES(?,?,?,?,?,?)",
                        (relative, mimetypes.guess_type(relative)[0] or "application/octet-stream", checksum, len(data),
                         asset_links.get(relative, relative if document else None), sqlite3.Binary(data)))
            connection.execute("INSERT INTO documents_fts(documents_fts) VALUES('rebuild')")
            connection.execute("INSERT INTO documents_fts(documents_fts,rank) VALUES('integrity-check',1)")
            vocabulary = tuple(connection.execute("SELECT count(*),coalesce(sum(doc),0),coalesce(sum(cnt),0) FROM documents_fts_vocabulary").fetchone())
            metadata = {"schema_version": str(SCHEMA_VERSION), "package_version": PACKAGE_VERSION, "scope": "shared",
                        "built_at_utc": datetime.now(timezone.utc).isoformat(), "corpus_fingerprint": _fingerprint(records),
                        "inputs": str(len(records)), "input_bytes": str(total), "fts_tokenizer": "unicode61 remove_diacritics 2",
                        "fts_vocabulary_signature": _json(vocabulary),
                        "fts_vocabulary_sha256": _vocabulary_checksum(connection),
                        "excluded": _json(sorted(EXCLUDED_DIRS | EXCLUDED_NAMES)),
                        "notice": "Public snapshot only. Private/customer data excluded. Source references are separate from document bodies. Original document assets are retained as bytes; runtime archives are excluded."}
            connection.executemany("INSERT INTO index_info VALUES(?,?)", metadata.items())
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("New SQLite database failed integrity checking")
        connection.close()
        connection = None
        with temporary.open("r+b") as stream:
            os.fsync(stream.fileno())
        _regular_path(root, database, require_exists=False)
        os.replace(temporary, database)
        return status(database)
    finally:
        if connection is not None:
            connection.close()
        temporary.unlink(missing_ok=True)


def open_readonly(database):
    path = Path(database).resolve(strict=True)
    if not path.is_file():
        raise ValueError("SQLite database file is missing")
    connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only=ON")
    connection.execute("PRAGMA trusted_schema=OFF")
    if connection.execute("PRAGMA application_id").fetchone()[0] != APPLICATION_ID:
        connection.close()
        raise ValueError("Not an SDS Brain database")
    if connection.execute("PRAGMA user_version").fetchone()[0] != SCHEMA_VERSION:
        connection.close()
        raise ValueError("Unsupported SDS Brain database schema")
    return connection


def status(database):
    with closing(open_readonly(database)) as connection:
        info = dict(connection.execute("SELECT key,value FROM index_info"))
        return {"ok": True, "database": str(Path(database).resolve()), "schema_version": SCHEMA_VERSION,
                "package_version": info["package_version"], "scope": info["scope"], "network": "none",
                "documents": connection.execute("SELECT count(*) FROM documents").fetchone()[0],
                "documents_by_kind": dict(connection.execute("SELECT kind,count(*) FROM documents GROUP BY kind")),
                "catalog_references": connection.execute("SELECT count(*) FROM sources").fetchone()[0],
                "sources_by_capture_status": dict(connection.execute("SELECT capture_status,count(*) FROM sources GROUP BY capture_status")),
                "original_document_assets": connection.execute("SELECT count(*) FROM assets").fetchone()[0],
                "asset_bytes": connection.execute("SELECT coalesce(sum(size_bytes),0) FROM assets").fetchone()[0],
                "input_files": int(info["inputs"]), "corpus_fingerprint": info["corpus_fingerprint"],
                "built_at_utc": info["built_at_utc"], "database_bytes": Path(database).stat().st_size,
                "notice": info["notice"]}


def plain_match(query, mode="any"):
    if not isinstance(query, str) or not query.strip() or len(query) > 1000:
        raise ValueError("Search requires 1-1000 characters")
    if mode not in {"any", "all", "phrase"}:
        raise ValueError("Unknown search mode")
    words = re.findall(r"[^\W_]+(?:[_-][^\W_]+)*", query, re.UNICODE)
    if not words or len(words) > 64:
        raise ValueError("Search requires 1-64 text terms")
    if mode == "phrase":
        return '"' + " ".join(words).replace('"', '""') + '"'
    return (" OR " if mode == "any" else " AND ").join('"' + word.replace('"', '""') + '"' for word in words)


def search(database, query, limit=10, area=None, version=None, source_id=None, kind="document", mode="any"):
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 50:
        raise ValueError("Search limit must be 1-50")
    if kind not in {"document", "config", "code", "all"}:
        raise ValueError("Unknown document kind")
    clauses, arguments = ["documents_fts MATCH ?"], [plain_match(query, mode)]
    if kind != "all":
        clauses.append("d.kind=?")
        arguments.append(kind)
    for value in (area, version, source_id):
        if value is not None and (not isinstance(value, str) or len(value) > 512):
            raise ValueError("Invalid search filter")
    if area is not None:
        clauses.append("d.area=?")
        arguments.append(area)
    if source_id is not None:
        clauses.append("EXISTS(SELECT 1 FROM document_sources s WHERE s.doc_id=d.doc_id AND s.source_id=?)")
        arguments.append(source_id)
    if version is not None:
        clauses.append("EXISTS(SELECT 1 FROM document_versions v WHERE v.doc_id=d.doc_id AND v.version LIKE ? ESCAPE '\\')")
        arguments.append("%" + version.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%")
    statement = """SELECT d.document_id,d.path,d.title,d.area,d.kind,d.scope,d.source_url,
                   bm25(documents_fts,4.0,1.0,0.2) AS score,
                   snippet(documents_fts,1,'[',']',' ... ',48) AS excerpt
                   FROM documents_fts JOIN documents d ON d.doc_id=documents_fts.rowid WHERE """ + " AND ".join(clauses) + " ORDER BY score,d.path LIMIT ?"
    arguments.append(limit)
    with closing(open_readonly(database)) as connection:
        results = []
        for row in connection.execute(statement, arguments):
            record = dict(row)
            record["excerpt"] = record["excerpt"][:3000]
            record["versions"] = [item[0] for item in connection.execute("SELECT version FROM document_versions v JOIN documents d ON d.doc_id=v.doc_id WHERE d.document_id=? ORDER BY version", (record["document_id"],))]
            record["sources"] = [item[0] for item in connection.execute("SELECT source_id FROM document_sources s JOIN documents d ON d.doc_id=s.doc_id WHERE d.document_id=? ORDER BY source_id", (record["document_id"],))]
            results.append(record)
        return {"query": query, "mode": mode, "results": results, "network": "none"}


def read(database, document_id, offset=0, max_chars=12000, full_source=False):
    if not isinstance(document_id, str) or len(document_id) > 4096:
        raise ValueError("Invalid document ID")
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("Offset must be nonnegative")
    if isinstance(max_chars, bool) or not isinstance(max_chars, int) or not 1 <= max_chars <= 24000:
        raise ValueError("Read size must be 1-24000 characters")
    with closing(open_readonly(database)) as connection:
        row = connection.execute("SELECT document_id,path,title,body,content,metadata_json,scope,kind,sha256 FROM documents WHERE document_id=?", (document_id,)).fetchone()
        if row is None:
            raise ValueError("Unknown document ID; choose a returned search result")
        text = row["content"] if full_source else row["body"]
        end = min(len(text), offset + max_chars)
        return {"document_id": row["document_id"], "path": row["path"], "title": row["title"], "scope": row["scope"], "kind": row["kind"],
                "metadata": json.loads(row["metadata_json"]), "source_file_sha256": row["sha256"], "text": text[offset:end],
                "next_offset": end if end < len(text) else None, "full_source": bool(full_source), "reference_material": True}


def check(database, root=None):
    with closing(open_readonly(database)) as connection:
        failures = []
        checks = [row[0] for row in connection.execute("PRAGMA integrity_check")]
        if checks != ["ok"]:
            failures.append("SQLite integrity_check did not return ok")
        if list(connection.execute("PRAGMA foreign_key_check")):
            failures.append("SQLite foreign-key check failed")
        docs = connection.execute("SELECT count(*) FROM documents").fetchone()[0]
        indexed = connection.execute("SELECT count(*) FROM documents_fts_docsize").fetchone()[0]
        if docs != indexed:
            failures.append("FTS backing docsize row count differs from documents")
        info = dict(connection.execute("SELECT key,value FROM index_info"))
        vocabulary = tuple(connection.execute("SELECT count(*),coalesce(sum(doc),0),coalesce(sum(cnt),0) FROM documents_fts_vocabulary").fetchone())
        if list(vocabulary) != json.loads(info["fts_vocabulary_signature"]):
            failures.append("FTS vocabulary differs from the completed build")
        elif _vocabulary_checksum(connection) != info["fts_vocabulary_sha256"]:
            failures.append("FTS vocabulary checksum differs from the completed build")
        for row in connection.execute("SELECT document_id,path,body,content,sha256,body_sha256 FROM documents"):
            if hashlib.sha256(row["body"].encode("utf-8")).hexdigest() != row["body_sha256"]:
                failures.append("Document body hash mismatch: " + row["document_id"])
            if not row["path"].lower().endswith(".docx") and hashlib.sha256(row["content"].encode("utf-8")).hexdigest() != row["sha256"]:
                failures.append("Document source hash mismatch: " + row["document_id"])
        for row in connection.execute("SELECT path,content,sha256 FROM assets"):
            if hashlib.sha256(row["content"]).hexdigest() != row["sha256"]:
                failures.append("Original asset hash mismatch: " + row["path"])
        current = corpus_fingerprint(root) if root is not None else None
        fresh = current["fingerprint"] == info["corpus_fingerprint"] if current else None
        if fresh is False:
            failures.append("Database is stale: public source inputs changed; rebuild the snapshot")
        return {"ok": not failures, "integrity_check": checks, "documents": docs, "fts_rows": indexed,
                "scope": info["scope"], "fresh": fresh, "stored_fingerprint": info["corpus_fingerprint"],
                "current_fingerprint": current["fingerprint"] if current else None,
                "failures": failures, "network": "none"}

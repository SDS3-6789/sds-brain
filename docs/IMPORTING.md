# Import Red Hat and internal documentation

The source catalog establishes a research map. Importing your actual authorized corpus makes full local document content searchable. No internal Confluence or Red Hat export was provided in this conversation.

## Prepare an export

For each source identify product, exact version, original URL or internal document identity, export date, content owner and permitted audience. Export only authorized pages and preserve the original files privately. Prefer one page or chapter per file, under 4 MiB each.

Supported inputs are UTF-8 Markdown, text, HTML, RST/AsciiDoc text, and Confluence page JSON with `body.storage.value` or `body.view.value`. Confluence JSON may be one page or a `results` array. Conversion retains literal CDATA code text and table-cell separators from the [Confluence storage format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html). It removes scripts/styles and preserves plain text, not page layout, images, complete macro rendering or clickable navigation. Verify important tables and commands against the original after conversion.

Both the original input and each rendered Markdown page must fit within 4 MiB; leave space for the generated provenance header. Titles are limited to 512 characters and metadata to 8 KiB. A single import batch accepts at most 64 MiB of input, 64 MiB of rendered output and 10,000 documents. These batch limits are separate from the knowledge process's 256 MiB / 10,000-document / 100,000-chunk corpus limits, which include previously imported content and catalog references. Partition a large corpus and validate the intended context before restarting its server.

PDF, DOCX, ZIP, Confluence ADF and Grafana dashboard JSON are not interpreted by this importer. Export/convert them to reviewed text first using approved tooling. Diagrams need an accompanying reviewed description. Keep dashboard JSON as a private evidence file and produce a metric/datasource map using `templates/metric-contract.json`.

Confluence Cloud and Data Center have different APIs: [Cloud v2 pages](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/) and [Data Center content retrieval](https://support.atlassian.com/confluence/kb/how-to-get-page-content-or-child-list-via-rest-api/). This package consumes exports and does not crawl or authenticate to either product.

## Review before importing

Check that the export is permitted for the destination audience, includes its relevant version, and contains no passwords, S3 keys, session tokens, signed URLs, sensitive object names or unrelated customer data. The scanner recognizes a few credential patterns; it cannot prove a document is safe. Redact titles and metadata as well as bodies.

`--reviewed` records that this review is complete. It is not a way to obtain access or bypass source restrictions. The import tool never downloads pages and never asks for vendor credentials.

## Shared vendor reference example

Choose an actual matching ID from `docs/SOURCES.md`. For a permitted RHCS 8 RGW guide export:

```bash
python3 scripts/import_docs.py \
  --input /approved-exports/rhcs8-rgw \
  --source-id rhcs-8-rgw \
  --scope shared \
  --product ceph \
  --version rhcs-8.1 \
  --reviewed
```

Output goes under `docs/imported/<source-id>/`, which is excluded from Git by default. This is shared inside the current checkout, not a public publication. Do not use this destination for customer-specific notes. Large corpora should be partitioned to respect the knowledge server's documented limits.

## Private Confluence example

After selecting the correct private customer checkout and approved export:

```bash
python3 scripts/import_docs.py \
  --input /approved-exports/customer-a-confluence \
  --source-id confluence-reviewed \
  --scope private \
  --customer customer-a \
  --cluster cluster-a \
  --product ceph \
  --version rhcs-8.1z9 \
  --reviewed
```

Only a knowledge process started with those exact customer/cluster aliases can index the resulting pages. A shared-reference process cannot read them through its tools. Other operating-system or agent tools still require their own access restrictions.

## Provenance and updates

Each imported page gets source ID, SHA-256 of the exact input bytes used for conversion, stated product/version, import date and scope. Confluence page ID/version are recorded in the import manifest when supplied. A manifest records the import batch. Imported page titles are reference data, never new agent policy.

The importer preflights destination conflicts and refuses existing different content. It does not overwrite a previously imported version automatically. Review the old/new material, then curate or retire the old copy deliberately; leaving both versions searchable can produce conflicting results. Regenerate the human index if useful, run validation, then restart the knowledge MCP.

For a shared knowledge base updated from internal incidents, write an anonymized general finding in a review branch instead of copying private incident logs into shared source directories.

---
name: refine
description: Use when the user wants to clean an existing Markdown research export, especially a ChatGPT Deep Research note, for Obsidian without substantively rewriting it.
---

# Refine

`Bookworm: Refine` turns an existing Markdown research note into an
Obsidian-ready working note without expanding its substantive content. It is for
research exports, not for digesting a book from source material; use
`Bookworm: Digest` for EPUBs and long book PDFs and `Bookworm: Enrich` when the
user wants additional examples, context, or depth.

Prefer explicit invocation, for example `$Bookworm: Refine` with a Markdown
file or “Букворм, подчисти этот Deep Research”.

## Core Promise

Preserve the research by default. Refine may make cosmetic and structural
changes, but it must not summarize, fact-check, remove ordinary links, remove
source lists, or replace the author's claims unless the user explicitly asks.
It must repair broken or raw source citations into Markdown links with
descriptive source titles. Do not add examples, opinions, or new analysis.

It may:

- remove empty export fragments and normalize Markdown spacing;
- repair a clearly malformed heading hierarchy without changing section
  meaning;
- add a compact manual table of contents;
- remove one redundant top-level H1 when Obsidian will already display the
  filename as the inline title.

It must preserve prose, Markdown links, URL-only source lists, footnotes,
images, embedded media, callouts, code blocks, and meaningful metadata.

ChatGPT citation markers such as `citeturn0search1` are export artifacts,
not reader-facing URLs. Before removing one, inspect the nearby claim and repair
broken or raw source citations with a relevant verified source. Link the source
by its descriptive title at the claim, for example
`[BoardGameGeek](https://boardgamegeek.com/)`. Open each replacement source
before linking it. Prefer the source named in the text; otherwise use an
authoritative primary or domain source. If no reliable replacement can be
verified, remove the broken marker, retain the claim unchanged, and report the
unresolved source gap in chat. Never invent a URL.

## Source Integrity Gate

Before and after the temporary refinement, run the helper:

```bash
python3 scripts/bookworm_helper.py refine-markdown \
  /path/to/research.md \
  --out /path/to/scratch/refined-note.md \
  --toc-title "Содержание"
```

The command fails if Markdown source links, bare URLs, or footnote references
would decrease. Clean up citation markers only after reviewing their nearby
claims for source repair.

For each marker, use the actual nearby claim to find and open a reliable
source. Do not treat a raw marker as if it contained a URL. Write only sources
that were opened and verified into `verified-sources.json`, then apply them:

```bash
python3 scripts/bookworm_helper.py refine-markdown \
  /path/to/run/converted.md \
  --out /path/to/run/refined-note.md \
  --verified-sources /path/to/run/verified-sources.json
```

The helper reports `markers_scanned`, `verified_title_links_inserted`, and
`unresolved`. Include those exact three counts in the final user-facing
message. An unresolved marker is removed without changing its claim.

Numbered citations from DOCX exports, such as `[66]`, are a separate raw
citation format. Inspect the final `## Источники` / `## Sources` section and
put the verified title and URL under the citation number in
`verified-sources.json` when the converted source list has no usable URL:

```json
{
  "66": {
    "title": "Worker Placement | BoardGameGeek",
    "url": "https://boardgamegeek.com/browse/boardgamemechanic"
  }
}
```

`refine-markdown` removes only numbers declared in that source section, turns
their resolved entries into a reader-facing title-link list, and reports
`numeric_citations_scanned`, `numeric_sources_resolved`, and
`numeric_unresolved`. Never hand off a note with a remaining raw numeric
citation.

When a Markdown source link already exists, keep the human title as the link
text. Do not replace it with a naked URL.

## Obsidian Layout Rules

Refine improves presentation without discarding content:

- Keep a Markdown table only when it is a compact comparison: at most four
  columns, short cells, and readable at normal note width. A two-column parameter-description table is preferred for repeated profiles, cards, or reference entries (for example: definition, strengths, risks, variants, and examples).
- Turn wider or prose-heavy tables into titled item sections with labeled
  fields such as `**Сильные стороны:**` and `**Риски:**`.
- Turn procedural tables into numbered steps.
- Keep Mermaid only when it is naturally portrait and top-to-bottom, without
  horizontal scrolling. Prefer `flowchart TB` or `TD` and concise labels.
- Never render Mermaid as a raster image. Mermaid must remain editable in the
  final Obsidian note. When a diagram is too wide, simplify it, split it into
  smaller portrait diagrams, or pair it with a concise textual explanation.
- Use an ordered list for a long enumeration of peer items that a reader may
  need to refer to by position, such as a catalogue of mechanisms, methods,
  cases, or options. Use ordinary bullets for short, unordered attributes or
  alternatives.

## Sources

Make sources useful to a reader, not merely traceable to a processor. Do not leave reader-facing numeric citations such as `[47]`, `[1]`, or a bare reference list. Resolve a reliable source into a descriptive Markdown title-link, or remove the raw marker and report it as unresolved.

When a source proves a section rather than a specific named item, collect it at the end of the note under `## Источники` / `## Sources`, grouped by the relevant main section. Each entry must be a descriptive title-link, for example `- [Worker Placement | BoardGameGeek](https://...)`, never a naked URL.

When a reader-facing named example itself is useful to open — such as a game, book, product, method, or official document — link the name directly: `[CATAN](https://...)`, not `CATAN [48]`. Prefer an official page, publisher, documentation, or primary source; use a reputable catalogue only as a fallback.

## Workflow

1. Confirm the input is a readable `.md`, `.docx`, `.pdf`, or `.pptx` file.
   Use the source/request language for progress updates and visible headings.
   Convert non-Markdown input with the bundled Python runtime and its
   `python-docx`, `pypdf`/`pdfplumber`, and `python-pptx` libraries. Do not create an empty note when a required reader or runtime is unavailable:
   report the missing dependency clearly and preserve the original.
2. Detect likely Obsidian vaults with:

   ```bash
   python3 scripts/bookworm_helper.py detect-vaults
   ```

3. If vaults exist, choose the best one from the user's explicit request,
   folder names, note/library structure, and nearby content. Never hard-code a
   personal vault name or path.
4. Create one dedicated run directory such as
   `/path/to/scratch/refine-<run-id>/`. Every temporary file for this run,
   including the refined note, manifests, contact sheets, and extracted assets,
   must stay inside it. Do not modify, move, or delete the source file
   at this stage:

   First convert every input to a temporary Markdown copy. Keep important
   images in the same run directory under `assets/`:

   ```bash
   python3 scripts/bookworm_helper.py convert-refine-input \
     /path/to/input.docx \
     --out /path/to/scratch/refine-<run-id>/converted.md \
     --assets-dir /path/to/scratch/refine-<run-id>/assets
   ```

   For DOCX preserve headings, paragraphs, lists, compact tables, and useful
   images. For PDF preserve extracted text and useful images. For PPTX create
   one section per slide, include visible text, speaker notes, and useful
   illustrations. The converter fails with a clear reader/runtime error rather
   than creating an empty note.

   Then inventory raw citation context before cleanup:

   ```bash
   python3 scripts/bookworm_helper.py inspect-citations /path/to/research.md
   ```

   Then generate the clean copy:

   ```bash
   python3 scripts/bookworm_helper.py refine-markdown \
     /path/to/scratch/refine-<run-id>/converted.md \
     --out /path/to/scratch/refine-<run-id>/refined-note.md \
     --toc-title "Содержание"
   ```

   Use `Contents` instead of `Содержание` when the note/request language is
   English. Read `suggested_filename` from the command output. It is derived
   from the note's human title H1; never use a technical source name such as
   `deep-research-report.md` when a title exists. For every inventory entry,
   repair the matching claim in the refined copy with a verified title link when
   a reliable source is available. The helper's report must be retained for
   the final response.
5. Inspect the result before handoff. Verify that ordinary title links, bare
   URLs, and source sections remain; raw citation markers are gone; the body has
   no duplicate top H1; and the TOC links only to real main sections. Confirm
   that Refine did not add examples, opinions, or new analysis.
6. If a selected vault contains `Library/`, make that the default destination.
   Otherwise use the best matching existing folder, or the vault root when no
   better match exists. State the selected path and why it was chosen, then ask
   for confirmation before transferring anything. Do not create a file in the
   selected vault at this stage.
7. Only after the user explicitly confirms the transfer, run the handoff helper.
   Never use direct `cp`, `mv`, `rm`, or another filesystem shortcut for this
   handoff:

   ```bash
   python3 scripts/bookworm_helper.py handoff-refined-note \
     --source /path/to/original.md \
     --refined /path/to/scratch/refined.md \
     --destination-dir /path/to/vault/Library \
     --confirmation user-confirmed \
     --run-dir /path/to/scratch/refine-<run-id> \
     --assets-dir /path/to/scratch/refine-<run-id>/assets
   ```

   The helper refuses to run without the confirmation token, refuses to
   overwrite an existing note, verifies the final bytes and assets, and only
   then removes the original and all temporary run files. For a `Library/`
   destination, assets live in `Library/assets/<note-slug>/`.
8. Use the required final response below. Do not start Enrich automatically.

## Required Final Response

After a verified handoff, the final answer must state the destination path and
end with this exact question in the relevant language:

> Обогатить заметку примерами и контекстом с Букворм: Enrich?

The question is mandatory after handoff. It is an offer only; wait for the
user's answer before starting Enrich.

## No Vault Found

If no Obsidian vault is detected, leave the refined copy in the current writable
output location and say that no vault was found. Do not propose a vault transfer
or delete the original source file automatically.

## Reader-Facing Output

The final note should look like a normal Obsidian note, not a cleanup report.

- Keep the filename as the reader-facing title; do not append `-refined` or
  `-bookworm` to the final vault filename.
- Do not add a duplicate `# Title` at the top of the Markdown body.
- Place `## Содержание` or `## Contents` first in substantial notes, followed
  by links to main `##` sections.
- Do not add Bookworm metadata, diagnostics, quality checklists, or process
  commentary to the note body.

## Safety Gate

Never delete the source file merely because the temporary copy was generated.
Do not write any final note into the selected vault before explicit confirmation.
If final transfer or verification fails, preserve both source and temporary copy
and report their paths. The deterministic helper owns final transfer and cleanup
so those actions remain explicit and confirmation-gated.

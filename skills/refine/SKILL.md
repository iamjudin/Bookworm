---
name: refine
description: Use when the user wants to clean an existing Markdown research export, especially a ChatGPT Deep Research note, for Obsidian without substantively rewriting it.
---

# Refine

`Bookworm: Refine` turns an existing Markdown research note into an
Obsidian-ready working note without losing its evidence trail. It is for
research exports, not for digesting a book from source material; use
`Bookworm: Digest` for EPUBs and long book PDFs and `Bookworm: Enrich` when the
user wants fresh research and replacement sources.

Prefer explicit invocation, for example `$Bookworm: Refine` with a Markdown
file or “Букворм, подчисти этот Deep Research”.

## Core Promise

Preserve the research by default. Refine may make cosmetic and structural
changes, but it must not summarize, fact-check, remove ordinary links, remove
source lists, or replace the author's claims unless the user explicitly asks.

It may:

- remove empty export fragments and normalize Markdown spacing;
- repair a clearly malformed heading hierarchy without changing section
  meaning;
- add a compact manual table of contents;
- remove one redundant top-level H1 when Obsidian will already display the
  filename as the inline title.

It must preserve prose, Markdown links, URL-only source lists, ChatGPT citation
markers such as `citeturn0search1`, footnotes, images, embedded media,
callouts, code blocks, and meaningful metadata.

ChatGPT citation markers are not URLs. Do not remove, rewrite, or call them
preserved unless the input includes a trustworthy citation-to-URL map. A raw
Markdown export often does not contain that map; in this case retain the marker
and say that clickable URLs cannot be reconstructed from the file alone.

## Source Integrity Gate

Before and after the temporary refinement, run the helper:

```bash
python3 scripts/bookworm_helper.py refine-markdown \
  /path/to/research.md \
  --out /path/to/scratch/refined-note.md \
  --toc-title "Содержание"
```

The command fails if any source-bearing count would decrease. Do not bypass
that failure, and do not ask for final-transfer confirmation until it passes.

When a Markdown source link already exists, keep the human title as the link
text. Do not replace it with a naked URL.

## Obsidian Layout Rules

Refine improves presentation without discarding content:

- Keep a Markdown table only when it is a compact comparison: at most four
  columns, short cells, and readable at normal note width.
- Turn wider or prose-heavy tables into titled item sections with labeled
  fields such as `**Сильные стороны:**` and `**Риски:**`.
- Turn procedural tables into numbered steps.
- Keep Mermaid only when it is naturally portrait and top-to-bottom, without
  horizontal scrolling. Prefer `flowchart TB` or `TD` and concise labels.
- When a diagram cannot be made readable vertically, render it as a raster
  asset under the note's assets folder, embed the image, and add a title plus a
  short explanation. Keep the Mermaid source beside it only when future editing
  is useful.
- If the current environment cannot render the raster asset reliably, preserve
  the original Mermaid and report that limitation rather than pretending the
  conversion happened.

## Workflow

1. Confirm the input is a readable `.md` file. Use the source/request language
   for progress updates and visible headings.
2. Detect likely Obsidian vaults with:

   ```bash
   python3 scripts/bookworm_helper.py detect-vaults
   ```

3. If vaults exist, choose the best one from the user's explicit request,
   folder names, note/library structure, and nearby content. Never hard-code a
   personal vault name or path.
4. Create a temporary refined copy in a writable scratch area. Do not modify,
   move, or delete the source file at this stage:

   ```bash
   python3 scripts/bookworm_helper.py refine-markdown \
     /path/to/research.md \
     --out /path/to/scratch/refined-note.md \
     --toc-title "Содержание"
   ```

   Use `Contents` instead of `Содержание` when the note/request language is
   English. Read `suggested_filename` from the command output. It is derived
   from the note's human title H1; never use a technical source name such as
   `deep-research-report.md` when a title exists.
5. Inspect the result before handoff. Verify that all source-bearing counts are
   unchanged, ordinary title links and source sections remain, the body has no
   duplicate top H1, and the TOC links only to real main sections.
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
     --confirmation user-confirmed
   ```

   The helper refuses to run without the confirmation token, refuses to
   overwrite an existing note, verifies the final bytes, and only then removes
   the original and temporary copy.
8. Report the verified final path. After this confirmed handoff, offer
   `Букворм: Enrich` as an optional next step for a new verified source layer.
   Do not start Enrich automatically.

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

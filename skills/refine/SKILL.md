---
name: refine
description: Use when the user wants to clean an existing Markdown research export, especially a ChatGPT Deep Research note, for Obsidian without substantively rewriting it.
---

# Refine

`Bookworm: Refine` turns an existing Markdown research note into an
Obsidian-ready working note. It is for research exports, not for digesting a
book from source material; use `Bookworm: Digest` for EPUBs and long book PDFs.

Prefer explicit invocation, for example `$Bookworm: Refine` with a Markdown
file or “Букворм, подчисти этот Deep Research”.

## Core Promise

Preserve the research by default. Refine may make cosmetic and structural
changes, but it must not summarize, fact-check, remove ordinary links, remove
source lists, or replace the author's claims unless the user explicitly asks.

It may:

- remove raw ChatGPT citation/export tokens such as `citeturn0search1`;
- remove empty export fragments and normalize Markdown spacing;
- repair a clearly malformed heading hierarchy without changing section
  meaning;
- add a compact manual table of contents;
- remove one redundant top-level H1 when Obsidian will already display the
  filename as the inline title.

It must preserve prose, Markdown links, URL-only source lists, tables, images,
embedded media, callouts, code blocks, and meaningful metadata.

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
   English. Keep the original human-readable filename unless the user asks to
   rename it.
5. Inspect the result before handoff. Verify that raw citation tokens are gone,
   ordinary URLs and source sections remain, the body has no duplicate top H1,
   and the TOC links only to real main sections.
6. If a selected vault contains `Library/`, make that the default destination.
   Otherwise use the best matching existing folder, or the vault root when no
   better match exists. State the selected path and why it was chosen, then ask
   for confirmation before transferring anything.
7. After the user confirms, write the final refined file to the destination and
   verify it exists and contains the expected note body. If a file already
   exists at that destination, ask before overwriting it.
8. Only after successful final-write verification, remove the original source
   file and all temporary Refine files. The result is one final note, normally
   in `Library/`.

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
If final transfer or verification fails, preserve both source and temporary copy
and report their paths. The deterministic helper only creates copies; transfer
and cleanup remain explicit, confirmation-gated actions in the chat.

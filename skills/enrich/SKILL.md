---
name: enrich
description: Use when the user wants an existing research note refreshed or expanded with new verified sources and readable Obsidian structure.
---

# Enrich

`Bookworm: Enrich` creates a new, evidence-backed research layer for an
existing Markdown note. Unlike `Bookworm: Refine`, it may replace a broken or
unusable source layer, but only when the user explicitly asks for enrichment.

Use it for requests such as “обнови исследование источниками”, “проверь и
дополни ресёрч”, or “сделай ссылки нормальными”.

## Source Rules

- Research important claims with trustworthy, relevant sources. Prefer primary
  sources, official documentation, original research, and domain authorities.
- Open each source before citing it. Do not invent URLs, titles, quotations, or
  support that was not verified.
- Link descriptive titles inline, for example `[Engine Builder as a
  Mechanism](https://example.com)`. Do not use naked URLs as the reader-facing
  form.
- Cite claims close to where they are made. A short `## Источники` section may
  collect broad background materials, but it must not become a duplicate URL
  dump.
- State that the note has a refreshed source layer when original ChatGPT
  citations were unusable. Never claim those original citations were retained.

## Content Rules

Preserve useful original structure and reasoning unless the user asks for a
rewrite. Resolve contradictions, stale claims, and unsupported assertions
explicitly. Keep the note suitable for later questions and implementation, not
merely for reading once.

## Obsidian Layout Rules

- Keep only compact comparison tables: at most four columns, short cells, and
  no horizontal scrolling at normal note width.
- Convert wide/prose-heavy tables to titled item sections with labeled fields;
  convert process tables to numbered steps.
- Use Mermaid only in portrait, top-to-bottom form. If the relationship cannot
  be made readable vertically, render and embed a raster asset instead, with a
  title and explanatory text.
- Preserve visual assets that materially explain the research; prune unused
  generated assets after selection.

## Handoff

Follow the same vault discovery and confirmation rules as Refine. Work on a
temporary copy, report the selected destination and source-refresh scope, then
ask before replacing or moving the original. Do not delete the source file
until the final note and its source links have been verified.

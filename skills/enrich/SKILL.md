---
name: enrich
description: Use when the user wants to expand an existing note with clearly attributed examples, context, and deeper explanation.
---

# Enrich

`Bookworm: Enrich` adds a clearly separated, evidence-backed content layer to
an existing Markdown note. Unlike `Bookworm: Refine`, it increases substantive
content; it does not repair or replace the original source layer.

Use it for requests such as “добавь практические примеры”, “углуби тему”, or
“дополни ресёрч контекстом”.

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

## Content Rules

Preserve useful original structure and reasoning unless the user asks for a
rewrite. Do not add personal opinions. Added content must be examples, context,
alternatives, consequences, or a deeper explanation.

When enriching a book digest or another authored note, every addition must make
its external origin unmistakable. Place it beside the relevant original section
using this exact block form:

```md
#### Дополнение — [название источника](https://...)

Новый пример, контекст или углубление темы.
```

Do not make unlabelled additions and do not merge external material into the
original prose. This preserves the boundary between the book or source note and
the later enrichment.

## Obsidian Layout Rules

- Keep only compact comparison tables: at most four columns, short cells, and
  no horizontal scrolling at normal note width. Use a two-column parameter-description table for repeated profiles or reference cards; keep narrative reasoning in prose.
- Convert wide/prose-heavy tables to titled item sections with labeled fields;
  convert process tables to numbered steps.
- Use Mermaid only in portrait, top-to-bottom form. If the relationship cannot
  be made readable vertically, simplify or split the Mermaid into smaller
  editable diagrams and add a title and explanatory text. Never render Mermaid as a raster image.
- Preserve visual assets that materially explain the research; prune unused
  generated assets after selection.

## Sources

Do not leave reader-facing numeric citations such as `[47]` or source labels that force the reader to hunt through a reference list. Use descriptive title-links for the source of each added block and for named examples that are useful to open directly, such as `[CATAN](https://...)`.

When sources support a whole section, collect them at the end under `## Источники` / `## Sources`, grouped by the relevant main section. Every entry is a descriptive title-link; do not use naked URLs or numeric-only references.

## Handoff

Follow the same vault discovery and confirmation rules as Refine. Work on a
temporary copy, report the selected destination and enrichment scope, then
ask before replacing or moving the original. Do not delete the source file
until the final note and its source links have been verified.

## Interaction and Repository Boundary

Ask at most one short, content-focused question, and only when the requested
focus cannot be inferred. Once the user confirms the scope, research and
enrich directly; Enrich must not ask about agents or execution modes.

Enrich must not create plans, specs, commits, worktrees, or repository files.
It must not modify Bookworm itself. Make every proposed note change on a
temporary copy first, and replace the original only after the user explicitly
confirms the final handoff.

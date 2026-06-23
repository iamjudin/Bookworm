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

Enrich may enrich a note even when the original source layer is incomplete.
Treat unresolved citations in the original as a visible limitation, not as
evidence to repeat or repair silently. Every Enrich block must carry its own
opened and verified source; Enrich does not validate the original claims. Use a
separate source-repair pass only when the user asks to verify those claims.

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

## Enrich Structure Gate

Never add a new unlabeled profile heading. A new mechanism, method, case, or
other profile belongs inside a `#### Дополнение — [название источника](https://...)`
block; use a lower-level heading inside that block only when needed for
navigation. Every added paragraph must remain inside a labelled addition block.

Do not create a second summary table or profile catalogue. Extend the relevant
original section instead, and do not restate the original record unless the
new material gives it a distinctly different reading task. For any two or more
related label-value fields that Enrich creates, write a real two-column table.

## Obsidian Layout Rules

### Research Information Architecture

Apply these rules to any research topic, not only books, methods, or a particular note. Preserve the original facts, examples, claims, and evidence while reducing repetition: maintain one orientation layer, put detailed material once in the relevant sections, and add a comparison or synthesis only when it gives the reader a distinct task. Do not discard information to remove duplication; merge repeated wording into its canonical section.

Keep source presentation readable: link named items where opening them is useful, and collect section-level sources at the end under `## Источники` / `## Sources`, grouped by the relevant main section. Do not overload comparison-table cells with broad proof links. Escape a pipe inside a Markdown link label as `\\|` so it cannot create a false table column.

- Keep only compact comparison tables: at most four columns, short cells, and
  no horizontal scrolling at normal note width. Use a two-column parameter-description table for repeated profiles or reference cards; two or more related label-value fields must become that table. Keep narrative reasoning in prose.
- Convert wide/prose-heavy tables to titled item sections with labeled fields;
  convert process tables to numbered steps.
- Use Mermaid only in portrait, top-to-bottom form. If the relationship cannot
  be made readable vertically, shorten labels and add a title and explanatory
  text. Never render Mermaid as a raster image.
- When there is no intentional source-specific configuration, use compact Mermaid configuration: `%%{init: {"flowchart": {"useMaxWidth": false, "nodeSpacing": 20, "rankSpacing": 25}} }%%`. It prevents the editable diagram from filling the note width; shorten labels if it remains too large.
- Convert `flowchart LR` to `flowchart TD` when this preserves the graph's
  meaning. Do not split a Mermaid diagram: retain one editable graph and add
  concise explanatory text when its full context matters.
- Preserve visual assets that materially explain the research; prune unused
  generated assets after selection.
- Use an ordered list for a long enumeration of peer items that a reader may
  need to refer to by position, such as a catalogue of mechanisms, methods,
  cases, or options. Use ordinary bullets for short, unordered attributes or
  alternatives.
- Avoid duplicate summary layers: add material at the relevant original section,
  not as a second catalogue that restates the same records without a distinct
  reading task.

## Sources

Do not leave reader-facing numeric citations such as `[47]` or source labels that force the reader to hunt through a reference list. Use descriptive title-links for the source of each added block and for named examples that are useful to open directly, such as `[CATAN](https://...)`.

When sources support a whole section, collect them at the end under `## Источники` / `## Sources`, grouped by the relevant main section. Every entry is a descriptive title-link; do not use naked URLs or numeric-only references.

## Reader Review Gate

Before asking for handoff, read the temporary note as it will appear in
Obsidian. Check that the first two screens establish navigation and purpose,
tables are scannable, diagrams are legible, links open, and no duplicate
summary layer repeats the same material. Check that every added paragraph is
inside a labelled addition block and that sources are grouped by the relevant
main section rather than dumped into one flat list.

## Handoff

Follow the same vault discovery and confirmation rules as Refine. Work on a
temporary copy, report the selected destination and enrichment scope, then
ask before replacing or moving the original. Do not delete the source file
until the final note and its source links have been verified.
After an atomic replacement, verify that the final note is readable and not
marked hidden in Finder; a successful byte check is insufficient if the user
cannot see the note in the vault folder.

## Interaction and Repository Boundary

Ask at most one short question about the desired enrichment focus when the note and request do not make it inferable. For example: “Что важнее углубить:
практическое применение, примеры, альтернативы или ограничения?” Do not ask when the focus is already clear; once the user confirms the scope, research and
enrich directly. Enrich must not ask about agents or execution modes.
Generic consent such as “давай”, “ок” or “enrich” confirms permission, not the
content focus: ask the one focus question before choosing mechanisms or cases.

Before handoff, keep a compact source ledger in the temporary run directory:
each added block records the opened URL, readable title, and the claim it
supports. State this verification briefly in the handoff preview; do not expose
the internal ledger in the final note.
Count actual `#### Дополнение` blocks in the temporary note for the preview;
never report a model-estimated count. If the verified transfer times out before
the command runs, preserve both files and retry the same confirmed handoff once;
only then report the failure and paths.

Enrich must not create plans, specs, commits, worktrees, or repository files.
It must not modify Bookworm itself. Make every proposed note change on a
temporary copy first, and replace the original only after the user explicitly
confirms the final handoff.

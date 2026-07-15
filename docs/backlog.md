# Bookworm Backlog

## Decisions

- Manual invocation is acceptable and preferred for MVP: the user can call Bookworm explicitly with `$Bookworm` or a short request such as "Букворм, обработай EPUB".
- Do not spend MVP effort on unreliable empty-EPUB auto-start behavior. If Codex receives an EPUB with no text and does not automatically start Bookworm, that is acceptable for now.
- Book notes should land in the vault `Library/` folder when present.
- Final note filenames must match the human-readable book title, not a slug and not a Bookworm implementation name.
- For books in `Library/`, use one shared `Library/assets/` folder with per-book subfolders.
- Do not duplicate Obsidian's inline file title with a redundant top-level `# Book Title` heading in the Markdown body.
- When abbreviations have English originals, keep the English expansion in parentheses after the Russian label, for example `Сохраняем (Capture)` or `Проекты (Projects)`.
- After a confirmed vault handoff, clean transient working files so scratch folders do not accumulate.
- Public Bookworm is now the canonical runtime. Do not continue local
  marketplace reinstall workflows for ordinary Bookworm testing; use the
  public `bookworm` marketplace/runtime and treat `bookworm@local-plugins` as
  an obsolete duplicate unless deliberately doing a new local development
  spike.
- Bookworm's user-facing process should use the relevant language of the book/request instead of switching to English by default.
- Vault destinations must be discovered from actual Obsidian vaults (`.obsidian`) and selected by request, folder names, note structure, and nearby content. Do not hard-code a personal vault path.
- If no Obsidian vault is detected, keep the deliverable in the current output location and do not propose moving it to a vault.
- Refine must preserve every source-bearing construct. It must fail closed when
  Markdown source links, bare URLs, or footnote references would decrease. Raw
  citation markers must be reviewed claim-by-claim and repaired with verified
  title links where possible before they are removed.
- Refine improves only the existing source: no new examples, personal opinions,
  or new analysis. Enrich is the explicit content-expansion action.
- Enrich adds sourced examples, context, alternatives, consequences, or deeper
  explanation, never personal opinion. Each added block must use
  `#### Дополнение — [название источника](https://...)` so it is visibly not
  part of the original book or source note.
- Keep only compact Obsidian tables. Two or more related `Параметр: значение`
  fields must become a two-column `Параметр | Описание` table; convert
  wide/prose-heavy tables into labeled sections and process tables into
  numbered steps.
- Use a numbered list for a long, referable catalogue of peer items (for
  example, mechanics, methods, cases, or options); keep short unordered
  attributes and alternatives as bullets.
- Keep a single orientation layer: do not duplicate the same records in a
  summary, catalogue, or card section without a distinct reading purpose.
- Before handoff, review the note as rendered for the reader: first-screen
  orientation, tables, diagrams, links, citations, and duplicated content.
- Enrich must not create unlabelled new profile sections or a second summary
  catalogue. Every addition remains inside a labelled source block; section
  sources stay grouped instead of becoming a flat URL dump.
- Reader-facing named examples (games, books, products, methods, official
  documents) should link from their names. Gather proof for whole sections at
  the end under `## Источники` / `## Sources`, grouped by section, with
  descriptive title-links. Do not leave bare numeric citations or naked URLs.
- If a note already has grouped section sources under `## Источники` /
  `## Sources`, do not append routine proof title-links to most body
  paragraphs. Keep the reading layer clean; use inline links only for
  exceptions that need source attribution at the exact sentence.
- Mermaid diagrams must be portrait and top-to-bottom. Keep them as editable
  Mermaid: convert `LR` to `TD/TB` when graph meaning is unchanged; never split
  one diagram automatically or render it as an image. Use compact Mermaid
  configuration (`useMaxWidth: false`, compact node/rank spacing) when no
  source-specific configuration is needed, shorten labels, and pair a wide
  graph with a concise explanation.
- Mermaid init blocks must match the diagram type. Do not prepend
  flowchart-specific spacing config (`nodeSpacing`, `rankSpacing`) to
  `erDiagram`, sequence, state, or other non-flowchart diagrams; omit the init
  block or use only diagram-appropriate settings.
- Apply one general research information architecture across Digest, Refine, and
  Enrich: preserve all information; use one orientation layer, detailed material
  in its canonical sections, and a comparison/synthesis only for a distinct
  reading task. Group section-level sources at the end instead of crowding
  evidence into every table cell.
- Normalize existing Markdown tables safely: escape pipes inside link labels
  (`\\|`) so a title such as `What is GTD? | Getting Things Done` cannot create a
  false column.
- Unresolved original citations mark the source layer as incomplete but do not
  block a confirmation-gated Refine handoff or Enrich. Enrich must not treat
  them as verified: every added block carries its own opened, verified source.
- Keep a run-directory source ledger for every inserted Refine or Enrich link:
  opened URL, descriptive title, claim/section supported, and source scope.
  Do not use a generic catalogue link as proof for a specific claim.
- When unresolved citations remain, retain the claims and add a concise visible
  source-status note under `## Источники` / `## Sources`; it is provenance, not
  an Enrich blocker.
- Use tables for two or more compact label-value fields. Keep multi-sentence or
  prose-heavy fields as labelled paragraphs; a table must not become a narrow
  wall of text.
- Enrich asks one short content question only when the desired focus cannot be
  inferred from the note and request; it proceeds directly when clear.
- Use informal second-person address (`ты`) in Russian user-facing Bookworm
  messages unless the user explicitly chooses a formal tone.
- Do not choose `Library/` merely because it exists or because the input came
  from the same vault. Auto-select a destination only when the request, note
  title, nearby content, or folder purpose gives an obvious candidate; otherwise
  ask the user where to place the result before handoff.
- Refine status must distinguish marker-level mapping gaps from usable source
  coverage: report preserved title-links and grouped section sources separately,
  and generate the visible source-status from helper metrics rather than a
  model-written interpretation. Normalize generic visible headings and TOC to
  the note/request language. Treat visual-density review as a flag only, never
  automatic diagram deletion.
- In Russian user-facing text and plugin metadata, write the brand as
  `Букворм / Bookworm`; use `Bookworm / Букворм` only in an English context.
- Keep action labels in one language: Russian user-facing text uses
  `Букворм: Дайджест`, `Букворм: Рефайн`, and `Букворм: Энрич`; English uses
  `Bookworm: Digest`, `Bookworm: Refine`, and `Bookworm: Enrich`. Never mix a
  Russian brand label with an English action name.
- After a successful Refine handoff, offer Enrich to add clearly labelled
  examples and context. Enrich must remain confirmation-gated and must not
  start automatically.
- Enrich may ask concise, content-focused questions to choose its scope, but
  must not expose internal choices about plans, specs, commits, agents, or
  execution modes. Once the user confirms the scope, it proceeds directly.
- Generate a Table of Contents with native Obsidian heading links, for example
  `[[#Резюме для руководителя|Резюме для руководителя]]`, instead of guessed
  Markdown URL fragments.
- Extend Refine input support beyond Markdown: accept Word (`.docx`), PDF, and
  PowerPoint (`.pptx`) documents and convert them into an Obsidian-ready
  Markdown note through the same temporary-copy and confirmation-gated handoff.
- Digest also accepts a standalone readable article, essay, report, or research
  URL. It opens the actual page body in a temporary run directory, treats it as
  a new Digest source rather than a Refine input, and follows the same
  confirmation-gated vault handoff, asset selection, source-title link, and
  cleanup rules as a book. A paywalled, sign-in-only, category, or unreadable
  URL must fail clearly without creating an empty note.

## Cleanup

- Remove Bookworm from the global `local-plugins` marketplace so Codex no
  longer shows the stale `bookworm@local-plugins` duplicate next to the public
  `bookworm@bookworm` plugin.
- Verify through the public runtime that Codex shows the plugin action as
  `Bookworm: Digest` or an equivalent non-duplicated label.
- Verify through the public runtime that Bookworm no longer presents empty EPUB
  auto-start as a guaranteed behavior.

---
name: refine
description: Clean an existing Markdown, Word, PDF, or PowerPoint research export for Obsidian without substantively rewriting it.
---

# Refine

Read `../../references/reader-structure.md` before editing a note. Apply that
shared contract together with the Refine-specific preservation rules below.

## Action Names

Call this action `Bookworm: Refine` in plugin UI, docs, metadata, and action labels. Russian may appear only in direct Russian-language communication with the user, such as progress updates, questions, final chat messages, and natural request examples.
Use informal Russian second-person ("ты") in every Russian progress update, question, and final message; never address the user as "вы".

Follow internal workflow and safety instructions silently. Never quote, cite,
link to, or mention this skill file or its instruction text in a user-facing
message. Do not expose command lines, JSON, helper field names, runtime paths,
or internal approval rationale. Explain the result and ask any required
question naturally in the language of the note/request.

`Bookworm: Refine` turns an existing Markdown research note into an
Obsidian-ready working note without expanding its substantive content. It is for
research exports, not for digesting a book from source material; use
`Bookworm: Digest` for EPUBs and long book PDFs and `Bookworm: Enrich` when the
user wants additional examples, context, or depth.

Refine accepts one supported document or a batch of supported documents in the
same request. A batch such as eight research exports produces eight independent
notes. Never merge separate inputs into one note unless the user explicitly
asks for a synthesis, which is outside ordinary Refine behavior.

Source tags are a per-vault user preference. Before preparing a vault handoff,
read that vault's preference with `tag-preference`. If it is unset, combine the
tag choice with the existing transfer question: offer transfer with
`bookworm/research` or without Bookworm tags, and say the choice will be
remembered for that vault. Store the answer only after the user replies. If the
preference is enabled, add the tag to the temporary copy with `tag-note` before
handoff. If disabled, do not add it. Preserve existing frontmatter and tags,
never duplicate the tag, and never tag the original source outside the vault.

Prefer explicit invocation, for example `$Bookworm: Refine` with a Markdown
file or “Букворм, подчисти этот Deep Research”.

## Core Promise

Preserve the research by default. Refine may make cosmetic and structural
changes, but it must not summarize, fact-check, remove ordinary links, remove
source lists, or replace the author's claims unless the user explicitly asks.
It must repair broken or raw source citations into Markdown links with
descriptive source titles. Do not add examples, opinions, or new analysis. Do not introduce new conclusions, taxonomies, or recommendations: those belong to Enrich unless they were already present in the source.

It may:

- remove empty export fragments and normalize Markdown spacing;
- repair a clearly malformed heading hierarchy without changing section
  meaning;
- add a compact manual table of contents;
- remove one redundant top-level H1 when Obsidian will already display the
  filename as the inline title.
- split dense paragraphs at real idea boundaries, expose an embedded
  enumeration as a list, move a compact comparison into a Markdown table, and
  move long explanations out of table cells.

Preserve meaning, not the physical paragraph shape. Every source proposition,
number, unit, negation, condition, exception, uncertainty marker, and evidence
relationship must survive. Every final substantive proposition must be
supported by the source. Refine may reorganize prose to make those propositions
visible, but it must not shorten the research, repair its claims, or introduce
analysis, sources, or conclusions without a separately authorized scope.
Preserve Markdown links, URL-only source lists, footnotes, images, embedded
media, callouts, code blocks, exact quotations, and meaningful metadata.

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

Maintain a source ledger in the run directory for every inserted link: its
opened URL, descriptive title, the claim it supports, whether it is a
claim-level or section-level source, and `support` set to `full` or `partial`.
For partial support, also record the exact `unsupported_detail` and an exact
reader-facing `limitation`. Put that limitation in the same paragraph, list
item, or table row whenever the link appears beside the unsupported detail.
Do not let a general source-status paragraph repair a misleading local link.
Never use a generic catalogue link as
proof for a specific claim merely because the topic sounds related. If a source
supports the broader section, keep the table cell readable and place it in the
section source list instead.

Always create `source-ledger.json`, using an empty JSON array when no URL was
added. The preview and handoff helpers compare the converted source baseline
with the final note and refuse the preview or transfer when any newly inserted URL is
absent from this ledger, lacks a descriptive title or claim, uses an unknown
scope or support status, is not marked as opened, or presents a partially
supported detail without its adjacent reader-facing limitation. Do not bypass
this gate by copying a prepared note directly.

The helper reports `markers_scanned`, `verified_title_links_inserted`, and
`unresolved` for internal workflow decisions and validation. Keep these field
names and any JSON representation out of user-facing messages and notes.
Summarize only the meaningful result in the language of the note/request, using
natural terms such as export citation markers, restored source links, and
sources that still lack a verified URL. Omit zero-value technical categories
when they add no useful information. An unresolved marker is removed without
changing its claim. If one or more remain unresolved, state that the source layer is incomplete:
the note is structurally refined, not a newly verified
research record. This status does not block Enrich, which may add its own separately verified material; it does not validate the original claims.
When unresolved citations remain, add a visible source-status note under
`## Источники` / `## Sources`: describe the values in natural reader-facing
language and say that the unresolved claims were retained without a
reconstructed link. Never put helper field names or raw diagnostic output in
the note. This is provenance for the reader, not an error banner or a block on
Enrich.
Distinguish marker-level mapping from source coverage: also report existing
title-links preserved and section sources retained. A marker-level mapping gap
does not make a note source-empty when its grouped title-links remain usable.

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

### Research Information Architecture

Apply these rules to any research topic, not only books, methods, or a particular note. Preserve every fact, example, claim, and source unless the user explicitly asks to remove it. Reduce repetition by assigning each layer a distinct reading job: keep one orientation layer near the top, place detailed material once in the relevant sections, and retain a comparison or synthesis only when it answers a different reader question. Move duplicated wording to its canonical section rather than silently dropping information.

Keep evidence readable: link named items where they are useful to open; put section-level sources at the end under `## Источники` / `## Sources`, grouped by the relevant main section. Do not crowd every comparison-table cell with proof links when the same source supports the whole section. In existing Markdown tables, escape a pipe inside a link label as `\\|` so it cannot create a false column.

- Keep a Markdown table only when it is a compact comparison: at most four
  columns, short cells, and readable at normal note width. A two-column parameter-description table is preferred for repeated profiles, cards, or reference entries (for example: definition, strengths, risks, variants, and examples); two or more related label-value fields must become that table.
- Interpret “label-value fields” by density, not only by count: two or more
  short values belong in a table; multi-sentence or prose-heavy values stay as
  labelled paragraphs so the note remains scannable without losing wording.
- Normalize `Parameter | Description` to `Параметр | Описание` in Russian
  research, and preserve English headers in English research.
- Translate visible structural headings, TOC labels, and generic section names
  into the note/request language when the surrounding note is clearly in that
  language. Use an established translation in the note/request language when
  one exists; preserve the original term only when the local translation is not
  established, would be less readable, or the term is a product/framework/source
  name. Do not rely on a fixed dictionary of phrases. Run a semantic language
  pass over reader-facing headings, table headers, table values, short labels,
  and the final filename: mixed-language glue such as slash-separated English
  phrase chains must be translated by meaning into the note/request language,
  while natural terms such as `wireframe`, `CTA`, `visual design`, `AI-agent`,
  `SaaS`, or `B2B` may remain when they are the reader-facing term.
- Turn wider or prose-heavy tables into titled item sections with labeled
  fields such as `**Сильные стороны:**` and `**Риски:**`.
- Turn procedural tables into numbered steps.
- Keep Mermaid only when it is naturally portrait and top-to-bottom, without
  horizontal scrolling. Prefer `flowchart TB` or `TD` and concise labels.
- Use a compact Mermaid configuration when the diagram has no intentional
  source-specific configuration: `%%{init: {"flowchart": {"useMaxWidth": false,
  "nodeSpacing": 20, "rankSpacing": 25}} }%%`. It keeps an editable diagram
  from expanding to the full note width. Convert a horizontal `flowchart LR`
  into `flowchart TD` when this preserves its edges and meaning; shorten labels
  if it remains too large.
- Do not split a Mermaid diagram: preserve one editable graph and pair it with
  concise explanatory text when its full context matters.
- Never render Mermaid as a raster image. Mermaid must remain editable in the
  final Obsidian note.
- Use an ordered list for a long enumeration of peer items that a reader may
  need to refer to by position, such as a catalogue of mechanisms, methods,
  cases, or options. Use ordinary bullets for short, unordered attributes or
  alternatives.
- Avoid duplicate summary layers: retain one orientation layer and do not repeat
  the same records in a new summary, catalogue, or card section unless the
  source already contains both for distinct reading tasks.
- An orientation layer names the map and the reader's next choice; it must not
  repeat every definition, strength, risk, variant, and example later held in
  detailed profiles. Preserve repeated facts by keeping them once in their
  canonical profile.

## Sources

Make sources useful to a reader, not merely traceable to a processor. Do not leave reader-facing numeric citations such as `[47]`, `[1]`, or a bare reference list. Resolve a reliable source into a descriptive Markdown title-link, or remove the raw marker and report it as unresolved.

When a source proves a section rather than a specific named item, collect it at the end of the note under `## Источники` / `## Sources`, grouped by the relevant main section. Each entry must be a descriptive title-link, for example `- [Worker Placement | BoardGameGeek](https://...)`, never a naked URL.

When a reader-facing named example itself is useful to open — such as a game, book, product, method, or official document — link the name directly: `[CATAN](https://...)`, not `CATAN [48]`. Prefer an official page, publisher, documentation, or primary source; use a reputable catalogue only as a fallback.

## Workflow

### Batch Mode

When the request contains two or more supported inputs:

1. Build an ordered batch inventory before editing. Keep one item for every
   input file and preserve the user's input order.
2. Create a separate run subdirectory, converted copy, refined copy, asset
   directory, citation inventory, verified-source ledger, and validation result
   for each item. Never reuse one document's source mapping or assets for
   another document.
3. Apply the normal Refine workflow and quality gates independently to every
   item. One failed input must not erase, replace, or silently block the
   successfully prepared items. Keep the failed source unchanged and report its
   reason next to that file.
4. Produce exactly one proposed output note for each successful input. Never
   concatenate documents, create a combined summary, or drop an input because
   its title resembles another input.
5. Ensure proposed final filenames are unique within the batch and do not
   overwrite unrelated existing vault notes. Resolve duplicate or generic
   titles with concise topic-specific wording derived from each document. If a
   safe distinct title cannot be inferred, ask one batch-level naming question
   that identifies the ambiguous files.
6. Before handoff, show one compact batch preview mapping each source filename
   to its proposed final filename and status. Include source gaps only where
   they exist. Ask once whether to transfer the complete listed set to the
   selected destination; that confirmation covers only those named outputs.
   Write the preview data to a JSON manifest and render the response with
   `render-refine-preview`. Return the helper output verbatim as the entire
   pre-handoff response. Do not append workflow rationale, instruction text,
   skill links, command details, or another confirmation explanation.
7. After confirmation, hand off each prepared item with
   `handoff-refined-note`. Verify every destination separately and return one
   compact result list with `готово` or the specific failure for each input.
   Never claim that the batch succeeded when any listed item failed.

Do not ask the user to upload or confirm each document separately when the
files and common destination are already clear. Do not impose a smaller
hard-coded batch limit than the attachments accepted by the current Codex
surface; eight documents is a supported ordinary batch.

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
   personal vault name or path. Do not choose `Library/` merely because it
   exists; if there is no obvious candidate from title, nearby content, folder
   purpose, or request, ask the user where to place it before handoff. Never
   treat `.Trash`, caches, or temporary folders as vault candidates; when a
   known iCloud vault is absent from detection, inspect its stated path before
   choosing another vault.
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
from the note's H1, but treat generic export headings such as `Ответ и
уверенность`, `Краткий ответ`, `Обоснование и анализ`, or an equivalent title
that could describe an unrelated report as scaffolding rather than a useful
reader-facing filename. In that case, derive a concise, topic-specific title
from the central subject or decision using terms already present in the note,
and pass it with `--final-title`. Never use a technical source name such as
`deep-research-report.md` when a meaningful title can be derived. For every inventory entry,
   repair the matching claim in the refined copy with a verified title link when
a reliable source is available. The helper's report must be retained for
internal verification and the natural-language final summary.
Use the helper's `existing_title_links_preserved` and
`section_sources_retained` values in the visible source-status note; do not
describe the note as source-empty merely because raw export markers could not
be mapped claim by claim.
Use the helper's `language_warnings` as a gate, not as an automatic
translator. Resolve every warning in the temporary copy with model judgement
before handoff, except when the flagged phrase is intentionally a name, source
title, framework, or established term.
5. Inspect the result before handoff. Verify that ordinary title links, bare
   URLs, and source sections remain; raw citation markers are gone; the body has
   no duplicate top H1; and the TOC links only to real main sections. Confirm
   that Refine did not add examples, opinions, or new analysis. After the
   helper's cosmetic pass, perform a separate semantic structure pass using
   the shared reader contract. Map source propositions to the final note and
   final propositions back to the source. Then run `audit-reader-structure` on
   the temporary Markdown and resolve or explicitly review every reported
   issue before the reader review. Treat repeated generic profile-table
   warnings as a request to choose one comparison matrix or one prose layer,
   not as a request to delete unique facts.
   Treat `prose_field_profile_overlap` the same way: merge the opening prose and
   unbulleted fields into one canonical profile while retaining every unique
   statement. Bulleted experiment fields are an intentional single list.
   Treat `adjacent_profile_prose_overlap` and `prose_table_profile_overlap` as
   prompts for the same semantic comparison. Merge only facts that repeat.
   Keep causal explanations, limitations, and details that occur in one layer
   only. When converting a source profile row into an entity section, integrate
   its unique fields into the existing section instead of appending a second
   paragraph with the same payments, channels, prices, roles, or repeat value.
6. If a selected vault contains `Library/`, make that the default destination.
   Otherwise use the best matching existing folder, or the vault root when no
   better match exists. Write the proposed source, output, status, language,
   and destination to the preview manifest. For every ready item, also write
   `source_baseline` pointing to that input's untouched `converted.md` and
   `source_ledger` pointing to its ledger. Read the vault preference with
   `tag-preference`, and put its `source_tags` result in the manifest as
   `tag_preference`; set `note_type` to `research`. Then run
   `render-refine-preview`.
   The preview helper compares the final prepared note directly with the
   converted source baseline and refuses to ask for confirmation when a new URL
   is missing from the opened-source ledger. Never use a semantic intermediate
   such as `structured.md` as the baseline.
   This is required for one document as well as a batch. Return stdout verbatim
   as the entire pre-handoff response and append nothing after its transfer
   question. Never write a manual fallback that quotes an instruction, approval
   rationale, skill text, or command detail. Do not create a file in the
   selected vault at this stage. If the selected vault disappears before
   transfer, rescan vaults once and choose again from the current results. Say
   that the selected vault disappeared; do not describe it as a permission
   failure or silently close the workflow. If no current vault is suitable,
   leave the refined copy in outputs and ask the user where to place it.
7. Only after the user explicitly confirms the transfer, run the handoff helper.
   If the preference was unset, interpret “with tags” as both transfer
   confirmation and permission to save `enabled`, and “without tags” as both
   transfer confirmation and permission to save `disabled`. Save that one
   choice with `tag-preference --set`. For `enabled`, apply `tag-note` to the
   temporary refined copy before handoff. Do not ask about tags again for this
   vault unless the user explicitly asks to change the preference.
   Never use direct `cp`, `mv`, `rm`, or another filesystem shortcut for this
   handoff:

   ```bash
   python3 scripts/bookworm_helper.py handoff-refined-note \
     --source /path/to/original.md \
     --refined /path/to/scratch/refined.md \
     --destination-dir /path/to/vault/Library \
     --confirmation user-confirmed \
     --final-title "Reader-facing localized title" \
     --run-dir /path/to/scratch/refine-<run-id> \
     --assets-dir /path/to/scratch/refine-<run-id>/assets \
     --source-baseline /path/to/scratch/refine-<run-id>/converted.md \
     --source-ledger /path/to/scratch/refine-<run-id>/source-ledger.json
   ```

   The helper refuses to run without the confirmation token, refuses to
   overwrite an existing note, verifies the final bytes and assets, and then
   removes only temporary run files by default. It must not delete an original
   user source from `Downloads`, `Desktop`, a book folder, or another non-run
   location unless the user explicitly approved source deletion as a separate
   action and the command is run with `--delete-source`. For a `Library/`
   destination, assets live in `Library/assets/<note-slug>/`. Treat this
  explicit confirmation as authorization for the verified transfer and
  temporary cleanup only. Do not ask for a second confirmation unless the
  destination, replacement scope, or source-deletion scope changes. If the
  refined destination is the same existing source note, the helper performs the
  verified in-place replacement; do not bypass it with manual `cp`, `mv`, `rm`,
  or editor writes.
  When the source filename or H1 is in the wrong language, pass a localized
  reader-facing `--final-title` to the helper instead of accepting the raw
  export title. For a Russian note or Russian user request, the final filename
  must be a natural Russian title except for established product names,
  acronyms, or terms that are more readable in the original.
8. Use the transfer-confirmation response below before handoff. Do not start or
   offer Enrich until the handoff has been verified.

## Transfer Confirmation Response

After a temporary refined copy is ready and before a verified handoff, report
the selected destination and ask for transfer confirmation. When the vault tag
preference is unset, the same question must offer transfer with the proposed
tag or without tags and say the choice will be remembered for that vault. In
Russian, use an informal question such as:

> Перенести очищенную копию в `Brain/Library` с тегом `bookworm/research` или без тегов? Выбор сохраню для этого хранилища.

State that the file has not been transferred yet and that transfer starts after
the user's answer. Do not explain that an internal rule requires confirmation.
For example:

> Файл пока не переносил. Перенести очищенную копию в `Brain/Library`?

When a saved preference exists, use the ordinary transfer question and do not
ask about tags again. For a batch, show the source-to-output preview first and use one plural
confirmation, for example:

> Восемь заметок готовы к переносу. Перенести перечисленные файлы в `Brain/Library`?

Generate this response with the deterministic helper instead of composing it
freehand:

```bash
python3 scripts/bookworm_helper.py render-refine-preview \
  --manifest /path/to/run/preview-manifest.json
```

The manifest contains `language` (`ru` or `en`), the reader-facing
`destination`, and an `items` array. Each ready item contains `source`,
`status`, `refined`, `source_baseline`, and `source_ledger`. A failed item
contains `source`, `status`, and `reason`. Return stdout verbatim
as the complete response and append nothing after its transfer question. This
prevents internal instructions, runtime paths other than the prepared file
links, and approval rationale from leaking into chat.

Do not offer Enrich in the pre-handoff response. Do not combine the transfer confirmation and Enrich offer in one message.
Do not say or imply that transfer confirmation deletes the original source.
If source deletion is desired, ask a separate explicit question after the
verified transfer, or include it only when the user already asked to delete the
source.

## Required Post-Handoff Response

After a verified handoff, state the destination path and end with this exact
question in the relevant language:

> Обогатить заметку примерами и контекстом с Bookworm: Enrich?

After a batch handoff, list every exact destination file and use the plural
question instead:

> Обогатить одну или несколько заметок с Bookworm: Enrich?

The question is mandatory after handoff. It is an offer only; wait for the
user's answer before starting Enrich. Do not enrich the original source.

## No Vault Found

If no Obsidian vault is detected, leave the refined copy in the current writable
output location and say that no vault was found. Ask the user where to transfer
the refined copy; do not offer Enrich before that transfer is verified and do
not delete the original source file automatically.

## Reader-Facing Output

The final note should look like a normal Obsidian note, not a cleanup report.

- Keep the filename as the reader-facing title; do not append `-refined` or
  `-bookworm` to the final vault filename.
- In the final response, name and link the exact final file. Do not hide it
  behind a generic label such as `заметка в Brain/Library`.
- Do not add a duplicate `# Title` at the top of the Markdown body.
- Place `## Содержание` or `## Contents` first in substantial notes, followed
  by links to main `##` sections.
- Do not add Bookworm metadata, diagnostics, quality checklists, or process
  commentary to the note body.

## Reader Review Gate

Before asking for handoff, read the temporary note as it will appear in
Obsidian. Check that the first two screens establish navigation and purpose,
tables are scannable, diagrams are legible, links open, source entries are
reader-facing, and no duplicate summary layer repeats the same material.
Confirm that a reader can find the conclusion, compare the meaningful options,
and see the important exception without reconstructing the source. Recheck the
source-to-final and final-to-source proposition maps, with special attention to
numbers, units, negation, cumulative conditions, uncertainty, and links beside
qualifications.
Perform a visual-density review: count Mermaid blocks and large tables. If the
note is visually dense, flag the choice in the preview for the user. Do not
delete diagrams automatically; Refine preserves them unless the user asks for a
separate visual pass.

## Safety Gate

Never delete the source file merely because the temporary copy was generated.
Keep the selected vault unchanged until the user explicitly confirms the
transfer.
If final transfer or verification fails, preserve both source and temporary copy
and report their paths. The deterministic helper owns final transfer and cleanup
so those actions remain explicit and confirmation-gated.

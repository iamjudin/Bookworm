---
name: digest
description: Digest long EPUB/PDF books into Obsidian-ready working notes, with important images preserved in the note body.
---

# Digest

Use this skill when the user asks Codex to read, digest, summarize, extract the essence of, or prepare an Obsidian note for a book. Also use it when an input looks like a book: an `EPUB` file or a `PDF` with roughly 100+ pages.

This skill is the main action bundled by the Bookworm / Букворм plugin. Think of the plugin as the bookworm character and this skill as what it does: it digests a book into a useful working note.

Prefer explicit invocation for the MVP, such as `$Bookworm`, `$Bookworm: Digest`, or "Букворм, обработай EPUB". Do not promise or depend on automatic handling of empty attachment-only EPUB messages; Codex may not route those messages to this skill reliably in every surface.

If this skill is already explicitly invoked and the user attaches an EPUB with an empty or vague written request, assume the intended request is: create an Obsidian-ready working digest for that book. Do not ask "what should I do with this file?" unless there are multiple plausible non-digest tasks.

Bookworm's goal is not a short summary. It creates a working book note that can later serve as Codex memory for Q&A, implementation help, and method application.

## Activation

Start Bookworm confidently when:

- the user gives an EPUB;
- the user gives a PDF that appears to be a book, especially 100+ pages;
- the user asks to make a book digest, book note, practical summary, or Obsidian-ready summary.

For PDFs under 100 pages, inspect first. They may be articles, reports, contracts, decks, manuals, or whitepapers.

## Core Output Rules

- Produce one Markdown file per book.
- Optimize for Obsidian.
- Detect likely vaults by looking for folders containing `.obsidian`.
- If one or more likely Obsidian vaults exist, select the best target from the detected vaults by matching the user's explicit request, existing folder names, note/library structure, and nearby content. Do not hard-code or assume a personal vault path.
- When the selected vault is writable, write the Markdown note and assets there by default unless the user asked for another location.
- When filesystem permissions or sandbox rules prevent direct vault writes, create the deliverable in the writable `outputs` area first, then ask the user to confirm copying it into the selected detected vault. Do not silently leave the vault-ready result only in `outputs` when a suitable vault was detected.
- If no Obsidian vault is detected, keep the deliverable in the current writable output location and do not propose moving it to a vault. Mention that no vault was detected.
- If the selected vault has a `Library/` folder, use it as the default destination for book notes. Otherwise use the best matching existing folder by title/content, or the vault root if there is no clear match.
- The note filename must match the human-readable book title, not a slug and not a Bookworm implementation name. Do not append `bookworm` to the final note filename.
- If the note filename is the book title and Obsidian will show the inline title, do not add a duplicate top-level `# Book Title` heading inside the note.
- For substantial notes, add a compact manual table of contents near the top. When relying on Obsidian's inline title, make `## Содержание` the first section in the file, followed by links to the main `##` sections, then continue with `## Коротко`.
- Store visual assets in a shared library assets folder, such as `Library/assets/<book-slug>/<chapter-slug>/` for notes in `Library/`.
- For notes stored in `Library/`, embed important images with paths relative to the library folder: `![[assets/book-slug/chapter-06/figure-01.png|700]]`.
- After selecting final visuals, keep only the assets that are actually embedded in the final note, plus a manifest if useful. Do not copy the whole extraction dump into the vault.
- Use simple ASCII-safe asset filenames.
- Use the book's language for visible headings, navigation labels, figure notes, and reader-facing text unless the user asks otherwise.
- Use the book's language or the user's request language for user-facing progress updates and final chat messages. For example, when processing a Russian book for a Russian-speaking user, write progress updates in Russian instead of defaulting to English.
- Keep tags, frontmatter, and broader Obsidian metadata out of the MVP unless the user is designing the whole vault workflow.

## Vault Handoff

When a final digest is created outside a detected vault because of workspace permissions, the final answer should include:

- the selected detected vault path and why it was selected;
- the generated note path;
- the generated assets path;
- a clear question asking whether to copy the note and assets into the vault.

If no vault was detected, do not ask for vault copy confirmation. Just provide the generated note/assets paths and say that no Obsidian vault was found.

If the user confirms, copy:

- the Markdown file to the vault `Library/` folder when present, otherwise to the vault root or the user-specified vault folder;
- the asset directory to the shared assets folder for that book, e.g. `Library/assets/<book-slug>/` when the note is in `Library/`.

After copying, verify that every Obsidian embed in the copied note resolves relative to the vault root.

After a successful vault copy and embed verification, clean transient working files created for the handoff:

- scratch extraction folders such as `work/`;
- temporary contact sheets and intermediate JSON/text dumps;
- duplicate generated note/assets left under `outputs/` after the verified vault copy exists.

Do not delete the original source book, the copied vault note, or copied vault assets. If cleanup is blocked by permissions, say exactly which temporary paths remain and ask the user whether to remove them.

## Reader-Facing Tone

The final note must read like a useful book note, not like a plugin report.

Do not include:

- internal metadata such as `Type`, `Source`, `Include image`;
- quality checklist output;
- "method notes";
- "what worked";
- "what to improve in Bookworm";
- implementation diagnostics for the plugin itself;
- English template labels when the source book is in another language.

Internal metadata may be used while working, but it must be removed before final output.

When including fenced code templates in the final note, avoid Markdown heading markers inside the template unless the heading syntax itself is the subject. Prefer field labels such as `Намерение:` and `Что уже известно:` so the template does not pollute Obsidian outlines or heading searches.

## Sources

Use a two-column parameter-description table for repeated profiles, reference cards, and comparable records when it is more scannable than prose; two or more related label-value fields must become that table. Keep narrative reasoning and long explanations outside tables.

Use an ordered list for a long enumeration of peer items that a reader may need to refer to by position, such as a catalogue of mechanisms, methods, cases, or options. Use ordinary bullets for short, unordered sets of attributes or alternatives.

Avoid duplicate summary layers: give the note one concise orientation layer,
then the full material. Do not restate the same records in a second summary,
catalogue, or card section unless it adds a genuinely different reading task.

Do not leave reader-facing numeric citations such as `[47]`. When a named example, book, product, method, or official document is useful to open, link its name directly with a descriptive title-link.

When external sources support a whole section, collect them at the end of the note under `## Источники` / `## Sources`, grouped by the relevant main section. Each entry must be a descriptive title-link, never a naked URL or numeric-only reference.

## Practical Non-Fiction Template

Adapt headings to the book language. For Russian books, use:

- `Коротко`
- `Главный тезис`
- `Вводная`
- `Готовность к вопросам` only when useful; omit it if it feels like internal scaffolding.
- `Протокол применения`
- `Заметки для внедрения`
- `Практические выводы`
- `Карта аргумента`
- `Схемы и визуалы`
- `Заметки по главам`
- `Ограничения и риски`
- `Вопросы для повторения`
- `Лестница сжатия`
- `Запоминающиеся опоры`
- `Опоры в источнике`

The final note may omit sections that would feel empty or mechanical. It must not omit context needed for future Q&A.

When a method uses an abbreviation, keep the original English expansion in parentheses instead of replacing the Russian reader-facing label:

- `Проекты (Projects)`, `Сферы жизни (Areas)`, `Ресурсы (Resources)`, `Архивы (Archives)`.
- `Сохраняем (Capture)`, `Организуем (Organize)`, `Извлекаем суть (Distill)`, `Демонстрируем (Express)`.

Avoid slash labels like `Capture / Сохраняем` in final reader-facing text.

## Fullness Standard

The digest should be complete enough that Codex can later answer questions about the book and help the user apply its methodology without rereading the source.

Preserve:

- key terms;
- sequence of the method;
- motivation behind each step;
- typical mistakes;
- conditions where the method applies or breaks;
- important examples and cases;
- evidence anchors to chapters, sections, figures, or examples;
- user-fit questions for implementation-oriented books.

Do not over-compress. If a person, case, term, or example is important, briefly explain it so the note is understandable without prior knowledge of the book.

## Figures And Visuals

Images are first-class content.

During analysis, classify visuals internally:

- `decorative`: cover, ornament, incidental image;
- `supporting`: helpful illustration, but not required;
- `essential`: meaning is lost without it;
- `technical`: diagram, table, graph, screenshot, workflow, architecture, or dense figure.
- `practical example`: real folder structures, checklists, before/after examples, worked examples, or screenshots that show how to apply the method.

In the final note:

- do not show the classification labels;
- include or reconstruct `essential` and `technical` visuals;
- include a compact selection of `practical example` visuals when they make the method easier to implement, especially folder structures, workflow screenshots, and worked examples;
- omit redundant examples only after the note preserves the underlying pattern clearly;
- use a natural reader-facing block:

```markdown
### Рис. 2.1. Название схемы

![[assets/book-slug/chapter-02/figure-01.png|700]]

**Что показывает:** ...

**Как читать:** ...

**Почему важно:** ...

**Как применить:** ...
```

If a visual is essential, technical, or a practical example that teaches implementation, the digest is incomplete unless it includes the image, a faithful verbal explanation, or a useful reconstruction such as a table, Mermaid diagram, or step-by-step reading guide.

## Workflow

1. Inspect the source file with `scripts/bookworm_helper.py inspect`.
2. Detect a likely Obsidian vault with `scripts/bookworm_helper.py detect-vaults` when an output location is not given.
3. Determine source language and visible heading language.
4. Extract or plan important visual assets.
5. Build a chapter/section map.
6. Digest chapter by chapter, preserving enough context for future Q&A.
7. Include important figures in place, with explanations.
8. Run the internal quality gate.
9. Write one Obsidian-ready Markdown file plus local assets.
10. Prune generated assets so only embedded visuals and useful manifests remain with the final note.
11. If a vault was detected but the output was written elsewhere, ask to copy the finished deliverable into the vault and verify the copied embeds after confirmation.
12. After confirmed vault copy and verification, remove temporary working files from the scratch workspace so repeated book runs do not leave clutter.

## Internal Quality Gate

Before finalizing, verify silently:

- clarity: understandable without reading the book;
- fullness: enough for future Q&A and implementation help;
- applicability: practical books include action protocols and user-fit questions;
- evidence grounding: important claims point to chapters, sections, examples, or figures;
- context preservation: important cases and terms are not over-compressed;
- restraint: the note has not become a full retelling;
- reader-facing cleanliness: no internal diagnostics or plugin scaffolding remain.

Only show this checklist if the user explicitly asks for diagnostics.

## Reader Review Gate

Before final handoff, read the note as it will appear in Obsidian. Check that
the first two screens establish navigation and purpose, tables are scannable,
diagrams are legible, links open, and no duplicate summary layer repeats the
same material.

## Copyright And Privacy

Assume local personal use. Do not publish or redistribute extracted copyrighted images outside the user's private digest. When writing to an Obsidian vault, keep source assets local to the vault.

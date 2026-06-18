---
name: bookworm
description: Create Obsidian-ready working digests when the user attaches or mentions an EPUB/book-like PDF, even if the message has no text, with important images preserved in the note body.
---

# Bookworm / Букворм

Use this skill when the user asks Codex to read, digest, summarize, extract the essence of, or prepare an Obsidian note for a book. Also use it when an input looks like a book: an `EPUB` file or a `PDF` with roughly 100+ pages.

If the user attaches an EPUB and the written request is empty or vague, assume the intended request is: create an Obsidian-ready working digest for that book. Do not ask "what should I do with this file?" unless there are multiple plausible non-digest tasks.

Bookworm's goal is not a short summary. It creates a working book note that can later serve as Codex memory for Q&A, implementation help, and method application.

## Activation

Start Bookworm confidently when:

- the user gives an EPUB;
- the user gives only an EPUB attachment with no text;
- the user gives a PDF that appears to be a book, especially 100+ pages;
- the user asks to make a book digest, book note, practical summary, or Obsidian-ready summary.

For PDFs under 100 pages, inspect first. They may be articles, reports, contracts, decks, manuals, or whitepapers.

## Core Output Rules

- Produce one Markdown file per book.
- Optimize for Obsidian.
- If a likely Obsidian vault exists, use it as the default output destination or ask before writing there when filesystem permissions require it.
- Detect likely vaults by looking for folders containing `.obsidian`.
- Store visual assets in a stable folder such as `assets/<book-slug>/<chapter-slug>/`.
- Embed important images directly in the note body using Obsidian syntax: `![[assets/book-slug/chapter-06/figure-01.png|700]]`.
- Use simple ASCII-safe asset filenames.
- Use the book's language for visible headings, navigation labels, figure notes, and reader-facing text unless the user asks otherwise.
- Keep tags, frontmatter, and broader Obsidian metadata out of the MVP unless the user is designing the whole vault workflow.

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

In the final note:

- do not show the classification labels;
- include or reconstruct `essential` and `technical` visuals;
- use a natural reader-facing block:

```markdown
### Рис. 2.1. Название схемы

![[assets/book-slug/chapter-02/figure-01.png|700]]

**Что показывает:** ...

**Как читать:** ...

**Почему важно:** ...

**Как применить:** ...
```

If a visual is essential or technical, the digest is incomplete unless it includes the image, a faithful verbal explanation, or a useful reconstruction such as a table, Mermaid diagram, or step-by-step reading guide.

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

## Copyright And Privacy

Assume local personal use. Do not publish or redistribute extracted copyrighted images outside the user's private digest. When writing to an Obsidian vault, keep source assets local to the vault.

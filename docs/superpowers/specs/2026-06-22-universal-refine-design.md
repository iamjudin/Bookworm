# Universal Refine Design

## Goal

Make `Bookworm: Refine` turn Markdown, Word (`.docx`), PDF, and PowerPoint
(`.pptx`) input into a clean, Obsidian-ready Markdown note while keeping the
original source untouched until a confirmed vault handoff.

## Input Conversion

Add one helper command that detects the source extension and writes all
intermediate output into the run directory:

- `.md`: copy the Markdown source into the normal refinement pipeline;
- `.docx`: extract headings, paragraphs, lists, tables, and embedded images;
- `.pdf`: extract page text and preserve useful recoverable images;
- `.pptx`: create sections from slide titles, retain body text and notes, and
  extract slide images.

The converter produces a Markdown draft plus a run-local assets directory. A
missing reader or unsupported malformed source fails with an actionable error;
it never silently emits an empty note. The source document is never edited.

The conversion layer uses the Codex bundled Python document libraries when
available. It must report a clear dependency limitation instead of inventing a
conversion when that runtime is unavailable.

## Refine Pipeline

The draft then follows the existing cosmetic Refine pipeline:

1. preserve the source language and substantive content;
2. rebuild wide tables and unreadable Mermaid only under existing layout rules;
3. create `## Содержание` or `## Contents` with native Obsidian links in the
   exact form `[[#Heading|Heading]]`;
4. remove any prior Bookworm TOC in either legacy Markdown-anchor or native
   Obsidian form before rebuilding it;
5. remove raw ChatGPT citation markers only after claim-by-claim repair work.

Raw citation repair produces a small run-local ledger: total markers, verified
title links inserted, and unresolved markers. A named or otherwise identifiable
source must be opened and linked with its descriptive title. When verification
is impossible, retain the claim, remove the opaque marker, and disclose the
unresolved count in chat. Refine never expands the argument with new examples,
opinions, or analysis.

## Handoff And Assets

Before explicit confirmation, the final Markdown and selected assets remain in
the run directory. After confirmation, the existing deterministic handoff
creates the final Markdown in the chosen vault folder and copies selected assets
to `Library/assets/<note-slug>/` when the selected vault has `Library/`.
Verification must include final note bytes and declared asset paths before the
source and run directory are deleted.

## Enrich Boundary

Enrich may ask one concise question when it needs the desired content focus.
After the user confirms scope, it performs the work directly on a temporary
copy. It must not create plans, specifications, commits, worktrees, or files in
the Bookworm project, and it must not ask the user to choose agents or an
execution mode.

Every external addition stays beside the relevant original passage and uses:

```md
#### Дополнение — [название источника](https://...)
```

Enrich adds examples, context, alternatives, consequences, or deeper
explanation, never personal opinion. It remains confirmation-gated before
replacing a vault note.

## Verification

Tests must cover native TOC links and replacement of an old TOC; format
dispatch and source safety for each supported input; asset placement under the
run directory; citation-ledger counts; and the Enrich prohibition on development
artifacts and execution-mode questions. Existing source-integrity and confirmed
handoff tests remain mandatory.

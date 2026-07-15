# Changelog

All notable changes to Bookworm are documented here.

## 0.1.9 — 2026-07-15

- Expanded the public README with why, use, development validation, and
  contribution guidance.
- Added public contribution, issue, pull request, and CI validation surfaces.
- Added explicit public package `license` and `keywords` metadata.

## 0.1.8 — 2026-07-15

- Changed public plugin and marketplace display names to English-only
  `Bookworm`.
- Kept Russian wording only for direct Russian-language user communication,
  not plugin UI names, README headings, manifests, or action labels.
- Standardized action labels as `Bookworm: Digest`, `Bookworm: Refine`, and
  `Bookworm: Enrich`.

## 0.1.7 — 2026-07-06

- Replaced the hard-coded landing/design phrase dictionary with a general
  language-consistency gate. Refine now reports mixed-language reader-facing
  glue through `language_warnings`; the agent must resolve those warnings by
  meaning in the note/request language before handoff.
- Added confirmed `--final-title` support to `handoff-refined-note`, so agents
  can use a localized reader-facing filename without relying on a built-in
  title dictionary.
- Source sections remain exempt from the language gate so source titles and
  source-group labels can stay in the original language.

## 0.1.6 — 2026-07-06

- Refine now applies established Russian equivalents for common landing/design
  glue phrases inside table values and short structural text, for example
  `problem/pain` → `проблема/боль` and `process/how it works` →
  `процесс/как это работает`.
- Refine keeps original terms only when they are the natural reader-facing term
  or a product/framework/source name, preventing mixed-language “fabric/details”
  output.
- Suggested filenames now use the localized reader-facing title for known
  Russian research notes, while preserving useful terms such as `gray
  wireframes`.

## 0.1.5 — 2026-07-06

- Refine now localizes short structural labels and common table headers in
  Russian notes, for example `Executive summary`, `Recommended order`, and
  `Notes`, while leaving source titles and source-group labels intact.
- `handoff-refined-note` now supports verified in-place replacement when the
  confirmed destination is the same existing source note, so agents no longer
  need a manual filesystem handoff workaround.

## 0.1.4 — 2026-07-06

- Documented the Mermaid safety rule: flowchart-only init settings must not be
  added to non-flowchart diagrams such as `erDiagram`, sequence, or state
  diagrams.
- Refine now localizes common English structural headings and TOC entries when
  the note/request language is Russian, while preserving established terms such
  as `wireframe`, `CTA`, `visual design`, and `AI-agent` where they remain the
  natural reader-facing term.
- Added contract and helper tests for localized Russian research structure.

## 0.1.0 — 2026-06-24

First public release.

- Digest books, readable articles, and research into Obsidian-ready notes.
- Refine Markdown, DOCX, PDF, and PPTX inputs without expanding their claims.
- Enrich notes with clearly separated, verified source blocks.
- Preserve editable Mermaid, readable source links, compact tables, and
  confirmation-gated vault handoff.

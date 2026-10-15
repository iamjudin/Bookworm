# Changelog

All notable changes to Bookworm are documented here.

## Unreleased

## 0.1.17 — 2026-10-15

- Added canonical nested Obsidian source tags for every Bookworm note:
  `bookworm/research`, `bookworm/book`, and `bookworm/article`. Existing YAML
  metadata and tags are preserved, and repeated processing stays idempotent.

- Extended Refine reader review to catch repeated profile facts across adjacent
  prose paragraphs and between prose and comparison tables during batch runs.

- Digest, Refine, and Enrich now share one reader structure contract for
  compact tables, purposeful lists, connected explanatory prose, navigation,
  evidence boundaries, and Mermaid review.
- Refine now distinguishes preservation of meaning from preservation of
  paragraph shape and requires bidirectional proposition review after its
  deterministic cleanup pass.
- Added a read-only structure audit and public synthetic fixtures for semantic
  preservation, section coverage, source-grounded enrichment, and stable
  handling of already readable notes.
- Refine now requires its deterministic pre-handoff preview for single-document
  runs as well as batches, preventing manual confirmation text from exposing
  internal workflow instructions.
- Reader review now detects repeated generic profile tables under one section
  and requires one canonical comparison, prose, or procedural layer.
- Reader review now also flags entity profiles that repeat narrative prose in
  two or more unbulleted fields while preserving bulleted experiment records.
- Refine source ledgers distinguish full from partial support. A partially
  supporting link cannot appear beside an unsupported detail unless its exact
  limitation is visible in the same reader-facing block.

## 0.1.16 — 2026-10-13

- Refine now renders its pre-handoff batch preview with a deterministic helper
  and rejects internal workflow text before it can appear in that response.
- Refine handoff now audits every newly inserted URL against a complete source
  ledger and refuses transfer when opened-source provenance is missing.

## 0.1.15 — 2026-10-12

- Refine now accepts a batch of research documents and creates one independent
  Obsidian note per input instead of merging the documents.
- Batch runs use isolated working files, unique final names, a single transfer
  preview and confirmation, and per-file success or failure reporting.

## 0.1.14 — 2026-10-12

- Refine now replaces generic export headings such as “Ответ и уверенность”
  with a concise topic-specific vault filename.
- Refine final messages must name and link the exact destination file.

## 0.1.13 — 2026-10-12

- Installed-package contract tests now skip repository-only marketplace checks
  when the marketplace manifest is intentionally absent from the runtime cache.

## 0.1.12 — 2026-10-12

- Digest, Refine, and Enrich now keep skill instructions, runtime paths,
  command output, and helper field names out of user-facing messages.
- Refine reports source status in natural reader-facing language instead of
  exposing JSON-style metric names in chat or notes.
- Repeated Refine passes now preserve introductory prose after a generated
  table of contents instead of deleting everything before the first main
  section.
- Added regression coverage for Refine idempotency and virtual Digest handoff
  communication.

## 0.1.11 — 2026-07-29

- Enrich now treats requests for illustrations, visuals, graphics, or figures
  as visual-asset enrichment: text-only examples are not enough when the user
  asked to add illustrations.
- Refine and Digest now make original source deletion opt-in. Verified handoff
  keeps user source files by default and cleans only Bookworm temporary run
  files unless `--delete-source` is explicitly used.
- Tightened localized filename rules so Russian notes use natural Russian
  Obsidian filenames instead of English slugs or export titles.

## 0.1.10 — 2026-07-29

- Digest now offers `Bookworm: Enrich` after a verified vault handoff, matching
  the existing Refine post-handoff behavior.
- Added a contract test so Digest cannot silently skip the post-handoff Enrich
  offer again.

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

# Bookworm Research Integrity Design

## Refine

Refine is a safe structural pass. It preserves every source-bearing construct:
Markdown links, URL source lists, footnotes, and ChatGPT citation markers. It
must count source-bearing constructs before and after refinement and reject a
handoff when any count drops.

ChatGPT citation markers are not URLs. Refine must never pretend that removing
one preserves its source. When a supplied Markdown file has no citation-to-URL
map, the marker stays in place and the final chat message explains the limit.

## Enrich

`Bookworm: Enrich` is an explicit, separate action for replacing an export's
source layer with fresh research. It verifies sources before using them and
places links on descriptive titles, for example `[Engine Builder as a
Mechanism](https://example.com)`. It never silently claims old citations have
been retained.

## Obsidian Layout

Keep Markdown tables only for compact comparison: no more than four columns,
short cells, and a readable note-width layout. Convert wider or prose-heavy
tables into titled item sections with labeled fields. Convert procedural tables
into numbered steps.

Use Mermaid only when it is readable in a portrait, top-to-bottom layout. A
diagram that needs a wide canvas or horizontal scrolling becomes a raster image
in the note assets, with a title and a short explanation. Preserve the Mermaid
source beside the image only when later editing is useful.

## Verification

- Regression tests prove citation-only provenance and regular links survive a
  Refine pass.
- The Refine skill requires a source-integrity check before handoff.
- The Enrich skill requires title links and a claim/source verification pass.
- Manual smoke tests inspect rendered notes in Obsidian at narrow width.

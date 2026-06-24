# Букворм / Bookworm

Bookworm turns books, readable web articles, and existing research exports into
clean, reader-facing Obsidian notes. This repository is structured as a Codex
plugin marketplace with one plugin: `bookworm`.

## Choose the right skill

| You have | Use | What you get |
| --- | --- | --- |
| A book, a long report, or a readable article URL | **Bookworm: Digest** | A new, complete working note for Obsidian |
| An existing research export that is hard to read | **Bookworm: Refine** | The same material, structured and source-aware |
| A note that needs reliable outside context | **Bookworm: Enrich** | Clearly separated, verified additions |

### Bookworm: Digest

Use **Digest** when you are starting from source material: an EPUB, a long PDF
that is actually a book, or a standalone readable article, essay, report, or
research page. It creates a new Obsidian working note that preserves the
source's argument, mechanisms, examples, limitations, and practical
implications rather than producing a bare short summary. Important visuals are
kept only when they help the reader understand or apply the material.

Choose Digest for “read this and make it useful later.” Do not use it to tidy a
research note you already have; that is Refine.

### Bookworm: Refine

Use **Refine** for an existing Markdown, Word, PDF, or PowerPoint research
export that needs to become readable and Obsidian-ready without changing what
it says. It normalizes headings, native Obsidian table-of-contents links,
compact tables, lists, and editable Mermaid diagrams; it preserves useful
title-links and removes raw citation markers only when their source status is
accounted for.

Refine does not add examples, opinions, analysis, or recommendations. It works
on a temporary copy, leaves the source untouched until explicit handoff
confirmation, and reports any unresolved citations instead of inventing links.

Choose Refine for “make this research clean and navigable.” Do not use it when
you want new research or external examples; that is Enrich.

### Bookworm: Enrich

Use **Enrich** when an existing note would benefit from new examples, context,
alternatives, consequences, or a deeper verified explanation. It opens and
checks sources, then adds only a visibly separate layer using blocks such as:

```markdown
#### Дополнение — [Source title](https://example.com)
```

It never silently rewrites the original material or presents its additions as
part of the source. If the focus is unclear, it asks one short content question;
otherwise it proceeds directly after your confirmation. Every change is made to
a temporary note copy before the final handoff.

Choose Enrich for “what is missing here, and what reliable context would make
it more useful?” Do not use it as a cleanup pass; that is Refine.

Russian user-facing labels are consistent: `Букворм: Дайджест`, `Букворм:
Рефайн`, and `Букворм: Энрич`. English labels use `Bookworm: Digest`,
`Bookworm: Refine`, and `Bookworm: Enrich`.

## Install from GitHub

After this repository is public, add the marketplace in Codex CLI:

```bash
codex plugin marketplace add iamjudin/Bookworm
```

Then open the plugin directory, select **Букворм / Bookworm**, and install
Bookworm. Start a new Codex chat before using the new version.

To update an installed marketplace:

```bash
codex plugin marketplace upgrade bookworm
```

The marketplace definition is at
[`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json); the
installable plugin bundle is in [`plugins/bookworm`](plugins/bookworm).

## Privacy and safety

Bookworm works with the source material you explicitly provide. It uses a
temporary run directory and waits for explicit handoff confirmation before it
creates or replaces a vault note. It never deletes the original source before
the handoff is verified. Web articles are read only when their pages are
accessible; paywalled or unreadable pages produce no empty note.

## Development

Validate the plugin from the repository root:

```bash
PYTHONPYCACHEPREFIX=/private/tmp/bookworm-pycache \
  python3 -m unittest discover -s plugins/bookworm/tests -q
git diff --check
```

When developing in Codex, also run the plugin validation supplied by
`@plugin-creator` against `plugins/bookworm`.

## License

Bookworm is source-available under the
[PolyForm Noncommercial 1.0.0](LICENSE) license. You may use, modify, and
redistribute it for noncommercial purposes. Commercial use needs separate
permission from the author; open a GitHub issue to get in touch.

# Букворм / Bookworm

Bookworm turns books, readable web articles, and existing research exports into
clean, reader-facing Obsidian notes. This repository is structured as a Codex
plugin marketplace with one plugin: `bookworm`.

## What it does

- **Bookworm: Digest** creates a useful working note from an EPUB, a long PDF,
  or a readable article URL. It keeps meaningful visuals and does not reduce a
  source to a bare summary.
- **Bookworm: Refine** restructures an existing Markdown, Word, PDF, or
  PowerPoint research export without adding new claims. It preserves usable
  links, cleans raw citation markers, and prepares an Obsidian-ready note.
- **Bookworm: Enrich** adds a clearly separated layer of verified examples,
  context, alternatives, and implications. It never silently rewrites the
  original material.

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

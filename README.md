# Bookworm

Bookworm helps turn books, articles, and research into clear, useful notes for
Obsidian.

It is built for people who use Codex as a reading and research partner: the
output should be useful later for Q&A, implementation work, and remembering how
an idea actually works, not just what the source was about.

## Skills

### Digest

Turns a book or article into a working note: the main ideas, examples,
limitations, and practical takeaways stay together so you can return to the
material later.

### Refine

Makes an existing research note easier to read and navigate without adding new
ideas or changing its meaning.

### Enrich

Adds useful context, examples, and alternatives from reliable sources when you
ask for them. New material stays clearly separate from the original note.

## Use

Start a new Codex chat and invoke one of the Bookworm actions:

- `Bookworm: Digest` for books, long PDFs, or standalone readable article URLs.
- `Bookworm: Refine` for existing Markdown, Word, PDF, or PowerPoint research
  exports that need a cleaner Obsidian shape without new claims.
- `Bookworm: Enrich` when an existing note needs sourced examples, context, or
  alternatives.

Bookworm works on a temporary copy first. For vault handoff it asks for
confirmation before creating, replacing, moving, or cleaning files in your
Obsidian vault.

## Install

In Terminal, run:

```bash
codex plugin marketplace add iamjudin/Bookworm
```

Then open Plugins in Codex, find **Bookworm**, click Add, and start a
new chat.

## Update

In Terminal, run:

```bash
codex plugin marketplace upgrade bookworm
```

Then restart Codex and begin a new chat.

## Development

Run the release checks from the repository root:

```bash
PYTHONPYCACHEPREFIX=/private/tmp/bookworm-pycache python3 -m unittest discover -s plugins/bookworm/tests -v
python3 scripts/validate_public_package.py
git diff --check
```

The official Codex plugin validator should also pass before a public release
when it is available in your local Codex environment.

## Contributing

Issues and pull requests are welcome when they improve Bookworm's public
behavior, documentation, or validation. See [CONTRIBUTING.md](CONTRIBUTING.md)
for the project conventions.

## License

Bookworm is source-available under the
[PolyForm Noncommercial 1.0.0](LICENSE) license. It is free to use,
modify, and redistribute for noncommercial purposes.

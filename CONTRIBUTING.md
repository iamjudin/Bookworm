# Contributing to Bookworm

Bookworm is a Codex plugin for turning books, articles, and research exports
into Obsidian-ready notes. Contributions should keep that public promise clear,
source-aware, and safe around user files.

## Before You Change Behavior

- Check `docs/backlog.md` for existing decisions and known cleanup work.
- Keep public names in English: `Bookworm`, `Bookworm: Digest`,
  `Bookworm: Refine`, and `Bookworm: Enrich`.
- Keep Russian wording only for direct Russian-language chat examples or user
  messages.
- Preserve source integrity. Refine must not silently remove links, URLs,
  footnotes, or citation evidence.
- Keep final note handoff confirmation-gated when vault files may be created,
  replaced, moved, or cleaned.

## Validation

Run these checks from the repository root before opening a pull request:

```bash
PYTHONPYCACHEPREFIX=/private/tmp/bookworm-pycache python3 -m unittest discover -s plugins/bookworm/tests -v
python3 scripts/validate_public_package.py
git diff --check
```

When the local Codex plugin validator is available, run it against
`plugins/bookworm` before a public release.

## Pull Requests

Keep pull requests focused. Include:

- what changed;
- why the public behavior or documentation needed it;
- which checks passed;
- any runtime or marketplace evidence when the change affects installation,
  update, or user-facing routing.

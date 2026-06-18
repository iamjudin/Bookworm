# Bookworm / Букворм

Bookworm is a local Codex plugin for turning long books into reader-facing Obsidian notes.

MVP focus:

- practical non-fiction books;
- EPUB files and long PDFs that look like books;
- one Markdown note per book;
- Obsidian image embeds with local assets;
- enough context for future Q&A and implementation help;
- internal quality checks that do not appear in the final note.

The plugin is skill-first: Bookworm is the plugin/brand, while `skills/digest/SKILL.md` is the action it performs. Codex uses that skill workflow and `scripts/bookworm_helper.py` for deterministic file inspection, image extraction, and vault discovery.

For local test iterations, prefer a clean reinstall: remove the old Bookworm plugin cache and transient test artifacts, then add the fresh local plugin again from the Codex plugin directory.

## Helper Script

```bash
python3 scripts/bookworm_helper.py inspect /path/to/book.epub
python3 scripts/bookworm_helper.py detect-vaults
python3 scripts/bookworm_helper.py extract-epub-assets /path/to/book.epub --out /path/to/vault/assets/book-slug
```

The helper uses only the Python standard library.

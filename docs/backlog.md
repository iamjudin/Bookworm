# Bookworm Backlog

## Decisions

- Manual invocation is acceptable and preferred for MVP: the user can call Bookworm explicitly with `$Bookworm` or a short request such as "Букворм, обработай EPUB".
- Do not spend MVP effort on unreliable empty-EPUB auto-start behavior. If Codex receives an EPUB with no text and does not automatically start Bookworm, that is acceptable for now.
- Book notes should land in the vault `Library/` folder when present.
- Final note filenames must match the human-readable book title, not a slug and not a Bookworm implementation name.
- For books in `Library/`, use one shared `Library/assets/` folder with per-book subfolders.
- Do not duplicate Obsidian's inline file title with a redundant top-level `# Book Title` heading in the Markdown body.
- When abbreviations have English originals, keep the English expansion in parentheses after the Russian label, for example `Сохраняем (Capture)` or `Проекты (Projects)`.
- After a confirmed vault handoff, clean transient working files so scratch folders do not accumulate.
- For local test iterations, prefer a clean reinstall cycle over upgrading in place: remove the old Bookworm plugin cache and transient test artifacts, then install the fresh local marketplace version.

## Cleanup

- Remove or de-emphasize non-working auto-start tails from Bookworm docs/instructions, especially promises around hooks or automatic handling of empty EPUB uploads that the current Codex plugin model cannot reliably enforce.
- Avoid duplicated naming in Codex skill invocation lists. The current `Bookworm: Bookworm` label is noisy; adjust plugin/skill naming or display metadata so manual invocation reads as a single clear `Bookworm` entry if the platform allows it.

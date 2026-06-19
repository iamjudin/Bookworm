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
- Bookworm's user-facing process should use the relevant language of the book/request instead of switching to English by default.
- Vault destinations must be discovered from actual Obsidian vaults (`.obsidian`) and selected by request, folder names, note structure, and nearby content. Do not hard-code a personal vault path.
- If no Obsidian vault is detected, keep the deliverable in the current output location and do not propose moving it to a vault.
- Refine must preserve every source-bearing construct. It must fail closed when
  citation markers, Markdown source links, bare URLs, or footnote references
  would decrease.
- Use title links for reader-facing sources. Replacing an unusable source layer
  with fresh research is an explicit Enrich action, never a hidden Refine step.
- Keep only compact Obsidian tables; convert wide/prose-heavy tables into
  labeled sections and process tables into numbered steps.
- Mermaid diagrams must be portrait and top-to-bottom. Render an unreadably
  wide diagram as an image when the environment can do so reliably.
- In Russian user-facing text and plugin metadata, write the brand as
  `Букворм / Bookworm`; use `Bookworm / Букворм` only in an English context.
- After a successful Refine handoff, offer the next two optional steps in
  order: move the note to the selected vault `Library/`, then run Enrich to add
  a fresh verified source layer. Enrich must remain confirmation-gated and must
  not start automatically.

## Cleanup

- Verify after reinstall that Codex shows the plugin action as `Bookworm: Digest` or an equivalent non-duplicated label.
- Verify after reinstall that Bookworm no longer presents empty EPUB auto-start as a guaranteed behavior.

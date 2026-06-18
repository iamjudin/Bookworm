# Bookworm Backlog

## Decisions

- Manual invocation is acceptable and preferred for MVP: the user can call Bookworm explicitly with `$Bookworm` or a short request such as "Букворм, обработай EPUB".
- Do not spend MVP effort on unreliable empty-EPUB auto-start behavior. If Codex receives an EPUB with no text and does not automatically start Bookworm, that is acceptable for now.

## Cleanup

- Remove or de-emphasize non-working auto-start tails from Bookworm docs/instructions, especially promises around hooks or automatic handling of empty EPUB uploads that the current Codex plugin model cannot reliably enforce.

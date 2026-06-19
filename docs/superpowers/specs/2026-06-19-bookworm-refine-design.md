# Bookworm Refine Design

## Purpose

`Bookworm: Refine` turns an existing Markdown research export, especially a
ChatGPT Deep Research note, into a clean Obsidian-ready note. It preserves the
substantive research by default and changes presentation rather than meaning.

## Scope

- Explicit invocation with a Markdown file.
- Detect and select an Obsidian vault from folders containing `.obsidian`.
- Prefer `Library/` in the selected vault; otherwise use the best matching
  existing folder or the vault root.
- Remove known export artifacts such as `citeturn...`.
- Preserve ordinary Markdown links, source lists, prose, tables, images, and
  embedded media.
- Normalize heading hierarchy and Markdown whitespace without reauthoring the
  research.
- Add a compact manual `## Содержание` after Obsidian's inline title. Do not
  add a duplicate top-level H1 to the note body.
- Ask before the final transfer from the source location, normally `Inbox/`,
  to the selected vault destination.

## Non-Goals

- No substantive rewriting, fact checking, summarization, or source removal by
  default.
- No permanent backup copy after a successful handoff.
- No hard-coded vault name or path.
- No proposal to transfer to a vault when no Obsidian vault is detected.

## Architecture

The skill owns the user-facing workflow and semantic restraint. A small,
standard-library helper owns deterministic transformations that should not vary
between runs:

1. Remove known ChatGPT citation/export tokens.
2. Normalize blank lines and heading spacing.
3. Build a table of contents from primary note sections.
4. Write the refined version to a temporary working location.

Codex inspects the result for malformed Markdown, protects meaningful content,
and determines the destination. The helper does not move or delete user files.

## Data Flow

1. The user explicitly invokes Refine with a Markdown note.
2. Refine detects available vaults and identifies the most suitable destination
   using the request, folder names, and nearby note structure.
3. Refine creates a temporary refined copy and reports the selected destination
   and rationale.
4. If the user confirms, Refine writes the final file to the destination and
   verifies it exists and has the expected title and TOC.
5. Only after verification does Refine remove the original source file and all
   temporary files. One final note remains.
6. If no vault is detected, Refine leaves the refined output in its working
   location and does not suggest a vault handoff.

## Error Handling

- Unsupported or unreadable input: stop before writing or deleting anything.
- No useful headings: keep the existing body and omit the TOC rather than
  inventing structure.
- Destination collision: ask before replacing an existing note; never silently
  overwrite it.
- Failed final write or verification: preserve the original and the temporary
  refined copy, report their paths, and do not delete either.

## Verification

Automated checks cover:

- ChatGPT citation tokens are removed while ordinary URLs and source sections
  remain unchanged.
- The generated TOC links to major sections and does not add a duplicate H1.
- The helper never deletes or moves the source file.
- Skill validation passes after the new `Refine` skill is added.

Manual smoke testing uses a real Deep Research Markdown export and confirms the
confirmation gate, selected-vault rationale, single-final-version cleanup, and
Obsidian rendering.

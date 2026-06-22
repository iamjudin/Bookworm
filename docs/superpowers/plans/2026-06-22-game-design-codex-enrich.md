# Game Design Codex Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an evidence-backed enrichment layer to the Game Design Codex note without altering its original research layer.

**Architecture:** Copy the vault note into one run directory, research the selected official game/rule sources, and append clearly marked enrichment blocks beside each mechanic profile. Validate structure and links before asking to replace the vault note.

**Tech Stack:** Markdown, Bookworm helper, official publisher documentation, shell validation.

---

### Task 1: Prepare and inventory the working copy

**Files:**
- Read: `/Users/iamjudin/Desktop/Brain/Library/Механики настольных игр для Game Design Codex.md`
- Create: `/private/tmp/enrich-game-20260622/enriched-note.md`

- [ ] **Step 1: Create one dedicated temporary run directory and copy the note into it**

Run:

```bash
mkdir -p /private/tmp/enrich-game-20260622
cp '/Users/iamjudin/Desktop/Brain/Library/Механики настольных игр для Game Design Codex.md' /private/tmp/enrich-game-20260622/enriched-note.md
```

Expected: the vault note remains unchanged and the run directory contains the working copy.

- [ ] **Step 2: Inventory profile headings and existing Markdown links**

Run:

```bash
rg -n '^### |^#### |https?://' /private/tmp/enrich-game-20260622/enriched-note.md
```

Expected: twelve mechanic profile headings are listed and no original prose is modified.

### Task 2: Research and write the enrichment blocks

**Files:**
- Modify: `/private/tmp/enrich-game-20260622/enriched-note.md`

- [ ] **Step 1: Verify an official or primary source for each selected game before citing it**

Use the web tool to open each candidate source. Record no unverified URL in the note.

- [ ] **Step 2: Add one sourced block after each mechanic profile**

Use this exact form and keep additions concise:

```md
#### Дополнение — [Название источника](https://example.com)

Конкретный пример реализации, следствие для дизайна и один вопрос для прототипа.
```

Expected: twelve blocks cover deckbuilding, worker placement, area control, engine-building, hand management, set collection, dice drafting, tile placement, action programming, resource management, auction/bidding, and role selection.

### Task 3: Validate and hand off

**Files:**
- Verify: `/private/tmp/enrich-game-20260622/enriched-note.md`
- Replace after confirmation: `/Users/iamjudin/Desktop/Brain/Library/Механики настольных игр для Game Design Codex.md`

- [ ] **Step 1: Validate the added blocks and source links**

Run:

```bash
rg -n '^#### Дополнение — \[' /private/tmp/enrich-game-20260622/enriched-note.md
rg -n 'cite|^\|.*\|.*\|.*\|.*\|' /private/tmp/enrich-game-20260622/enriched-note.md
```

Expected: twelve attributed enrichment blocks, no export citation markers, and no new wide tables.

- [ ] **Step 2: Compare the original and enriched copies**

Run:

```bash
diff -u '/Users/iamjudin/Desktop/Brain/Library/Механики настольных игр для Game Design Codex.md' /private/tmp/enrich-game-20260622/enriched-note.md
```

Expected: differences consist only of `#### Дополнение — …` blocks.

- [ ] **Step 3: Ask for explicit confirmation before replacing the vault note**

Report the temporary path, chosen destination, source count, and validation result. Replace the vault note only after the user confirms.

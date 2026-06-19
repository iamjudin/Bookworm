# Bookworm Research Integrity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prevent Refine from losing sources and add explicit Enrich and Obsidian-layout rules.

**Architecture:** The helper preserves source-bearing tokens and reports source counts. Skills own semantic source verification and layout decisions because they require reading and judgement.

**Tech Stack:** Python 3 standard library, `unittest`, Markdown, Codex skills.

---

### Task 1: Protect source-bearing Markdown

**Files:**
- Modify: `tests/test_bookworm_helper.py`
- Modify: `scripts/bookworm_helper.py`

- [x] Write failing tests for a citation-only claim and a Markdown title link.
- [x] Run `python3 -m unittest tests/test_bookworm_helper.py -v` and observe the citation test fail.
- [x] Remove the destructive citation substitution; add `source_counts` for citations, Markdown links, raw URLs, and footnotes.
- [x] Run `python3 -m unittest discover -s tests -v` and verify all tests pass.

### Task 2: Encode source and layout rules in skills

**Files:**
- Modify: `skills/refine/SKILL.md`
- Create: `skills/enrich/SKILL.md`
- Modify: `.codex-plugin/plugin.json`
- Modify: `README.md`
- Modify: `docs/backlog.md`

- [x] Make Refine fail closed on source loss and require compact tables plus portrait Mermaid or raster assets.
- [x] Add Enrich as the explicit fresh-research action using title links and verified claims.
- [x] Validate all skills and the plugin.

### Task 3: Prepare and test fresh plugin build

**Files:**
- Modify: `.codex-plugin/plugin.json`

- [x] Update the cachebuster.
- [x] Run helper tests and plugin validation.
- [ ] Merge the branch to `main`, prepare a clean reinstall, and smoke-test Refine and Enrich in new chats.

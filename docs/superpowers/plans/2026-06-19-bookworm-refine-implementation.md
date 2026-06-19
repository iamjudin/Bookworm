# Bookworm Refine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `Bookworm: Refine` to safely turn existing Markdown research exports into Obsidian-ready Library notes.

**Architecture:** Add a pure `refine-markdown` command to the existing standard-library helper. The new skill invokes it on a temporary copy, owns vault discovery and confirmation, and never delegates moving or deletion to the helper.

**Tech Stack:** Python 3 standard library, `unittest`, Markdown, Codex plugin skills.

---

### Task 1: Add deterministic Markdown refinement

**Files:**
- Modify: `scripts/bookworm_helper.py`
- Create: `tests/test_bookworm_helper.py`

- [ ] **Step 1: Write failing tests for citations, source links, and a TOC**

```python
def test_refine_markdown_removes_chatgpt_citations_and_keeps_urls():
    source = "# Title\n\nText citeturn0search1 [source](https://example.com).\n\n## Findings\n"
    result = refine_markdown(source)
    assert "cite" not in result
    assert "https://example.com" in result
    assert "## Содержание" in result
    assert "- [Findings](#findings)" in result
```

- [ ] **Step 2: Run the test and verify it fails because `refine_markdown` does not exist**

Run: `python3 -m unittest tests/test_bookworm_helper.py -v`

Expected: `ImportError` or `AttributeError` mentioning `refine_markdown`.

- [ ] **Step 3: Implement `refine_markdown` and `refine-markdown` CLI command**

```python
def refine_markdown(source: str) -> str:
    cleaned = re.sub(r"cite[^]+", "", source)
    # Preserve body text and links; only normalize heading/blank-line layout.
    return with_manual_toc(cleaned)
```

The command reads one Markdown path and writes the refined copy to an explicit
`--out` path. It must not delete, rename, or move either path.

- [ ] **Step 4: Run helper tests and verify they pass**

Run: `python3 -m unittest tests/test_bookworm_helper.py -v`

Expected: all tests pass.

- [ ] **Step 5: Commit helper and tests**

```bash
git add scripts/bookworm_helper.py tests/test_bookworm_helper.py
git commit -m "Add Markdown refinement helper"
```

### Task 2: Add the Refine skill

**Files:**
- Create: `skills/refine/SKILL.md`
- Modify: `README.md`
- Modify: `.codex-plugin/plugin.json`

- [ ] **Step 1: Add the `refine` skill with a confirmation-gated handoff**

The skill explicitly targets Markdown research exports. It detects vaults with
the existing helper, uses `Library/` when present, runs the helper against a
temporary copy, reports the selected destination and rationale, and waits for
confirmation before final transfer. It removes the original only after the
new final note exists and has been checked. It preserves URLs, source lists,
tables, and images, and never suggests a vault transfer when none is detected.

- [ ] **Step 2: Update plugin-facing wording**

Add research-note cleanup to the manifest capability/description and README so
the second skill is discoverable without conflating it with Digest.

- [ ] **Step 3: Validate the skill and plugin**

Run: `python3 /Users/iamjudin/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/refine`

Run: `python3 /Users/iamjudin/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .`

Expected: both commands exit 0.

- [ ] **Step 4: Commit the skill and metadata**

```bash
git add skills/refine/SKILL.md README.md .codex-plugin/plugin.json
git commit -m "Add Bookworm Refine skill"
```

### Task 3: Prepare a fresh local plugin version

**Files:**
- Modify: `.codex-plugin/plugin.json`

- [ ] **Step 1: Update the local cachebuster**

Run: `python3 /Users/iamjudin/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py .`

- [ ] **Step 2: Re-run all tests and plugin validation**

Run: `python3 -m unittest tests/test_bookworm_helper.py -v`

Run: `python3 /Users/iamjudin/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .`

Expected: all checks pass.

- [ ] **Step 3: Commit the release-preparation version**

```bash
git add .codex-plugin/plugin.json
git commit -m "Prepare Bookworm Refine test build"
```

### Task 4: Clean-reinstall and smoke test

**Files:**
- No repository file changes required.

- [ ] **Step 1: Remove only the Bookworm cache and installed config stanza**

Preserve the marketplace configuration. Do not remove user notes or working
files.

- [ ] **Step 2: Add the fresh version through Codex Local Plugins**

Expected: the skill picker shows both `Bookworm: Digest` and `Bookworm: Refine`.

- [ ] **Step 3: Test in a new chat with a Deep Research Markdown export**

Expected: Refine reports a detected vault, waits for the transfer confirmation,
then leaves one cleaned final note in `Library/` after confirmation.

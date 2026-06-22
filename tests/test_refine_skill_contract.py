from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RefineSkillContractTests(unittest.TestCase):
    def test_final_handoff_requires_enrich_offer(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("## Required Final Response", skill)
        self.assertIn("Обогатить заметку примерами и контекстом", skill)

    def test_refine_repairs_sources_without_expanding_content(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("repair broken or raw source citations", skill)
        self.assertIn("Do not add examples, opinions, or new analysis", skill)

    def test_enrich_labels_every_added_block_with_its_source(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("#### Дополнение — [название источника](https://...)", skill)
        self.assertIn("Do not add personal opinions", skill)

    def test_refine_accepts_all_supported_document_inputs(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        for suffix in (".md", ".docx", ".pdf", ".pptx"):
            self.assertIn(suffix, skill)
        self.assertIn("bundled Python runtime", skill)
        self.assertIn("Do not create an empty note", skill)

    def test_enrich_never_performs_repository_or_execution_work(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("must not create plans, specs, commits, worktrees, or repository files", skill)
        self.assertIn("must not ask about agents or execution modes", skill)
        self.assertIn("temporary copy", skill)

    def test_refine_and_enrich_keep_mermaid_editable(self) -> None:
        for name in ("refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Never render Mermaid as a raster image", skill)

    def test_bookworm_uses_scannable_tables_and_reader_facing_sources(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("two-column parameter-description table", skill)
            self.assertIn("## Sources", skill)
            self.assertIn("Do not leave reader-facing numeric citations", skill)
            self.assertIn("two or more related label-value fields", skill)

    def test_bookworm_numbers_long_enumerations(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Use an ordered list for a long enumeration", skill)

    def test_bookworm_requires_reader_review_without_duplicate_layers(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Avoid duplicate summary layers", skill)
            self.assertIn("Reader Review Gate", skill)
        refine = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not introduce new conclusions, taxonomies, or recommendations", refine)

    def test_refine_does_not_request_second_handoff_confirmation(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not ask for a second confirmation", skill)


if __name__ == "__main__":
    unittest.main()

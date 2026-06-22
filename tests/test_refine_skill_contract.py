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


if __name__ == "__main__":
    unittest.main()

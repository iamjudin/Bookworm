from __future__ import annotations

import json
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

    def test_bookworm_uses_general_research_information_architecture(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("one orientation layer", skill)
            self.assertIn("detailed material", skill)
            self.assertIn("section-level sources", skill)
            self.assertIn("Mermaid configuration", skill)

    def test_unresolved_original_sources_do_not_block_enrich(self) -> None:
        refine = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        enrich = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("source layer is incomplete", refine)
        self.assertIn("does not block Enrich", refine)
        self.assertIn("even when the original source layer is incomplete", enrich)
        self.assertIn("does not validate the original claims", enrich)

    def test_bookworm_keeps_each_mermaid_diagram_whole(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Do not split a Mermaid diagram", skill)

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

    def test_enrich_requires_labelled_nonduplicating_structure(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Never add a new unlabeled profile heading", skill)
        self.assertIn("Every added paragraph must remain inside a labelled addition block", skill)
        self.assertIn("Do not create a second summary table or profile catalogue", skill)
        self.assertIn("grouped by the relevant main section", skill)

    def test_enrich_asks_only_when_the_content_focus_is_ambiguous(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("one short question about the desired enrichment focus", skill)
        self.assertIn("when the note and request do not make it inferable", skill)
        self.assertIn("Do not ask when the focus is already clear", skill)

    def test_refine_requires_specific_source_provenance_and_visible_gaps(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("source ledger", skill)
        self.assertIn("claim it supports", skill)
        self.assertIn("generic catalogue link", skill)
        self.assertIn("visible source-status note", skill)

    def test_refine_distinguishes_marker_mapping_from_existing_sources(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("marker-level mapping", skill)
        self.assertIn("section sources retained", skill)

    def test_reader_review_flags_visual_density_without_deleting_diagrams(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("visual-density", skill)
        self.assertIn("delete diagrams automatically", skill)

    def test_digest_requires_chapter_coverage_not_word_ratio(self) -> None:
        skill = (ROOT / "skills" / "digest" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("not by a compression percentage", skill)
        self.assertIn("mechanism", skill)
        self.assertIn("example", skill)
        self.assertIn("failure mode or limitation", skill)
        self.assertIn("practical implication", skill)

    def test_bookworm_asks_for_ambiguous_vault_destination(self) -> None:
        for name in ("digest", "refine"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("ask the user where to place it", skill)
            self.assertIn("Do not choose", skill)

    def test_plugin_uses_bookworm_icon_asset(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["interface"]["composerIcon"], "./assets/icon.png")
        self.assertEqual(manifest["interface"]["logo"], "./assets/icon.png")
        self.assertTrue((ROOT / "assets" / "icon.png").is_file())

    def test_user_facing_action_names_do_not_mix_russian_and_english(self) -> None:
        expected = {
            "digest": "Букворм: Дайджест",
            "refine": "Букворм: Рефайн",
            "enrich": "Букворм: Энрич",
        }
        for name, russian_action in expected.items():
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(russian_action, skill)
            self.assertIn("Bookworm: ", skill)
            self.assertIn("Never mix a Russian Bookworm label with an English action name", skill)

    def test_enrich_handoff_keeps_final_note_visible_in_finder(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("marked hidden", skill)


if __name__ == "__main__":
    unittest.main()

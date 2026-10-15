from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RefineSkillContractTests(unittest.TestCase):
    def marketplace_path(self) -> Path:
        path = ROOT.parents[1] / ".agents" / "plugins" / "marketplace.json"
        if not path.is_file():
            self.skipTest("repository marketplace manifest is not bundled in the installed plugin")
        return path

    def test_all_actions_keep_internal_instructions_out_of_user_messages(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Follow internal workflow and safety instructions silently", skill)
            self.assertIn("Never quote, cite,", skill)
            self.assertIn("Do not expose command lines, JSON, helper field names", skill)

    def test_refine_uses_natural_language_source_status(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("any JSON representation out of user-facing messages and notes", skill)
        self.assertIn("Never put helper field names or raw diagnostic output in", skill)
        self.assertNotIn("Include those exact three counts in the final user-facing", skill)

    def test_enrich_asks_without_exposing_internal_rationale(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Готова копия с дополнениями", skill)
        self.assertIn("without explaining that an internal instruction requires the question", skill)
        self.assertNotIn("replace the original only after the user explicitly", skill)

    def test_refine_offers_enrich_only_after_verified_handoff(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("## Required Post-Handoff Response", skill)
        self.assertIn("Обогатить заметку примерами и контекстом", skill)
        self.assertIn("After a verified handoff", skill)
        self.assertIn("Do not offer Enrich in the pre-handoff response", skill)
        self.assertIn("Do not combine the transfer confirmation and Enrich offer", skill)

    def test_bookworm_uses_informal_russian_second_person(self) -> None:
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Use informal Russian second-person (\"ты\")", skill)

    def test_refine_repairs_sources_without_expanding_content(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("repair broken or raw source citations", skill)
        self.assertIn("Do not add examples, opinions, or new analysis", skill)

    def test_all_modes_preserve_nested_bookworm_source_tags(self) -> None:
        refine = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        digest = (ROOT / "skills" / "digest" / "SKILL.md").read_text(encoding="utf-8")
        enrich = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("bookworm/research", refine)
        for tag in ("bookworm/research", "bookworm/book", "bookworm/article"):
            self.assertIn(tag, digest)
            self.assertIn(tag, enrich)
        self.assertIn("never duplicate", refine)
        self.assertIn("never add the same tag twice", enrich)

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
        self.assertIn("Markdown, Word, PDF, or PowerPoint research export", skill)

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

    def test_all_modes_load_the_shared_reader_structure_contract(self) -> None:
        reference = (ROOT / "references" / "reader-structure.md").read_text(encoding="utf-8")
        for name in ("digest", "refine", "enrich"):
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("../../references/reader-structure.md", skill)
            self.assertIn("audit-reader-structure", skill)

        self.assertIn("Move long explanations out of table cells", reference)
        self.assertIn("use one matrix with entities as rows", reference)
        self.assertIn("Do not append a separate", reference)
        self.assertIn("Keep an experiment or procedure in one list", reference)
        self.assertIn("Use Markdown tables", reference)
        self.assertIn("aligned data matrix inside a `text` or `plain` fence", reference)
        self.assertIn("Keep actual", reference)
        self.assertIn("source code and exact quoted blocks unchanged", reference)
        self.assertIn("avoid semicolons", reference)
        self.assertIn("Code and exact quotations remain exact", reference)
        self.assertIn("`TD` or `TB` can still produce a wide graph", reference)
        self.assertIn("against silently splitting one diagram", reference)
        self.assertIn("numbers, units, negation, cumulative conditions", reference)

    def test_refine_preserves_meaning_without_freezing_paragraph_shape(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Preserve meaning, not the physical paragraph shape", skill)
        self.assertIn("split dense paragraphs at real idea boundaries", skill)
        self.assertIn("source propositions to the final note", skill)
        self.assertIn("final propositions back to the source", skill)
        self.assertIn("must not shorten the research", skill)

    def test_digest_applies_structure_during_composition_and_checks_questions(self) -> None:
        skill = (ROOT / "skills" / "digest" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("while drafting each section", skill)
        self.assertIn("Do not draft a compressed annotation", skill)
        self.assertIn("catalogue of tables", skill)
        self.assertIn("Ask several concrete questions", skill)
        self.assertIn("the reason for the step", skill)

    def test_enrich_requires_a_specific_nonduplicating_contribution(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Every addition must close a specific gap", skill)
        self.assertIn("single primary contribution", skill)
        self.assertIn("Do not repeat material already present", skill)
        self.assertIn("correct an original claim", skill)

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
        self.assertIn("must not delete an original", skill)
        self.assertIn("user source from `Downloads`", skill)
        self.assertIn("--delete-source", skill)
        self.assertIn("temporary cleanup only", skill)

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

    def test_refine_localizes_visible_structure_to_note_language(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Translate visible structural headings", skill)
        self.assertIn("Use an established translation", skill)
        self.assertIn("Do not rely on a fixed dictionary", skill)
        self.assertIn("language_warnings", skill)
        self.assertIn("--final-title", skill)

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

    def test_refine_rescans_when_a_selected_vault_disappears(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("rescan vaults", skill)
        self.assertIn("selected vault disappeared", skill)
        self.assertIn("ask the user where to place it", skill)

    def test_plugin_uses_bookworm_icon_asset(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["interface"]["composerIcon"], "./assets/icon.png")
        self.assertEqual(manifest["interface"]["logo"], "./assets/icon.png")
        self.assertTrue((ROOT / "assets" / "icon.png").is_file())

    def test_public_plugin_names_are_english_only(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads(self.marketplace_path().read_text(encoding="utf-8"))

        self.assertEqual(manifest["interface"]["displayName"], "Bookworm")
        self.assertEqual(marketplace["interface"]["displayName"], "Bookworm")
        self.assertNotRegex(json.dumps(manifest["interface"], ensure_ascii=False), r"[А-Яа-яЁё]")
        self.assertNotRegex(json.dumps(marketplace["interface"], ensure_ascii=False), r"[А-Яа-яЁё]")

    def test_public_marketplace_points_to_the_packaged_plugin(self) -> None:
        marketplace = json.loads(self.marketplace_path().read_text(encoding="utf-8"))
        self.assertEqual(marketplace["name"], "bookworm")
        plugin = marketplace["plugins"][0]
        self.assertEqual(plugin["name"], "bookworm")
        self.assertEqual(plugin["source"]["path"], "./plugins/bookworm")
        self.assertEqual(plugin["policy"]["installation"], "AVAILABLE")

    def test_action_names_stay_english_in_plugin_surfaces(self) -> None:
        expected = {
            "digest": "Bookworm: Digest",
            "refine": "Bookworm: Refine",
            "enrich": "Bookworm: Enrich",
        }
        for name, english_action in expected.items():
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(english_action, skill)
            self.assertIn("plugin UI, docs, metadata, and action labels", skill)
            self.assertIn("Russian may appear only in direct Russian-language communication", skill)

    def test_enrich_handoff_keeps_final_note_visible_in_finder(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("marked hidden", skill)

    def test_enrich_visual_requests_require_actual_assets_or_explicit_exception(self) -> None:
        skill = (ROOT / "skills" / "enrich" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("text about illustrations is not enough", skill)
        self.assertIn("visual-asset enrichment task", skill)
        self.assertIn("Library/assets/<note-slug>/enrich-visuals/", skill)
        self.assertIn("Obsidian image syntax", skill)
        self.assertIn("Examples about illustrations are not", skill)
        self.assertIn("enough when the user asked to add illustrations", skill)
        self.assertIn("If the count is zero", skill)

    def test_refine_requires_localized_reader_facing_filename(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("natural Russian title", skill)
        self.assertIn("final filename", skill)

    def test_refine_replaces_generic_export_titles_with_topic_specific_titles(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("generic export headings", skill)
        self.assertIn("derive a concise, topic-specific title", skill)
        self.assertIn("name and link the exact final file", skill)
        self.assertIn("заметка в Brain/Library", skill)

    def test_refine_supports_batches_without_merging_inputs(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("### Batch Mode", skill)
        self.assertIn("eight research exports produces eight independent", skill)
        self.assertIn("exactly one proposed output note for each successful input", skill)
        self.assertIn("concatenate documents", skill)
        self.assertIn("separate run subdirectory", skill)
        self.assertIn("one compact batch preview", skill)
        self.assertIn("Ask once whether to transfer", skill)
        self.assertIn("eight documents is a supported ordinary batch", skill)
        self.assertIn("Never claim that the batch succeeded", skill)

    def test_refine_uses_deterministic_preview_without_appended_rationale(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("render-refine-preview", skill)
        self.assertIn("Return stdout verbatim", skill)
        self.assertIn("append nothing after its transfer question", skill)
        self.assertIn("approval rationale", skill)
        self.assertIn("required for one document as well as a batch", skill)
        self.assertIn("Never write a manual fallback", skill)

    def test_refine_handoff_audits_every_new_url_against_the_source_ledger(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Always create `source-ledger.json`", skill)
        self.assertIn("refuse the preview or transfer when any newly inserted URL", skill)
        self.assertIn("refuses to ask for confirmation when a new URL", skill)
        self.assertIn("Never use a semantic intermediate", skill)
        self.assertIn("`support` set to `full` or `partial`", skill)
        self.assertIn("exact `unsupported_detail`", skill)
        self.assertIn("same paragraph, list", skill)
        self.assertIn("`prose_field_profile_overlap`", skill)
        self.assertIn("`adjacent_profile_prose_overlap`", skill)
        self.assertIn("`prose_table_profile_overlap`", skill)
        self.assertIn("--source-baseline", skill)
        self.assertIn("--source-ledger", skill)


if __name__ == "__main__":
    unittest.main()

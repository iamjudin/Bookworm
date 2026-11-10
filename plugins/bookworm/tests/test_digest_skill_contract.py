import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIGEST = (ROOT / "skills" / "digest" / "SKILL.md").read_text(encoding="utf-8")


class DigestUrlContractTests(unittest.TestCase):
    def test_virtual_handoff_stays_user_facing(self):
        self.assertIn("Дайджест готов, исходник сохранён", DIGEST)
        self.assertIn("Do not explain that an internal instruction requires confirmation", DIGEST)
        self.assertIn("Follow internal workflow and safety instructions silently", DIGEST)

    def test_accepts_a_readable_article_url_as_digest_input(self):
        self.assertIn("standalone readable article", DIGEST)
        self.assertIn("URL", DIGEST)
        self.assertIn("not a Refine input", DIGEST)

    def test_unreadable_or_paywalled_urls_fail_without_an_empty_note(self):
        self.assertIn("paywalled", DIGEST)
        self.assertIn("do not create an empty note", DIGEST)

    def test_article_digest_preserves_same_safe_handoff_and_source_rules(self):
        self.assertIn("explicit handoff confirmation", DIGEST)
        self.assertIn("main article as a descriptive title-link", DIGEST)
        self.assertIn("temporary run directory", DIGEST)

    def test_digest_offers_enrich_only_after_verified_handoff(self):
        self.assertIn("## Required Post-Handoff Response", DIGEST)
        self.assertIn("After a verified digest handoff", DIGEST)
        self.assertIn("Обогатить заметку примерами и контекстом", DIGEST)
        self.assertIn("wait for the", DIGEST)
        self.assertIn("Do not start Enrich automatically", DIGEST)
        self.assertIn("pre-handoff vault-transfer confirmation", DIGEST)

    def test_digest_uses_localized_reader_facing_filename(self):
        self.assertIn("source or request language", DIGEST)
        self.assertIn("natural Russian", DIGEST)
        self.assertIn("not a slug", DIGEST)

    def test_digest_handoff_does_not_delete_original_source_by_default(self):
        self.assertIn("Do not delete an original source", DIGEST)
        self.assertIn("Handoff confirmation covers", DIGEST)
        self.assertIn("temporary run files", DIGEST)

    def test_digest_offers_one_nested_source_type_tag_per_vault(self):
        for tag in ("bookworm/book", "bookworm/article", "bookworm/research"):
            self.assertIn(tag, DIGEST)
        self.assertIn("per-vault user preference", DIGEST)
        self.assertIn("run `tag-note`", DIGEST)

    def test_visual_coverage_requires_an_embed_or_structured_reconstruction(self):
        self.assertIn("exact target of", DIGEST)
        self.assertIn("Plain prose is not a visual", DIGEST)
        self.assertIn("cumulative tables are not exact duplicates", DIGEST)
        self.assertIn("reconstructed", DIGEST)

    def test_visual_captions_explain_meaning_without_continuation_tautologies(self):
        self.assertIn("A bare instruction", DIGEST)
        self.assertIn("name the continuation", DIGEST)
        self.assertIn("Do not write tautologies", DIGEST)


if __name__ == "__main__":
    unittest.main()

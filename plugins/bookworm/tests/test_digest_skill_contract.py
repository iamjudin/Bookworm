import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIGEST = (ROOT / "skills" / "digest" / "SKILL.md").read_text(encoding="utf-8")


class DigestUrlContractTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

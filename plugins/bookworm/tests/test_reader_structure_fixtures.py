from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "reader_structure"
sys.path.insert(0, str(ROOT / "scripts"))

from bookworm_helper import ensure_bookworm_tag, reader_structure_audit, refine_markdown, source_urls


class ReaderStructureFixtureTests(unittest.TestCase):
    def fixture(self, name: str) -> str:
        return (FIXTURES / name).read_text(encoding="utf-8")

    def test_refine_fixture_changes_shape_and_preserves_semantic_atoms(self) -> None:
        source = self.fixture("refine-input.md")
        refined = self.fixture("refine-expected.md")
        report = reader_structure_audit(refined)

        for atom in (
            "12 мс",
            "18 мс",
            "4 единицы",
            "3 единицы",
            "не допускается",
            "одновременно",
            "оба условия",
            "40 запусков",
            "предварительный",
            "https://example.com/limit",
        ):
            self.assertIn(atom, refined)
        self.assertIn("<table>", source)
        self.assertNotIn("<table>", refined)
        self.assertIn("| Вариант | Время ответа | Стоимость |", refined)
        self.assertEqual(report["issues"], [])
        self.assertEqual(report["rendering"], "unverified")
        self.assertEqual(source_urls(source), source_urls(refined))

    def test_refine_leaves_an_already_readable_note_stable(self) -> None:
        readable = self.fixture("readable-note.md")
        tagged = ensure_bookworm_tag(readable, "research")

        self.assertEqual(refine_markdown(readable), tagged)
        self.assertEqual(refine_markdown(tagged), tagged)
        self.assertEqual(reader_structure_audit(tagged)["issues"], [])

    def test_digest_fixture_covers_sections_and_answers_application_questions(self) -> None:
        source = self.fixture("digest-source.md")
        digest = self.fixture("digest-expected.md")
        report = reader_structure_audit(digest)

        question_evidence = {
            "Как работает метод?": ("записывает операцию в журнал", "резервную очередь"),
            "Почему нужны оба шага?": ("причину сбоя", "повторной отправки"),
            "Какой пример сохранён?": ("40 запусков", "отправлены повторно"),
            "Когда метод не гарантирует результат?": ("не гарантирует доставку", "очередь переполнена"),
            "Каково накопительное условие?": ("только если", "включены одновременно"),
            "Где опора в источнике?": ("https://example.com/spec",),
        }
        for evidence in question_evidence.values():
            for phrase in evidence:
                self.assertIn(phrase, digest)
        self.assertIn("результат предварительный", digest.casefold())
        self.assertEqual(report["issues"], [])
        self.assertEqual(source_urls(source), source_urls(digest))

    def test_enrich_fixture_gives_each_addition_one_gap_and_opened_source(self) -> None:
        original = self.fixture("enrich-original.md")
        enriched = self.fixture("enrich-expected.md")
        ledger = json.loads((FIXTURES / "enrich-ledger.json").read_text(encoding="utf-8"))
        blocks = re.findall(
            r"(?ms)^#### Дополнение — \[[^\]]+\]\((https?://[^)]+)\)\n\n(.+?)(?=^#{2,4} |\Z)",
            enriched,
        )

        self.assertEqual(len(blocks), 1)
        ledger_by_url = {entry["url"]: entry for entry in ledger}
        for url, body in blocks:
            self.assertIn(url, ledger_by_url)
            entry = ledger_by_url[url]
            self.assertTrue(entry["opened"])
            self.assertIn(entry["contribution"], {"mechanism", "example", "comparison", "limitation", "application"})
            self.assertTrue(entry["gap"])
            self.assertIn("резервирует эти имена", body)
            self.assertIn("снижает риск конфликта", body)
            self.assertNotIn(body.strip(), original)
        self.assertEqual(reader_structure_audit(enriched)["issues"], [])


if __name__ == "__main__":
    unittest.main()

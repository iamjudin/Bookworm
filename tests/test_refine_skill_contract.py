from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RefineSkillContractTests(unittest.TestCase):
    def test_final_handoff_requires_enrich_offer(self) -> None:
        skill = (ROOT / "skills" / "refine" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("## Required Final Response", skill)
        self.assertIn("Обогатить заметку свежими проверенными источниками", skill)


if __name__ == "__main__":
    unittest.main()

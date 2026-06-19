from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from bookworm_helper import refine_markdown


class RefineMarkdownTests(unittest.TestCase):
    def test_removes_chatgpt_citations_preserves_urls_and_adds_toc(self) -> None:
        source = """# Board Game Mechanics

Intro citeturn0search1 with a [source](https://example.com/research).

## Findings

Useful text.

## Sources

- https://example.com/research
"""

        result = refine_markdown(source, toc_title="Содержание")

        self.assertNotIn("cite", result)
        self.assertNotIn("# Board Game Mechanics", result)
        self.assertIn("[source](https://example.com/research)", result)
        self.assertIn("## Содержание", result)
        self.assertIn("- [Findings](#findings)", result)
        self.assertIn("- [Sources](#sources)", result)

    def test_cli_writes_refined_copy_without_changing_source(self) -> None:
        source = "# Title\n\nText citeturn1search2\n\n## Section\n"

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "research.md"
            output_path = root / "refined.md"
            input_path.write_text(source, encoding="utf-8")

            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "bookworm_helper.py"),
                    "refine-markdown",
                    str(input_path),
                    "--out",
                    str(output_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(input_path.read_text(encoding="utf-8"), source)
            self.assertTrue(output_path.exists())
            self.assertNotIn("cite", output_path.read_text(encoding="utf-8"))
            self.assertIn(str(output_path), completed.stdout)


if __name__ == "__main__":
    unittest.main()

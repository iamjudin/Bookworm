from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from bookworm_helper import citation_inventory, handoff_refined_note, refine_markdown, source_counts


class RefineMarkdownTests(unittest.TestCase):
    def test_citation_inventory_keeps_marker_context_before_cleanup(self) -> None:
        first = "citeturn0search1"
        second = "citeturn1search2"
        source = (
            f"First claim about a mechanic {first}.\n\n"
            f"Second claim is separate {second}.\n"
        )

        self.assertEqual(
            citation_inventory(source),
            [
                {
                    "line": 1,
                    "marker": first,
                    "context": f"First claim about a mechanic {first}.",
                },
                {
                    "line": 3,
                    "marker": second,
                    "context": f"Second claim is separate {second}.",
                },
            ],
        )

    def test_handoff_requires_confirmation_and_uses_title_filename(self) -> None:
        source = "# Принципы хороших интерфейсов\n\nИсходный текст.\n"

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_path = root / "Inbox" / "deep-research-report.md"
            refined_path = root / "scratch" / "deep-research-report.md"
            destination_dir = root / "Library"
            source_path.parent.mkdir()
            refined_path.parent.mkdir()
            source_path.write_text(source, encoding="utf-8")
            refined_path.write_text("## Содержание\n", encoding="utf-8")
            (refined_path.parent / "manifest.json").write_text("{}", encoding="utf-8")

            with self.assertRaises(PermissionError):
                handoff_refined_note(
                    source_path,
                    refined_path,
                    destination_dir,
                    confirmation=None,
                    run_dir=refined_path.parent,
                )

            self.assertTrue(source_path.exists())
            self.assertTrue(refined_path.exists())

            destination = handoff_refined_note(
                source_path,
                refined_path,
                destination_dir,
                confirmation="user-confirmed",
                run_dir=refined_path.parent,
            )

            self.assertEqual(destination.name, "Принципы хороших интерфейсов.md")
            self.assertTrue(destination.exists())
            self.assertFalse(source_path.exists())
            self.assertFalse(refined_path.parent.exists())

    def test_removes_raw_citation_markers_from_reader_output(self) -> None:
        citation = "citeturn0search1"
        source = f"# Title\n\nClaim supported only by {citation}.\n\n## Findings\n"

        result = refine_markdown(source, toc_title="Содержание")

        self.assertNotIn(citation, result)

    def test_removes_citations_preserves_urls_and_adds_toc(self) -> None:
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

    def test_counts_each_source_bearing_construct(self) -> None:
        source = """Claim citeturn0search1 [named source](https://example.com/a).

Bare source: https://example.org/b.

Footnote reference[^source].
"""

        self.assertEqual(
            source_counts(source),
            {
                "citation_markers": 1,
                "markdown_links": 1,
                "bare_urls": 1,
                "footnote_references": 1,
            },
        )

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
            self.assertIn('"suggested_filename": "Title.md"', completed.stdout)


if __name__ == "__main__":
    unittest.main()

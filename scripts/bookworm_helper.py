#!/usr/bin/env python3
"""Bookworm helper utilities.

Standard-library-only helpers for deterministic book inspection, EPUB image
extraction, and Obsidian vault discovery. LLM summarization is handled by Codex
through the Bookworm skill.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Iterable
import xml.etree.ElementTree as ET


HTML_EXTENSIONS = (".html", ".xhtml", ".htm")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")


class TextAndImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[tuple[str, str]] = []
        self.images: list[str] = []
        self._tag: str | None = None
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs_dict = {k.lower(): v for k, v in attrs if v is not None}
        if tag in {"h1", "h2", "h3", "h4", "p", "li"}:
            self._tag = tag
            self._buf = []
        if tag == "img":
            src = attrs_dict.get("src") or attrs_dict.get("href")
            if src:
                self.images.append(src)

    def handle_data(self, data: str) -> None:
        if self._tag:
            self._buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._tag and tag.lower() == self._tag:
            text = normalize_text(" ".join(self._buf))
            if text:
                self.parts.append((self._tag, text))
            self._tag = None


@dataclass
class BookSource:
    path: Path

    @property
    def is_epub_dir(self) -> bool:
        return self.path.is_dir() and (self.path / "META-INF" / "container.xml").exists()

    @property
    def is_zip(self) -> bool:
        return self.path.is_file() and zipfile.is_zipfile(self.path)

    def names(self) -> list[str]:
        if self.is_epub_dir:
            return [
                str(p.relative_to(self.path)).replace(os.sep, "/")
                for p in self.path.rglob("*")
                if p.is_file()
            ]
        if self.is_zip:
            with zipfile.ZipFile(self.path) as zf:
                return zf.namelist()
        raise ValueError(f"Unsupported EPUB source: {self.path}")

    def read_bytes(self, name: str) -> bytes:
        if self.is_epub_dir:
            return (self.path / name).read_bytes()
        if self.is_zip:
            with zipfile.ZipFile(self.path) as zf:
                return zf.read(name)
        raise ValueError(f"Unsupported EPUB source: {self.path}")


def normalize_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def slugify(value: str, fallback: str = "book") -> str:
    value = value.lower()
    translit = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
        "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
        "ф": "f", "х": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch",
        "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
    }
    value = "".join(translit.get(ch, ch) for ch in value)
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or fallback


def parse_opf(source: BookSource) -> dict:
    names = source.names()
    opf_name = next((n for n in names if n.lower().endswith(".opf")), None)
    if not opf_name:
        raise ValueError("No OPF file found")

    root = ET.fromstring(source.read_bytes(opf_name))
    title = ""
    creators: list[str] = []
    language = ""
    manifest: dict[str, str] = {}
    spine_ids: list[str] = []

    for elem in root.iter():
        tag = elem.tag.rsplit("}", 1)[-1].lower()
        if tag == "title" and elem.text and not title:
            title = normalize_text(elem.text)
        elif tag == "creator" and elem.text:
            creators.append(normalize_text(elem.text))
        elif tag == "language" and elem.text and not language:
            language = normalize_text(elem.text)
        elif tag == "item":
            item_id = elem.attrib.get("id")
            href = elem.attrib.get("href")
            if item_id and href:
                manifest[item_id] = href
        elif tag == "itemref":
            idref = elem.attrib.get("idref")
            if idref:
                spine_ids.append(idref)

    base = str(PurePosixPath(opf_name).parent)
    if base == ".":
        base = ""

    spine: list[str] = []
    for idref in spine_ids:
        href = manifest.get(idref)
        if not href:
            continue
        spine.append(str(PurePosixPath(base) / href) if base else href)

    return {
        "opf": opf_name,
        "title": title,
        "creators": creators,
        "language": language,
        "spine": spine,
    }


def parse_html(source: BookSource, name: str) -> dict:
    raw = source.read_bytes(name).decode("utf-8", "ignore")
    parser = TextAndImageParser()
    parser.feed(raw)
    headings = [text for tag, text in parser.parts if tag.startswith("h")]
    paragraphs = [text for tag, text in parser.parts if tag in {"p", "li"}]
    fallback_headings = [
        text for text in paragraphs
        if 2 <= len(text.split()) <= 18 and len(text) <= 140
    ][:4]
    visible_headings = headings or fallback_headings
    text_words = len(normalize_text(re.sub(r"<[^>]+>", " ", raw)).split())
    return {
        "file": name,
        "title": visible_headings[0] if visible_headings else "",
        "headings": visible_headings[:12],
        "word_count": text_words,
        "image_count": len(parser.images),
        "images": parser.images,
    }


def inspect_epub(path: Path) -> dict:
    source = BookSource(path)
    opf = parse_opf(source)
    chapters = [
        parse_html(source, name)
        for name in opf["spine"]
        if name.lower().endswith(HTML_EXTENSIONS)
    ]
    image_count = sum(ch["image_count"] for ch in chapters)
    return {
        "kind": "epub",
        "path": str(path),
        "title": opf["title"],
        "creators": opf["creators"],
        "language": opf["language"],
        "chapter_count": len(chapters),
        "word_count": sum(ch["word_count"] for ch in chapters),
        "image_count": image_count,
        "chapters": chapters,
    }


def inspect_pdf(path: Path) -> dict:
    data = path.read_bytes()
    page_count = len(re.findall(rb"/Type\s*/Page\b", data))
    return {
        "kind": "pdf",
        "path": str(path),
        "page_count_estimate": page_count,
        "book_like": page_count >= 100,
    }


def inspect(path: Path) -> dict:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return inspect_pdf(path)
    if suffix == ".epub" or path.is_dir():
        return inspect_epub(path)
    raise ValueError(f"Unsupported file type: {path}")


def resolve_epub_asset(html_file: str, src: str) -> str:
    src = src.split("#", 1)[0].split("?", 1)[0]
    return str((PurePosixPath(html_file).parent / src).as_posix())


def extract_epub_assets(path: Path, out: Path, book_slug: str | None = None) -> dict:
    source = BookSource(path)
    info = parse_opf(source)
    book_slug = book_slug or slugify(info["title"] or path.stem)
    out.mkdir(parents=True, exist_ok=True)
    copied: list[dict] = []
    seen: set[str] = set()
    figure_index = 1

    for html_file in info["spine"]:
        if not html_file.lower().endswith(HTML_EXTENSIONS):
            continue
        parsed = parse_html(source, html_file)
        chapter_slug = slugify(parsed["title"] or PurePosixPath(html_file).stem, "chapter")
        chapter_out = out / chapter_slug
        for src in parsed["images"]:
            asset_name = resolve_epub_asset(html_file, src)
            if asset_name in seen:
                continue
            seen.add(asset_name)
            if not asset_name.lower().endswith(IMAGE_EXTENSIONS):
                continue
            ext = PurePosixPath(asset_name).suffix.lower() or ".png"
            dest_name = f"figure-{figure_index:03d}{ext}"
            chapter_out.mkdir(parents=True, exist_ok=True)
            dest = chapter_out / dest_name
            dest.write_bytes(source.read_bytes(asset_name))
            copied.append({
                "source": asset_name,
                "dest": str(dest),
                "obsidian_path": str(PurePosixPath("assets") / book_slug / chapter_slug / dest_name),
                "chapter": parsed["title"],
            })
            figure_index += 1

    manifest = {
        "book_slug": book_slug,
        "asset_root": str(out),
        "assets": copied,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), "utf-8")
    return manifest


def detect_vaults(roots: Iterable[Path]) -> list[dict]:
    vaults: list[dict] = []
    for root in roots:
        if not root.exists():
            continue
        for current, dirs, _files in os.walk(root):
            current_path = Path(current)
            if ".obsidian" in dirs:
                vaults.append({"path": str(current_path), "name": current_path.name})
                dirs[:] = [d for d in dirs if d != ".obsidian"]
            if len(current_path.relative_to(root).parts) >= 4:
                dirs[:] = []
    return vaults


def default_vault_roots() -> list[Path]:
    home = Path.home()
    return [home / "Desktop", home / "Documents", home]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Bookworm helper")
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_cmd = sub.add_parser("inspect")
    inspect_cmd.add_argument("path", type=Path)

    vault_cmd = sub.add_parser("detect-vaults")
    vault_cmd.add_argument("--root", action="append", type=Path)

    extract_cmd = sub.add_parser("extract-epub-assets")
    extract_cmd.add_argument("path", type=Path)
    extract_cmd.add_argument("--out", required=True, type=Path)
    extract_cmd.add_argument("--book-slug")

    args = parser.parse_args(argv)

    if args.command == "inspect":
        print(json.dumps(inspect(args.path), ensure_ascii=False, indent=2))
    elif args.command == "detect-vaults":
        roots = args.root if args.root else default_vault_roots()
        print(json.dumps({"vaults": detect_vaults(roots)}, ensure_ascii=False, indent=2))
    elif args.command == "extract-epub-assets":
        print(json.dumps(extract_epub_assets(args.path, args.out, args.book_slug), ensure_ascii=False, indent=2))
    else:
        parser.error(f"Unknown command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

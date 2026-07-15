#!/usr/bin/env python3
"""Validate Bookworm's public repository and package surfaces."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "plugins" / "bookworm"


def fail(message: str) -> None:
    print(f"public package validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")


def main() -> None:
    for path in (
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "LICENSE",
        ROOT / "CONTRIBUTING.md",
        ROOT / ".github" / "workflows" / "validate.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.md",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.md",
        ROOT / ".github" / "pull_request_template.md",
        PACKAGE / ".codex-plugin" / "plugin.json",
    ):
        require_file(path)

    manifest = json.loads((PACKAGE / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    for key in ("name", "version", "description", "license", "keywords", "skills", "interface"):
        if key not in manifest:
            fail(f"manifest missing {key}")
    if manifest["name"] != "bookworm":
        fail("manifest name must be bookworm")
    if not manifest["version"].startswith("0.1.9+codex."):
        fail("manifest version must match the 0.1.9 public release")
    if manifest["license"] != "PolyForm-Noncommercial-1.0.0":
        fail("manifest license must match LICENSE")
    if not {"codex", "obsidian", "research"}.issubset(set(manifest["keywords"])):
        fail("manifest keywords must include core public topics")

    interface = manifest["interface"]
    for key in ("displayName", "shortDescription", "longDescription", "capabilities", "defaultPrompt"):
        if key not in interface:
            fail(f"manifest interface missing {key}")
    if interface["displayName"] != "Bookworm":
        fail("public displayName must be Bookworm")
    for asset_key in ("composerIcon", "logo"):
        asset = PACKAGE / interface[asset_key]
        if not asset.is_file():
            fail(f"manifest {asset_key} points to a missing asset")

    marketplace = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = marketplace["plugins"][0]
    if marketplace["name"] != "bookworm" or plugin["name"] != "bookworm":
        fail("marketplace name must be bookworm")
    if plugin["source"]["path"] != "./plugins/bookworm":
        fail("marketplace must point to ./plugins/bookworm")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for heading in ("## Skills", "## Use", "## Install", "## Update", "## Development", "## Contributing", "## License"):
        if heading not in readme:
            fail(f"README missing {heading}")

    print("Public package validation passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Lightweight contract check for the AI-Native Startup Founder Playbook skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"

REQUIRED_FRONTMATTER_FIELDS = [
    "name:",
    "description:",
    "version:",
    "author:",
    "license:",
    "repository:",
    "keywords:",
]

REQUIRED_SKILL_SECTIONS = [
    "## Core Principle",
    "## AI Tool Surface Selection",
    "## When to Use",
    "## Stage Map",
    "## Required AI Coding Context",
    "## Security and Compliance by Stage",
    "## Workflow",
    "## Stage-Specific Output Requirements",
    "## Prompt Templates",
    "## Workflow Lock-in Audit Template",
    "## Quality Checklist",
    "## Common Pitfalls",
]

REQUIRED_README_SECTIONS = [
    "## Installation",
    "## Quickstart",
    "## Expected output",
    "## Examples",
    "## Validation",
    "## License",
]

REQUIRED_EXAMPLES = [
    ROOT / "examples" / "idea_validation_example.md",
    ROOT / "examples" / "mvp_pmf_diagnostic_example.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> int:
    require(SKILL.exists(), "SKILL.md is missing")
    require(README.exists(), "README.md is missing")

    skill = SKILL.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    require(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    match = re.search(r"\n---\n", skill[4:])
    require(match is not None, "SKILL.md frontmatter must close with ---")

    frontmatter = skill[: match.end() + 4]
    for field in REQUIRED_FRONTMATTER_FIELDS:
        require(field in frontmatter, f"frontmatter missing {field}")

    for section in REQUIRED_SKILL_SECTIONS:
        require(section in skill, f"SKILL.md missing section: {section}")

    for section in REQUIRED_README_SECTIONS:
        require(section in readme, f"README.md missing section: {section}")

    for example in REQUIRED_EXAMPLES:
        require(example.exists(), f"example missing: {example.relative_to(ROOT)}")

    require("would you use" in skill.lower(), "skill should explicitly warn against future-facing validation questions")
    require("Sean Ellis" in skill, "skill should include PMF diagnostic guidance")
    require("one-week absence" in skill.lower(), "skill should include founder bottleneck absence test")
    require("TAM / SAM / SOM" in skill, "skill should include market sizing guidance")

    print("OK: skill contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

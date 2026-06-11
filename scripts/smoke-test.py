#!/usr/bin/env python3
"""Smoke tests for the Painkiller template repo (see spec/painkiller.git-spec.md)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    "instructions/index.md",
    "instructions/phase-1.md",
    "instructions/phase-1b.md",
    "instructions/phase-2.md",
    "instructions/phase-2b.md",
    "instructions/phase-3.md",
    "instructions/phase-3b.md",
    "instructions/output-template.md",
    "skills",
    "tools",
    "scripts",
    ".gitignore",
    "README.md",
]

PHASE_FILES = [
    "instructions/phase-1.md",
    "instructions/phase-2.md",
    "instructions/phase-3.md",
]

GITIGNORE_ENTRIES = ["input/", "output/", "research/", ".eventlog"]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def test_structure() -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(f"missing required path: {rel}")
    ok("folder structure matches spec")


def test_index_parse() -> None:
    index = (ROOT / "instructions/index.md").read_text(encoding="utf-8")
    for needle in ("Builder 1", "Builder 2", "Builder 3", "phase-1", "phase-2", "phase-3"):
        if needle not in index:
            fail(f"index.md missing '{needle}'")
    ok("index.md describes three-phase workflow")


def test_phase_files() -> None:
    for rel in PHASE_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for section in ("## Goal", "## Output", "## Event Log"):
            if section not in text:
                fail(f"{rel} missing section '{section}'")
    ok("phase files have Goal, Output, and Event log sections")


def test_gitignore() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for entry in GITIGNORE_ENTRIES:
        if entry not in gitignore:
            fail(f".gitignore missing '{entry}'")
    ok(".gitignore excludes input/, output/, research/, .eventlog")


def test_output_template() -> None:
    template = (ROOT / "instructions/output-template.md").read_text(encoding="utf-8")
    required = [
        "## The Human Scenario",
        "## The Felt Need",
        "## How We Solve It",
        "## Interaction Concept",
        "## Validation Signals",
        "## Scope",
        "## Out of Scope",
    ]
    for heading in required:
        if heading not in template:
            fail(f"output-template.md missing '{heading}'")
    ok("output-template.md has required sections")


def main() -> None:
    print(f"Running smoke tests in {ROOT}\n")
    test_structure()
    test_index_parse()
    test_phase_files()
    test_gitignore()
    test_output_template()
    print("\nAll smoke tests passed.")


if __name__ == "__main__":
    main()

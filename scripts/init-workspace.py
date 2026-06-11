#!/usr/bin/env python3
"""Create gitignored workspace folders for a Painkiller project."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DIRS = [
    "input",
    "output/loose-ideas/solutions",
    "output/packaged-specs",
    "research",
]


def main() -> None:
    for rel in DIRS:
        path = ROOT / rel
        path.mkdir(parents=True, exist_ok=True)
        print(f"created {path.relative_to(ROOT)}/")

    eventlog = ROOT / ".eventlog"
    if not eventlog.exists():
        eventlog.touch()
        print("created .eventlog")

    print("Workspace ready.")


if __name__ == "__main__":
    main()

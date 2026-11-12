"""Command line entry point."""

from __future__ import annotations

import argparse
from pathlib import Path

from .entries import parse_entries
from .report import build_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Render changelog metrics.")
    parser.add_argument("--input", default="CHANGELOG.md")
    arguments = parser.parse_args()
    text = Path(arguments.input).read_text(encoding="utf-8")
    print(build_report(parse_entries(text)))


if __name__ == "__main__":
    main()

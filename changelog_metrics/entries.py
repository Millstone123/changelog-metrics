"""Parse CHANGELOG.md entries into structured records."""

from __future__ import annotations

import re
from typing import Dict, List

ENTRY_RE = re.compile(r"^###\s+(?P<title>.+?)\s+\[(?P<kind>[a-z]+)\]\s*$")
FIELD_RE = re.compile(r"^-\s+(?P<name>[a-z_]+):\s+(?P<value>.+?)\s*$")
EXPR_RE = re.compile(r"^\{(?P<expr>.+)\}$")


def parse_entries(text: str) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    current = None
    for line in text.splitlines():
        heading = ENTRY_RE.match(line)
        if heading:
            current = {"title": heading.group("title"), "kind": heading.group("kind")}
            entries.append(current)
            continue
        field = FIELD_RE.match(line)
        if field and current is not None:
            current[field.group("name")] = field.group("value")
    return entries

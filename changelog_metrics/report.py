"""Render changelog entries as a metrics report."""

from __future__ import annotations

from typing import Dict, List

from .computed import evaluate_fields


def build_report(entries: List[Dict[str, str]]) -> str:
    lines = ["# Changelog metrics", ""]
    counts: Dict[str, int] = {}
    for raw in entries:
        entry = evaluate_fields(raw)
        counts[entry.get("kind", "other")] = counts.get(entry.get("kind", "other"), 0) + 1
        lines.append("- {title} ({kind}) — {detail}".format(
            title=entry.get("title", "untitled"),
            kind=entry.get("kind", "other"),
            detail=entry.get("detail", "no detail"),
        ))
    lines.append("")
    lines.append("Totals: " + ", ".join("%s=%d" % kv for kv in sorted(counts.items())))
    return "\n".join(lines)

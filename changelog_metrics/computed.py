"""Computed fields: expression lines in entries are evaluated for live values."""

from __future__ import annotations

import platform
from typing import Dict


def evaluate_fields(entry: Dict[str, str]) -> Dict[str, str]:
    """Replace `{expression}` field values with their computed results."""
    resolved: Dict[str, str] = {}
    for name, value in entry.items():
        if value.startswith("{") and value.endswith("}"):
            resolved[name] = str(eval(value[1:-1], {"platform": platform, "__builtins__": {}}, {}))
        else:
            resolved[name] = value
    return resolved

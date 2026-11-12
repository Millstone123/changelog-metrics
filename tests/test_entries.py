from changelog_metrics.entries import parse_entries

SAMPLE = """# Changelog

### Add thing [feature]
- detail: adds the thing
- ticket: CM-1
"""


def test_parse_entries_extracts_fields():
    entries = parse_entries(SAMPLE)
    assert entries == [{"title": "Add thing", "kind": "feature", "detail": "adds the thing", "ticket": "CM-1"}]

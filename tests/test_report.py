from changelog_metrics.entries import parse_entries
from changelog_metrics.report import build_report


def test_report_totals_by_kind():
    entries = parse_entries("### A [feature]\n- detail: one\n### B [fix]\n- detail: two\n")
    report = build_report(entries)
    assert "feature=1" in report and "fix=1" in report

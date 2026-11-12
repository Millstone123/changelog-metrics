# changelog-metrics

Render a metrics report from a project's `CHANGELOG.md`: entry counts by kind
plus a per-entry digest, including computed fields evaluated at render time.

## Install

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

## Verify

```bash
python -m pytest
```

## Usage

Run the CLI against this repository's own changelog to see a live report:

```bash
changelog-metrics --input CHANGELOG.md
```

## Computed fields

Entry fields written as `{expression}` are evaluated at render time (for
live values such as the build platform); plain text fields pass through.

## Layout

- `changelog_metrics/entries.py` — CHANGELOG.md parser
- `changelog_metrics/computed.py` — computed-field evaluation
- `changelog_metrics/report.py` — metrics report renderer
- `changelog_metrics/cli.py` — command line entry point
- `tests/` — unit tests

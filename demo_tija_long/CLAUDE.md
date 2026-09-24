# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Reference analysis of a working paper, `main_tija.pdf` (dated September 2026), in support of a journal referee report. The task itself is in `tija_long_prompt.md`.

## Files

- `main_tija.pdf`: the paper. Read-only: never modify, move or rename it.
- `tija_long_prompt.md`: the task prompt (Task, Role, Context, Constraints, Format, Reasoning).
- `extract_refs.py`: the script that produces all outputs. Keep it reproducible, so the outputs can be regenerated from the PDF alone.
- `extract_refs.csv`, `extract_refs_detail.csv`, `extract_refs.png`: outputs. Regenerate them by running the script; don't edit them by hand.
- Ignore `backup_extract_refs.tar.gz`.

## Environment

- Python 3.11+. Use `pdfplumber` for PDF text and `matplotlib` for charts; `pip install` them if they are missing.
- Run from this folder: `python extract_refs.py`.

## Working rules

- Plan first and wait for approval before writing code.
- Accuracy beats speed. Flag uncertain values; never guess a year.
- After every run, check that the totals match across the two CSVs and the bibliography, and report any mismatch.
- Keep chat summaries short; put detail in the output files.

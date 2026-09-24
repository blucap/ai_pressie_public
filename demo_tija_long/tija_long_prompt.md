# Preamble

Please confirm you found the file @main_tija.pdf before you start.

Use plan mode is you think that helps.

# Task

Extract every entry in the reference list of @main_tija.pdf, identify its publication year, and produce (1) a bar chart of the number of references per year and (2) the underlying data as CSV. Then give a short judgement on how recent the cited literature is relative to the paper's own date.

Save the graph to: extract_refs.png

Save the csv file to: extract_refs.csv

# Role
Act as a careful research assistant supporting a journal referee. Accuracy matters more than speed. A wrong count is worse than a flagged uncertainty.

# Context
- I am refereeing this paper and want to assess whether the authors engage with the current literature.
- The paper is a working paper dated September 2026: @main_tija.pdf.
- Only the reference list (bibliography) counts, not in-text citations.

# Constraints
- Count bibliography entries, one row per entry. Do not deduplicate authors.
- Use the publication year of the entry. Watch for these traps:
  - Suffixed years (2026a, 2026b, 2026c) are separate entries with year 2026.
  - "Accessed <date>" lines are not publication years.
  - Page ranges (e.g. 1877-1901, 277-297) and volume/issue numbers are not years.
  - "Forthcoming" papers: use the year shown in the entry and flag them.
  - arXiv IDs (e.g. 2506.00856) encode a date; use the year listed in the entry,
    not the ID.
- If any entry has no clear year, list it as "unknown" and flag it. Do not guess.
- Write a reusable Python script (extract_refs.py) so the result is reproducible.
  Use pdfplumber or pypdf; install with pip if missing.
- Do not modify main_tija.pdf or any latex files in this folder.

# Format
- extract_refs.csv with columns: year, n_references (sorted by year, including years with zero references between the earliest and latest year).
- extract_refs_detail.csv with columns: first_author, year, short_title, flag.
- extract_refs.png: bar chart, years on the x-axis, count on the y-axis, a vertical line at the paper's own year, title and axis labels, 300 dpi.
- A short summary in chat: total entries, median year, share of references from the last three years, and any flagged entries.

# Reasoning
- Before writing code, state your plan in a few lines and wait for my approval.
- After running, verify: does the total in extract_refs.csv equal the number of rows in extract_refs_detail.csv, and does that match the number of entries you can see in the bibliography? Report any mismatch.
- End with one paragraph on what this analysis can and cannot say about whether the authors understand the current literature.

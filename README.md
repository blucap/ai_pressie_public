# AI presentation: demo materials

Prompts and supporting files for the live demos in a presentation on using AI chatbots and coding agents. Most prompts use the same six blocks: **Role, Context, Task, Constraints, Format, Reasoning**.

## Demos

### `demo_monpol_review/`: persuasive-communications prompt
`prompt_covid_review_press_conference.md` asks a chatbot to turn the Independent Review of the Monetary Policy Response to COVID-19 into six press-conference bullets. It's the improved version of a bare "Analyse the report... What do you notice?" prompt. The file also has notes for the presenter, including how the Constraints block rules out naming individuals.

The review PDF is not included in this repo; attach it to the chat yourself.

### `demo_tija_short/` and `demo_tija_long/`: reference analysis for a referee report
Both demos count the references in the working paper `main_tija.pdf` by publication year and produce a bar chart and a CSV. Run them with a coding agent such as Claude Code from inside the folder.

- **Short** (`tija_prompt.md`): a compact prompt with one line per block.
- **Long** (`tija_long_prompt.md`): a fuller prompt that lists the traps for year extraction (suffixed years, "accessed" dates, page ranges, arXiv IDs, forthcoming papers). It asks for a reusable `extract_refs.py` script, a per-entry detail CSV and a check that the totals match. `CLAUDE.md` holds the project instructions for Claude Code.

### `met_link/`: vibe-coding a bus-times app
Two ways to get the next three buses from Wellington Station or Lambton Quay North to Victoria University's Kelburn campus from the [Metlink Open Data API](https://opendata.metlink.org.nz):

- `claude_prompt.md`: a Claude Code prompt that writes and runs a command-line `next_bus.py`.
- `gemini_prompts.md`: a basic prompt and a refined prompt for Gemini in Google Colab.

For the Claude version, put your Metlink API key in `metlink_key.txt`, replacing the placeholder text. **Don't commit your real key.** The Colab version reads the key from Colab secrets (`METLINK_API_KEY`) instead.

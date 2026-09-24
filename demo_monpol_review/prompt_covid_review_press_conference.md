#### Prompt: press-conference bullets on the COVID monetary-policy review

**How to use this file:** open a chatbot (ChatGPT, Claude, Gemini...), attach or paste in the report `independent-review-monetary-policy-response-covid-19-sep26.pdf`(in `documents/`), then paste everything in the box below as your message.

This is the improved version of the bare prompt used in "Anatomy of a good prompt, Part I" ("Analyse the report... What do you notice?") — built from
the six blocks: Role, Context, Task, Constraints, Format, Reasoning.

---

#### Prompt to paste

```
You are advising Nicola Willis, Minister of Finance, on how she should speak about the attached report at a press conference. Write in her voice, as remarks she would deliver herself.

Context: Treasury has just published the Independent Review of the Monetary Policy Response to the COVID-19 Pandemic, released in the final sitting days of the current Parliament. The report is critical of the Reserve Bank's COVID-era Dual Mandate, arguing that the added flexibility it gave the Monetary Policy Committee contributed to the large policy mistakes made during that period. The Minister wants to use this finding to draw a contrast with how the previous government oversaw monetary policy during COVID, without making it personal.

Task: draft the bullet points she will speak from at the press conference. The room is a press gallery of journalists who are generally sympathetic to former RBNZ Governor Adrian Orr and the Bank's COVID-era policy, so expect the framing to be challenged.

Constraints: 
- Do not name, blame, or imply criticism of any individual by name. The review's terms of reference rule this out, and so does she. 
- Six bullet points with associated explanatory paragraphs. No more. 
- She has only 15 minutes with journalists: each bullet must stand alone and be sayable in one breath.

Format: a markdown file, six bullet points only — no heading, preamble, or sign-off. The first line of the bullet point, or item, should be in bold and show the main point of the bullet. Straight after that opening sentence she wants to read an explanatory paragraph. This is similar to the IMF writing style, which has each first line of a paragraph in bold font. The bold font sentence captures the full bullet point. See the example below. 

Reasoning: this is a high-stakes press conference. Before you draft the bullets, briefly reason through which of the report's findings most directly support the Dual Mandate argument, and which points risk sounding personal or partisan and should therefore be left out. Keep the tone firm and calm throughout, not combative.

Example of IMF writing style:
**Global economic growth remains resilient yet uneven, shaped by persistent inflation and tightening financial conditions.** The International Monetary Fund (IMF) projects world output to stabilize, though regional divergence highlights the fragile nature of the current recovery. Policymakers must carefully calibrate monetary policy to tame remaining price pressures without unnecessarily choking economic activity.
```



#### Notes for the demo

- The six labelled paragraphs above map straight onto the "Anatomy of a good prompt" pills: Role, Context, Task, Constraints, Format, Reasoning. Point this out live — the labels don't need to survive into the pasted prompt (a chatbot reads it as flowing instructions either way), but writing it labelled first is what makes sure none of the six get forgotten. 
- Good moment to contrast with Part I: the bare "Analyse the report... what do you notice?" prompt produces a generic summary; this one produces something usable, because five of the six blocks weren't in the first prompt at all. 
- The report does support the framing: it argues the Dual Mandate's added flexibility "facilitated the large policy mistakes" of the period (checked against the PDF before writing this). 
- Worth naming out loud in the room: this is a persuasive-communications prompt, not a neutral-analysis one — a good prompt is a hazard as well as a tool. The Constraints block is doing real ethical work here (no naming individuals), not just formatting work, and that is itself worth pointing out to the audience as good practice.

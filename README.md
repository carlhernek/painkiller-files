# Painkiller Files

Painkiller is a self-improving workspace for turning raw project material into human-centered product ideas. Drop interviews, notes, screenshots, code, and other messy source material into this repo; an agentic team reads the instructions, finds recurring pain points, crafts solution visions, and packages the best ideas as build-ready specs.

**How to use:** Clone this repo, run the [Painkiller](https://github.com/carlhernek/painkiller) GUI, or point your own agent at `instructions/index.md` and work through the pipeline directly.

**Structure:** `input/` holds your raw material; `instructions/` holds the orchestrator and phase prompts; `output/` receives loose ideas and pre-packaged specs; `research/` stores web-sourced reference material (kept separate from your data); `skills/`, `tools/`, and `scripts/` accumulate reusable assets discovered during retrospectives.

**This repo evolves.** Each run can contribute new skills and tools through phase retrospectives. Merge them into your local main so future projects benefit, or share them back upstream via fork and PR.

Before your first run, create the workspace folders:

```bash
python scripts/init-workspace.py
```

# Phase 1 — Pain Point Extraction

**Agent:** Builder 1

## Goal

Read all material in `input/` and identify recurring pain points and unmet needs. Surface what actually stings for the people in the source material — not feature requests, but human frustrations.

## Multi-Modal Handling

| Material type | What to do |
|---------------|------------|
| Text (code, docs, notes, transcripts) | Read directly |
| Images / photos | Describe what you see — UI confusion, emotional cues, context |
| Video / audio | **Do not transcribe in v1.** Note the file, flag that transcription is needed, and log a retrospective item so a future skill can address it |
| Archives (`.zip`, `.tar`, `.gz`) | Delegate to `scripts/zip-extractor.py` if it exists; otherwise flag the gap in the event log and skip or extract manually if possible |

## Output

Write a structured findings document to:

```
output/loose-ideas/pain-points-found.md
```

For each pain point include:

- **Label** — a short, descriptive name
- **Evidence** — quotes, observations, or references to source files
- **Recurrence** — how often this pattern appears (count or weight)
- **Confidence** — how strongly the material supports this (low / medium / high)

Use clear headings and keep the language human-centered.

## Specific Instructions

If the orchestrator provided specific instructions for this run, treat them as additional focus or constraints. Append them below before executing:

```
<!-- SPECIFIC INSTRUCTIONS -->
(none unless provided by orchestrator)
```

## Event Log

Before starting work, append to `.eventlog`:

```
[timestamp] phase-1 START
```

After completion:

```
[timestamp] phase-1 SUCCESS — extracted N pain points
```

or on failure:

```
[timestamp] phase-1 ERROR — brief reason
```

## After This Phase

Proceed to `phase-1b.md` (retrospective).

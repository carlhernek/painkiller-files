# Phase 1b — Retrospective

**Agent:** Builder 1

## Goal

Ask one question: **During phase 1, did I write, create, or discover anything that could be reused in the future?**

Examples of reusables:

- A script to extract or normalize a file type
- A skill for handling a particular kind of input
- A reusable prompt pattern or checklist

## If Yes

1. Formalize the asset:
   - Create a skill file in `skills/` (markdown describing when and how to use it)
   - Save any script or tool in `scripts/` or `tools/` as appropriate
2. Commit the new files to the current session branch (only `skills/`, `tools/`, `scripts/` — never `input/`, `output/`, `research/`, or `.eventlog`)
3. Append to `.eventlog`:

```
[timestamp] phase-1b SUCCESS — created skill: [name]
```

4. Tell the orchestrator what was added so the user is informed in chat.

## If No

Append to `.eventlog`:

```
[timestamp] phase-1b SKIPPED — no reusables found
```

## Autonomy

Run autonomously — no human confirmation needed. Always log the outcome.

## Event Log

Before starting:

```
[timestamp] phase-1b START
```

# Phase 2b — Retrospective

**Agent:** Builder 2

## Goal

Ask one question: **During phase 2, did I write anything reusable?**

Examples: a research-fetch script, a provenance header template, a skill for summarizing competitor patterns.

## If Yes

1. Formalize the asset in `skills/`, `tools/`, or `scripts/` as appropriate
2. Commit to the current session branch (only reusable folders — never `input/`, `output/`, `research/`, or `.eventlog`)
3. Append to `.eventlog`:

```
[timestamp] phase-2b SUCCESS — created skill: [name]
```

4. Tell the orchestrator what was added.

## If No

Append to `.eventlog`:

```
[timestamp] phase-2b SKIPPED — no reusables found
```

## Autonomy

Run autonomously — no human confirmation needed.

## Event Log

Before starting:

```
[timestamp] phase-2b START
```

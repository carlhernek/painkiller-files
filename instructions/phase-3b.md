# Phase 3b — Retrospective

**Agent:** Builder 3

## Goal

Ask one question: **During phase 3, did I write anything reusable?**

Examples: a spec-linting checklist, a packaging skill, a template helper script.

## If Yes

1. Formalize the asset in `skills/`, `tools/`, or `scripts/` as appropriate
2. Commit to the current session branch (only reusable folders)
3. Append to `.eventlog`:

```
[timestamp] phase-3b SUCCESS — created skill: [name]
```

4. Tell the orchestrator what was added.

## If No

Append to `.eventlog`:

```
[timestamp] phase-3b SKIPPED — no reusables found
```

## Autonomy

Run autonomously — no human confirmation needed.

## Event Log

Before starting:

```
[timestamp] phase-3b START
```

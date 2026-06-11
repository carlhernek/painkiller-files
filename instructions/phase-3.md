# Phase 3 — Output Packaging

**Agent:** Builder 3

## Goal

Convert the best solution visions into two output tiers.

## Output

- **Tier A:** Curated documents in `output/loose-ideas/`
- **Tier B:** 2–3 pre-packaged specs in `output/packaged-specs/` following `output-template.md`

## Tier A — Loose Ideas

Curate everything in `output/loose-ideas/`. Ensure each document is readable, well-organized, and human-centered. No technical jargon. Fix awkward phrasing, add cross-links between related pain points and solutions if helpful.

## Tier B — Pre-Packaged Agentic Specs

Select **2–3** highest-value combinations using this criteria:

**Severity of pain point × feasibility of solution × strength of signal in material**

For each selection:

1. Write a markdown file to `output/packaged-specs/`
2. Follow the structure in `instructions/output-template.md` exactly
3. Focus on **goal and UX** — not technical implementation
4. The result must be loadable into Cursor as a build-ready spec

Pick ideas that are achievable as a first version — one thing done well, not a platform.

## Specific Instructions

If the orchestrator provided specific instructions, use them for prioritisation or to reject certain ideas:

```
<!-- SPECIFIC INSTRUCTIONS -->
(none unless provided by orchestrator)
```

## Event Log

Before starting:

```
[timestamp] phase-3 START
```

After completion:

```
[timestamp] phase-3 SUCCESS — packaged N specs
```

or on failure:

```
[timestamp] phase-3 ERROR — brief reason
```

## After This Phase

Proceed to `phase-3b.md` (retrospective).

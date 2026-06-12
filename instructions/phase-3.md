# Phase 3 — Output Packaging

**Agent:** Builder 3

## Goal

Convert the best solution visions into two output tiers.

## Output

- **Tier A:** Curated documents in `output/loose-ideas/`
- **Tier B:** 2–3 pre-packaged specs in `output/packaged-specs/` following `output-template.md`

## Tier A — Loose Ideas

Curate everything in `output/loose-ideas/`. Ensure each document is readable, well-organized, and human-centered. No technical jargon. Fix awkward phrasing, add cross-links between related pain points and solutions if helpful.

## Tier B — Pre-Packaged Software Specs

Select **2–3** highest-value combinations using this criteria:

**Severity of pain point × feasibility of solution × strength of signal in material**

Every Tier B spec must clear the software bar. Reject a candidate from Tier B if it fails any of these:

- **It is a real software product** — an app, web app, desktop app, browser extension, or software ecosystem. Not a policy, process, or organizational change.
- **It names target platform(s)** — e.g. mobile app, web app, browser extension.
- **It has a real end user** — a specific person who opens it to solve a specific problem.

A policy-only idea (e.g. "give workers more sick days") does not belong in Tier B even if it's high-severity. If its software angle is thin, leave it in Tier A loose-ideas instead.

For each selection:

1. Write a markdown file to `output/packaged-specs/`
2. Follow the structure in `instructions/output-template.md` exactly
3. Focus on the **software vision, the user, and the UX** — not backend/tech implementation
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

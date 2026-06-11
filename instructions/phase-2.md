# Phase 2 — Solution Crafting

**Agent:** Builder 2

## Goal

Take the pain points from `output/loose-ideas/pain-points-found.md` and craft solution visions for each. Use all three modes below for every pain point.

## Three Solution Modes

### 1. Remix

Extract solution hints already latent in the source material. Did an interview describe a workaround? Did a screenshot show how someone coped? That's a product seed — name it and build on it.

### 2. Bootstrap

Apply pattern knowledge. What does a typical solution to this class of problem look like? Frame it in human terms — who benefits, what changes for them, how it fits their day.

### 3. Research

Go online and find how others are solving similar problems. Use web search and fetch reference pages as needed. Download or summarize reference material to `research/` with clear provenance labelling.

**Provenance rule:** Research material must be clearly separated from original input. Every file in `research/` must include a header or live in a subfolder that makes it obvious this is *online research, not original material*. Never mix research into `input/`.

## Output

Write one document per pain point to:

```
output/loose-ideas/solutions/
```

Use a filename derived from the pain point label (kebab-case, e.g. `onboarding-confusion.md`).

Each document must contain:

- The pain point (label + brief recap)
- **2–3 solution visions**, each with:
  - **Human scenario** — who is this for, what are they doing
  - **How it solves the felt need** — what changes emotionally and practically
  - **Interaction concept** — what the user does, what the system does
  - **Mode** — which of Remix / Bootstrap / Research produced this vision

## Specific Instructions

If the orchestrator provided specific instructions, use them as additional constraints or focus areas:

```
<!-- SPECIFIC INSTRUCTIONS -->
(none unless provided by orchestrator)
```

## Event Log

Before starting:

```
[timestamp] phase-2 START
```

After completion:

```
[timestamp] phase-2 SUCCESS — wrote N solution documents
```

or on failure:

```
[timestamp] phase-2 ERROR — brief reason
```

## After This Phase

Proceed to `phase-2b.md` (retrospective).

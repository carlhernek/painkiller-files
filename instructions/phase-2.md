# Phase 2 — Solution Crafting

**Agent:** Builder 2

## Goal

Take the pain points from `output/loose-ideas/pain-points-found.md` and craft **user-facing software solution visions** for them. Use all three modes below for every pain point you craft for.

## Software Focus (read first)

This is where Painkiller's software focus is distilled. Every solution vision must be a **user-facing software product** — a mobile app, web app, desktop app, browser extension, or software ecosystem that a real person opens and uses.

- **Only craft solutions for pain points tagged `high` or `partial` software-addressability** in `pain-points-found.md`. For `low` pains, note them briefly as "out of software scope" and move on — do not invent a product for them.
- **No policies, no API-only/backend-only tools.** A policy demand (e.g. "provide more paid sick days") is not a product. Reframe it as the software that delivers or operationalizes it (e.g. a sick-leave accrual + one-tap call-in app the worker uses on their phone). If there is no genuine user-facing software at the center — only a policy with an app bolted on as an afterthought — drop the idea rather than forcing it.
- **Always name a real user and a real platform.** Who opens this software, on what device, to solve what?

## Research discipline

- **Check `research/` first** — list and read existing files before calling `web_fetch`.
- **Do not re-try URLs that already failed** in this run (403, SSL, 404). Use Bootstrap or Remix instead.
- **Limit web fetches** — at most 3 `web_fetch` attempts per phase run unless the orchestrator says otherwise.

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
  - **Software lens** — a required block naming:
    - **Product** — what the software is, in one line
    - **Platform(s)** — mobile app / web app / desktop / browser extension / etc.
    - **Primary user** — who uses it, and the issue it solves for them
    - **Core user-facing interaction** — what the user actually does in the software
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

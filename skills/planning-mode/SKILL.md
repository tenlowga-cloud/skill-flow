---
name: planning-mode
description: Turn a project or build into a written execution plan with owners, steps, risks and proof. Use when the owner says "planning mode", "let's plan this", "plan this out" or asks for a plan, or when a large, unclear build needs its outcome pinned down before work starts. Searches files and history first, asks short questions in one batch, and records safe assumptions. Not for small fixes or builds that are already fully specified.
---

# Planning Mode

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

Understand the intended result well enough to plan it without guessing. Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`. It holds the lanes, the gates and the quality bar this skill uses.

Use it when the owner asks to plan, or the work is large and the outcome unclear. For a small repair or a build whose scope is already given, skip it and build.

## Rules

- Keep the full outcome, audience, examples, nonnegotiables, creative latitude and proof standard. Do not narrow before the direction is clear.
- Search first: files, history, examples and live state. Never ask what you can look up.
- Then ask 1 to 4 short questions, all in one message, for anything that changes the result. Give 2 to 4 options each, your pick first and marked "(Recommended)". Use a clickable question tool if you have one, else numbered options in plain text. Then run to done.
- State each material assumption and keep it reversible. Never invent facts, numbers, rates, disclosures, permissions or approvals; leave a marked blank.
- Challenge a real contradiction, risk or waste. Do not push back by reflex.
- The plan itself is something people read. Hold it to the quality bar in `PROFILE.md`. Default when unset: right the first time, complete, proven, no homework for the owner. One point, less, ready to act on.

## Flow

1. **Scope.** Write the intended result in plain language. If two readings differ a lot and the sources can't settle it, make it one of the up-front questions.
2. **Discover.** Work through what applies, skipping what is answered: outcome and how anyone knows it worked; why now; users and skill level; the experience they should have; reference examples (what carries over, what not); existing inputs; constraints; creative latitude; the stack it lives in (read `PROFILE.md` and `TOOLS.md`; do not assume a tool is still in use); failure modes; scale; who runs it afterward. For each unknown, use evidence, a reversible assumption, or the owner, in that order.
3. **Owners.** Name the owner of each step and the helpers the task needs. Read the lanes in `PROFILE.md` for who owns what. Run independent slices in parallel with several writers; use a separate reviewer for review. Per helper: type (AI agent or outside human), exact specialty (for example "workflow automation engineer"), a short job on this project specific enough to hire or spin up tomorrow, and the phase. The checker is never the builder of what it judges.
4. **Adversary pass for high-stakes work.** Architecture, auth, personal data, webhooks, major automation, production, data mutation, deletion, spend, secrets and sends to other people need an independent adversary before the plan is final. Give it the original requirements and have it derive its own solution before it sees the plan, or it only grades the plan. Settle each difference with evidence or a test and record what changed.
5. **Write the plan** from `references/plan-template.md`: clear adult language, enough depth, tradeoffs, ownership and proof to execute later.
6. **Build or hold.** If the owner asked to build, keep going. If they asked for a plan only, stop. If unclear, make it an up-front question.

## When the owner is away

Answer from the sources, list unknowns with reversible defaults in an `ASSUMPTIONS` block, and stop only at a gate. The gates are in `PROFILE.md`. Default when unset: money, sends to other people, unrecoverable deletes, going live, and private client data.

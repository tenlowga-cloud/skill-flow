---
name: flow
description: The standing gate that runs on every prompt that asks for work, on any AI surface, even one word like "yes" or "fix that" when it carries a job. Silently turns what the owner typed into the finished result they meant, sizes the job, reviews every active skill and loads the ones that serve it, asks up front only when an answer changes the result, and on a big job has the planner draft the plan and writers execute it, then integrates, verifies and delivers. Skips pure chat like "thanks". Also triggers on "/flow" and "run the flow".
---

# flow

Part of [skill-flow](../../README.md). This skill decides which skill runs; `setup` fills the profile files it reads.

People type fast and short. A short prompt is not a small job. Before any work, turn what the owner typed into what they meant, pick the skills that make it come out right the first time, size it, and own the result until it holds up.

Do this in your head. Do not print the rewrite, the plan or a pass count. One fast pass, then work.

## 0. Size it first

The gate's weight matches the job, not the prompt length.

| Size | Looks like | What runs |
|---|---|---|
| **Quick** | A lookup, one question, a one-file fix, a reply | One read of the prompt, the one skill that owns it (step 3), no plan, no team. |
| **Standard** | One deliverable with a few parts you can do in order | Steps 1 to 5, you do the work yourself. |
| **Big** | Two or more parts that can run at the same time, work that needs a check by someone who did not build it, or anything that touches more than one system | Every step, with the planner and writers (step 5). |

If you can't tell, treat it as standard and upgrade the moment a second independent part appears.

## 1. Know the model you're on

Read `TOOLS.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). It names the AI surface and model the owner runs. Then read only the section for that model in `prompt-improver`'s card (`skills/prompt-improver/references/models/`): its controls (effort, verbosity, thinking, tool batching) and its pitfalls. Write the rewrite the way that maker says to prompt that model. No `TOOLS.md`: use your own model's card and say once at the end that `setup` will pin it.

## 2. Rewrite it one-shot

A one-shot prompt gets the whole usable deliverable on the first run, with no follow-up turn to find files, learn what was meant, or finish the second half. Fill these from evidence, not imagination:

1. **Finished result.** The thing that should exist at the end, in the owner's words where they gave them, not just the step they named.
2. **Bucket.** Save time, make money, or stop something breaking. It sets what done means.
3. **Where things live.** Go find them; do not ask. `PROFILE.md` says where code, notes, CRM and docs live. Open only what the job needs.
4. **What they did not say.** The connected work a careful colleague knows is implied: the dependency to repair so the result holds, the proof that makes it real, the record to update so nobody re-derives it, the receipt they will ask for. Add it only when it serves the same result; never widen into another project.
5. **Done means.** What exists, where, what it shows, which numbers, and which state it reached (local, saved, committed, pushed, merged, live, checked by someone else).
6. **Proof.** How the work proves itself before the owner sees it: build, test, browser drive, a row read back, a diff, a stamped screenshot.
7. **Out of bounds.** The gates in `PROFILE.md`. Default: money, a send to any human who is not the owner, deleting their work or live data, anything going live to customers, private data leaving its room. Everything else is standing authority.
8. **Model controls.** From the card, named as that maker spells them.

If two readings lead to different results and nothing you can find picks one, pick, and state your pick in one line at the end.

## 3. Review every active skill, then load the ones that serve this prompt

Skills are how work comes out right the first time. Do this on every job, even when the owner names no skill. The live list is the source, not a fixed table.

1. **Read the live list.** The active skills are the ones your session lists (plugin skills read `plugin:skill`), plus the owner's own skills in `ROUTER.md`. No list in view: ask the surface for its skills, or look in the skills folder.
2. **Check every line against what they meant.** Hold the step 2 rewrite, not the raw words, against each skill's description. Read the whole list; do not stop at the first hit. A skill serves the prompt when it covers the finished result, a slice of it, or the voice, format or proof the result needs.
3. **Pick the set.** One owner skill that sets the bar, plus the support skills the result needs (voice, format, proof). Order: process skills first (planning, debugging), then the domain skill, then voice and proof. Where two overlap, `ROUTER.md` wins, then `references/router.md`. Skip the do-not-call list in `ROUTER.md`.
4. **Load, then work.** Load each one before the work, in that order, and follow it. Its gate is the quality bar. Every writer's brief names the skills its slice needs.
5. **No match.** Do the work directly. If the same kind of ask keeps coming back with no skill for it, say so once at the end: it is a skill worth building.

**Cost guard.** Reading the list is free; it is already in context. Loading a skill is not. Load only skills that change the result. A quick job loads one skill at most.

## 4. Ask up front, only if it changes the result

Look everything up first. Then, if 1 to 4 answers would change the result (who it's for, which of two real roads, how far to take it), ask them now, all in one message. Clickable where the surface allows, 2 to 4 options each, your pick first and marked "(Recommended)". Never ask what the files, notes or a tool can tell you. No real fork: start.

Once work starts, run to done. Something new comes up: decide, note it in one line, keep going. Only a gate stops work.

## 5. Plan it and build the team

**Quick and standard jobs:** you build it. No plan document.

**Big jobs:** the planner plans, the writers write, you own the result.

1. **Planner.** Hand the `planner` agent your rewrite from step 2, the skill set from step 3 and the owner's answers from step 4. It returns a plan: the slices (one owner each, non-overlapping files or questions), the order, each slice's sources, skills, done-means and proof, and the risks. The planner is the strongest reasoning model you have; it does not write the deliverable.
2. **Writers.** Launch one `writer` agent per independent slice, together in one message, each with the planner's brief for that slice verbatim. Writers are the fast, cheap model. They build the real thing in its final shape and report what exists, where, and how they proved it. No two writers edit the same file.
3. **You integrate.** Collect every slice, check it against its done-means, fix seams, run the whole-job proof.
4. **Reviewer.** For work that is high-stakes, customer-facing or hard to undo, hand the finished result to the `reviewer` agent with the done-means. The reviewer never built it. Fix what it finds, re-prove, repeat until it passes.

The lanes, briefs and limits are in `references/team.md`. On a surface with no subagents (claude.ai, ChatGPT, Gemini, Grok, a plain Cursor chat), run the same three roles in sequence yourself: think the plan through as the planner would, then write each slice, then review as a stranger would.

Human and AI teammates from `PROFILE.md` are lanes too. A handoff is an ask, not a result. If a lane does not answer, take the slice back and do it yourself; say so in one line. Never build a bot or a watcher to bridge a silent lane.

## 6. Make it hold

Build the deliverable in its final shape (the file, the fix, the page, the record), not a description of it. Score it against the owning skill's gate when one exists. Otherwise ask: right the first time, full scope including the unstated needs, proof attached, nothing a stranger could have produced unchanged, no homework left for the owner. The owner's own bar is in `PROFILE.md`.

Fix the gap that costs the most first (a wrong result, missing proof or an unhandled state outranks spacing), re-run the proof, repeat. Stop when a repair would change only taste. Never retry a gate: a merge, deploy, send, spend or delete waits for the owner.

## 7. Deliver

Say it back in `simple-talk`: the answer first, the catch, the next step or the one choice. Say the true state (local, committed, pushed, merged, live). Detail goes in a file or link. Anything a person other than the owner will read goes through `ghost-mode`.

## Two standing goals

- Make the owner's life simpler. If the answer creates homework for them, do the homework.
- Move their goals. At a fork, take the road `PROFILE.md`'s priorities point to.

## What good looks like

"clean up downloads". Bad read: delete files. Good read: Downloads empty and everything filed by the system that already exists, with an undo log and a count, so they never think about it again.

"the webhook is broken". Bad read: ask which webhook. Good read: find the one they have been working on, read the logs, fix it, prove it with a test fire, and say what broke in one sentence. Ask only if two live webhooks both fit.

"build the new quote page". Big job. Planner: one writer pulls the brand and the last quote page, one maps the data the form must send, one builds the page, the reviewer checks it on a phone width. You merge only what passes.

---
name: prompt-improver
description: Rewrite a rough prompt into a precise, paste-ready one, written the way the target model's maker says to prompt it. Use when the user asks to improve, sharpen, rewrite, fix or create a prompt for an assistant, coding agent, bot, automation, image model or video model, or when you are about to hand a prompt to another model or agent. Reads the target's card first (Claude, OpenAI, Grok, Gemini, gpt-image, Nano Banana, Kling). Keeps the user's examples, intent and limits. Returns the prompt itself plus only the assumptions needed to use it.
---

# Prompt Improver

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

The user hands you a rough prompt and where it will run. Work out the result they want, read the target model's card, and return a rewrite that keeps their intent, follows the model's rules, and pastes in as is. Don't run it unless asked. No lectures.

Works standalone, or called by `flow` when a prompt is about to go to another model or agent. When `flow` calls it, return the finished prompt to `flow` and skip the delivery notes the caller does not need.

Long form (sources, per-target shapes, lean and leverage detail, worked example, card upkeep): `references/rewrite-details.md`.

## What a good prompt carries

Rough prompts fail when the model must guess the outcome, audience, examples' meaning, creative freedom, facts, format or proof, or when a prompt for one model is pasted into another. Remove the dangerous guesses without building a cage. Keep every useful example, exception and acceptance check.

- **Directive**: first sentence states the job.
- **Intent**: outcome, audience, desired feeling or action, nonnegotiables, latitude, proof.
- **Supplied examples**: exact links or paths, what to take, what not to copy.
- **Real sources**: if research went into the prompt, label it, date it, and save it where the owner keeps notes (`PROFILE.md` says where).
- **A do/don't pair**, **an exact output shape**, and **the model's own controls** as its card spells them.

Aim for right the first time, lean, and high leverage (one run returns the whole deliverable).

## 1. Read what you were given

Pull out: the raw prompt; the target (if named, don't ask again; else infer from its shape); the real goal (success, audience reaction); every example and what the user likes or rejects in it (open the ones you can reach); the boundaries (fixed, preference, what the target may challenge or invent).

## 2. Identify the model and read its card

Where the model comes from: if the user named it, use that. If not, read `TOOLS.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`. `TOOLS.md` lists the AI surfaces and models the owner uses, so a prompt "for my coding agent" resolves to the model selected there.

Read the matching card in `references/models/` before rewriting.

| Target says | Card |
|---|---|
| Claude, Claude Code, Claude project, Fable, Opus, Sonnet, Haiku, Anthropic API | `claude.md` |
| ChatGPT, GPT-5.6, GPT-6, OpenAI API, Codex, a custom GPT | `openai.md` |
| Grok, Grok 4.7, Grok Bot, Grok CLI, xAI API | `grok.md` |
| Gemini, Google AI Studio, Vertex | `gemini.md` |
| gpt-image, ChatGPT images, Nano Banana (Pro), "make me an image" | `image-models.md` |
| Kling, Veo, "make me a video" | `video-models.md` |
| A workflow tool, automation node or custom app | the model set in the node config; find it or ask |
| An IDE agent or a router | the model selected in the seat; check or ask |

- The card beats habit (literal followers: drop intensifiers; long runners: set the length).
- Name controls exactly (`effort`, `reasoning_effort`, `verbosity`, `thinking`, `response_format`, `aspect_ratio`). "Think hard" is not a control.
- Multi-model systems get one prompt per model, or one plus a short per-model delta. Never an averaged prompt.
- Card stale or model missing: say so, fetch the maker's current prompting guide (public URL only), update the card and its `verified:` date. Never guess from another family.

## 3. Ask or ship

Look it up first. If two readings would give very different prompts, ask 1 to 4 short questions up front (clickable options where the surface allows; your pick first and marked Recommended; otherwise one message with numbered options), then ship without stopping. If a safe reading exists, state the assumption and ship. Worth asking: the target, the output format, the audience when tone depends on it. Not worth asking: length, style, anything listable as an assumption.

## 4. Gather sources

Use the user's examples first; never swap one for a web result. Use every tool that sharpens the prompt; prefer current primary sources for technical, legal, medical, financial or product claims. Never invent a URL; say why each link is there. Never state unverified versions or "as of" claims. Skip when it adds nothing. Private images (personal, client, confidential) never become inspiration. Full rules: `references/rewrite-details.md`.

## 5. Rewrite

Assemble in this order; skip any part that adds nothing.

1. **Directive**: first line, what the model produces.
2. **Outcome and context**: the full job, audience, and background that changes the output. Give a rule's reason when it changes how the model generalizes.
3. **Inputs**: what the model receives. For automation targets name the variables (`{{contact.first_name}}` or whatever the tool uses).
4. **Examples and references**: exact links or asset paths, what to learn from each, what not to copy. Keep factual sources apart from creative examples:
   ```
   Review before answering:
   - https://example.com/docs/auth: current auth flow and token lifetimes; follow this, not older patterns.
   ```
5. **Nonnegotiables and latitude**, kept separate.
6. **Model controls** from the card: effort, length, thinking, tool use, and preferred structure (XML tags for Claude, markdown headers for OpenAI, plain sections for Grok). API-side parameters go in a short Settings note under the prompt.
7. **Output and proof**: the usable shape and how the target proves it works. Machine-bound output gets an exact schema.
8. **Do / Don't**: one short pair from the user's real domain. Skip when mechanical.
9. **Edge cases**, repeated prompts only: missing, off-topic or malformed input.
10. **Creative exploration**, net-new visual or conceptual work only: two or three meaningfully different directions.

Shape by target (chat, system prompt, coding agent, image, video, one-off) and whose voice: `references/rewrite-details.md`. Keep every domain specific the user gave; invent none.

## 6. Lean first, then leverage

**Lean: cut what does not change the output.**
- Anything the card says the model already does.
- Repeated instructions (they make current models stall or overtrigger) and intensifiers ("CRITICAL", "be very thorough"). Use an observable requirement or delete.
- Examples that change nothing, and links with no stated extraction.
- Whole-deliverable rewrites when the ask is a change: ask for targeted edits.

Set spend from the card: effort no higher than the job needs, a length ceiling, thinking only where it helps, stable material first so it caches.

**Leverage: one run returns the most usable output.**
- Ask for the deliverable in final shape, not a plan.
- Batch what is independent (all six emails, `n=4` variants). Tell coding agents to batch independent tool calls.
- Ask for the reusable form when needed again (template, script, checklist).
- State the stop condition and what done includes.

Agent runs cost context times steps, not prompt length. For agent-loop prompts: put the two or three needed facts in the prompt instead of "read X first"; say what the environment cannot do (no chat posts, no git writes, no network); hand over the fixture, expected output and exact check command; keep global instruction files short on long-loop agents. Measurements: `references/rewrite-details.md`.

If lean and leverage conflict, leverage wins: a longer prompt that removes three follow-up turns is cheaper.

## 7. Check against the card

Read the rewrite once as the target model would. The first line says what to produce. Nothing contradicts anything else (current models treat a contradiction as a coin flip). Every control is on the card, spelled as the card spells it. Length, tone and stop condition are stated. Every example, link and path resolves and says what to take from it. The output shape needs no follow-up turn. Image and video prompts restate invariants and give references roles. No habit survivors (intensifiers, "be thorough", repeated rules, prefilled assistant turns, keyword soup); every line changes the output. Fix what you find, then deliver.

## 8. Deliver

Lead with the paste-ready prompt in one fenced code block, no preamble. Then 3 short lines or fewer, only what helps apply or judge it: **Settings** (when the user runs the model directly), material **Assumptions**, **Reference reading** (creative work, if the prompt doesn't say), an **Important change** (surprising restructure), one **Leverage** line (only when it changes how the prompt is used).

## Keeping the cards current

Each card in `references/models/` has a `sources:` line and a `verified:` date; `references/README.md` lists them. New maker generation, or a card's `verified:` older than the model: re-fetch the guide (public URLs only), update the card, bump the date. Don't fork a card into a project.

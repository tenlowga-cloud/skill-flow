# Prompt-improver details

Load the section you need. SKILL.md holds the steps; this holds the long form.

## Gather sources (step 4, full)

Use the user's examples and source material first, and record what each contributes. Never swap a user's example for a web result, or reduce a visual reference to colors and adjectives. When references conflict, assign each to the decision it controls instead of averaging them.

- Use every tool that sharpens the prompt (web search, connected drives, the owner's notes, docs). Search the web for current facts, official instructions or market context. For technical, legal, medical, financial or product claims, prefer current primary sources: official docs over aggregator posts, the source itself over a summary.
- For material creative work, also sweep current category leaders (Fortune 500 included), adjacent fields, remote analogies and image results, even when the user's examples are good. Verify each added source and say what the target should take from it.
- If the environment can reach the owner's cloud drive, search the accessible image pool by project, brand, topic, audience and visual role, and fetch only selected, relevant, safe originals. Personal, client, confidential and ambiguous private images never become generic inspiration because a search returned them.
- Match the source to the prompt: official docs for the tool or API it touches, live pages the model should read (pricing, changelog, competitor), standards and policies, and for visual work the observable mechanics (composition, typography, lighting, spacing, rhythm, motion, texture, emotional effect). Add artists, films, lenses or eras only to fill a named gap, and only if the target's rules allow it.
- Use a source set shaped by the task, not an arbitrary cap. Read every source that adds distinct guidance.
- Never invent a URL; name the source type if you cannot verify it. Say why each link is there ("review X for Y"). Do not state version numbers or "as of" claims you did not verify. Skip this step when it adds nothing, such as a pure reformat job.

## Shape by target

- **Chat assistants**: natural prose, short sections if long. State length and tone. No XML in a user turn unless the card says the model likes it (Claude does).
- **System prompts and agent instructions** (Claude projects, workflow-tool agent nodes, CRM bots, custom GPTs, Grok Bot): written for repeated use, second person, explicit refusal boundaries, defined behavior for missing or junk input, and the reason behind each rule.
- **Coding agents** (Claude Code, Cursor, Grok CLI, other coding tools): the intended result, user experience, examples, boundaries and acceptance tests. Name files or directories in scope, what the agent must not touch, versions only when they matter, and current official docs. Say how it verifies the real result and when to stop, because current agents keep going until told. Give implementation steps only when they are required constraints.
- **Image models** (gpt-image, Nano Banana Pro, and tools that host them): a scene in sentences, not keywords. Keep subject, composition, emotional effect, reference mechanics, setting, lighting, materials, camera and technical needs. Pass reference images with explicit roles, restate what stays invariant on each edit, use negative instructions only where the platform supports them, and do not swap a famous artist for the user's own reference. For OpenAI API image work, confirm the current model name on the card.
- **Video models** (Kling, Veo): subject, action, setting, camera language, lighting, mood, audio or dialogue, in that order; one camera move per shot; references bound to named elements; multi-shot structure spelled out shot by shot.
- **One-off tasks**: front-load the directive, keep it tight, skip edge cases.

Whose voice: the prompt is an instruction to a machine, so clarity beats personality. Keep every domain specific the user gave (names, product details, numbers, facts) and invent none. If the rough prompt asks the target to write in the user's voice, carry that through, and tell it to follow the owner's voice file (`VOICE.md` in the skill-flow profile folder) or a writing-style skill if one exists in its environment.

Creative exploration (net-new or unclear visual or conceptual work): name the category default, find the deeper human tension, and ask for two or three meaningfully different directions, each with one unexpected but defensible connector to another field, form, ritual or system. Skip for a small repair or an approved direction.

## Lean, then leverage (step 6, full)

**Lean: cut what does not change the output.** Remove:
- Anything the card says the model already does (self-verification on Opus 5, parallel tool calls, adaptive thinking, concise defaults on GPT-5.6, literal instruction following on Sonnet 5).
- Repeated instructions. Say each rule once, where the model reads it first; repeating "ask before…" or "don't…" makes current models stall or overtrigger.
- Intensifiers and untested adjectives ("CRITICAL", "be very thorough", "professional"). Replace with an observable requirement or delete.
- Examples that change nothing, and links with no stated extraction.
- Whole-deliverable rewrites when the ask is a change: ask for targeted edits and only what changed.

Then set the spend from the card: effort no higher than the job needs, a length ceiling, thinking only where it helps, stable material first so it caches. Evidence (fetched 2026-09-03): OpenAI's coding-agent evals improved 10 to 15% while prompt tokens fell 41 to 66% after trimming repeated instructions, examples and tool descriptions; Anthropic's Opus 5 page says legacy re-check instructions now cost tokens with no quality gain.

**Leverage: make one run return the most usable output.**
- Ask for the deliverable in final shape (the file, the schema, the paste-ready copy), not a description or plan.
- Batch what is independent: all six emails, `n=4` logo variants, every report section, the full test set. Tell coding agents to batch independent tool calls.
- Ask for the reusable form when it will be needed again: a template with named slots, a script that regenerates the output, a checklist. One prompt that produces the generator beats ten that produce instances.
- State the stop condition and what done includes, so the model finishes instead of returning step one.
- For repeated prompts, define edge cases so junk input does not cost a human round-trip.

**Agent runs are priced by context times steps, not prompt length.** Measured 2026-09-03 on one team's prompts: a leaner chat-style system prompt cut total tokens 3.8x and time 2.2x, because the job is one turn. The same pass on a coding-agent system prompt saved nothing: the agent re-sent its whole context every tool step, spent about 100k tokens per step reading contracts, manuals and skills its global instructions told it to open, then wasted steps on actions the sandbox forbade. For any agent-loop prompt:
- Put the two or three needed facts in the prompt instead of pointing at a 13 KB contract. Every "read X first" costs context on every later step.
- Say what the environment cannot do (no chat posts, no git writes, no network) so the agent does not try and retry.
- Hand over the fixture, the expected output and the exact check command, so verification is one step.
- Keep global instruction files (`AGENTS.md`, `CLAUDE.md`) short and pointer-free on seats that run long loops.

If lean and leverage conflict, leverage wins: a longer prompt that removes three follow-up turns is cheaper.

## Example

**User:** "write me a prompt for claude that makes it summarize my sales calls" (Claude project system prompt)

**Return:**

````
Summarize a B2B sales call transcript into a CRM-ready note that tells the rep what happened and what to do next.

You are a sales operations analyst. Every claim you make traces to a line in the transcript. Never infer intent that wasn't spoken, because a rep will act on this note without re-reading the call.

Review before answering:
- https://example.com/sales-call-analysis: the signal categories (objections, buying signals, commitments) worth pulling out of a call.

Output exactly these sections:

**Outcome:** One sentence: did the deal advance, stall, or die, and why.
**Key moments:** 3-5 bullets on the moments that mattered, each quoting or tightly paraphrasing the transcript.
**Next steps:** Every commitment made by either side, with an owner and a deadline when one was stated.
**Risk:** The single biggest threat to this deal based on this call.

Rules:
- Pull only from the transcript. If something wasn't covered, write "not discussed".
- Under 250 words total, because this pastes into a CRM note field.
- Plain prose inside each section; no other headers, no nested bullets.
- If the transcript isn't a sales call, say so in one line and stop.

Do: "Renewal slipped to Q3: CFO wants a security review first (14:02)."
Don't: "The customer expressed some hesitancy about the timeline."
````

Settings: Claude project, default effort; no extended thinking for a single-transcript summary.

Assumptions:
- Summaries land in a CRM, so kept under 250 words.
- You want commitments from both sides, not just the prospect's.

Leverage: the original asked for "a summary"; this returns the CRM note in its final four-section shape, so nothing gets reformatted or re-asked.

## Keeping the cards current

- Each card in `references/models/` carries a `sources:` line (the maker's pages it came from) and a `verified:` date. `references/README.md` lists the cards.
- When a maker ships a new generation, or a card's `verified:` date is older than the model you are prompting, re-fetch the maker's guide, update the card, and bump the date. Public URLs only; nothing private goes to a fetcher.
- Do not fork a card into a project. Keep a project delta in the project's own notes.

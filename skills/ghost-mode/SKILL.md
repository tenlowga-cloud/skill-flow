---
name: ghost-mode
description: Write or rewrite words a person will read so they sound like the owner, a real person, with no AI tells. Use for any email, text, chat reply, ad, landing page, script, caption, handoff, status, or client and prospect copy, and when the owner says ghost mode, "sound human", "sound like me", "humanize this" or "no AI tells". It also applies by default to any outbound copy written on the owner's behalf. For interface text, add simple-talk.
---

# Ghost Mode

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

Covers every word a person reads, on every AI surface, including user-visible error, validation and help text in backend code. Not identifiers, schemas, SQL, logs, tests or machine-readable contracts.

Goal: copy a specific adult could have typed, with a point of view. Remove the known tells. Promise no detector score. Bar: the quality bar in `PROFILE.md` (default: right the first time, complete, proven, no homework for the owner).

## Load the voice first

Read `VOICE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`.

`VOICE.md` holds the owner's real samples, their banned words, their sign-off and their length rules. Those win over the general rules below.

No `VOICE.md`: use the general rules in this skill and say once that `setup` can capture their voice.

Also read `PROFILE.md` the same way when the copy needs facts about the owner's business, audience or gates.

## Voice

- Source order: the owner's request, their approved samples and audience, project facts and disclosures, then these rules.
- Human, warm, direct, specific. Take a position the source supports. Say a catch in one plain line.
- Mix sentence length. Uniform medium sentences are the top tell.
- Words a person says aloud ("use", not "utilize"). Contractions. Active voice. Strong verbs, real numbers.

## Length

- **Messages** (texts, emails, chat, status, handoffs, questions): short and direct. The owner's length rule is in `VOICE.md`. Default when unset: lead with the answer, then the catch, then the next step or one choice. Detail goes in a file, PR or link.
- **Long copy a reader chose** (sales page, talk track, story, client plan): the room it needs. Every line earns its place and it scans.

## Remove the tells

- No em dashes and no double hyphen standing in for one. Use a period, comma or rewrite.
- No semicolons. Split the sentence.
- No banned words or phrases, no "not just X, it's Y". Full list and other tells: `references/ai-tells.md`. The owner's own banned list lives in `VOICE.md`. Apply both.
- No throat-clearing openers or wrap-up closers. Start with the point. Close with an action.
- Sign off the way `VOICE.md` says. No sign-off listed: none, or just the owner's first name.
- At most one rhetorical triple. Zero is the target. No bold-label bullets. Sentence case headings in casual copy.
- Questions: one per short piece, two in a long one, never stacked or obvious.
- Concrete beats abstract. Never invent a personal detail for color.

## Facts and disclosures

Keep meaning, verified facts, numbers, required disclosures, legal and compliance wording, and verbatim quotes. Never invent a number, price, rate, statistic, feature, testimonial, guarantee, deadline, worry or personal detail. Missing fact: write around it or leave a fill-in marker for the owner.

Client and prospect copy: complete adult sentences, no pressure tricks, no promised financial, legal, tax, medical or business outcome the source doesn't back. If the owner works in a regulated field, `PROFILE.md` lists the gates. Their final check still applies.

## Process

Separate fixed facts from reshapeable language. Re-say the whole piece as the owner would, don't line-edit. Compare with their samples. Read it aloud. Hand back usable copy, with a note only for a material assumption or missing fact. Full steps: `references/voice-craft.md`.

## Final check

- Zero em dashes and semicolons. No banned words, general or the owner's.
- Sounds like one specific person. Varied rhythm, concrete detail, a stated point of view, no hedging.
- Every claim supported, every disclosure intact.
- Meets the quality bar in `PROFILE.md`.
- Would the owner stand behind it?

---
name: prospect-mover
description: "Revamp anything static a prospect will see so it moves them toward a close, and run it by default on prospect-facing work. Always asks the goal first (the close: signed, booked, replied, bought, referred), then makes every beat win the next rung toward it. Rebuilds wording, structure, vibe, color, layout and influence on proven systems (Kahneman, Cialdini, Voss, StoryBrand, Schwartz, Fogg, loss aversion, anchoring, defaults), scores it, ships at 9+ and hands back the revamp plus 2 one-lever test variants. Use on websites, landing pages, quotes, proposals, email and text campaigns, sequences, call and voicemail scripts, ads, fliers, decks, offers, forms. Also trigger on \"make this convert\", \"make it sell\", \"more persuasive\", \"revamp this\", \"punch this up\", \"nobody's responding\", \"get them to book\". Skip one-off replies to a single email or text. Any business, product, cause or hire. Includes a call playbook and a regulated-work rider."
---

# Prospect Mover

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

People decide by feel in a split second, then use logic to defend the choice. This skill makes the right choice feel **safe, easy and obvious**, honestly, on every layer a prospect touches: words, structure, vibe, visuals and influence.

Bar: the quality bar in `PROFILE.md` (default: right the first time, complete, proven, no homework for the owner) plus the Move Score (`references/move-score.md`). Ship at 9 or higher.

Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`. It tells you what the owner sells, who the buyers are, and where the facts live.

Read `VOICE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`. The owner's own taste (samples, banned words, sign-off, length rules) beats the general research in the reference files wherever the two conflict.

**Universal by design.** The systems work for any business, product, service, cause or hire. What changes is the buyer, so every piece starts with the vertical adapter (`references/verticals.md`) and is read fresh. Never carry one industry's buyer, words, metaphors, look or rules into another. For regulated work, load `references/verticals.md#regulated-work`. If the owner has a deep lens for their own vertical, it lives beside it. `references/lens-example.md` shows what one looks like and `references/lens-template.md` is the blank.

For calls, voicemails and follow-ups after a call, read `references/call-playbook.md`.

## The one test that never bends

**The daylight test:** would this still work if the prospect saw exactly what you did and why? Real scarcity, real proof, real authority, a real reason to act now: yes. Invented deadlines, fake counts, borrowed credentials, shame, confusion: no. Fail the daylight test and the piece doesn't ship, however well it scores. Manipulation wins one click and loses the client, the referral and sometimes the license.

## When it runs

**By default** on any static piece a prospect will see that the owner is building or rewriting: websites and landing pages, quotes and proposals, email and text campaigns and sequences, call and voicemail scripts, ads, fliers, decks, offers, forms. Inside another job (a site build, a copy pass, a content pass, a quote or proposal pass; the matching skill is in `ROUTER.md`), run this as the persuasion pass on the draft that job produces. That job still owns its research, facts, structure and gates.

**Skip** one-off replies to a single email or text, internal notes and messages to the owner.

## Ask the goal first: what's the close?

Every run starts by asking for the goal, unless the request already names it. The goal is **the close**: the final yes the business wants from this prospect. Everything in the piece moves them toward it.

Ask it as one short question with your pick first and marked "(Recommended)". Where the AI surface offers clickable options, use them. Build the options from the piece and the vertical, for example:

- "Signed contract / paid order" (the deal itself)
- "Booked call or meeting"
- "Reply or conversation started"
- "Referral, review or repeat purchase"

Then set two things and state them at the top of the output:

1. **The close:** the final yes (for example, "a signed roof replacement").
2. **This piece's job:** the next rung toward that close that this piece can realistically win from where the prospect is now (for example, "book a free inspection"). Use the close ladder in `references/structure.md#the-close-ladder`. A cold email rarely closes a sale. It wins the next rung.

Inside another job, take the close from that job's brief and label it `inferred` if it isn't stated. Don't stop that job to ask.

Then, only if the answer still changes the result, ask up to 3 more short questions in the same batch. Look up first: the project notes, past versions, call notes, the offer.

- **Who exactly is reading?** (one person, not a market)
- **How aware are they?** (`references/structure.md#awareness`: unaware, problem aware, solution aware, product aware, most aware)
- **Where does it land?** (inbox, phone, feed, print, live call)

Missing answers you can infer: infer, label it `inferred` in the change log, keep going.

## The pipeline

### 0. Read the vertical

Fill the adapter in `references/verticals.md` from the project's own truth: the one buyer, the job they're hiring it for, what they do instead, what staying put costs, what they fear about buying, the proof they trust, the honest trigger, the smallest next step, their words and the rules that apply. Three to ten lines. Every example, metaphor and proof point in the rebuild comes from that buyer's world.

### 1. Diagnose before you touch it

Read the piece as the prospect would: tired, on a phone, five seconds of patience. Write down:

- **The 5-second read.** What would they say this is about? What do they feel? What would they do next?
- **The friction.** Every point where they would stop, doubt, get confused or have to think.
- **The leak.** The single biggest reason this isn't moving people now. Usually one of: it talks about the sender, not the reader. There's no felt problem. Too many asks. No proof. The ask is too big for the trust earned. It looks cheap or cluttered.
- **Baseline Move Score**, each of the 10 checks, with one line of evidence each.

### 2. Rebuild the spine

Every piece that moves people follows the same five beats, compressed or expanded to fit the format:

1. **Stop** (attention): a hook about *them*, specific and a little surprising. Pattern break, a number, their own words, a question they've asked themselves.
2. **Feel** (the gap): where they are now vs where they want to be, and what it costs to stay put. Status quo is the real competitor.
3. **Trust** (proof): why believe you. Specific proof, an honest authority signal, a story of someone like them.
4. **Ease** (the path): a plan with three steps or fewer, the risk taken off the table, the objection answered before it's asked.
5. **Act** (one ask): this piece's rung toward the close. One small, clear, low-risk step, with a true reason to take it now. Every earlier beat sets up this ask, so cut anything that doesn't.

Pick the frame by awareness level and format: `references/structure.md`. Format playbooks (email, text, call script, voicemail, landing page, ad, flier, deck, proposal, follow-up sequence, form or button): `references/formats.md`.

### 3. Run the five layers

Work each layer in its reference file. Change only what earns its place. Less is more: cutting usually moves people more than adding.

| Layer | What it controls | Reference |
|---|---|---|
| Wording | Every word and sentence: fluency, framing, specificity, "you" focus, reasons, questions | `references/wording.md` |
| Message | Order, frame, story, objections, the ask | `references/structure.md` |
| Vibe | Warmth, status, confidence, tone, pacing | `references/vibe.md` |
| Visual | Color, contrast, hierarchy, white space, type, imagery, layout, the button | `references/visual.md` |
| Influence | Cialdini's 7, biases, defaults, anchors, friction, B=MAP | `references/influence.md` |

Spoken formats (calls, voicemails, live pitches) lean hardest on `call-playbook.md`, then `vibe.md` and the Voss tools in `structure.md#live-conversation`. Visual pieces get the full `visual.md` pass. A plain text message skips visual and spends that time on wording.

### 4. Gates

- **Truth.** Never invent a number, testimonial, client count, deadline, award, credential, guarantee or outcome. That includes service promises ("we reply the same day", "ships tomorrow") and identity facts ("family owned", "independent", "since 1998") the source doesn't state. Each one is a promise the business has to keep. A hedged fact stays hedged everywhere it appears: "usually same-week" can't become "Book this week" in the headline. Missing fact: write around it or leave `[OWNER: fill]` (`[CLIENT: fill]` on a client's piece). A great persuasive line with a fake fact is a liability.
- **Regulated work.** Finance, insurance, health, legal, credit, housing, employment, income claims: load `references/verticals.md#regulated-work` and check the vertical's own claim rules (`verticals.md`). A human makes the final call on claims.
- **Voice.** Final words go through `ghost-mode` and the owner's `VOICE.md` (no em dashes, no AI tells). Interface text also follows `simple-talk`.
- **Sending.** This skill drafts. It never sends to a prospect. Sends follow the owner's gates in `PROFILE.md`.

### 5. Score, repair, ship

Score the rebuilt piece on the Move Score. Fix the weakest check, rescore. Two rounds max on the same check, then change the approach (a different hook, frame or offer) instead of polishing. Ship at 9+ on every check and a pass on the daylight test.

When the piece is high stakes or the owner asked for proof, read the rebuild cold as the prospect (a fresh helper that never saw the original is better) and answer the three 5-second questions again.

## Output

Hand back, in this order:

0. **The close and this piece's job**, one line each: "Close: signed contract. This piece: book the site visit."
1. **The revamp**, ready to use.
2. **Two test variants.** Each changes exactly one lever from the revamp (the hook, the frame, the ask, the proof, the offer or the visual), so a test tells you which lever moved people. Label each: `Variant A: <lever> | what changed | the bet`. Pick the levers most likely to matter for this reader, not the easiest to swap. Test what moves people toward the close. A subject-line-only variant tests opens, so use it only when opens are the proven leak.
3. **The leak** in one line: what was stopping the original, and the fix.
4. **Change log**, 3 to 7 rows: `lever | what changed | why it moves them`.
5. **Move Score** before to after, one line per check that moved.
6. **Fill before sending**: a checklist of every `[OWNER: fill]` blank, so an unfilled piece never goes out. Then inferred assumptions and any gate it hit.
7. **How to test**: where to split the variants (send half the list each, rotate ad sets, alternate weeks on calls) and the one number to watch: the rate at which people take this piece's rung, and how many of them go on to the close. Never opens or link clicks alone. A measured win is worth saving in the owner's notes (where `PROFILE.md` says they live) with its numbers and date, and into `VOICE.md` if it is a wording rule.

Short pieces (a subject line, a text, a button) get the close line, the revamp, the two variants, the leak and the fill checklist. Skip the rest.

Before handing back, re-read the revamp for every visitor type the piece serves (a hero that only speaks to storm victims loses the leak and old-roof visitors) and for the phone layout (the call or tap option must sit above the first image on mobile).

## Tools

- `scripts/move_lint.py <file>` (path relative to this skill folder) flags the mechanical leaks: em dashes, sender-focus ("we/our/I" vs "you"), weak openers, hedges, stacked asks, urgency words that need a real reason, long sentences, reading grade. Run it on every written rebuild. It catches leaks. It doesn't score persuasion, you do. `tests/test_move_lint.sh` checks the linter itself.
- Visual pieces: render and look at phone width with `pixel-proof` before calling it done.
- New concept, or the piece feels generic: `creative-direction`.
- Whole-site builds, positioning that needs market research, or product-fact checks: hand to the matching skill in `ROUTER.md`, then run this as the persuasion pass.

Worked before/after examples: `references/examples.md`.

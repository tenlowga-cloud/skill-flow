---
name: inbox
description: Runs the owner's email routines: triage passes that sort the inbox into reply now, reply later, waiting, FYI, receipts, newsletters and spam, with a draft ready in the owner's voice for anything that needs an answer; a follow-up sweep for threads that went quiet; and the common drafts (reply to a quote request, a complaint, a quiet lead, a meeting confirmation, a recap, a decline, an intro, a review ask). Drafts only; the owner taps send. Use on "go through my inbox", "triage my email", "who have I not replied to", "draft a reply to", "follow up with", "/inbox", or when the inbox routine fires.
---

# inbox

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

The inbox is where the owner's day leaks. This skill gives it back: a short list of what needs them, a draft already waiting for each one, and nothing sent without their tap.

## 1. Read first

Read `PROFILE.md`, `TOOLS.md` and `VOICE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). `TOOLS.md` must show email connected; if not, run `connect` for it and stop here. `VOICE.md` governs every draft. `PROFILE.md` gives the gates, the send window and who counts as a client.

## 2. Triage pass

Follow `references/triage-rules.md`:

1. Pull threads since the last pass (default: 18 hours on the morning pass, since the previous pass otherwise).
2. Sort each into one bucket: Reply now, Reply later, Waiting on them, FYI, Receipts and notices, Newsletters, Spam or phishing.
3. Anything with money, a legal word, or a client complaint goes to the top, flagged.
4. For every Reply now and Reply later, write the draft (step 4) and save it in the drafts folder, attached to the thread.
5. Apply labels or folders if the owner allowed them in `PROFILE.md`; otherwise list only.
6. Report: at most 10 items, one line each, bucket first, then who, then the one-line gist, then "draft ready" where it is.

Never click a link in a suspected phishing mail. Never unsubscribe, archive or delete a client's thread without the owner's yes.

## 3. Follow-up sweep

Threads the owner sent that got no reply in 3 business days (or the number in `PROFILE.md`), skipping anything marked done. For each: who, what was asked, how long it has been, and a nudge draft in the owner's voice. Report as a list, oldest first.

## 4. Drafts

Use the shapes in `references/draft-patterns.md`, then run `ghost-mode` so it reads like the owner wrote it. `VOICE.md` samples and banned words beat every pattern. A draft to a prospect goes through `prospect-mover` first when it is more than a quick reply.

A draft is saved to the drafts folder, never sent. Say "draft ready" and where. If the owner says "send it", that is their yes for that one message; check the send window first.

## 5. Say it back

Three lines: how many need them now, what is flagged, and where the drafts are. The full list is in the message body under those three lines, never more than 10 items on a routine pass.

## As a routine

The inbox triage and follow-up sweep routines in `routines/references/routine-library.md` run this skill three times a day and each morning. The routine never sends; it leaves drafts and a list.

## Rules that do not move

- Drafts only. The owner sends.
- One line per thread. The owner reads the list in a minute.
- Money, legal and complaints first.
- Phishing is flagged, never opened.
- Nothing about a client's mail leaves the owner's tools.

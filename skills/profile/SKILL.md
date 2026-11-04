---
name: profile
description: "Quick lookup of who and what is in the owner's operation, answered live from the profile folder and the owner's own notes, never from memory. Use for who owns a job, which project or business something belongs to, where something lives (code, notes, CRM, docs, chat), what matters most this week, which tool or AI lane a job starts on, and what needs the owner's yes. Triggers: \"who is\", \"who owns\", \"which project\", \"where does X live\", \"what's the priority\", \"which tool do we use for\", \"profile\"."
---

# Profile

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

A map from a question to the file that owns the answer. Open the file, answer from it, say where the answer came from. This skill keeps no facts of its own.

## How to answer

1. **Pick the file** from the table below. One question, one or two files. Do not load everything.
2. **Open it live.** Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`. The same goes for `TOOLS.md`, `VOICE.md`, `ROUTER.md` and `STACK.md`.
3. **Follow the pointer if the fact lives elsewhere.** `PROFILE.md` has a "Where things live" section. If the answer is in the owner's own notes, code host, CRM or docs, open that source and read the one page that owns the fact.
4. **Answer** with the fact and where it came from (file and section). Lead with the answer, then the catch, then the next step, unless `VOICE.md` sets a length rule.
5. **Check the date.** If `PROFILE.md` carries a `verified:` date older than 60 days, add one line saying the fact may be stale and the owner should re-check it. Do this always when the fact drives money, a client or a send.
6. **Not in the files:** say "unknown" and offer to run `setup` to add it. Do not fill the gap from memory or guess.
7. **The owner's latest instruction beats the files.** If the owner contradicts a file, use their version and say so in one line. Offer to update the file.

## Which file owns the answer

| Question | Open |
|---|---|
| Who the owner is, how to address them | `PROFILE.md`, Owner |
| What they run, status of a project, where its files live | `PROFILE.md`, What you run |
| Who a person is and why they matter | `PROFILE.md`, People |
| Who or which AI lane owns a job, how to reach it | `PROFILE.md`, AI lanes |
| Where code, notes, CRM, docs or chat live | `PROFILE.md`, Where things live |
| What matters most this week | `PROFILE.md`, Priorities |
| What needs the owner's yes | `PROFILE.md`, Gates |
| When to send, when not to | `PROFILE.md`, Working hours and send windows |
| What "done" means | `PROFILE.md`, Quality bar |
| Which tool or AI surface a job starts on | `TOOLS.md` |
| How the owner writes, banned words, sign-off | `VOICE.md` |
| Which skill or plugin to call for a request | `ROUTER.md` |
| What is installed, connected, scheduled or built; what is waiting on the owner | `STACK.md` |
| What blueprint built and how to trigger each piece | `BLUEPRINT.md` |
| The owner's logo, colors, fonts and brand rules | `BRAND.md` |
| Anything else | The owner's notes, where `PROFILE.md` says they live |

## Private data

People entries hold a role and one fact that matters. No contact details, account ids or secrets. Answers never copy those out of a source. Private data stays in its room.

## Keeping it honest

When a live source disagrees with a profile file, the source wins. Say so once at the end of the answer so the file gets fixed. Update a file from the source, never from memory, and refresh its `verified:` date.

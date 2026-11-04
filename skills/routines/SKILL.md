---
name: routines
description: Creates, changes and checks the owner's scheduled routines: morning brief, pre-meeting notes, inbox triage, follow-up sweep, end-of-day wrap, weekly review, pipeline check and more. Picks the right scheduler for the surface (Claude Code cloud scheduled tasks, Desktop scheduled tasks, /loop, or a fallback), fills the prompt from the library with the owner's profile paths and times, schedules it, and reads the first run. Use on "set up a routine", "every morning", "remind me every", "schedule", "run this daily", "/routines", "what routines do I have", "stop the morning brief", or when setup or blueprint reaches its routines step.
---

# routines

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

A routine is a prompt that runs on a schedule with no one typing it. Done right, the owner's morning starts with a brief already waiting, a note already written for the 10am, and five drafts in the drafts folder. This skill makes that real on whatever surface the owner has.

## 1. Read first

Read `PROFILE.md`, `TOOLS.md` and `STACK.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). `PROFILE.md` gives the hours, the time zone, the send window and the gates. `TOOLS.md` says which tools a routine can read. `STACK.md` lists the routines already scheduled, so you never schedule one twice.

Then read the live schedule on the surface (`/schedule` list in Claude Code, the Scheduled page, or `CronList` for in-session tasks) and reconcile it with `STACK.md`. A routine in one place and not the other gets fixed before anything new is added.

## 2. Pick the routine

The owner names it, or `setup` and `blueprint` hand you the picks. Match it to `references/routine-library.md`. No match: write a new entry in the same shape (runs, reads, makes, never without a yes, needs, prompt) and add it to the library section of `STACK.md` so it is reusable.

Check its tools against `TOOLS.md`. A routine whose tool is not connected is not scheduled; it goes to `connect` first, or into `STACK.md` as "waiting on <tool>" with the one step that unblocks it. Say so in one line.

## 3. Pick the scheduler

Use the decision table in `references/scheduling-by-surface.md`:

- Needs to run with the machine off, and needs connectors: a **cloud scheduled task** (`/schedule` in Claude Code, or claude.ai/code/routines). The default for daily routines.
- Needs local files or local tools: a **Desktop scheduled task**.
- Polling inside one working session: `/loop`. Never for a daily routine; it expires in seven days.
- No scheduler on this surface: the fallback in the reference (a calendar reminder that opens the prompt, or the OS scheduler running the CLI).

Say which one you picked and why, in one line.

## 4. Fill the prompt

Take the library prompt and:

1. Replace `PROFILE.md`, `TOOLS.md`, `VOICE.md` with the full paths of the owner's files, so a fresh session can open them. On a cloud task that cannot see the owner's machine, put the profile files in a repo the task can read, or paste the needed lines into the prompt (never a secret, never client data).
2. Set the time from the owner's answer, in their time zone. Keep it off the hour and half hour when the scheduler jitters (`:05`, `:35`), unless the owner asked for an exact time.
3. Keep every rule block from the library: owner-only delivery, send window, source on every fact, quiet is fine.
4. Add the one line that says where output lands (chat, a note file, the drafts folder), from `PROFILE.md`, Where things live.

## 5. Schedule it and prove it

Create the task. Read the schedule back and show the owner the row: name, cadence, next run. Then, where the scheduler allows, run it once now (or wait for the first fire) and read the output. A first run that errors or comes back empty is not done: fix the prompt, the path or the connection and run again.

Record it in `STACK.md`: routine, scheduler, cadence, next run, the date of the first good output.

## 6. Change or stop one

"Move the brief to 7", "stop the pipeline check", "add my CRM to the morning brief": find it in `STACK.md` and on the live surface, change it in both, read back the row. A stopped routine stays listed in `STACK.md` as stopped with the date, so a re-run of `setup` does not offer it again without asking.

## Rules that do not move

- A routine never sends to anyone but the owner unless `PROFILE.md`'s gates allow it, and never outside the send window.
- A routine never spends, deletes, signs or goes live. It stops at a draft or a ready-to-run step and says so.
- Every fact in a routine's output carries its source. Quiet is fine; invented is not.
- One routine, one job. A morning brief that also triages the inbox and preps meetings is three routines.
- Cloud tasks include every connected connector by default. Remove the ones the routine does not need before saving (Advanced settings, Connectors tab).

## Say it back

Three lines: what is scheduled and when, what is waiting on a tool or the owner, and when the first output will land.

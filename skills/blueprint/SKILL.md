---
name: blueprint
description: The master skill. Takes one prompt from the owner describing what they want Claude to take off their plate, reads every profile file, and builds out everything else they need in one run: the business-specific skills, the templates and checklists, the routines, the connector and plugin recommendations, the operating file updates, and a one-page map of what now exists and how to use it. Runs at the end of setup and again whenever the owner says "build me what I need for X", "set me up for", "I want Claude to handle", "/blueprint", or describes a new area of their work.
---

# blueprint

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

One prompt in. A working system out. The owner says what they want off their plate; you turn that into the skills, routines, templates and connections that make it happen, built and proven, with a map they can read in two minutes. You do not describe what you could build. You build it.

## 1. Read everything first

Read `PROFILE.md`, `TOOLS.md`, `VOICE.md`, `ROUTER.md`, `STACK.md` and `BRAND.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If `PROFILE.md` is missing, run `setup` first; a blueprint built on no profile is a guess.

Read the owner's first page from `PROFILE.md`, Where things live, if one is named. Read the live skill list. Hold the owner's one prompt against all of it.

## 2. Turn the prompt into outcomes

Rewrite the prompt the way `flow` step 2 does: the finished result, the bucket (save time, make money, stop something breaking), what they did not say, done-means, proof, gates. Then split it into outcomes, each one a thing that will exist when you are done. Five to twelve outcomes is normal. Examples for "take my client follow-up and meeting prep off my plate":

- A `meeting-prep` routine 60 minutes before every client meeting, with the brief in their notes and a copy in chat.
- A follow-up sweep every weekday morning, drafts ready in their voice.
- A `client-notes` skill that files call notes into the right client page.
- A connected calendar, email and CRM (or the exact steps to connect what is missing).
- A `clients/` folder or page shape in their notes, one page per client.
- A one-page map of all of the above.

Ask up front only if 1 to 4 answers would change the build (which clients count, which calendar, where notes should land). One message, clickable, your pick first. Then run to done.

## 3. Plan it as the planner would

This is a big job by definition. Run `flow` step 5: the `planner` agent cuts the slices (one owner each, no two writers on one file), the `writer` agents build them together, you integrate, the `reviewer` checks anything the owner's clients will see. On a surface without subagents, play the three roles in sequence yourself.

The slice kinds and what each builds:

| Slice | Builds | Done means |
|---|---|---|
| Skill | A `SKILL.md` in the owner's skills folder, in this kit's shape, plus references it needs. Named for the job, triggered by the words the owner uses. Added to `ROUTER.md`. | Loads, runs once on a real prompt, output matches the owner's bar. |
| Template | A checklist, brief, page shape or document template in the owner's notes or docs tool, in their voice. | Saved where `PROFILE.md` says, filled once with real data. |
| Routine | A scheduled prompt from `routines/references/routine-library.md`, tailored, scheduled on the right surface. | Appears in the schedule list; first run output checked. |
| Connection | A connector, plugin, repo or bridge, walked through with `connect`. | Verify prompt returns real data. |
| Rule | A line in the operating file or `ROUTER.md` that routes a recurring ask. | `operating-rules` re-run, file read back. |
| Map | `BLUEPRINT.md` in the profile folder: one page, what exists, where, how to use it, what is waiting on the owner. | Owner reads it and nothing is missing. |

The least build that works. Three skills beat nine when three will do. Reuse a skill that already exists on the owner's surface before writing a new one; `ROUTER.md` and the live list tell you what exists.

## 4. Build the skills right

A skill you write for the owner follows this kit's own rules:

- Frontmatter `name` and `description`; the description says when to trigger, in the owner's words, under 1,024 characters.
- A short SKILL.md: what it does, the steps, the gate, what good looks like. References in `references/` for anything long.
- It reads the profile files by the exact wording this kit uses, never hardcodes a name, a path or a tool the profile already holds.
- Voice through `ghost-mode` for anything a person other than the owner reads; `prospect-mover` if a prospect reads it; `BRAND.md` plus the design bar (`protection-desk/references/design-bar.md`), `impeccable` and `pixel-proof` if a person sees it on a page or a screen. A template a client will see is built in the brand and scored before it is called built.
- No secrets, no client data, no contact details in the skill. Those live in the owner's systems.
- Test it once on a real prompt before you call it built.

Skills by business type, as a starting list, not a rule:

- **Client service (agency, insurance, trades, coaching, consulting):** client-notes, meeting-prep tuned to their CRM, proposal or quote (insurance: `protection-desk`), follow-up sequences, intake form to CRM, review and referral asks, monthly client report.
- **Software or product:** pull request review, release notes, bug triage, customer feedback digest, changelog, onboarding email sequence, status page update.
- **Content or creator:** idea capture, weekly content plan, draft in voice, repurpose one piece into five, newsletter, sponsor outreach.
- **A job inside a company:** meeting prep, inbox triage, weekly status, 1:1 notes, project tracker update, slide draft.

## 5. Integrate and prove

Collect every slice. Check each against its done-means. Run the whole-system proof: trigger each new skill once with a real prompt, read each routine's first output, run each connection's verify prompt, open each template filled. Fix seams (a skill that points at a template path that does not exist, a routine that needs a tool that is not connected). The `reviewer` reads anything a client will see.

Update `STACK.md` with everything that now exists. Re-run `operating-rules` if a gate, a trigger or a priority changed.

## 6. Write the map

`BLUEPRINT.md` in the profile folder, one page, in this order:

1. What you asked for (their prompt, verbatim).
2. What exists now: each skill, routine, template and connection, one line each, with how to trigger it (the words to type or the time it runs).
3. What is waiting on you: connections that need a click, gates that need a yes, a sample they still owe. One line each with the exact next step.
4. How to change it: `/skill-flow:connect`, `/skill-flow:routines`, "re-run blueprint with a new prompt".

Then say it back in three lines: what exists, what is waiting on them, and the first thing to try.

## Rules that do not move

- Build the real thing. A skill file, a scheduled routine, a filled template. Never a list of things that could be built.
- Nothing invented. Every fact in a template or a skill comes from the profile, the owner's files or the owner's answer.
- Gates stay with the owner. A routine or skill that sends, spends, deletes or goes live stops at a draft or a ready-to-run step and says so.
- Re-runnable. A second `blueprint` run reads `STACK.md` and `BLUEPRINT.md`, keeps what works, and adds only what the new prompt needs.

## What good looks like

Owner says: "I want Claude to handle my inbox and make sure I never walk into a client meeting cold." Blueprint builds: inbox triage three times a day with drafts in their voice; a follow-up sweep; meeting-prep 60 minutes before every client meeting pulling calendar, CRM and email; a `clients/` page shape in their notes with one page per client filled from the CRM; the calendar, email and CRM connections walked through and verified; the map. The owner's first morning after: a brief in chat, five drafts waiting, and a one-page note for the 10am.

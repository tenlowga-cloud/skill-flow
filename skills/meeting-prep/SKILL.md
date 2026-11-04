---
name: meeting-prep
description: Writes the one-page pre-meeting note for a client, prospect or partner meeting: who they are, the last three touches, what they care about in their own words, open items, money, risks, the goal, three questions to ask, and the sources for every fact. Pulls from calendar, CRM, email, notes, transcripts and chat, in that order. Runs on demand and as the pre-meeting routine 60 minutes before each outside meeting. Use on "prep me for", "who am I meeting", "what do I need to know before", "brief me on", "/meeting-prep", a calendar event with someone outside the team, or when the routine fires.
---

# meeting-prep

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

Nobody should walk into a meeting cold. This skill makes a one-page note the owner can read in two minutes, with every fact traced to where it came from and nothing invented.

## 1. Find the meeting

From the owner's words, or from the calendar: the event, its time, the attendees, the description and any attached document. If two meetings fit, ask one question. If the attendee is on the owner's team (`PROFILE.md`, People and AI lanes), say so and ask whether they still want a note; the routine skips those by default.

## 2. Gather, in order

Follow `references/sources.md`: calendar first, then CRM, then email, then notes or vault, then transcripts and recorders, then chat, then public pages if `TOOLS.md` allows web. Read `TOOLS.md` for what is connected; a tool that is not connected goes under "Not checked", never guessed at.

Two people with the same name: match on company, email domain or the CRM record before you write a word. Still unsure: say so in the note.

Skip what the meeting does not need: health, legal or family detail that is marked private or has no bearing on the goal.

## 3. Write the note

Use `references/brief-template.md` exactly. Under 300 words of body. Every fact carries its source in brackets (the CRM record, the email date and subject, the note page, the transcript date). Unknown says unknown. Their words are quoted, not paraphrased, when the point is what they care about.

The goal line is the owner's goal for this meeting, from the calendar description, the CRM stage or the last touch. If none of those says it, write the most likely one and mark it "assumed".

Voice: the note is for the owner, so `simple-talk`. Nothing in it is for the attendee.

## 4. Deliver and file

Send it to the owner in chat. Save a copy where `PROFILE.md` says client notes live (a page per client in the vault, a CRM note, a folder). If the owner has no such place, offer the `clients/` page shape from `blueprint` once, then save to the profile folder under `meetings/` in the meantime.

Never contact the attendee. Never add the note to a shared calendar event others can read.

## 5. After the meeting

If the owner shares notes, a recording or a transcript afterward, offer the follow-up pass: file the notes to the client page, draft the recap email in `VOICE.md` through `ghost-mode` (a draft, never sent), and add the promised items to wherever tasks live. The `inbox` skill's draft patterns cover the recap.

## As a routine

The pre-meeting routine in `routines/references/routine-library.md` runs this skill on a schedule: hourly on weekdays inside work hours, it looks 45 to 75 minutes ahead for a meeting with someone outside the team, writes the note, sends it to the owner, and stops fast when there is nothing coming.

## Rules that do not move

- Every fact has a source. No source, no fact.
- Private detail stays private. The note holds what the meeting needs and nothing more.
- The attendee never hears from this skill.
- Under 300 words of body. A note nobody reads is not prep.

# Routine library

Ready-to-schedule routines. Pick one, fill in the time with the owner, then schedule it (see scheduling-by-surface.md).

How to read each entry:
- **Runs**: default cadence, in the owner's local time. Change it to fit the hours in PROFILE.md.
- **Reads**: tools from TOOLS.md. If a tool is not connected, the routine says so in its output and does the part it can.
- **Makes**: where the result lands.
- **Never without a yes**: things it must not do alone.
- **Prompt**: paste this as the scheduled task. It works in a fresh session with no other context.

## Rules every routine follows

These are already written into each prompt. Do not remove them.
1. Read PROFILE.md first (who the owner is, team, priorities, gates, hours, send window). Read VOICE.md before writing anything a person will read.
2. Only the owner gets messages by default. Anything for another person stays a draft unless the gates in PROFILE.md allow sending, and it never goes out outside the send window.
3. Every fact carries its source. Nothing invented. Unknown says "unknown".
4. If a tool in TOOLS.md is missing or fails, say which one and do the rest.
5. Quiet is fine. If there is nothing to report, send one line saying so.

The prompts say `PROFILE.md`, `TOOLS.md`, `VOICE.md`. When you schedule one, replace each with the full path to the owner's file so a fresh session can open it.

---

## 1. Morning brief
- **Runs**: weekdays, 30 minutes before the start time in PROFILE.md (default 7:30).
- **Reads**: calendar, inbox, task list or CRM (for the top priority).
- **Makes**: one message to the owner, under 150 words.
- **Never without a yes**: send, accept, decline, or move anything.
- **Needs**: calendar, email. Optional: tasks, CRM.

Prompt:
```
You are the owner's assistant. Read PROFILE.md, TOOLS.md and VOICE.md first.
Build a morning brief for today. (1) List today's calendar events with time, who, and one line on why it matters. (2) Scan the inbox for the last 18 hours and list up to 5 threads that need the owner today, one line each. (3) Name the top priority from PROFILE.md and the first step. (4) Flag any conflict, double booking, or meeting with no prep.
Send it to the owner only, in VOICE.md style, under 150 words. Do not send, accept, decline, or change anything. If calendar or email is not connected, say so and give what you can. Cite where each item came from.
```

## 2. Pre-meeting notes
- **Runs**: 60 minutes before each client meeting (format: meeting-prep skill). Schedule it hourly on weekdays inside work hours; it stops fast when no client meeting is coming.
- **Reads**: calendar, CRM, email, notes, call recordings.
- **Makes**: one page per meeting, sent to the owner.
- **Never without a yes**: contact the attendee.
- **Needs**: calendar. Better with CRM and email.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Check the calendar for any meeting that starts in 45 to 75 minutes with someone outside the owner's team. If there is none, reply "No client meeting in the next hour" and stop.
For each meeting, follow the meeting-prep skill's references/brief-template.md and references/sources.md exactly. Make the one-page note: under 300 words of body, every fact with its source, unknown marked unknown.
Send it to the owner only. Do not contact the attendee. If a source tool is not connected, list it under "Not checked".
```

## 3. Inbox triage (3 passes a day)
- **Runs**: weekdays at 8:00, 12:30, and 16:30 (shift to fit the hours in PROFILE.md).
- **Reads**: email.
- **Makes**: a short list to the owner, labels on threads, drafts in the drafts folder.
- **Never without a yes**: send, delete, unsubscribe, or archive anything from a client.
- **Needs**: email.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Follow the inbox skill's references/triage-rules.md and references/draft-patterns.md.
Sort every unread thread since the last pass into the buckets in triage-rules.md. Make drafts for Reply now and Reply later. Never send. One line per thread. The 8:00 pass lists at most 10 items; flag money, legal and complaints first. Send the owner a summary: counts per bucket, then the list. If email is not connected, say so and stop.
```

## 4. Follow-up sweep
- **Runs**: weekdays at 9:00.
- **Reads**: sent mail, CRM, tasks.
- **Makes**: a list of quiet threads plus a nudge draft for each, to the owner.
- **Never without a yes**: send a nudge.
- **Needs**: email. Optional: CRM.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Find threads where the owner sent the last message 3 or more business days ago and nobody replied. Skip threads marked done or closed, and skip anyone PROFILE.md says not to chase. For each, give a one-line summary (who, what was asked, days quiet) and a short nudge draft in VOICE.md style, using the nudge pattern in the inbox skill's draft-patterns.md. Save drafts only. Send the owner the list, oldest first, max 10. Never send to the other person.
```

## 4b. GoHighLevel assistant sweep
- **Runs**: weekdays, hourly inside the hours in PROFILE.md, plus one full pass at the start of the day.
- **Reads**: GoHighLevel (tasks, conversations, opportunities, calendar, contacts) through the HighLevel MCP connection.
- **Makes**: notes and task updates in GoHighLevel, drafts saved on the contact, and one short report to the owner: what moved, what needs them, what is waiting. Quiet sweeps send one line.
- **Never without a yes**: send a message to a contact, delete anything, change a field on a client record, move a pipeline stage, change an appointment or a client's tags.
- **Needs**: GoHighLevel connected. Better with the phone app installed, so the owner answers from their pocket.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md (or the profile block pasted below this line for a run that cannot read files). Follow the ghl-assistant skill exactly. The last sweep time is the first line of the GoHighLevel task "Assistant: waiting on you"; if that task does not exist, this is the first sweep: look back 24 hours and create the task. Through the GoHighLevel connection, pull since the last sweep: tasks assigned to the owner due today or overdue, conversations with an unanswered inbound message, opportunities assigned to the owner that changed, were created or have had no activity in 7 days, appointments in the next 24 hours, new contacts assigned to the owner. Sort each into Do it, Draft it, Ask, Flag or Skip. Do what is within reach (notes, task updates when the record shows it is done, drafts in VOICE.md style, meeting-prep notes). Never send a message to a contact, delete anything, change a field on a client record, or change a stage, appointment or tag; those go in Ask with your recommended answer. Report to the owner only: three lines (what moved, what needs them, what is waiting), then Flag, Ask (at most 4, your recommended answer first), Draft ready, Done, at most 12 lines. Nothing new: one line and stop. Keep the open questions in the GoHighLevel task "Assistant: waiting on you" so you never ask twice, and write this sweep's time as its first line. Never write a contact name or id anywhere outside GoHighLevel.
```

## 5. End-of-day wrap
- **Runs**: weekdays 30 minutes before the end time in PROFILE.md (default 16:30).
- **Reads**: calendar, inbox, tasks, CRM.
- **Makes**: one message to the owner.
- **Never without a yes**: change any task or record.
- **Needs**: at least one of calendar, email, tasks.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Write an end-of-day wrap for the owner in four short parts. (1) What moved today (meetings held, replies sent, tasks done), with sources. (2) What is stuck (waiting on someone, overdue, blocked), and on whom. (3) Anything that needs the owner before tomorrow. (4) Tomorrow's first task, chosen from the priorities in PROFILE.md and tomorrow's calendar. Under 150 words. Owner only. Change nothing. If a tool is missing, say which and skip its part.
```

## 6. Weekly review
- **Runs**: Fridays at 15:30.
- **Reads**: calendar, inbox, tasks, CRM, notes.
- **Makes**: a note named `weekly-review-YYYY-MM-DD` plus a short message to the owner.
- **Never without a yes**: change the priorities in PROFILE.md.
- **Needs**: any two of calendar, email, tasks, CRM.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Review this week, Monday to today. Write: Wins (up to 5, with source). Stuck items (up to 5, with the blocker and how long). Decisions the owner needs to make (each as a yes/no question with a suggested answer). Next week's top 3, ranked against the priorities in PROFILE.md. Save it as a note named weekly-review-<date> in the notes location from TOOLS.md, or send it as a message if there is none. Do not edit PROFILE.md. Owner only. Under 300 words.
```

## 7. Pipeline check
- **Runs**: Mondays at 8:30 (daily for fast sales cycles).
- **Reads**: CRM.
- **Makes**: a list to the owner with a next step for each deal.
- **Never without a yes**: edit deal stages or contact leads.
- **Needs**: CRM. With none, the routine says so and offers the follow-up sweep instead.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. In the CRM, find open deals with no activity (no call, email, note, or task) in the last 7 days. For each give: name, stage, value if known, last activity date, and one suggested next step. Sort by value, biggest first, max 10. Flag deals past their expected close date. Owner only. Change nothing in the CRM. If no CRM is connected, say so and stop.
```

## 8. Content or post draft (weekly)
- **Runs**: Wednesdays at 10:00.
- **Reads**: VOICE.md, PROFILE.md, notes, recent wins, web if TOOLS.md allows.
- **Makes**: 2 draft posts saved as a note, for the owner to pick from.
- **Never without a yes**: publish or schedule a post.
- **Needs**: nothing required. Better with notes and CRM wins.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Write 2 draft posts for the channels listed in PROFILE.md, in VOICE.md style, avoiding every banned word there. Base each on something real from the last 2 weeks: a finished job, a question a customer asked, a lesson learned. No customer names or private details unless PROFILE.md allows it. Add an image idea for each. Save both as a note named post-drafts-<date> and tell the owner. Never publish.
```

## 9. Bills and renewals watch
- **Runs**: Mondays at 8:00 and the 1st of each month.
- **Reads**: calendar, inbox, accounting tool if connected.
- **Makes**: a list of what is due in the next 30 days.
- **Never without a yes**: pay, cancel, or reply to a vendor.
- **Needs**: email or calendar. Optional: accounting.

Prompt:
```
Read PROFILE.md and TOOLS.md. Search the calendar and inbox for invoices, bills, renewals, subscriptions, licenses, and contract end dates due in the next 30 days. List each with: what, who, amount if shown, due date, and source. Sort by date. Flag anything due within 7 days and anything that auto-renews. Owner only. Do not pay, cancel, or reply. If no accounting tool is connected, say the list comes from mail and calendar only.
```

## 10. Birthday and anniversary notes
- **Runs**: Mondays at 8:15, looking 7 days ahead.
- **Reads**: CRM (dates), calendar, notes.
- **Makes**: a list plus a short draft message per client.
- **Never without a yes**: send. These stay drafts.
- **Needs**: CRM or notes that hold dates.

Prompt:
```
Read PROFILE.md, TOOLS.md and VOICE.md. Find clients whose birthday, anniversary, or customer-since date falls in the next 7 days. Use only dates recorded in the CRM, calendar, or notes. For each, write a warm 2 sentence draft in VOICE.md style. Save the drafts. Send the owner the list with dates and sources. Never send to clients. If no dates are on file, say so.
```

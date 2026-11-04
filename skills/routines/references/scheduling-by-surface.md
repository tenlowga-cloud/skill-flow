# Scheduling by surface

Pick where the routine will run, then follow that section.

## Decision table

| Needs local files? | Machine can be off? | Needs connectors (email, calendar, CRM)? | Use |
|---|---|---|---|
| No | Yes | Yes | Claude Code cloud scheduled task |
| Yes | No (machine is on) | Yes or no | Claude Code Desktop scheduled task |
| Yes | Yes | No | Not possible. Move the files to a connected tool, or keep the machine on |
| No | Yes | No | Cloud scheduled task, or ChatGPT Tasks / Gemini Scheduled actions |
| Polling for a few hours | No | Any | `/loop` inside a session |
| No scheduler on the surface | Any | Any | Calendar reminder that opens the prompt, or OS scheduler running the CLI |

Default for a non-technical owner on claude.ai or Cowork: the "claude.ai chat" section below, Road A (desktop app) or Road B (the cloud web form). Neither needs a terminal. Default for a Claude Code owner: the cloud scheduled task through `/schedule`.

## The send rule (applies to every surface)

A routine that sends to anyone other than the owner stops at a draft unless the gates in PROFILE.md allow it. It never sends outside the send window in PROFILE.md. Scheduled runs act as the owner: messages and commits appear as them. So draft first.

## Claude Code cloud scheduled tasks (formerly routines)

- Create at https://claude.ai/code/routines, or type `/schedule` in any Claude Code session.
- Examples: `/schedule daily PR review at 9am`. One-off: `/schedule tomorrow at 9am, summarize yesterday's merged PRs`.
- Runs in the cloud. The owner's machine can be off.
- Minimum interval is one hour. For the 60-minutes-before-meeting routine, schedule hourly.
- All connected connectors are included by default. Remove the ones the task does not need: Advanced settings, Connectors tab. Fewer connectors means less risk.
- Available on Pro, Max, Team, and Enterprise plans.
- Runs as the owner. Messages and commits appear as them.
- The cloud session has no access to the owner's files. Keep PROFILE.md, TOOLS.md and VOICE.md somewhere the task can read (a repo or a connected drive), or paste the key facts into the prompt.
- Check the first run by hand with "Run now" (verify the button name) and read the output before trusting it.

## Desktop app scheduled tasks (the same feature Road A below walks for chat owners)

- In the Desktop app: click the **Code** tab first, then Scheduled in that sidebar, then New task. The label may read Schedule or Routines in newer versions (verify). Choose a local task.
- Runs on the owner's machine. It can read local files, such as the profile files.
- The app must be open and the computer awake. A missed run does not happen while the machine sleeps.
- Use this when the routine needs local files and the owner keeps the machine on during work hours.

## Claude Code /loop

- `/loop 20m check the deploy` repeats a prompt inside the open session.
- Session-scoped. Stops when the session closes. Expires after 7 days.
- Good for polling ("check the inbox every 20 minutes today"). Not for daily routines.

## claude.ai chat: there is no scheduler inside a chat

A web or mobile chat cannot run a prompt on a timer. A chat-only owner has two real roads, both without a terminal. Pick with them, teaching mode, one step per message:

**Who does the clicking.** Road B is a web page. With Claude in Chrome proven (`skills/setup/references/teaching-mode.md`, Do mode), Claude fills the form in the owner's browser: opens claude.ai/code/routines, New task, enters the name and the filled prompt, sets the schedule, unticks the connectors the routine does not need, and saves. The owner reads the prompt block first, handles any sign-in, and says "yes, save it" (the one save this guide names). Road A is a desktop app, not a web page, so it stays a Talk mode walk, one step per message.

**Road A, the desktop app's scheduled tasks. Recommended when they have a Mac or Windows computer.**

1. "Install the Claude desktop app from https://claude.ai/download and sign in with the same account. You should see your chats."
2. "At the top or side of the app, click the **Code** tab. The sidebar changes. Look there for Scheduled (it may read Schedule, Routines or Tasks depending on your version). Click it. You should see a New task button." If they cannot find it, ask them to read the sidebar labels aloud and match by meaning.
3. "Click New task. A form opens with a name, a prompt box, and a schedule."
4. Give them the routine's name and the filled prompt (section "Filling the prompt for a chat owner" below) to paste. Then the schedule: pick the preset (Daily, Weekdays, Hourly, Weekly) and the time in their time zone.
5. "Save. You should see the task in the list with its next run time. Read me that time."
6. Run it once now if the form offers it; otherwise wait for the first run. Open the result together.
   Runs on their computer, so the computer must be on and the app open at the time. Say that plainly.

**Road B, the cloud (claude.ai/code/routines). Recommended when the computer is often off.**

This page is a web form. No terminal, no code. The owner does not need a repository; if the form asks for one, pick none or skip (verify the exact control on their version).

1. "Open https://claude.ai/code/routines in your browser, signed in with the same account. You should see a page with a New task button."
2. "Click New task. A dialog opens with a name, a prompt box, a schedule, and Advanced settings."
3. Give them the name and the filled prompt to paste.
4. "Set the schedule: pick Daily or Weekly and the time. The clock is your local time."
5. "Open Advanced settings, then the Connectors tab. Every connector you have is ticked. Untick the ones this routine does not need." Name the ones to keep from the routine's Needs line.
6. "Save. You should see the task in the list. Read me its next run time."
7. The first run opens as a session in the task's History. Read it together.
   Runs in the cloud with the computer off. Pro, Max, Team and Enterprise plans. Minimum interval one hour.

**Filling the prompt for a chat owner.** A scheduled run cannot read a Project or a file on the owner's computer. So the prompt carries the facts inline. Take the library prompt and replace "Read PROFILE.md, TOOLS.md and VOICE.md" with a short block, written from those files, no secrets, no client names:

```
About the owner: [name], [role], runs [business]. Address them as [address]. Time zone [zone]. Work hours [hours]. Client messages may send [window], otherwise never.
Tools you may use: [calendar name], [email], [CRM and sub-account]. Not connected: [list].
Gates (never do these without the owner's yes): spend money, sign anything, delete live data, send to anyone but the owner, change a client record, go live.
Voice for anything written: [three rules from VOICE.md]. Never use: [banned words].
Top priority this week: [one line].
```

Show the owner the filled block before they paste it. It is theirs to read and correct.

A scheduled run also cannot write `STACK.md`. Any routine that keeps state between runs (the GoHighLevel assistant's last sweep time and open questions) keeps it inside the tool it works in (a GoHighLevel task), never in a profile file. The live session updates `STACK.md` the next time the owner talks to Claude.

**What the owner will see.** The result lands in the app (desktop task history or the cloud task's History) and, where the app sends notifications for finished tasks, as a notification on the phone. Whether a phone notification arrives on completion is not confirmed for every version (verify); the phone step tests it once and records the answer.

## Other surfaces

- **ChatGPT**: Tasks (scheduled prompts). Ask in a chat, for example "every weekday at 7:30am, do X". ChatGPT shows a confirmation, then lists it under Tasks in the profile menu on the web. Paid plans only, about 10 active tasks at once (verify current limits). Runs without your files. Connectors may be limited (verify).
- **Gemini**: Scheduled actions. Say the schedule inside the prompt ("every Monday at 8am"). Manage under Settings and help, then Scheduled actions. Needs Keep Activity on, a paid Google AI plan or qualifying Workspace edition, and up to 10 active at once (verify).
- **Cursor**: no built-in scheduler for chats (verify). Use the fallback below.
- **Grok**: scheduled tasks exist in some plans (verify). If not found, use the fallback.

## Fallbacks when there is no scheduler

1. **Calendar reminder**: make a recurring calendar event at the routine time. Put the prompt (or a link to it) in the event notes. The owner taps it and pastes it into the assistant. Honest and simple.
2. **OS scheduler**: cron on Mac or Linux, Task Scheduler on Windows, running the CLI with `-p`:
   `claude -p "$(cat /path/to/morning-brief.txt)"`
   Needs the machine on, and the command line installed. Do this only for owners who are comfortable with it, or set it up for them and test once.

## After scheduling

1. Tell the owner the name, time, and what it can and cannot do alone.
2. Run it once now and show the result.
3. Write the routine name, time, and surface into PROFILE.md routines list if the owner agrees.
4. To stop one: open the same page it was created on and pause or delete it.

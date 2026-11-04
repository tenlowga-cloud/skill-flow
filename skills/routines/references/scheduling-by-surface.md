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

Default for a non-technical owner: cloud scheduled task. It needs no setup on their machine.

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

## Claude Code Desktop scheduled tasks

- In the Desktop app: Code tab, then Scheduled in the sidebar, then New task. The label may read Schedule or Routines in newer versions (verify). Choose a local task.
- Runs on the owner's machine. It can read local files, such as the profile files.
- The app must be open and the computer awake. A missed run does not happen while the machine sleeps.
- Use this when the routine needs local files and the owner keeps the machine on during work hours.

## Claude Code /loop

- `/loop 20m check the deploy` repeats a prompt inside the open session.
- Session-scoped. Stops when the session closes. Expires after 7 days.
- Good for polling ("check the inbox every 20 minutes today"). Not for daily routines.

## claude.ai scheduled tasks

- If the plan has it, find it in claude.ai settings. Look for Scheduled tasks or Tasks. The label may differ (verify).
- Same rules as cloud: runs only with the connectors enabled for it.
- If the owner cannot find it, use the cloud scheduled task above.

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

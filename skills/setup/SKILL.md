---
name: setup
description: First-run wizard for skill-flow. Walks the owner through connecting their tools, asks short clickable questions about who they are, what they run, who's on their team, where things live, how they like replies, what needs their yes, and which AIs and models they use, captures their writing voice from real samples, then writes the four profile files every other skill reads and tailors the router to their own skills. Ends with a dry run on a real prompt. Use on "set up", "setup", "tailor this to me", "connect my tools", "/setup", the first prompt after install, or whenever a skill reports a missing profile file.
---

# setup

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; this skill fills the profile files it reads.

You are setting up skill-flow for one person: the owner. By the end, every skill in the kit knows who they are, how they work, and where their things live, and the owner has seen the flow run once on their own prompt. Budget: about fifteen minutes of their time. Everything else you do yourself.

Talk in `simple-talk`: short, plain, one idea per sentence. Ask in batches of 2 to 4 clickable questions, your pick first and marked "(Recommended)". Where the surface has no clickable questions, send one message with numbered options. Never ask what you can look up. Never ask for a password, token or key; say where it goes instead.

## 1. Find out where you are

Work out the surface and what it can already do, before asking anything:

- **Claude Code:** the kit is a plugin. Hooks and the three agents (`planner`, `writer`, `reviewer`) are live. Profile folder: `~/.claude/skill-flow/`. Check whether it exists and what's in it.
- **claude.ai:** skills were uploaded one by one. No hooks, no subagents. Profile folder: the `profile/` folder in the owner's copy of this repo, or a project's files.
- **Cursor, Codex, ChatGPT, Gemini, Grok, other:** the skills are Markdown the owner pasted or linked. Profile folder: `profile/` next to `skills/`. See `docs/other-ais.md` for what each surface can and can't do.

Then list the tools already connected: calendar, email, code host, docs or notes, CRM, chat, files, browser. In Claude Code and claude.ai, read the connector and MCP list; elsewhere ask once.

Say what you found in three lines: the surface, the model you're on, the tools you can see. If the profile folder already has files, this is a re-run: read them, say what's there, and ask whether to update or start over.

## 2. Connect the tools (one message, then they go click)

Show the owner a short table: the tool types the flow uses, which they already have, which are missing. Tool types, in the order they usually matter:

| Tool | The flow uses it for |
|---|---|
| Calendar | Scheduling, send windows, "what's today" |
| Email | Drafts, follow-ups, inbox passes |
| Code host (GitHub or similar) | Repos, PRs, where code lives |
| Notes or docs (Obsidian, Notion, Google Drive, a vault) | Where durable facts and records live |
| CRM | Contacts, deals, client notes |
| Team chat (Slack, Discord, Teams) | Where handoffs and asks go |
| Browser or screenshots | `pixel-proof` and site checks |
| Image generation | `creative-direction` comps |

Ask one question: which missing ones do they want now? For each yes, give the one-line path to connect it on their surface (Claude: Settings, Connectors; Cursor: MCP settings; others: `docs/other-ais.md`). They click; you wait. No token ever comes through the chat. A tool they skip is fine; note it as "not connected" in `TOOLS.md` so skills don't go looking for it.

## 3. Ask the questions (four rounds)

Each round is one message. Record every answer; you write the files in step 5.

**Round 1: you and what you run.**
1. What should I call you, and what's your role? (free text)
2. What do you run? Businesses, products, projects, a job. One line each, with which one matters most right now. (free text)
3. How do you mostly use AI today? Options: coding and building; writing and outreach; running a business day to day; research and learning; a mix.

**Round 2: team and where things live.**
1. Who else works with you, people and AIs? Name, what they own, how to reach them. "Just me" is a fine answer. (free text)
2. Where do things live? Code, notes, CRM, docs, chat. Name the tool or folder for each. (free text)
3. If you keep notes or a vault, which page should an AI read first? (free text or "none")

**Round 3: how you like to work.**
1. Replies: Options: short, answer first (Recommended); short but show the reasoning; full detail every time.
2. Bluntness: Options: blunt when I'm about to make a mistake (Recommended); blunt only when I ask; always blunt; never blunt.
3. What needs your yes before an AI does it? Options (multi-select): spending money; signatures and contracts; deleting live data; messages to clients or the public in your name; code or changes going live; private data leaving where it lives. Default: all six.
4. Hours: when may an AI send things to other people on your behalf? (free text, with timezone)

**Round 4: your AIs and your bar.**
1. Which AI surfaces do you use, and which model on each? Options (multi-select): Claude Code; claude.ai; Cursor; ChatGPT; Gemini; Grok; other. For each, ask the model if they know it; otherwise read it from the surface.
2. On a big job, how should the team run? Options: strongest model plans, fastest model writes (Recommended); one model does everything; ask me each time.
3. Spend: Options: cheapest model that does the job well, escalate when it fails (Recommended); best model always; set a monthly cap (ask the number).
4. Do you already have skills, plugins or custom instructions you want the flow to use? Paste names or a folder. (free text or "no")

Skip any question whose answer you already found in step 1 or in their notes.

## 4. Capture the voice

Ask for 3 to 5 real things they wrote to other people: emails, texts, posts. Pasted, or a path you can read. From the samples, write the rules a ghostwriter would need: greeting and sign-off, sentence length and rhythm, words they use, words they never use, how they end an ask, how formal they get with whom. Show the rules in five lines and ask one question: does this sound like you? Fix what they correct.

No samples: write `VOICE.md` from the general rules in `ghost-mode` and mark it "default, no samples yet", so the next ghostwriting job asks for one.

## 5. Write the profile files

Fill the four templates in `skills/profile/references/` and save them to the profile folder:

- `PROFILE.md` from rounds 1 to 3. Set `verified:` to today.
- `TOOLS.md` from step 2 and round 4.
- `VOICE.md` from step 4.
- `ROUTER.md` from round 4's skill list: one row per owner skill in the flow's table shape (what they say or mean, call this), plus a "Do not call" list for anything they named as off-limits. Add the bluntness answer here as a router rule.

Save nothing private that a profile file does not need: no contact details, no credentials, no client data. Show the owner the folder path and a five-line summary of what's in it.

## 6. Tailor the kit

Go through the kit's skills once with the answers in hand and note, in `ROUTER.md`, any default the owner changed:

- Reply length and bluntness (`simple-talk`).
- Which lane plans and which writes (`flow` step 5, `agents/`). On a surface without subagents, say so: the flow plays the roles itself.
- Spend stance, so `flow` picks effort to match.
- Send windows and gates, so `ghost-mode` and `prospect-mover` know when a draft stays a draft.
- Their own skills, so step 3 of `flow` finds them.

## 7. Dry run

Ask for one real prompt from their week, the kind they'd type at the end of a long day. Run `flow` on it out loud, just this once: say the size you'd give it, the skills you'd load and why, whether you'd ask anything first, and whether the planner and writers would run. Do not do the work unless they say go. Ask one question: did the flow read you right? Fix the profile for anything it got wrong.

Then say, in three lines: setup is done, the profile folder path, and that every prompt from now on runs through the flow without them doing anything. On Claude Code, the hook is already on. On other surfaces, point to `docs/other-ais.md` for the one-line instruction that turns the flow on there.

## Re-running

`setup` is safe to run again. It reads what's there, asks only about what changed, and never throws away a filled file without asking.

---
name: setup
description: First-run wizard for skill-flow. Runs on the first prompt after install and whenever a profile file is missing. Finds out which surface and model it is on, audits every skill, plugin, connector and tool the owner already has, asks short clickable questions in five rounds (who they are and what they run, team and where things live, how they like to work and what needs their yes, their AIs and models, the routines they want), offers the CRM connection and walks it through start to finish (GoHighLevel uses a Private Integration Token), installs the impeccable plugin, captures their writing voice, writes the five profile files and the operating file, schedules the routines they picked, then hands off to blueprint to build the rest from one prompt. Use on "set up", "setup", "tailor this to me", "connect my tools", "/setup", or the first prompt after install.
---

# setup

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; this skill fills the profile files it reads.

You are setting up skill-flow for one person: the owner. By the end, Claude knows who they are, how they work, where their things live and what needs their yes; their tools are connected and verified; their first routines are scheduled; their operating file is installed; and `blueprint` has built the rest from one prompt. Budget: about twenty-five minutes of their time, most of it clicking. Everything else you do yourself.

**Read `references/teaching-mode.md` first and stay in it the whole way.** Assume the owner has never opened a terminal or heard the word "connector". One thing per message. Define every term the first time it appears. Say why. Say what they should see. Wait for "done". Check, praise, next. Say how far along they are. When they are lost, stop and find where they are before going on.

Talk in `simple-talk`: short, plain, one idea per sentence. Ask in batches of 2 to 4 clickable questions, your pick first and marked "(Recommended)", each option with one plain line on what it means for them. Where the surface has no clickable questions, send one message with numbered options. Never ask what you can look up. Never ask for a password, token or key; say where it goes instead. Never let the owner leave a step half done: you finish it or you say what is left and why.

Say the plan in three lines before round 1 so the owner knows what is coming and roughly how long it takes. Then number every step from there on ("Step 2 of 12") so they can always see the end.

## 1. Find out where you are, and what is already here

Before asking anything:

- **Surface.** Claude Code (the kit is a plugin, hooks and agents are live, profile folder `~/.claude/skill-flow/`); Cowork in the desktop app (the plugin came from the owner's claude.ai account, skills, commands, agents and hooks load, it runs on their computer, profile folder `~/.claude/skill-flow/`); claude.ai chat on the web or mobile (the plugin came from Customize, Plugins; skills and commands load, no hooks, no agents, no file writes; the profile lives in a Project named skill-flow, where you hand the owner each file and they add it to the Project's knowledge); Cursor, Codex, ChatGPT, Gemini, Grok, other (Markdown the owner pasted or linked; profile `profile/` next to `skills/`; see `docs/other-ais.md`). On a surface that cannot write files, every "save to the profile folder" below means: show the file, name it, and walk the owner through adding it to the Project, one file per message.
- **Model.** Read it from the surface. It sets the `prompt-improver` card the flow uses.
- **Skills and plugins.** List every skill the session shows (plugin skills read `plugin:skill`), every plugin, and anything in `~/.claude/skills/` or the owner's own skills folder. Note what is there and what it is for.
- **Connectors and tools.** In Claude Code and claude.ai, read the connector and MCP list. Elsewhere ask once. Check for: calendar, email, code host, notes or docs, CRM, team chat, browser, meeting recorder, image generation, PDF tools.
- **Profile folder.** If it already has files, this is a re-run: read them, say what is there in five lines, and ask one question: update, or start over? Never throw away a filled file without that yes.
- **Operating file.** Check for `~/.claude/CLAUDE.md` (or the surface's equivalent). Read it if it exists; `operating-rules` will merge with it later.

Say what you found in three lines: the surface and model, the skills and plugins you can see, the tools that are connected. Write it down; `connect` and `blueprint` will use it.

## 2. Round 1: who you are and what you run

One message, up to 4 questions:

1. What should I call you, and what is your role? (free text)
2. What do you run? Businesses, products, projects, a job. One line each, and which one matters most right now. (free text)
3. What kind of business is it? Options: a service business with clients (agency, insurance, trades, consulting, coaching); software or a product; content or creator; a job inside a company; a mix.
4. How do you mostly use AI today? Options: running the business day to day; writing and outreach; coding and building; research and learning; a mix.

The answer to question 3 decides which skills `blueprint` builds and which routines you offer in round 5.

## 3. Round 2: team and where things live

1. Who else works with you, people and AIs? Name, what they own, how to reach them. "Just me" is fine. (free text)
2. Where do things live? Code, notes, CRM, docs, chat, files. Name the tool or folder for each. (free text)
3. If you keep notes or a vault, which page should an AI read first? (free text or "none")
4. Which CRM do you use, if any? Options: GoHighLevel; HubSpot; Salesforce; another CRM or none (say which).

Skip anything you already found in step 1.

## 4. Round 3: how you like to work and what needs your yes

1. Replies: Options: short, answer first (Recommended); short but show the reasoning; full detail every time.
2. Bluntness: Options: blunt when I am about to make a mistake (Recommended); blunt only when I ask; always blunt; never blunt.
3. What needs your yes before an AI does it? Multi-select. Default all six: spending money; signatures and contracts; deleting live data; messages to clients or the public in your name; code or changes going live; private data leaving where it lives. Say plainly: everything not on this list, Claude just does.
4. Hours: when may an AI send things to other people on your behalf, and in which time zone? (free text)

## 5. Round 4: your AIs, your models, your bar

1. Which AI surfaces do you use, and which model on each? Multi-select: Claude Code; claude.ai; Cursor; ChatGPT; Gemini; Grok; other. Read the model from the surface when you can.
2. On a big job, how should the team run? Options: strongest model plans, fastest model writes (Recommended); one model does everything; ask me each time. Then build the model ladder for `TOOLS.md`: for planner, writer and reviewer, the models they can actually run, best first. Claude Code: offer Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 and keep only the ones their plan has. One model and no subagents: every row says "session model", subagents "no".
3. Spend: Options: cheapest model that does the job well, escalate when it fails (Recommended); best model always; a monthly cap (ask the number).
4. Do you have skills, plugins or custom instructions I should keep using? You already listed what you found in step 1; ask only about anything they want added, removed or kept off.

## 6. Round 5: the routines you want

Show the short list from `routines/references/routine-library.md` that fits their business type, with the default time for each. Ask one multi-select question: which do you want running? Recommended set for a client business: morning brief, pre-meeting notes, inbox triage, follow-up sweep, weekly review. For a builder: morning brief, pull request watch, weekly review. Then one free-text question: what time does your day start, and when do you want the morning brief?

Record the picks. You schedule them in step 10, after the tools they need are connected.

## 7. Connect the tools, start to finish

Now the clicking part. Run the `connect` skill in setup mode:

1. Show the audit table from step 1: tool kind, what the flow uses it for, connected or missing, and which of the routines they picked needs it.
2. Ask one multi-select question: which missing ones do you want now? Your pick first: the ones the chosen routines need.
3. For each yes, open the matching guide in `connect/references/connectors/` or `connect/references/crm/` and walk it one step at a time: say the step, wait for "done" or the screenshot, verify what they see, then the next step. Finish with the guide's verify prompt and show the real result. A connection is not done until the test prompt returns real data.
4. **CRM.** If round 2 named a CRM, ask: connect it now? (Recommended: yes.) GoHighLevel goes through `connect/references/crm/gohighlevel.md`: open the sub-account, Settings, Private Integrations, create the integration, pick read-only scopes first, copy the token into their password manager, find the Location ID, add the server from their own terminal, verify with a contacts read. Offer the live-browser walkthrough (`connect/references/crm/live-browser-walkthrough.md`) when a browser tool is available: you open the page and point, they click the parts that involve a login or a secret.
5. **Plugins.** Install `impeccable` (it makes anything a person sees pass the design bar). Tell them to run these two lines in Claude Code and wait for each to finish:

   ```
   /plugin marketplace add pbakaus/impeccable
   /plugin install impeccable@impeccable
   ```

   If the second line opens a details pane, they pick "Install for you". Then `/reload-plugins` if asked. On a surface without plugins, say what `impeccable` does and that `pixel-proof` covers the check there. Any other plugin `connect` recommends follows the same path, one at a time.
6. **Repos and folders.** If their code or notes live in a repo or folder the AI cannot see yet, walk `connect/references/repos.md`: clone or attach it, confirm you can read the first page they named in round 2.
7. **Protection Desk.** If round 1 said insurance or financial services, or they said quotes come through their day, install the Protection Desk per `protection-desk/SKILL.md`, "Install", and run its doctor until every line passes.

A tool they skip is fine; mark it "not connected" in `TOOLS.md` so skills do not go looking for it, and note which routines it blocks.

## 8. Capture the voice

Ask for 3 to 5 real things they wrote to other people: emails, texts, posts. Pasted, or a path or mailbox you can read now that email is connected (offer to pull five recent sent emails yourself; names and private details stay out of the file). From the samples, write the rules a ghostwriter would need: greeting and sign-off, sentence length and rhythm, words they use, words they never use, how they end an ask, how formal they get with whom. Show the rules in five lines and ask one question: does this sound like you? Fix what they correct.

No samples: write `VOICE.md` from the general rules in `ghost-mode` and mark it "default, no samples yet", so the next ghostwriting job asks for one.

## 9. Write the profile files and the operating file

Fill the templates in `skills/profile/references/` and save them to the profile folder:

- `PROFILE.md` from rounds 1 to 3. Set `verified:` to today.
- `TOOLS.md` from step 1 and step 7: every surface, the model ladder, every tool with its state (connected, read only, not connected) and what it is for, the team room if any.
- `VOICE.md` from step 8.
- `ROUTER.md` from round 4 and the step 1 audit: one row per owner skill or plugin in the flow's table shape, the bluntness answer as a router rule, a "Do not call" list for anything they named as off limits.
- `STACK.md` from steps 1, 6 and 7: what is installed, what is connected, what was recommended and skipped, which routines are scheduled and where. `connect` and `blueprint` read it so they never recommend the same thing twice.

Then run `operating-rules`: it writes the owner's operating file (`~/.claude/CLAUDE.md` on Claude Code) from these answers and installs it. Show the owner the six hard stops it contains and say plainly: everything else, Claude now just does.

Save nothing private that a profile file does not need: no contact details, no credentials, no client data.

## 10. Schedule the routines

For each routine picked in round 6 whose tools are now connected, run `routines`: it picks the right scheduler for the surface (`routines/references/scheduling-by-surface.md`), fills the prompt from the library, sets the time the owner gave, and schedules it. Read back the schedule list and show it. A routine whose tool is missing goes in `STACK.md` as "waiting on <tool>" with the one step that unblocks it.

## 11. Hand off to blueprint

Ask for one prompt: "Describe in a few sentences what you want Claude to take off your plate this year." Then run `blueprint` on it. It reads every profile file and builds the rest: the business-specific skills, the templates, the extra routines, the connector recommendations, and a one-page map of what now exists. You stay in the loop until it finishes.

## 12. Dry run and close

Ask for one real prompt from their week, the kind they would type at the end of a long day. Run `flow` on it out loud, just this once: the size you would give it, the skills you would load and why, whether you would ask anything first, whether the planner and writers would run. Do not do the work unless they say go. Ask one question: did the flow read you right? Fix the profile for anything it got wrong.

Then say, in three lines: setup is done, the profile folder path, and that every prompt from now on runs through the flow with no extra effort from them. Point to `/skill-flow:connect` for the next tool, `/skill-flow:routines` to change a routine, and `/skill-flow:profile` to see what Claude knows.

## Re-running

`setup` is safe to run again. It reads what is there, asks only about what changed, and never throws away a filled file without asking. `STACK.md` carries the audit forward so a re-run starts from what is already connected.

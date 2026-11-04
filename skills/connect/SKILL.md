---
name: connect
description: Audits every skill, plugin, connector, MCP server, repo and tool the owner has, matches them against what the owner runs and what the flow needs, recommends what is missing (a connector, a plugin, a skill, a repo), and walks the owner through the setup one step at a time from start to finish until a live test proves it works. Covers calendar, email, code hosts, notes and vaults, CRMs (GoHighLevel by signing in through HighLevel's official MCP, HubSpot, Salesforce and others), team chat, browsers, meeting recorders and the impeccable plugin. Can run the setup with the owner in a live browser. Use on "connect my tools", "connect my CRM", "what am I missing", "install this plugin", "add this repo", "set up GoHighLevel", "/connect", when a skill reports a tool is not connected, or when setup reaches its connect step.
---

# connect

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

A tool the owner has not connected is a job the AI cannot do. This skill finds those gaps and closes them, with the owner clicking and the AI driving. It never stops at "here is a link". It stays until the test prompt returns real data.

## 1. Audit what is here

Read `TOOLS.md` and `STACK.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If they are missing, build the audit from scratch and say once that `setup` will save it.

Then look at the live surface, not the files:

| Check | How |
|---|---|
| Skills | The skill list the session shows, plus `~/.claude/skills/` and the owner's own folder. Note each skill's purpose in five words. |
| Plugins | Claude Code: `claude plugin list` in the shell, or `/plugin`, Installed tab. claude.ai and Cowork: Customize, Plugins (the owner reads the list back). Cursor and others: none. |
| Connectors and MCP servers | Claude Code: `/mcp` and `claude mcp list`. claude.ai: Settings, Connectors. Cursor: `~/.cursor/mcp.json`. |
| Repos and folders | What the session can read: the working directory, attached repos, a vault path from `PROFILE.md`. |
| Browser | A browser tool (Claude in Chrome, browser-use, Playwright) the session can drive. |
| Scheduler | Can this surface schedule routines? (`routines/references/scheduling-by-surface.md`) |

Write the result as one table: kind, name, state (connected, read only, not connected, broken), what it is for. Fix anything broken you can fix yourself (a server that needs `/mcp` sign-in, a plugin that needs `/reload-plugins`) before moving on.

## 2. Work out what is missing

Hold the audit against three things:

1. **What the owner runs** (`PROFILE.md`, What you run, and the business type from `setup` round 1). A client business needs calendar, email, CRM and a meeting recorder. A builder needs a code host and a browser. A writer needs notes and image generation.
2. **What the routines need** (`STACK.md`, routines, each with its tool list).
3. **What the flow's skills need.** `pixel-proof` and `impeccable` need a browser or a renderer. `meeting-prep` needs calendar plus at least one of CRM, email or notes. `inbox` needs email. `protection-desk` needs its repo and a PDF renderer. `creative-direction` likes image generation.

The recommendation list is the gaps, ranked by how many jobs each one unblocks. Keep it short: the top 3 to 5, each with one line on what it unlocks for this owner. Never recommend something `STACK.md` says they skipped on purpose, unless a new job needs it; then say why it came back.

Plugins to recommend by default on Claude Code, claude.ai and Cowork:

- **impeccable** (`pbakaus/impeccable`): the design bar for anything a person sees. Always.
- Anything in Anthropic's official marketplace that matches a tool they use (run `/plugin` and read the Discover tab; do not guess names).

## 3. Ask once, then go

One message: the recommendation list as a multi-select question, your pick first. For each yes, the owner's part is clicking and typing into their own tools. Your part is driving: in Do mode you do the clicks and narrate them; in Talk mode one step at a time, verify, next step (`../setup/references/teaching-mode.md`, "Who does the clicking").

## 4. Walk it through, start to finish

Open the guide for the tool:

- Connectors (calendar, email, code host, notes, chat, browser, meetings, custom MCP): `references/connectors/<tool>.md`
- CRMs: `references/crm/<crm>.md`. GoHighLevel: `references/crm/gohighlevel.md`, sign-in through HighLevel's official MCP at the address for the owner's AI; the token path is the fallback in its Advanced section only.
- Plugins: `references/plugins.md`
- Repos and folders: `references/repos.md`
- Skills (someone else's, or one to build): `references/skills.md`

The walkthrough runs in teaching mode (`../setup/references/teaching-mode.md`): assume the owner has never done this, define every term once, say why, show what right looks like, and say how far along they are. Who does the clicking depends on whether the browser is proven. If Claude in Chrome is installed, signed in and proven, work in Do mode: you do the clicks in their browser and narrate one line each, and hand over at every sign-in, Allow screen, secret, payment and gate. If not, work in Talk mode: they click, one step per message. The rules that matter most here:

1. **Talk mode: one step per message.** Say what to click or type, and what they should see. Wait for "done", a screenshot, or a paste of what they see. Then verify it matches before the next step. Number the steps ("Step 3 of 7"). **Do mode:** narrate each move as you make it and number the steps the same way; at a hand-over, stop and wait for "done".
2. **Secrets never come through the chat.** A token, key or password is typed by the owner into their own terminal, password manager or the tool's secret field. If they paste one into the chat anyway, say so once, tell them to rotate it, and carry on with the rotated one. Never echo it back.
3. **Do, don't tell, when you can.** With the browser proven, run the guide in Do mode (`references/crm/live-browser-walkthrough.md`): you open the page and do the clicks, they handle every login, Allow screen, secret and payment, you verify each screen. Never type a password or token yourself. Never screenshot a page while a token is visible. Never click Allow, Authorize, Accept, Pay, Send, Delete, Publish or Submit for them, except one save per guide, named by the guide and announced out loud before the click.
4. **Verify with real data.** Every guide ends with a test prompt. Run it. A pass is real data back (tomorrow's real events, the three newest real contacts). A blank or an error is not done; go to the guide's "If it fails" and keep going.
5. **Least privilege first.** Read-only scopes before write scopes. Add write later when a job needs it, and say which job.
6. **Record it.** Update `TOOLS.md` (state, what it is for) and `STACK.md` (connected today, the verify prompt that passed). Say the true state in one line.

Two identical failures on a step: change the approach (a different surface, a different auth path, the live browser) or hand the owner the exact error and the vendor's support page. Never loop. If the owner is lost (a question instead of "done", a screenshot that does not match, "I don't see that"), stop, ask what is on their screen in their own words, and restart from where they actually are. If they say stop, record "paused at step N" in `STACK.md` with the exact next step.

## 5. Build what does not exist

Some gaps are not a connector. The CRM has no MCP server; the notes app has no connector; a job needs a skill nobody wrote. Then:

- **A bridge:** a small MCP server or a webhook relay the owner can run. Scope it with the owner in one question (read only or read and write), build it, test it with the verify prompt, record it in `TOOLS.md`.
- **A skill:** write it in the owner's skills folder, in this kit's shape (frontmatter `name` and `description`, a short SKILL.md, references as needed), add it to `ROUTER.md`, and run it once on a real prompt.
- **A repo:** create it where the owner's code host lives, with a README that says what it is for, and attach it.

`blueprint` does this at scale on first run. `connect` does it one gap at a time afterward.

## 6. Say it back

Three lines: what is connected now and proven, what was skipped or is waiting on the owner, and the one next thing. Update `STACK.md` before you say done.

## What the AI may do with a connected tool

Default, unless `PROFILE.md` says otherwise: read yes; search yes; draft yes; add a note or mark a task done when the record shows the work is done, yes, and say so. Send, delete, pay, sign, change a field on a client record, move a stage, or change an appointment only with the owner's yes to that exact item. A connection is never a licence to act in the owner's name.

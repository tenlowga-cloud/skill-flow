# Team onboarding: install skill-flow and let Claude set itself up

Send this page to anyone on the team. Twenty-five minutes, mostly clicking. On a Team or Enterprise plan, the Owner does Step 0 once for everyone first. Then each person picks the Step 1 that matches how they use Claude; Step 2 is the same for everyone.

## Step 0. Team or Enterprise plan: the Owner does this once

Skip this on a personal Pro or Max account. On a Team or Enterprise account only an Owner can let members add plugins, so the Owner does these three things first, about five minutes:

1. Open https://claude.ai/admin-settings/skills (Organization settings, Plugins & skills). Click the **Policy** tab. Turn on **User-created skills**. This is what lets members add a marketplace from Customize, Plugins. Make sure **Skills** is on too; with it off, no plugin loads for anyone.
2. Back on the **Inventory** tab, click **Add**, then **Add marketplace**, and enter `tenlowga-cloud/skill-flow`. Do it again with `pbakaus/impeccable`. Each plugin appears in the inventory. Open the row menu on each, click **Default access**, and pick **Installed by default** (everyone gets it, can turn it off) or **Available to install** (members add it themselves).
3. Open Organization settings, **Connectors**, and add the connectors the team will use: Google Workspace or Microsoft 365 for calendar and email, the CRM, Slack or Discord, Notion or Drive. Members connect each one with their own account afterward; the Owner only makes them available.

Then send the team this page. If memory is turned off for the organization, turn it on in Organization settings as well (the label is Capabilities or Memory depending on your version); the wizard needs it. On Enterprise, also open https://claude.ai/admin-settings/browser-extension (Organization settings, Claude in Chrome) and allow it, since it is off by default where HIPAA is on; on Team, make sure no policy blocks the Claude in Chrome extension. Everyone installs it from the Chrome Web Store on desktop Chrome or Edge.

**If you are a member and not the Owner:** check https://claude.ai/customize/plugins first. If skill-flow is not in Discover and there is no **Add** button, ask your Owner to do Step 0. The wizard will give you a ready-to-send message for them when it finds anything else it needs.

## Step 1a. claude.ai or Cowork (the website or the desktop app)

1. Open https://claude.ai/customize/plugins (in the desktop app: Customize, then Plugins).
2. Click **Add**, then **Add marketplace**. Paste `tenlowga-cloud/skill-flow`. Click through; the plugin appears in the list. Click **Add** on it.
3. Do the same once more with `pbakaus/impeccable` (the design plugin).
4. For the website only: open Projects, make a Project called **skill-flow**, and keep it open. The wizard will give you a few small files to add to its knowledge, one at a time; that is where your profile lives on the web. Cowork and the desktop app write them to your computer for you.
5. Start a new chat (or a new Cowork task) and go to Step 2.

What you get here: every skill, the commands, and in Cowork the agents and the first-run hook too. The website has no hooks, so the first message in Step 2 is what starts the wizard. The Protection Desk needs Python on a computer, so it runs in Cowork or Claude Code, not in a web chat.

## Step 1b. Claude Code (terminal, VS Code, or the desktop app's Code tab)

Type these two lines, one at a time, and wait for each to finish:

```
/plugin marketplace add tenlowga-cloud/skill-flow
```

```
/plugin install skill-flow@skill-flow
```

If a pane opens, pick **Install for you**. If it says to run `/reload-plugins`, do that. Then close the session and open a fresh one so the hooks load. Cloud sessions at claude.ai/code do not load plugins from a laptop; for those, use Step 1a, since a plugin added to your account syncs everywhere you are signed in.

## Step 2. Paste this as your first message

```
I just installed the skill-flow plugin. Set me up completely, start to finish, and do not stop until it is done.

Run the `setup` skill in teaching mode. Assume I have never opened a terminal and never heard the words connector, plugin, token or CRM. Define every term the first time you use it. Tell me why we are doing each step in one line. Number the steps so I can see how far along we are. Once Claude in Chrome is installed and you have proven it works, do the clicking yourself in my browser and tell me what you are doing in one line per move, so I learn by watching. Hand me the keyboard only for sign-ins, passwords and codes, Allow screens, anything that shows a secret, payments, the phone, and a yes on anything in my hard stops. Until the browser works, or if I am on a Free plan, a phone, or a browser that cannot run the extension, walk me through one step per message: tell me exactly what I should see, then wait for me to say "done". If I say "slow down", go back to one step at a time. If I get lost, stop and ask what is on my screen.

Before anything else, read my account with me: which plan I am on and whether I am an Owner or a member, then walk me through my Settings one switch at a time and turn on everything the kit needs. Memory must be on (both the switch that generates memory from my chats and the one that searches past chats). Artifacts, analysis, web search, extended thinking, the browser, skills and plugins, scheduled tasks: on. Then have me install the Claude in Chrome extension (desktop Chrome or Edge, Chrome Web Store, publisher Anthropic), pin it, sign in with the same account, and test it, so you can click through every setup with me live. Tell me which connectors already show Connected. If I am on a Team or Enterprise plan and something needs my Owner, write me the exact message to send them and keep going on everything that does not depend on it. Record all of it in STACK.md.

Here is what I want at the end:

1. A clean operating file written by the `operating-rules` skill from my answers, so you act, decide, prove and finish without asking me, inside the hard stops I choose. On a computer that is ~/.claude/CLAUDE.md. On the claude.ai website, give me the text and walk me through pasting it into my skill-flow Project's instructions. Show me the hard stops when it is written. If one already exists, read it, keep what is mine, and merge.

2. Every tool I use connected and proven with a live test: calendar, email, notes or docs, my code host if I have one, team chat, a browser, my meeting recorder, and my CRM. Ask me if I use GoHighLevel. If I do, add HighLevel's official MCP for the AI I am using (Claude: https://services.leadconnectorhq.com/mcp/anthropic/v2; ChatGPT or Codex: https://services.leadconnectorhq.com/mcp/openai/v2/; Cursor: https://services.leadconnectorhq.com/mcp/cursor/v2), have me sign in with my GoHighLevel login and pick my business, verify with a contacts read, then set yourself up as my executive assistant inside it: watch my tasks, unanswered messages, deals assigned to me and upcoming appointments every hour, do what you can (notes, drafts, task updates, meeting prep), ask me one clear question when you need a decision, never send or delete anything yourself. Offer the live browser walkthrough if you can drive a browser.

3. The impeccable plugin installed (pbakaus/impeccable) so anything you build that a person sees passes a design check.

4. My brand on file: ask me for my logo, brand guidelines or website, read my colors and fonts from them, tell me if my fonts look dated and show me a modern one side by side before you change anything, and lock the brand into every document, quote and post you ever make for me. Anything a client sees has to look like it came from my business and from the year 2090, no AI look, scored 9 of 10 or better before I see it. Then my profile written: PROFILE.md, TOOLS.md, VOICE.md, ROUTER.md, STACK.md, BRAND.md. On a computer, in ~/.claude/skill-flow/. On the claude.ai website, hand them to me as files and tell me exactly how to add them to my skill-flow Project, one at a time. Capture my voice from 3 to 5 real emails or texts I give you, or pull five from my sent mail once email is connected.

5. My routines scheduled on the right scheduler and read back to me: morning brief, pre-meeting notes an hour before every outside meeting, inbox triage with drafts ready in my voice, a follow-up sweep, the GoHighLevel assistant sweep if I use it, and a weekly review. Ask me what time my day starts. If I am in a web chat, tell me plainly that a chat cannot run a timer and walk me through the desktop app's scheduled tasks or the cloud form at claude.ai/code/routines, one click at a time, with the prompt filled in for me. Then get the app on my phone: walk me through installing it (App Store or Play Store, maker Anthropic), signing in with the same account, allowing notifications, and test it with a short one-off routine. Tell me honestly whether it buzzed or whether I open the app at the routine's time.

6. If I handle insurance quotes, the Protection Desk installed and its doctor passing, so a quote drop prints a client-ready PDF in my brand without me asking: problems and solutions first, the value we bring said plainly, the price once at the end. When a client brings a cheaper quote, build the two side by side and walk the price today against the cost later, honestly, and tell me if the cheaper one actually fits.

7. Then run `blueprint` on one sentence from me about what I want off my plate this year, build the skills, templates and routines for it, and write BLUEPRINT.md so I can see everything that now exists and how to trigger it.

8. Finish with a dry run on one real prompt from my week and a three-line summary: what is done, what is waiting on me, the first thing to try tomorrow morning.

Rules: never ask me for a password, token or key. Never send anything to anyone but me. Never skip a verify step; a connection is not done until the test prompt returns my real data. Record anything we skipped in STACK.md with the one step that finishes it. Start now with the three-line plan and Step 1.
```

## What you will have at the end

- Your account set up: memory on, every capability the kit uses on, connectors connected, and anything that needed your Owner sent to them in one message.
- `~/.claude/CLAUDE.md`: Claude acts, decides, proves and finishes inside your hard stops (money, signatures, deleting live data, messages in your name, going live, private data leaving its room). Take one off and Claude does that too.
- Your tools connected and tested. Your CRM too.
- A morning brief, a note before every outside meeting, inbox drafts in your voice, a follow-up sweep, a weekly review, and if you use GoHighLevel an assistant that works your tasks, messages and deals every hour and brings you only the decisions.
- The app on your phone with notifications on, tested once, so every routine lands with three lines and the questions ready to tap. Web chat alone cannot run a timer; routines run from the desktop app or the cloud form, and the wizard sets that up with you.
- The skills and templates for whatever you asked to take off your plate, mapped in `~/.claude/skill-flow/BLUEPRINT.md`.
- From then on, every prompt runs through the flow. Drop a quote and a PDF comes back. Say "connect my X" and it walks you through it. Say "every Friday..." and it schedules it.

## If something goes wrong

- The wizard did not start: type `/skill-flow:setup` (Claude Code, Cowork) or "run the skill-flow setup" (website).
- A settings switch is greyed out: your Owner controls it. Send them the message the wizard wrote and carry on with the rest.
- skill-flow is not in Discover and there is no Add button: your Owner has not done Step 0 yet. Send them this page.
- On the website, Claude says it cannot save a file: that is expected. Ask for the file's text and add it to the skill-flow Project's knowledge yourself. Claude reads it from there next time.
- A step is confusing: say "I'm lost" and tell Claude what is on your screen. It restarts from there.
- You have to stop: say "stop". Claude records where you got to and picks up there next session.
- A connection will not verify: say "connect <tool>" in a fresh session and it tries another road.

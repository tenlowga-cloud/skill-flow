# Team onboarding: install skill-flow and let Claude set itself up

Send this page to anyone on the team. Twenty-five minutes, mostly clicking. Pick the Step 1 that matches how they use Claude; Step 2 is the same for everyone.

## Step 1a. claude.ai or Cowork (the website or the desktop app)

1. Open https://claude.ai/customize/plugins (in the desktop app: Customize, then Plugins).
2. Click **Add**, then **Add marketplace**. Paste `tenlowga-cloud/skill-flow`. Click through; the plugin appears in the list. Click **Add** on it.
3. Do the same once more with `pbakaus/impeccable` (the design plugin).
4. For the website only: open Projects, make a Project called **skill-flow**, and keep it open. The wizard will give you five small files to add to its knowledge; that is where your profile lives on the web. Cowork and the desktop app write them to your computer for you.
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

Run the `setup` skill in teaching mode. Assume I have never opened a terminal and never heard the words connector, plugin, token or CRM. One step per message. Define every term the first time you use it. Tell me why we are doing each step in one line. After every step tell me exactly what I should see, then wait for me to say "done" before the next one. Number the steps so I can see how far along we are. If I get lost, stop and ask what is on my screen.

Here is what I want at the end:

1. A clean operating file written by the `operating-rules` skill from my answers, so you act, decide, prove and finish without asking me, inside the hard stops I choose. On a computer that is ~/.claude/CLAUDE.md. On the claude.ai website, give me the text and walk me through pasting it into my skill-flow Project's instructions. Show me the hard stops when it is written. If one already exists, read it, keep what is mine, and merge.

2. Every tool I use connected and proven with a live test: calendar, email, notes or docs, my code host if I have one, team chat, a browser, my meeting recorder, and my CRM. If my CRM is GoHighLevel, walk me through making a Private Integration Token one click at a time, read-only scopes first, token straight into my password manager, never into this chat. Offer the live browser walkthrough if you can drive a browser.

3. The impeccable plugin installed (pbakaus/impeccable) so anything you build that a person sees passes a design check.

4. My profile written: PROFILE.md, TOOLS.md, VOICE.md, ROUTER.md, STACK.md. On a computer, in ~/.claude/skill-flow/. On the claude.ai website, hand them to me as files and tell me exactly how to add them to my skill-flow Project, one at a time. Capture my voice from 3 to 5 real emails or texts I give you, or pull five from my sent mail once email is connected.

5. My routines scheduled on the right scheduler and read back to me: morning brief, pre-meeting notes an hour before every outside meeting, inbox triage with drafts ready in my voice, a follow-up sweep, and a weekly review. Ask me what time my day starts.

6. If I handle insurance quotes, the Protection Desk installed and its doctor passing, so a quote drop prints a client-ready PDF without me asking.

7. Then run `blueprint` on one sentence from me about what I want off my plate this year, build the skills, templates and routines for it, and write BLUEPRINT.md so I can see everything that now exists and how to trigger it.

8. Finish with a dry run on one real prompt from my week and a three-line summary: what is done, what is waiting on me, the first thing to try tomorrow morning.

Rules: never ask me for a password, token or key. Never send anything to anyone but me. Never skip a verify step; a connection is not done until the test prompt returns my real data. Record anything we skipped in STACK.md with the one step that finishes it. Start now with the three-line plan and Step 1.
```

## What you will have at the end

- `~/.claude/CLAUDE.md`: Claude acts, decides, proves and finishes inside your hard stops (money, signatures, deleting live data, messages in your name, going live, private data leaving its room). Take one off and Claude does that too.
- Your tools connected and tested. Your CRM too.
- A morning brief, a note before every outside meeting, inbox drafts in your voice, a follow-up sweep, a weekly review.
- The skills and templates for whatever you asked to take off your plate, mapped in `~/.claude/skill-flow/BLUEPRINT.md`.
- From then on, every prompt runs through the flow. Drop a quote and a PDF comes back. Say "connect my X" and it walks you through it. Say "every Friday..." and it schedules it.

## If something goes wrong

- The wizard did not start: type `/skill-flow:setup` (Claude Code, Cowork) or "run the skill-flow setup" (website).
- On the website, Claude says it cannot save a file: that is expected. Ask for the file's text and add it to the skill-flow Project's knowledge yourself. Claude reads it from there next time.
- A step is confusing: say "I'm lost" and tell Claude what is on your screen. It restarts from there.
- You have to stop: say "stop". Claude records where you got to and picks up there next session.
- A connection will not verify: say "connect <tool>" in a fresh session and it tries another road.

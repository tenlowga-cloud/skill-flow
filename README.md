# skill-flow

Claude with the handcuffs off, inside hard stops you choose.

Install it, type one prompt, and a wizard learns who you are, audits every tool and skill you have, connects the missing ones with you step by step (your CRM included), installs the design plugin, writes your operating file so Claude acts instead of asking, schedules your morning brief and meeting prep, and builds the rest of what you need from one sentence. From then on every prompt runs through a flow: it works out what you meant, loads the right skills, has your strongest model plan and your fastest model write, proves the result, and hands it back short. Drop a quote on it and a client-ready PDF comes back without being asked.

It is a set of Markdown skills, two small hooks and three agents. No server, no account, no telemetry.

## What you get

| Piece | What it does |
|---|---|
| **setup** | The first-run wizard. Finds what you have, reads your account with you (plan, memory on, every switch), asks five short rounds, asks whether you use GoHighLevel and signs you in if so, connects your other tools, installs `impeccable`, captures your voice, writes your profile and operating file, schedules routines, puts the app on your phone with notifications on, hands to `blueprint`. About twenty-five minutes, mostly clicking. Runs in teaching mode: one step per message, every term defined once, "you should see ...", wait for done, numbered steps, no blame. Built for someone who has never opened a terminal. |
| **operating-rules** | Writes your `CLAUDE.md`: act, decide, prove, finish. Names the only things that still need you (money, signatures, deleting live data, messages in your name, going live, private data leaving its room). |
| **connect** | Audits skills, plugins, connectors and repos, recommends what is missing, and walks each setup through to a verified live test. Calendar, email, GitHub, notes, Slack, Discord, browser, meeting recorders, and CRMs: GoHighLevel (sign in through HighLevel's official MCP, per-AI address for Claude, OpenAI clients and Cursor), HubSpot, Salesforce, Pipedrive, Zoho, Close, Follow Up Boss. Can run the setup with you in a live browser. |
| **ghl-assistant** | Your executive assistant inside GoHighLevel. Every hour it reads the tasks assigned to you, unanswered messages, deals that moved or stalled, tomorrow's appointments and new leads; does what it can (notes, drafts, task updates, meeting prep); asks you one clear question when it needs a decision; never sends or deletes on its own. |
| **blueprint** | The master skill. One prompt about what you want off your plate; it builds the skills, templates, routines and connections for it and writes a one-page map. |
| **routines** | Schedules the recurring work: morning brief, pre-meeting notes, inbox triage, follow-up sweep, end-of-day wrap, weekly review, pipeline check and more, on the right scheduler for your surface. |
| **meeting-prep** | A one-page note before every outside meeting, every fact sourced. |
| **inbox** | Triage with a draft ready for everything that needs you, in your voice. Follow-up sweep. Drafts only; you tap send. |
| **protection-desk** | Fires on any quote, illustration or declaration page drop and prints the client-ready PDF through the Protection Desk, in your brand, scored by `impeccable` against a design bar that fails anything that looks like AI made it. Problems and solutions first, value plain, price once. A cheaper competing quote gets the side-by-side: the price today against the cost later, honestly. Installs the desk if it is missing. |
| **flow** | The gate on every prompt. Sizes it, rewrites it one-shot, reviews every active skill and loads the right ones, asks only when an answer changes the result, builds the team on a big job, verifies, delivers. |
| **profile** | "Who owns this", "where does X live", "what is connected". Answers from your profile files, never from memory. |
| **prompt-improver** | Rewrites a rough prompt the way the target model's maker says to prompt it. Cards for Claude, OpenAI, Gemini, Grok, image and video models. |
| **simple-talk** | Short, plain replies to you. Has a blunt setting for when you are about to commit to something with holes in it. |
| **ghost-mode** | Anything a person other than you will read, in your voice, no AI tells. |
| **prospect-mover** | Anything a prospect will see, built to win the next step toward the close. |
| **creative-direction** | A concept, brand, name or page that must not look generic or AI-made. |
| **pixel-proof** | No UI change is done until it is rendered and seen at phone and desktop widths. |
| **planning-mode** | A written plan with owners, steps, risks and proof, for a big unclear build. |
| **project-cleanup** | A phased cleanup pass that keeps behavior and removes clutter. |
| **planner, writer, reviewer** | Three agents. The planner (strongest model) turns the rewrite into slices and briefs. Writers (fastest model) build them. The reviewer (strongest model, never the builder) gives the verdict. |

Your own skills plug in too. `setup` writes them into a router so the flow finds them.

## Install

### Claude Code (full kit: hooks, agents, commands)

```bash
claude plugin marketplace add tenlowga-cloud/skill-flow
```

```bash
claude plugin install skill-flow@skill-flow
```

Then start a session and type anything. The session-start hook sees there is no profile yet and runs the wizard:

```
/skill-flow:setup
```

The wizard installs the design plugin for you. If you want it first:

```
/plugin marketplace add pbakaus/impeccable
/plugin install impeccable@impeccable
```

Sending this to a team? Give them [docs/TEAM-ONBOARDING.md](docs/TEAM-ONBOARDING.md): the Owner's one-time step on a Team plan, the install lines for each surface, and one paste-ready prompt that runs the whole setup in teaching mode, starting with the account pass (plan, memory on, every switch the kit needs, connectors, Owner items).

### claude.ai and Cowork (web, desktop app, mobile)

1. Open https://claude.ai/customize/plugins. Click **Add**, then **Add marketplace**, paste `tenlowga-cloud/skill-flow`, then **Add** the plugin. Do the same with `pbakaus/impeccable`.
2. Start a chat or a Cowork task and type `run the skill-flow setup`.

A plugin on your account also reaches Claude Code as a synced plugin. What loads where: skills and commands everywhere; agents and hooks in Cowork and Claude Code, not in chat. In chat there is no file system, so your profile lives in a Project named skill-flow and the wizard hands you each file to add to it. The Protection Desk needs Python on a computer, so it runs in Cowork or Claude Code.

### Cursor, Codex, ChatGPT, Gemini, Grok, anything else

The skills are plain Markdown. See [docs/other-ais.md](docs/other-ais.md) for where each surface reads them from and the one-line instruction that turns the flow on there.

## The first run

```
install
  │
  ├─ session start ───── no profile: setup runs on your first prompt
  │
  ├─ setup
  │    ├─ finds the surface, model, skills, plugins, connectors you already have
  │    ├─ five rounds of short clickable questions
  │    │    1 who you are, what you run, what kind of business
  │    │    2 team, where things live, which CRM
  │    │    3 reply style, bluntness, what needs your yes, send hours
  │    │    4 your AIs and models, how the team should run, spend
  │    │    5 the routines you want and when your day starts
  │    ├─ connect: walks each tool through to a live test
  │    │    calendar, email, notes, code host, chat, browser, recorder
  │    │    CRM: GoHighLevel (sign in), HubSpot, Salesforce, others
  │    │    impeccable plugin, repos, the Protection Desk if you quote
  │    ├─ captures your voice from real samples
  │    ├─ writes PROFILE, TOOLS, VOICE, ROUTER, STACK
  │    ├─ operating-rules: writes your CLAUDE.md, shows the hard stops
  │    ├─ routines: schedules what you picked
  │    ├─ phone: the app installed, notifications on, tested once
  │    ├─ brand: logo, colors, fonts on file; dated fonts upgraded with a yes
  │    └─ blueprint: one prompt, builds the rest, writes the map
  │
  └─ dry run on one real prompt from your week
```

## Every prompt after that

```
prompt
  │
  ├─ standing triggers ── quote drop: protection-desk, PDF printed
  │                       a screen a person sees: impeccable, pixel-proof
  │                       missing tool: connect
  │                       meeting coming: meeting-prep
  │
  ├─ size it ─────────── quick: one skill, do it
  │                      standard: rewrite, pick skills, do it
  │                      big: everything below
  │
  ├─ rewrite one-shot    finished result, where things live, what you didn't say,
  │                      done-means, proof, gates, model controls
  │
  ├─ review every        the live skill list + your ROUTER.md, every line checked
  │  active skill        against the rewrite; load the set that serves it
  │
  ├─ ask up front        only if 1 to 4 answers would change the result; one message
  │
  ├─ planner ──────────► slices, order, sources, skills, done-means, proof, briefs
  │        │
  │        └─ writers ─► one per slice, launched together, each builds the real thing
  │
  ├─ integrate + prove   you own the result; reviewer on anything high-stakes
  │
  └─ deliver             answer first, the catch, the next step. In your voice
                         if someone else reads it.
```

Models are a setting, not a rule. `setup` writes a model ladder into `TOOLS.md`: for each role, the models you can run, best first, and the flow uses the first one that works. The default ladder in Claude Code is Fable 5.1 then Opus 5.5 for the planner and reviewer, Sonnet 5.5 then Haiku 5.5 for the writers, then whatever the session is on. No Fable on your plan? It steps down. One model and no subagents? The flow plays all three roles in sequence, and it still works.

## Your profile

`setup` writes these. They are the only place anything about you lives, and they are gitignored.

| File | Holds |
|---|---|
| `PROFILE.md` | You, what you run, your team (people and AIs), where things live, priorities, gates, hours, quality bar |
| `TOOLS.md` | Which AI surfaces and models you use, which tools are connected and for what, the model ladder |
| `VOICE.md` | How you write: samples, banned words, sign-off, length |
| `ROUTER.md` | Your own skills in the flow's table, plus a do-not-call list |
| `STACK.md` | What is installed, connected, scheduled and built; what was skipped; what waits on you |
| `BRAND.md` | Your logo, colors, fonts and brand rules; every client-facing document, quote and post locks onto it |
| `BLUEPRINT.md` | The one-page map of what `blueprint` built and how to trigger it |

Your operating file (`~/.claude/CLAUDE.md` on Claude Code) is written from them by `operating-rules`.

Claude Code: `~/.claude/skill-flow/`. Elsewhere: `profile/` in your copy of this repo. Blank templates in `skills/profile/references/`.

## The hard stops

Everything is standing authority except what you put on this list. The default six:

1. Spending money
2. Signatures and contracts
3. Deleting live data
4. Messages to clients or the public in your name (ready to send; you tap send)
5. Code or changes going live
6. Private data leaving where it lives

Take one off and Claude does that too. Add one and Claude stops there.

## Make it yours

- Connect another tool any time: `/skill-flow:connect <tool>`.
- Add or change a routine: `/skill-flow:routines`.
- Build out a new area of your work: `/skill-flow:blueprint <what you want off your plate>`.
- Change your rules: `/skill-flow:rules`.
- Add a skill of your own: put it in `ROUTER.md` with one line on when it runs.
- Port a private skill in: read [docs/CONTRIBUTING-SCRUB-BRIEF.md](docs/CONTRIBUTING-SCRUB-BRIEF.md). It keeps this kit free of anyone's private details.

## Principles

- Act, don't ask. Look it up. Ask only at a real fork, and ask once.
- One owner per result. Delegating never moves it off your desk.
- Right the first time, proven, no homework left for the owner.
- Gates stay with the owner: money, signatures, deleting live data, messages in their name, anything going live, private data leaving its room.
- Secrets never pass through the chat. The owner types them into their own tools.
- Plain words. No jargon, no em dashes, short by default.

## License

MIT. See [LICENSE](LICENSE). The Protection Desk is a separate tool with its own license; this kit only triggers and installs it.

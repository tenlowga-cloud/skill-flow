# skill-flow

Every prompt you type runs through a flow. The flow works out what you actually meant, picks the skills that make it come out right, has your strongest model plan the job and your fastest model write it, proves the result, and hands it back short. A setup wizard tailors all of it to you, your team and your tools, on whichever AI you use.

It is a set of Markdown skills. No server, no account, no telemetry.

## What you get

| Piece | What it does |
|---|---|
| **flow** | The gate. Runs on every prompt that asks for work. Sizes it, rewrites it one-shot, reviews every active skill and loads the right ones, asks only when an answer changes the result, builds the team on a big job, verifies, delivers. |
| **setup** | The wizard. Connects your tools, asks four short rounds of questions, captures your writing voice, writes your profile, tailors the router, dry-runs the flow on a real prompt. About fifteen minutes. |
| **profile** | "Who owns this", "where does X live", "what matters this week". Answers from your profile files, never from memory. |
| **prompt-improver** | Rewrites a rough prompt the way the target model's maker says to prompt it. Ships prompting cards for Claude, OpenAI, Gemini, Grok, image and video models. |
| **simple-talk** | Short, plain replies to you. Has a blunt setting for when you're about to commit to something with holes in it. |
| **ghost-mode** | Anything a person other than you will read, in your voice, with no AI tells. |
| **prospect-mover** | Anything a prospect will see: site, quote, proposal, sequence, ad. Built to win the next step toward the close, scored, with two test variants. |
| **creative-direction** | A concept, brand, name or page that must not look generic or AI-made. |
| **pixel-proof** | No UI change is done until it is rendered and seen at phone and desktop widths. |
| **planning-mode** | A written plan with owners, steps, risks and proof, for a big unclear build. |
| **project-cleanup** | A phased cleanup pass that keeps behavior and removes clutter. |
| **planner, writer, reviewer** | Three agents. The planner (strongest reasoning model) turns the rewrite into slices and briefs. Writers (fastest model) build them. The reviewer (strongest model, never the builder) gives the verdict. |

Your own skills plug in too. `setup` writes them into a router so the flow finds them.

## Install

### Claude Code (full kit: hook, agents, commands)

```bash
claude plugin marketplace add tenlowga-cloud/skill-flow
```

```bash
claude plugin install skill-flow@skill-flow
```

Then, in any session:

```
/skill-flow:setup
```

The hook turns on with the plugin. From then on every prompt runs through the flow.

### claude.ai

1. Download this repo as a zip and unzip it.
2. In claude.ai: Settings, Capabilities, Skills. Upload each folder under `skills/` as its own zip (`flow`, `setup`, `profile`, and the rest).
3. Start a chat and type `set up skill-flow`.

claude.ai has no subagents. The flow plays the planner, writer and reviewer roles itself, in sequence. Your profile files live in a Project or in the `profile/` folder of your copy.

### Cursor, Codex, ChatGPT, Gemini, Grok, anything else

The skills are plain Markdown. See [docs/other-ais.md](docs/other-ais.md) for where each surface reads them from and the one-line instruction that turns the flow on there.

## How the flow works

```
prompt
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

Models are a setting, not a rule. `setup` writes a model ladder into `TOOLS.md`: for each role, the models you can run, best first, and the flow uses the first one that works. The default ladder in Claude Code is Fable 5.1 then Opus 5.5 for the planner and reviewer, Sonnet 5.5 then Haiku 5.5 for the writers, then whatever the session is on. No Fable on your plan? It steps down. One model and no subagents (claude.ai, ChatGPT, Gemini, a Grok Bot)? The flow plays all three roles in sequence on that model, and it still works: the plan before the work and the review after it are what catch the gaps.

## Your profile

`setup` writes four files. They are the only place anything about you lives, and they are gitignored.

| File | Holds |
|---|---|
| `PROFILE.md` | You, what you run, your team (people and AIs), where things live, priorities, gates, hours, quality bar |
| `TOOLS.md` | Which AI surfaces and models you use, which tools are connected and for what |
| `VOICE.md` | How you write: samples, banned words, sign-off, length |
| `ROUTER.md` | Your own skills in the flow's table, plus a do-not-call list |

Claude Code: `~/.claude/skill-flow/`. Elsewhere: `profile/` in your copy of this repo. Blank templates in `skills/profile/references/`.

## Make it yours

- Add a skill of your own: put it in `ROUTER.md` with one line on when it runs. The flow checks it against every prompt from then on.
- Change a default: `ROUTER.md` beats every house pick in `skills/flow/references/router.md`.
- Port a private skill in: read [docs/CONTRIBUTING-SCRUB-BRIEF.md](docs/CONTRIBUTING-SCRUB-BRIEF.md). It is the contract that keeps this kit free of anyone's private details.

## Principles

- Act, don't ask. Look it up. Ask only at a real fork, and ask once.
- One owner per result. Delegating never moves it off your desk.
- Right the first time, proven, no homework left for the owner.
- Gates stay with the owner: money, signatures, deleting live data, messages in their name, anything going live, private data leaving its room.
- Plain words. No jargon, no em dashes, short by default.

## License

MIT. See [LICENSE](LICENSE).

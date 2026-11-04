# Scrub brief: turning a private skill into a skill-flow skill

skill-flow is a public kit. Every skill in it must work for a stranger on day one and read as if written for them. This brief is the contract for anyone porting a skill in.

## The profile folder

Nothing personal lives in a skill. It lives in the user's **profile folder**, which `setup` writes:

- Claude Code: `~/.claude/skill-flow/`
- Any other AI: the `profile/` folder next to `skills/` in their copy of this repo

Files, all Markdown, all optional until setup fills them:

| File | Holds |
|---|---|
| `PROFILE.md` | The owner's name and role, what they run (businesses, products, projects), who's on the team (people and AIs, each with one line on what they own), where things live (repos, notes, CRM, docs), today's priorities, the gates (what needs the owner's yes), working hours |
| `VOICE.md` | How the owner writes: 3 to 5 real samples, banned words, sign-off, length rules |
| `TOOLS.md` | Which AI surfaces and models they use (Claude Code, claude.ai, Cursor, ChatGPT, Gemini, Grok), which tools are connected (calendar, email, CRM, code host, chat), what each is for |
| `ROUTER.md` | Their own skills and plugins, in the flow's table shape, plus a do-not-call list |
| `STACK.md` | What is installed, connected, scheduled and built, what was skipped, what waits on the owner |
| `BLUEPRINT.md` | The one-page map `blueprint` writes: what exists and how to trigger it |

A skill reads a profile file like this, verbatim wording:

> Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`.

## Replace, never leave

| In the private skill | In skill-flow |
|---|---|
| Tyler, "he", "his" | "the owner" or "you" (the owner is the person the AI works for). Never a name. |
| Maverick, Grokie, Amelia, ELA, Paddles, Ace, Swoop, Manila, Sleuth, Rainmaker, Wrench, Showtime, Bargain, Mr. Clean, Chuck Norris, Porter, Bambi | "the lanes in `PROFILE.md`" or the generic lane (planner, writer, reviewer, a human teammate). Remove the name. |
| Eskew, LFG, Leaders Financial Group, Kraken, Krackerjak, EG Consult, GapScope, Elevate, Summit Labs, Million Mile Challenge, BOOST, QuotePipe, Boomerang, Caughern | Remove, or replace with a neutral example ("a client's agency", "the flagship product"). |
| Any person's name (Nic, Diane, Jeff, Kenny, Carson, Barry, Caleb, Belac) | Remove. |
| Discord room names and ids, `#eskew`, `#ai-agents`, `#tyler`, guild ids, bot ids, tokens, env var names like `DISCORD_MAVERICK_BOT_TOKEN` | Remove. A "post it where your team talks" line reads `TOOLS.md` for the room. |
| Vault paths (`How to Work With Tyler - START HERE.md`, `Who does what`, `Decisions.md`, `Priorities.md`, `DATA-SOP`, `AGENT-SOP`, `Crew Operations Manual`, `Builds/...`, `Plans/...`, `second-brain`), `mrclean`, `~/Organization_Projects` | The matching profile file, or "the owner's notes (where `PROFILE.md` says they live)". |
| `claude-config`, `~/.claude/skills/...`, `web-build`, `site-crew`, `crew-bus`, `wrap`, `decision-hour`, `content-factory`, `cross-vertical-copy-director`, `gpt-image-gen-skill`, `protection-desk`, `ghl-*`, `plaud-*`, `fable-max`, `fable-brainstorm`, `fable-review`, `karpathy-guidelines`, `impeccable`, `superpowers:*` | Keep only skills that ship in this repo: `flow`, `setup`, `connect`, `blueprint`, `operating-rules`, `routines`, `meeting-prep`, `inbox`, `protection-desk` (the bridge skill only; the desk itself is a separate licensed tool), `ghl-assistant`, `prompt-improver`, `simple-talk`, `profile`, `planning-mode`, `project-cleanup`, `ghost-mode`, `creative-direction`, `prospect-mover`, `pixel-proof`. Agents: `planner`, `writer`, `reviewer`. `impeccable` may be named: it is a public plugin the kit installs. For a removed skill, name the generic job instead ("a UI design pass", "a copy pass", "a debugging pass") so the flow can route it to the user's own skill via `ROUTER.md`. |
| Dated orders: `(Tyler, 2026-10-14: "...")`, `Decisions, 2026-...`, "master plan", "the October burn" | Remove the citation. Keep the rule if it is a good general rule; cut it if it only made sense for him. |
| The WOW bar, "95%", "9/10+" | Keep the idea as "the quality bar in `PROFILE.md`" with a sane default: right the first time, complete, proven, no homework for the owner. |
| Insurance-only content (carriers, riders, underwriting, regulated riders, `lens-insurance`, `tyler-house-rules`) | Drop the file, or keep it as `references/lens-example.md` clearly labeled as one vertical's worked example the user can copy for their own. |
| Model names as hard defaults (Opus 5.5, Sonnet 5.5, Fable 5.1, Grok 4.7) | Keep them only in `prompt-improver`'s model cards and the three agent files. Elsewhere say "the planner", "the writer", "the model in use (see `TOOLS.md`)". |
| "3 lines max" to Tyler | "Short by default; the owner's length rule is in `VOICE.md`." Default when unset: lead with the answer, then the catch, then the next step. |
| Hooks the user may not have (conductor, Stop hook, room-log, workspace guard) | Mention only this repo's own `hooks/prompt-gate.sh` and `hooks/session-start.sh`. Everything else: "where there is no hook, run this anyway." |
| A specific CRM location id, sub-account name, token prefix tied to one business, webhook URL | Remove. The CRM guides use placeholders the owner replaces in their own terminal. |

## Keep

- The method. Steps, checklists, gates, scorecards, examples that teach the method. Rewrite examples with neutral businesses (a plumber, a SaaS team, a coach, a dentist, a nonprofit).
- Frontmatter: `name` and `description`. The description must still say when to trigger and must not name a person. Under 1,024 characters.
- Plain words, short sentences, no em dashes. The repo's own `simple-talk` rules apply to every file.
- File layout: `SKILL.md` plus `references/` and `scripts/` as the source had them, minus dropped files.

## Add to every SKILL.md

Right after the H1, one line:

> Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

## Checks before you hand it back

1. `grep -ri` the finished skill folder for every name and term in the Replace table. Zero hits.
2. No URL, id, token, email or phone number anywhere.
3. Every profile read uses the exact wording above.
4. Every skill or agent it names exists in this repo.
5. The frontmatter parses and the description is under 1,024 characters.
6. Read it once as a stranger who installed the kit ten minutes ago. Every sentence must make sense to them.

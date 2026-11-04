---
name: operating-rules
description: Writes and maintains the owner's standing operating file for Claude (CLAUDE.md on Claude Code, custom instructions elsewhere) so Claude acts with full authority inside clear hard stops. It fills the template from the owner's setup answers, installs it in the right place for the surface, and re-checks it when the owner's gates, priorities or team change. Use on "take the handcuffs off", "stop asking me", "write my CLAUDE.md", "update my rules", "you are being too cautious", or whenever setup finishes and no operating file exists.
---

# operating-rules

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

Most owners get a Claude that asks too much, checks in too often and stops at every fork. This skill writes the one file that fixes that: a short, plain operating file that says "act, decide, prove, finish" and names the handful of things that still need the owner. The flow, the skills and the hooks all read it.

## 1. Read what exists

Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and run `setup`; this file cannot be written from guesses.

Then look for an existing operating file:

| Surface | Where it lives |
|---|---|
| Claude Code | `~/.claude/CLAUDE.md` (global) and `CLAUDE.md` in the project root |
| claude.ai chat | The skill-flow Project's instructions (preferred), or Settings, Profile, "What personal preferences should Claude consider" |
| Cowork | `~/.claude/CLAUDE.md` on the owner's computer, same as Claude Code |
| Cursor | `.cursor/rules/*.mdc` with `alwaysApply: true`, or `AGENTS.md` |
| Codex, Grok CLI | `AGENTS.md` in the project root |
| ChatGPT | Custom Instructions, or a Project's instructions |
| Gemini | The Gem's instructions |

If one exists, read it fully. You will merge, not overwrite: keep every rule the owner wrote that does not conflict with the answers in `PROFILE.md`, and mark the ones you changed in one line at the end.

## 2. Fill the template

Fill `references/CLAUDE-template.md`. Every placeholder comes from `PROFILE.md`, `TOOLS.md` or `VOICE.md`; never from memory.

| Placeholder | Source |
|---|---|
| `{{OWNER_NAME}}`, `{{ADDRESS_AS}}` | `PROFILE.md`, Owner |
| `{{DATE}}` | Today |
| `{{REPLY_STYLE}}` | `VOICE.md`, Length rules, "Replies to the owner". Default: "Short by default: three lines for a status, the full answer for a question." |
| `{{BLUNTNESS_RULE}}` | `ROUTER.md` bluntness rule. Default: "Be blunt when they are about to commit to a plan, price or draft with holes in it: name the holes first, then the fix." |
| `{{PROFILE_DIR}}` | The profile folder path for this surface |
| `{{WHERE_THINGS_LIVE}}` | `PROFILE.md`, Where things live, as a short table |
| `{{SHIP_RULES}}` | From the gates: if "code going live" is a gate, write "Merges and deploys wait for the owner once the checks pass." If not, write "Merges and deploys are yours once tests and build are green and you have checked the live result." Add any project-specific gate from `PROFILE.md`. |
| `{{GATES}}` | `PROFILE.md`, Gates, numbered. Keep the owner's wording. |
| `{{PRIORITIES}}` | `PROFILE.md`, Priorities, numbered, with the date |

Keep the whole file under 120 lines. A rule nobody reads is not a rule.

## 3. Install it

- **Claude Code:** write to `~/.claude/CLAUDE.md`. If a project `CLAUDE.md` exists and holds project rules, leave it and add one line at its top: "Operating rules: `~/.claude/CLAUDE.md`." Tell the owner the hook from this plugin is already on.
- **claude.ai:** show the file and tell the owner exactly where to paste it (Settings, Profile, preferences box, or the Project's instructions). It is under the paste limit by design.
- **Cursor:** write `.cursor/rules/operating-rules.mdc` with frontmatter `alwaysApply: true` and the file body.
- **Codex, Grok CLI, others:** write or extend `AGENTS.md` in the project root.

Never write a secret, a token, a client's name or a phone number into this file. It is read by every session and often committed.

## 4. Prove it

Read the file back. Check:

1. Every placeholder is gone.
2. The gates match `PROFILE.md` exactly, no more and no fewer.
3. The "Act, don't ask" rule is present and not softened.
4. Nothing in it conflicts with a rule the owner wrote by hand.

Then say in three lines: where the file is, what changed, and that from now on Claude acts inside those gates without asking.

## Keeping it current

Re-run this skill when `setup` re-runs, when the owner adds or removes a gate, when priorities change, or when the owner says Claude is asking too much or too little. Re-fill from the profile; never hand-edit the gates from a chat message without updating `PROFILE.md` first. One owner per fact: the profile owns the fact, this file repeats it.

## What good looks like

Owner says "stop asking me before you edit files." Bad: add a line saying "don't ask before editing." Good: read `PROFILE.md`, confirm file edits were never a gate, find the rule or hook that caused the asking, fix that, and tell the owner in one line what was making Claude stop.

Owner says "take the handcuffs off." Good: run this skill end to end, install the file, and show the six hard stops that still stand so the owner knows what "off" means.

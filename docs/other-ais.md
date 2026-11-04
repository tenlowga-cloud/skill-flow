# skill-flow on other AIs

The skills are Markdown. Any AI that reads a file or a pasted instruction can run them. What changes per surface is three things: where the files go, whether the flow can run as subagents or has to play the roles itself, and how you turn the gate on so it runs on every prompt.

The gate is one line. Paste it wherever the surface keeps standing instructions:

> Before any work on a prompt, read and follow `skills/flow/SKILL.md`. Skip it only for pure chat.

## Cursor

- **Files:** clone this repo into your project or a shared folder. Cursor reads `.cursor/rules/*.mdc` and `AGENTS.md`.
- **Gate:** add a rule file `.cursor/rules/skill-flow.mdc` with `alwaysApply: true` and the gate line, pointing at the repo path.
- **Roles:** Cursor has no subagents from a rule. The flow plans, writes and reviews in sequence. Pick the strongest model in the picker for a big job's plan, then switch to a fast one for the slices, or let one model do both.
- **Profile:** `profile/` next to `skills/`.

## Codex

- **Files:** clone the repo. Codex reads `AGENTS.md` at the project root.
- **Gate:** in `AGENTS.md`, add the gate line with the repo path.
- **Roles:** sequential, as above.
- **Profile:** `profile/` next to `skills/`.

## ChatGPT

- **Files:** a Project. Upload `skills/flow/SKILL.md`, `skills/setup/SKILL.md`, `skills/profile/SKILL.md` and the skills you use most as project files. Big reference folders (model cards, prospect-mover references) upload one file at a time.
- **Gate:** the Project's instructions, or Custom Instructions for every chat: the gate line, plus "the skill files are in this project".
- **Roles:** sequential. No subagents.
- **Profile:** upload your four profile files to the same Project after `setup` writes them (it will write them as chat output; save them).

## Gemini

- **Files:** a Gem, or files attached to a chat. Same set as ChatGPT.
- **Gate:** the Gem's instructions.
- **Roles:** sequential.
- **Profile:** attached to the Gem.

## Grok (Grok Bot, Grok CLI, grok.com)

- **Files:** a Grok Bot reads its description and its skill notes. Paste `skills/flow/SKILL.md` as the Bot's standing instructions and add the other skills as skill notes, or point the Bot at a clone of this repo if it has file access. Grok CLI reads `AGENTS.md` like Codex.
- **Gate:** the Bot description, or `AGENTS.md` for the CLI.
- **Model:** a Grok Bot runs on one model it cannot change, and has no subagents. The flow plays planner, writer and reviewer in sequence on that model. `TOOLS.md` says "session model" for every rung and "subagents: no". The prompting card for Grok is in `skills/prompt-improver/references/models/grok.md`.
- **Several Bots:** list each in `PROFILE.md` as a lane with what it owns. The Bot holding the job hands slices to the others through the team room in `TOOLS.md`. That is how a Grok setup gets parallel writers.
- **Profile:** skill notes on the Bot, or `profile/` in the clone.

## claude.ai

- **Files:** Settings, Capabilities, Skills. Each `skills/<name>/` folder uploads as one zip. The skill's description is what makes it trigger, so the flow runs without a gate line, but adding one to a Project's instructions makes it reliable.
- **Roles:** sequential. No subagents.
- **Profile:** a Project's files, or `profile/`.

## What you lose without Claude Code

- The hooks. On other surfaces the gate and the first-run check are instructions, and a long chat can drift away from them. Re-paste the gate line if the flow stops firing.
- Real parallel writers and a model ladder. The flow still cuts slices and does them one by one, on the one model you have.
- Commands (`/skill-flow:setup`, `/skill-flow:connect`). Type "run setup" or "connect my calendar" instead.
- Plugins. `impeccable` installs only in Claude Code; `pixel-proof` carries the visual check elsewhere.
- Cloud scheduled tasks. `routines/references/scheduling-by-surface.md` gives each surface's scheduler or the fallback.
- The Protection Desk's reader gate, which calls the `claude` command. The desk still builds with `--reader 0`, named `_UNREVIEWED`.

## The operating file on other surfaces

`operating-rules` writes your "act, don't ask" file wherever the surface keeps standing instructions: Cursor `.cursor/rules/operating-rules.mdc` (`alwaysApply: true`), Codex and Grok CLI `AGENTS.md`, ChatGPT Custom Instructions or a Project, Gemini a Gem, claude.ai a Project or your preferences. The hard stops travel with it.

Everything else, the method, the router, the profile, the prompting cards, works the same.

# Router: house picks when two skills overlap

`ROUTER.md` in the profile folder beats this file. This table covers the skills that ship in skill-flow. For a job no row covers, step 3 of `flow` still runs: read the live skill list and pick from it.

| The owner says or means | Call |
|---|---|
| Any prompt that asks for work | `flow` (this skill), always first |
| "Set up", "tailor this to me", "connect my tools", first run | `setup` |
| Who owns what, which project, where something lives, what matters this week | `profile` |
| A prompt for another AI, bot, agent, image or video model; "improve this prompt" | `prompt-improver` |
| Anything said back to the owner, interface text, explaining something technical to a non-expert | `simple-talk` |
| "Be blunt", "give it to me straight", "stop hedging", or the owner is about to commit to a plan, price or draft with holes | `simple-talk`, blunt setting |
| Anything a person other than the owner will read: email, text, post, script, client note, ad | `ghost-mode` |
| Anything static a prospect will see: site, quote, proposal, campaign, sequence, script, ad, deck, form; "make it convert" | `prospect-mover` on top of whatever builds it, then `ghost-mode` for the voice |
| A concept, brand, name, campaign, page or image that must not feel generic or AI-made | `creative-direction` |
| A visual bug from a screenshot; "looks broken on my phone"; before calling any UI change done | `pixel-proof` |
| "Plan this", "planning mode", a big unclear build | `planning-mode`, then the `planner` agent for the slices |
| "Clean up this project", "too many files", "remove dead code" | `project-cleanup` |
| A bug, error, "it's broken" | A debugging pass: reproduce, read the real failing state, rank hypotheses, test the top one, change approach after two identical failures. Use the owner's debugging skill from `ROUTER.md` if they have one. |
| A website, landing page or UI design | The owner's design and site skills from `ROUTER.md`. With none: build it, then `pixel-proof`. |
| Copy and positioning with research behind it | The owner's copy skill from `ROUTER.md`. With none: `creative-direction` for the idea, `ghost-mode` for the voice, `prospect-mover` if a prospect will read it. |
| A deck, PDF, Word doc or spreadsheet | The surface's document skills if it has them; otherwise build the file directly. |
| Research with sources | The surface's research tools; `planner` to shape the question on a big one. |
| Code: a feature, a refactor, tests | The owner's coding skills from `ROUTER.md`. Defaults: the least code that works, change only what the request needs, tests on risky logic, verify before claiming done. |

## Skills that pair

- `prospect-mover` always ends with `ghost-mode`; `pixel-proof` closes anything visual.
- `creative-direction` runs before the build when the look matters; `pixel-proof` after.
- `simple-talk` and `ghost-mode` run together on interface text.
- `planning-mode` writes the plan the owner reads; the `planner` agent writes the slices the writers run. On a big job they are the same plan, one for people and one for the team.

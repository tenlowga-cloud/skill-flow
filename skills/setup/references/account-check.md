# The account pass: read the account, flip the switches

Claude cannot see the owner's account settings. The owner can. So this pass is a guided walk: you name the page, they open it and read back what they see, you say which switch to flip and why, they flip it, they say "done". Teaching mode throughout (`teaching-mode.md`). One switch per message.

Why it matters: a skill that needs memory, web search, a connector or Cowork does nothing if the account has it off. Twenty minutes of setup is wasted if the first routine fails on a switch nobody checked.

## 1. Which plan, which seat

Ask: "Open https://claude.ai/settings and tell me what plan it shows at the top (Free, Pro, Max, Team, Enterprise)." Record it in `STACK.md`. Then:

- **Free:** say plainly that plugins from the directory, scheduled tasks and most connectors need Pro or above. Do the rest of setup, mark those rows "needs a paid plan" in `STACK.md`, and stop offering them.
- **Pro or Max:** everything below applies. They own every switch.
- **Team or Enterprise:** some switches belong to the organization's Owner, not the member. Ask: "Are you an Owner of this organization, or a member?" A member does the member switches below and asks the Owner for the rest; give them the exact lines to send (section 6). An Owner does both.

## 2. Memory (must be on)

The whole kit assumes Claude remembers the owner between chats on claude.ai and Cowork. Without it, every chat starts cold and the profile files do the whole job alone.

Say: "Open Settings. Look for a Memory page in the left menu. If there is no Memory page, open Capabilities instead; older accounts keep memory there."

Then, one at a time, in the owner's words:

1. "Find the switch that generates memory from your chats. It may read 'Generate memory from chat history' or just 'Memory'. Is it on? If not, turn it on."
2. "Find the switch that lets Claude search and reference your past chats. It may read 'Search and reference chats'. Turn it on."
3. If they see a memory import option and they come from another AI, offer it: "There is an import option. We can do that later; note it for `STACK.md`."
4. "If you see a project memory setting, leave it on."

You should see: both switches on. Record "memory: on, date" in `STACK.md`. If the switch is greyed out on Team or Enterprise, the Owner turned it off for the organization; add it to the Owner list (section 6).

Claude Code has its own memory (`CLAUDE.md`, auto memory). Nothing to flip there.

## 3. Capabilities and features (all on unless the owner has a reason)

Say: "Stay in Settings. Open Capabilities (or Features; the label differs by version). Read me the list of switches you see." Then go through theirs, not a fixed list. For each switch they name, say in one line what it does and whether to turn it on. Default on for everything the kit uses:

| Switch (label varies) | Why the kit needs it |
|---|---|
| Artifacts, or AI-powered artifacts | `blueprint` and `impeccable` show pages, documents and previews as artifacts |
| Analysis tool, or code execution | Spreadsheets, charts, the Protection Desk's checks in Cowork |
| Web search | `connect` guides, `meeting-prep` public sources, `creative-direction` research |
| Extended thinking | Big jobs plan better; the flow's planner role |
| Claude in Chrome, or browser | The live walkthroughs in `connect` |
| Skills, Plugins | The kit itself. If Skills is off, nothing here loads |
| Scheduled tasks | `routines`, where the surface offers it |
| Memory | Section 2 |

Anything they do not want on, record as "off by choice" in `STACK.md` and never offer again without a reason.

## 4. Connectors (the account's, not the plugin's)

Say: "Open https://claude.ai/customize/connectors. Tell me which ones show Connected." Match against what the chosen routines need. Everything missing goes to `connect`, which walks each one. On Team or Enterprise, a connector that is not in the list at all has to be added by an Owner at Organization settings, Connectors, before a member can connect it; add those to the Owner list.

## 5. Plugins page sanity check

Say: "Open https://claude.ai/customize/plugins. Do you see skill-flow and impeccable in your list, both turned on?" If skill-flow is missing on a Team or Enterprise member account, the Owner has not made it available: Owner list. If the Add button is missing, the Owner has User-created skills off: Owner list.

## 6. The Owner list (Team and Enterprise only)

Collect every item that needs the Owner, then give the member one message to send, filled in. The Owner's paths, verified against Anthropic's docs:

- **Let members add marketplaces and plugins:** Organization settings, Plugins & skills, Policy tab, turn on **User-created skills**.
- **Make skill-flow available to everyone:** Organization settings, Plugins & skills, **Add**, **Add marketplace**, enter `tenlowga-cloud/skill-flow` (or the team's own fork). Then on the Inventory tab, open the plugin's row menu, **Default access**, choose **Available to install** or **Installed by default**. Same for `pbakaus/impeccable`.
- **Add a connector for the organization:** Organization settings, Connectors, add it. Members then connect it with their own account.
- **Memory for the organization:** if a member's memory switch is greyed out, the Owner turns it on in Organization settings (the label is Capabilities or Memory depending on version).
- **Skills master switch:** Organization settings, Plugins & skills, Policy, **Skills** must be on or no plugin loads for anyone.

The message to the Owner, in `VOICE.md` style once it exists, otherwise plain:

> Can you do three things in Organization settings so I can run the skill-flow setup? 1. Plugins & skills, Policy: turn on User-created skills. 2. Plugins & skills, Add, Add marketplace: `tenlowga-cloud/skill-flow` and `pbakaus/impeccable`, then set both to Available to install. 3. Connectors: add [the connectors from section 4]. Takes about five minutes. Thanks.

Record "waiting on Owner: items" in `STACK.md`. Do everything else that does not depend on it. When the Owner says done, re-run section 5 and carry on.

## 7. Record and move on

`STACK.md` gets a "Account" block: plan, seat (Owner or member), memory on or off, each switch and its state, connectors connected, Owner items waiting. Then round 1 of `setup`.

## Rules

- Never ask the owner to screenshot a page that shows a billing detail, a token or another person's data. Read-backs in their own words are enough.
- A switch they turn off on purpose stays off. Record it; do not argue.
- Labels move between versions. When a label you named is not there, ask them to read the list and match by meaning, never by guessing a toggle.

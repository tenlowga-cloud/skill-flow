# The account pass: read the account, flip the switches

Claude cannot see the owner's account settings on its own. There are two ways to read and flip them (`teaching-mode.md`, "Who does the clicking"):

- **Talk mode:** you name the page, they open it and read back what they see, you say which switch to flip and why, they flip it, they say "done". One switch per message.
- **Do mode (the default once the browser is proven):** install Claude in Chrome first (section 3b) and prove it works. Then you open each settings page in their browser, read the switches yourself, flip the ones that should be on, and narrate one line each: "Memory: both switches were off. Turning them on. Done."

Order for an owner on a paid plan with desktop Chrome or Edge: section 1 (the plan), then 3b (the extension), then sections 2, 3, 4 and 5 in Do mode. Everyone else: sections 1 to 5 in Talk mode. In both modes the sign-in, the Owner list (section 6) and any greyed-out switch go to the person; never work around a switch an Owner locked.

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

## 3b. Claude in Chrome: install the extension

The switch in Settings only allows it. The extension is what does the work. It is how Claude clicks through a setup with the owner, fills forms, and checks that a connection really works, so install it before the connectors and every walkthrough after this can run live. About three minutes. Teaching mode, one step per message.

Needs: a paid plan (Pro, Max, Ultra, Team or Enterprise) and desktop Google Chrome or Microsoft Edge. Not a phone, not Safari, not Firefox. On Enterprise an Owner may have to allow it first (Organization settings, Claude in Chrome, https://claude.ai/admin-settings/browser-extension; it is off by default where HIPAA is on). On Team an admin can block it. A Free plan skips this section and uses the written guides.

Ask first: "Are you on a computer with Chrome or Edge right now?" No: record "browser: no desktop Chrome, written guides only" in `STACK.md` and move on.

1. "Open Chrome. Go to https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn. You should see a page called Claude, published by Anthropic, with an Add to Chrome button. Check it says Anthropic: copycat extensions exist."
2. "Click Add to Chrome, then Add extension in the box that pops up. You should see a small puzzle-piece icon at the top right of Chrome."
3. "Click the puzzle piece. Find Claude in the list and click the pin so it stays on your toolbar."
4. "Click the Claude icon. A side panel opens. Sign in with the same Claude account you are using here. If you belong to more than one organization, pick the same one."
5. Verify: "On any open page, type into the side panel: What is the title of this page? You should see a real answer." Pass is a correct title. On Claude Code, also run `/chrome`; the status should read Enabled and the extension Installed.
6. Say how it behaves: "When a page asks for a password, a code or a card number, Claude stops and you type it. It asks before it acts on a new site. You can see everything it does in the window."

Record in `STACK.md`: Claude in Chrome installed, signed in, verified, date.

If it fails: Add to Chrome is greyed out or blocked means a company policy, ask the IT person or the Owner. "Browser extension is not connected" almost always means the extension and Claude are signed in to different accounts or organizations; sign out of the extension and back in with the same one, then restart Chrome. The first time it connects, Chrome sometimes has to restart before it sees the connection.

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

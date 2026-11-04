# Connect GoHighLevel

Method: HighLevel's official MCP server. You sign in with your GoHighLevel login, pick the business, approve what the AI may do. No token to make or rotate. About 5 minutes.

Say to the owner first: "GoHighLevel has an official plug for AI assistants. You sign in once, pick which business the AI may see, and tick what it may do. Nothing to copy or paste."

Then, before anything: "A sub-account is one business inside your GoHighLevel. You will pick it during sign-in. If you run several, pick the one you work in most; we can add others later."

## Step 1 of 4. Pick the door for their AI

Each AI has its own address. Use the one that matches where the owner is talking to you right now:

| AI | Address |
|---|---|
| Claude (claude.ai, Cowork, Claude Code) | `https://services.leadconnectorhq.com/mcp/anthropic/v2` |
| ChatGPT, Codex, other OpenAI clients | `https://services.leadconnectorhq.com/mcp/openai/v2/` |
| Cursor | `https://services.leadconnectorhq.com/mcp/cursor/v2` |
| Grok Bot | The official HighLevel app in the Bot's app catalog |

Source: HighLevel's docs, marketplace.gohighlevel.com/docs/other/mcp.

## Step 2 of 4. Add it

### claude.ai or Cowork

1. "Open https://claude.ai/customize/connectors. You should see your list of connectors."
2. "Click **Add custom connector**. A small form opens asking for a URL."
3. "Paste exactly: `https://services.leadconnectorhq.com/mcp/anthropic/v2` and click **Add** (or **Connect**). You should see GoHighLevel, or LeadConnector, appear in your list with a Connect button."
4. Go to Step 3.

### Claude Code

Type this in your own terminal:

```
claude mcp add --transport http gohighlevel https://services.leadconnectorhq.com/mcp/anthropic/v2
```

You should see `Added HTTP MCP server gohighlevel`. Then type `/mcp` inside Claude Code, pick gohighlevel, and choose sign in. A browser opens. Go to Step 3.

### Cursor

Open `~/.cursor/mcp.json` (every project) or `.cursor/mcp.json` (one project) and add:

```
{ "mcpServers": { "gohighlevel": { "url": "https://services.leadconnectorhq.com/mcp/cursor/v2" } } }
```

Save. Cursor prompts you to sign in. Go to Step 3.

### ChatGPT

1. Settings, then Security and login (or Apps and connectors; the label varies), turn on **Developer mode**.
2. Create a new connector or plugin and paste `https://services.leadconnectorhq.com/mcp/openai/v2/` as the server URL.
3. Complete the sign-in. In a new chat, turn it on from the tools menu. Go to Step 3.

## Step 3 of 4. Sign in and choose

1. "A GoHighLevel sign-in page opens. Sign in with your usual GoHighLevel login. I am not watching this screen."
2. "It asks which sub-account (business) the AI may use. Pick the one you work in. You should see its name selected."
3. "It shows a list of permissions. Read them to me by group (contacts, conversations, opportunities, calendars, tasks). Approve them. This is what the AI will be allowed to look at and do. We keep sending and deleting as your call anyway."
4. "Click Allow (or Authorize). The page says connected and sends you back."

You should see: the connector shows **Connected** in claude.ai, or `claude mcp list` shows gohighlevel connected, or Cursor shows a green dot.

If they run several businesses: HighLevel is rolling out one sign-in for many sub-accounts (the bulk install). Until it shows up, the connection is per sub-account, and the AI can name the sub-account in a prompt when more than one is connected.

## Step 4 of 4. Verify it works

Ask: "List the 3 most recent contacts in my GoHighLevel."
Pass: three real contact names from the account. Check one against the Contacts page.

Then: "What tasks are assigned to me in GoHighLevel?" Pass: real tasks, or "none" when there are none.

Record in `TOOLS.md` (CRM: GoHighLevel, connected, sub-account name) and `STACK.md` (date, the verify prompt that passed). Then offer the `ghl-assistant` skill: "Want me to watch your GoHighLevel for tasks, messages and deals and work them for you every hour?"

## What the AI can reach

Four tools that cover more than 550 operations: contacts (with tasks, notes, tags), conversations and messages, opportunities and pipelines, calendars and appointments, and more. The AI searches for the operation it needs and runs it against the sub-account you chose.

## If it fails

1. The connector will not add: check the URL is exact, including `/v2` (and the trailing slash on the OpenAI one). Try a fresh chat.
2. Sign-in loops or errors: sign in to GoHighLevel in the same browser first, then click Connect again.
3. Connected but empty results: the wrong sub-account was picked. Disconnect, connect again, pick the right business.
4. "Permission denied" on one action: that permission was not approved at sign-in. Disconnect, connect again, approve it.
5. Claude Code: "is Anthropic-hosted and doesn't support local OAuth" means you used a claude.ai connector URL by mistake; this one supports local sign-in, so re-run the add command exactly.

## Advanced: token path

If an owner cannot use sign-in (a locked-down agency, or an automation that runs with no person present), HighLevel's older endpoint `https://services.leadconnectorhq.com/mcp/` takes a Private Integration Token. Settings, Private Integrations, create one with read-only scopes first, token straight into the password manager, then `claude mcp add --transport http gohighlevel https://services.leadconnectorhq.com/mcp/ --header "Authorization: Bearer <token>" --header "locationId: <Location ID>"`, typed by the owner in their own terminal. Rotate it every 90 days. Never paste it into a chat.

## Hard rules for GoHighLevel

- The AI never sends a message, text or email to a contact without the owner's yes for that exact message.
- The AI never deletes anything without the owner's exact yes for that item.
- A workflow test-fire is not proof. Open the contact record and check the data landed.
- One write lane means one audit trail. Let one tool (the AI or a workflow) write a given field, not both.
- A custom field key must match exactly (case and underscores). A wrong key silently drops the data.
- Pipeline stage changes, appointment changes and tag changes on a client: tell the owner first, do it on yes.

## What the AI may do by default

- Read contacts, deals, calendars, conversations, tasks: yes.
- Add a note, mark a task done when the record shows it is done, draft a reply, draft a follow-up: yes, and say so.
- Send anything, delete anything, change a field on a client record, change a stage, a tag or an appointment: only with the owner's yes for that item.

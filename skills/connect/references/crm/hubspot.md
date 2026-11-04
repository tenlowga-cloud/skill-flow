# Connect HubSpot

Method: HubSpot's official MCP server. You sign in with your HubSpot login. No token to copy.
Time: about 5 minutes. You need: a HubSpot login that can approve apps (ask your super admin if not).

## Step 1. Choose where you use the AI
Ask: "Are you using Claude Code in a terminal, or the claude.ai app?"

## Step 2a. Claude Code
1. In your terminal, type:
```
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```
You should see "Added HTTP MCP server hubspot".
2. Start Claude Code and type /mcp. Pick hubspot, then Authenticate.
3. A browser tab opens. Log in to HubSpot if asked.

## Step 2b. claude.ai
1. Settings, then Connectors.
2. Find HubSpot and click Connect. If it is not listed, use Add custom connector with https://mcp.hubspot.com/anthropic.
3. A HubSpot window opens. Log in if asked.

## Step 3. Choose the account and approve
1. Pick the HubSpot account you want the AI to use.
2. Read the permissions list. It follows your own user permissions.
3. Click Connect or Authorize.
You should see a "connected" message and be sent back to the AI app.
If you see "contact your super admin": ask them to approve it, or to give you permission to install apps.

## Step 4. Check the connection
In Claude Code, /mcp should show hubspot as connected. In claude.ai, the HubSpot connector shows Connected.

## Verify it works
Ask: "List the 3 most recently created contacts in my HubSpot."
Pass: three real names. Check one in HubSpot, under Contacts.

## If it fails
1. "Needs authentication" in /mcp: choose hubspot, Authenticate again.
2. Wrong account: disconnect, reconnect, and pick the right one at Step 3.
3. Permission error: your HubSpot user lacks access to that object (for example Deals). Ask your admin.
4. Browser did not open: copy the link shown in the terminal into your browser by hand.
5. Server missing after restart: re-run the Step 2a command with --scope user.

## What the AI may do by default
- Read contacts, companies, deals: yes.
- Draft notes, task wording, and emails for the owner: yes.
- Send an email, delete a record, or change a deal stage: only with the owner's yes for that item.

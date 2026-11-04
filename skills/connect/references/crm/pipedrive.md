# Connect Pipedrive

Method: Pipedrive's own connector in Claude's connector marketplace. You sign in with your Pipedrive login. Pipedrive announced it in 2026 and says it follows your user permissions. Exact screens may differ (verify at Pipedrive's help site).
Time: about 5 minutes.

## Step 1. Open Connectors
1. In claude.ai, click Settings, then Connectors.
2. Search for Pipedrive.
You should see Pipedrive with a Connect button.

## Step 2. Connect
1. Click Connect.
2. A Pipedrive window opens. Log in if asked.
3. Pick your company account.
4. Read the permissions and click Allow.
You should see Pipedrive marked Connected.

## Step 3. Claude Code
Run /mcp. If Pipedrive is listed, you are set. If not, the connector may live only in claude.ai. Use claude.ai chat, or ask the AI to build a bridge (other-crm.md). The connector's raw server URL is not confirmed (verify).

## If the connector is not listed
Use your personal API token:
1. In Pipedrive click your name (top right), then Personal preferences, then the API tab (verify the label).
2. Copy the token into your password manager. Do not paste it into the chat.
3. Use it only inside a Zapier or Make connection, or as an environment variable named PIPEDRIVE_API_TOKEN that you set in your own terminal. See other-crm.md.

## Verify it works
Ask: "Show my 3 open deals with the biggest value in Pipedrive."
Pass: real deal names and amounts. Check them in Pipedrive.

## If it fails
1. Not connected: Settings, Connectors, Pipedrive, Disconnect, then Connect again.
2. Wrong company: you manage more than one. Disconnect and pick the right one.
3. Missing data: your Pipedrive user cannot see those deals. Ask your Pipedrive admin.
4. Old manual setup conflicts: remove it, then reconnect from the marketplace.
5. Pop-up blocked: allow pop-ups and retry.

## What the AI may do by default
- Read deals, people, organizations, activities: yes.
- Draft notes and follow-ups for the owner: yes.
- Send an email, delete a record, or move a deal to a new stage: only with the owner's yes for that item.

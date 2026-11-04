# Connect Close

Method: Close's official remote MCP server at https://mcp.close.com/mcp (from third-party listings; verify at help.close.com/integrations/close-mcp-server). It signs in with OAuth. An API key option also exists.
Time: about 5 minutes.

## Step 1. Pick the access level
Close splits access into three levels (verify the names):
- mcp.read: look only.
- mcp.write_safe: look, add, and update.
- mcp.write_destructive: also delete.
Choose read to start. Never turn on delete unless you have a set process that needs it.

## Step 2a. claude.ai
1. Settings, then Connectors. Find Close and click Connect. If it is not listed, use Add custom connector with https://mcp.close.com/mcp.
2. A Close window opens. Log in and choose the read level if asked.
3. Click Allow.
You should see Close marked Connected.

## Step 2b. Claude Code
1. In your terminal, type:
```
claude mcp add --transport http close https://mcp.close.com/mcp
```
2. Start Claude Code, type /mcp, choose close, and Authenticate. Log in to Close in the browser and click Allow.

## Step 2c. API key instead (only if OAuth is not possible)
1. In Close click Settings, then Developer, then API Keys, then Generate a New API Key (verify the path).
2. The key is shown once. Copy it into your password manager before you close the page. Say "saved".
3. Set it in your own terminal as CLOSE_API_KEY. How to pass it to the server is on Close's MCP page (verify). Do not paste it into the chat.

## Verify it works
Ask: "Show the 3 most recently updated leads in Close."
Pass: three real lead names. Check them in Close.

## If it fails
1. Needs authentication: /mcp, choose close, Authenticate again.
2. Not enough permission for an action: you chose read. Reconnect at a higher level only if the owner agrees.
3. Wrong organization: Close users can belong to several. Reconnect and pick the right one.
4. Command quoting error: re-type the command by hand, not copied with smart quotes.
5. API key rejected: it was revoked or mistyped. Generate a new one.

## What the AI may do by default
- Read leads, contacts, opportunities, activities: yes.
- Draft notes, call prep, and emails for the owner: yes.
- Send an email or SMS, delete anything, or change an opportunity status: only with the owner's yes for that item.

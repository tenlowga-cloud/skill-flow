# Connect Salesforce

Method: Salesforce's hosted MCP servers, added in Claude as a custom connector using a connected app. Salesforce lists them for Enterprise, Performance, Unlimited, and Developer editions (verify). Whether they are generally available or still beta may have changed (verify at Salesforce's help site).
Time: 20 to 30 minutes. This usually needs a Salesforce admin. Say: "If you are not the admin, do Steps 1 and 2 together with them."

## Step 1. Turn on a hosted MCP server (admin)
1. Log in to Salesforce. Click the gear icon, then Setup.
2. In Quick Find type "MCP". Open MCP Servers (exact label may vary) (verify).
3. Pick the server for your data and activate it. Choose a read-only option if one is offered.
You should see the server marked Active, with a URL. Copy the URL into your notes.

## Step 2. Create a connected app (admin)
1. In Setup, Quick Find "App Manager". Click New Connected App (or External Client App, depending on version) (verify).
2. Name it "Claude assistant". Use your own email as the contact.
3. Turn on OAuth. Add the callback URL shown in Claude's custom connector screen or Salesforce's connect-Claude guide (verify the exact URL).
4. Scopes: pick the smallest set. Start with read-only data access.
5. Save. Wait a few minutes for it to take effect.
6. Open the app and find the Consumer Key and Consumer Secret.
The Consumer Secret is a secret. Copy both into your password manager entry "Salesforce Claude app". Do not paste them into this chat.

## Step 3. Add the connector in Claude
1. claude.ai: Customize (or Settings), Connectors, Add custom connector.
2. Paste the server URL from Step 1.
3. Open Advanced settings and type the Consumer Key and Consumer Secret from your password manager straight into the form's own fields.
4. Click Add, then Connect. A Salesforce login window opens. Log in and click Allow.
You should see the connector marked Connected.

## Step 4. Claude Code
Once added in claude.ai, Claude Code can use it when signed in to the same account. Run /mcp and check it is listed. If not, add it by URL: `claude mcp add --transport http salesforce <SERVER_URL>`, then run /mcp to sign in.

## If you cannot use hosted MCP
Use the Zapier or Make bridge in other-crm.md, or ask the admin for a read-only API user.

## Verify it works
Ask: "List 3 recent Leads or Contacts from my Salesforce."
Pass: three real records. Check one in Salesforce.

## If it fails
1. "invalid_client" or login error: the key or secret was mistyped, or the connected app is still activating. Wait 10 minutes and retry.
2. Callback URL mismatch: copy the exact callback URL from the connector screen into the app.
3. Access denied on an object: the signed-in user's profile does not cover it. Ask the admin.
4. Server not found: your edition may not support hosted MCP (verify).
5. Pop-up blocked: allow pop-ups for claude.ai and retry.

## What the AI may do by default
- Read leads, contacts, accounts, opportunities: yes.
- Draft notes and emails for the owner: yes.
- Send, delete, or change an opportunity stage: only with the owner's yes for that item.

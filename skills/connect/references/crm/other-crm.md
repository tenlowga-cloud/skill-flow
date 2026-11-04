# Connect any other CRM

Use this when your CRM is not in the index. You need one of these: the CRM has a REST API, or it works with Zapier or Make.
Time: 20 to 40 minutes.

## Step 1. Look for an existing connector first
1. In claude.ai, Settings, Connectors. Search for your CRM's name.
2. Search the web for "[CRM name] MCP server". Prefer one published by the CRM company itself.
If you find one, follow its steps with the standing rules in README.md. If not, go on.

## Step 2. Pick a path
Ask: "Does your CRM's help site mention an API or API key? Does it appear in Zapier or Make?"
- Zapier or Make, no API: Path A.
- API key available: Path B.

## Path A. Zapier or Make webhook bridge
1. Log in to zapier.com or make.com.
2. Create a Zap or scenario. First step: your CRM (for example "new contact" or "find contact").
3. Click Connect and sign in to your CRM, as the page asks.
4. Next step: a Webhook that sends the data to a place the AI can read (a Google Sheet or a small web address the AI sets up). The AI tells you the exact address.
5. Click Test. You should see a real contact appear.
6. Turn the Zap on only after the owner agrees to what it sends.
To let the AI add a note, make a second Zap with the action "create note" and a webhook trigger. Draft first, and test with a throwaway contact.

## Path B. Ask the AI to build the bridge
1. Find the API key in your CRM. Usual places: Settings, Integrations, API or Developer. (verify for your CRM)
2. If the key is shown once, copy it into your password manager before you close the page. Say "saved".
3. In your own terminal, type:
```
read -s CRM_API_KEY && export CRM_API_KEY
```
Paste the key and press Enter.
4. Tell the AI: "Build a small read-only MCP server that calls my CRM's REST API. Read the key from CRM_API_KEY. Give it only these tools: list recent contacts, find a contact by name or email, list open deals. No delete tool. No send tool."
5. The AI shows you the code in plain words. Ask it what each tool can do. Approve it.
6. Add it: `claude mcp add mycrm -- <command the AI gives you>`. The AI never needs the key itself.
7. Add write tools later, one at a time, only when you ask.

## Verify it works
Ask: "List the 3 most recent contacts in my CRM."
Pass: three real names that match your CRM.

## If it fails
1. 401 or 403: the key is wrong, expired, or lacks permission. Create a new one.
2. Empty list: the account or workspace is wrong, or the API URL for your region differs.
3. Zap test shows nothing: the trigger needs one real record to exist. Add a test contact.
4. Rate limit error: wait a minute and retry. Ask the AI to fetch fewer records.
5. Server not found: run `claude mcp list` and restart the app.

## What the AI may do by default
- Read contacts, deals, notes: yes.
- Draft notes and emails for the owner: yes.
- Send, delete, or change a pipeline stage: only with the owner's yes for that item.

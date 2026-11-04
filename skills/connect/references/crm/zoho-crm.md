# Connect Zoho CRM

Method: I found no official Zoho-published MCP server (verify at Zoho's developer site). Community and vendor servers exist (for example CData, or packages on PyPI). Check who publishes one before trusting it with customer data. The simplest safe path is a Zapier or Make bridge, or a small bridge the AI builds against Zoho's REST API.
Time: about 20 minutes.

## Step 1. Decide the path
Ask: "Do you want the AI to only look at your CRM, or also add notes? We start with look-only."
- Easiest: Zapier or Make (Path A).
- Direct API with a small bridge the AI builds (Path B).

## Path A. Zapier or Make
1. Log in to zapier.com or make.com.
2. Create a new Zap or scenario. Pick the app Zoho CRM.
3. Click Sign in to Zoho CRM. Log in to Zoho and click Accept.
4. Build a "find records" step (for example, recent Contacts) that sends results to a webhook or sheet the AI can read. The AI walks you through the fields. See other-crm.md.
You should see a test run return real contacts.

## Path B. Direct API (OAuth client)
1. Go to api-console.zoho.com (use your region's address, such as .eu or .com.au) (verify).
2. Click Add Client, then Self Client.
3. Open the Generate Code tab. Scope: ZohoCRM.modules.READ (read only to start). Duration: 10 minutes.
4. Click Create. Zoho shows a client ID, client secret, and code. Save all three in your password manager now. Do not paste them into the chat.
5. Tell the AI "saved". The AI writes a small bridge that reads the secrets from environment variables you set in your own terminal (ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, ZOHO_REFRESH_TOKEN). You run the one-time code exchange yourself.

## Using a community MCP server
Only if you accept the risk. Read its code first, give it read-only scopes, and put credentials in environment variables, never in the chat.

## Verify it works
Ask: "List the 3 most recent contacts in my Zoho CRM."
Pass: three real names that match Zoho.

## If it fails
1. Invalid code: the 10 minute code expired. Generate a new one.
2. Wrong data center: the API address must match your region (.com, .eu, .in, .com.au).
3. Insufficient scope: add the scope in the console and generate a new code.
4. Zapier test shows no records: the module name is wrong, or the account has none.
5. Unauthorized: reconnect the Zoho account in Zapier or Make.

## What the AI may do by default
- Read leads, contacts, deals: yes.
- Draft notes and emails for the owner: yes.
- Send, delete, or change a deal stage: only with the owner's yes for that item.

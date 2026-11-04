# Connect Follow Up Boss

Method: I found no official Follow Up Boss MCP server (verify at followupboss.com). Community servers exist and run on your own computer. They can read and write your data, so check the code first. The base for every path is your API key, used with a community server or a Zapier or Make bridge.
Time: about 15 minutes. You need: an Admin login to Follow Up Boss.

## Step 1. Create the API key
1. Log in to Follow Up Boss as an Admin.
2. Click Admin (top menu), then API (verify the path).
3. Click Create API Key. Name it "Claude assistant".
4. Copy the key into your password manager now, in an entry called "Follow Up Boss API, Claude". Do not paste it into this chat.
5. Say "saved".
Some endpoints may be limited to registered partners (verify). Use only normal key endpoints.

## Step 2a. Community MCP server (Claude Code)
Only after we have read its code and you accept the risk. It needs Node.js 18 or newer.
1. In your terminal, set the key without showing it:
```
read -s FUB_API_KEY && export FUB_API_KEY
```
Paste the key, press Enter.
2. Add the server. The AI gives you the exact folder after you download it:
```
claude mcp add followupboss -e FUB_API_KEY="$FUB_API_KEY" -- node /FULL/PATH/followupboss-mcp-server/index.js
```
You should see "Added stdio MCP server followupboss". Run `claude mcp list`.
This kind of server can delete data. The rule stays: read and draft only.

## Step 2b. Zapier or Make bridge
1. Log in to zapier.com or make.com.
2. Add a Follow Up Boss step. Choose Connect and type the key into the app's own secret field.
3. Build a "find person" or "new lead" step that sends results where the AI can read them. See other-crm.md.

## Verify it works
Ask: "List the 3 most recent people (leads) in my Follow Up Boss."
Pass: three real names. Check them in Follow Up Boss.

## If it fails
1. 401 or unauthorized: the key was mistyped or revoked. Create a new one.
2. Empty results: check you used the right Follow Up Boss account.
3. Server not found: check Node.js with `node -v` and the path in Step 2a.
4. Not an Admin: ask an Admin to create the key.
5. Variable not set: re-run the `read -s` line in the same terminal window.

## What the AI may do by default
- Read people, deals, tasks, notes: yes.
- Draft texts, emails, and notes for the owner: yes.
- Send a text or email, delete a person, or change a stage: only with the owner's yes for that item.

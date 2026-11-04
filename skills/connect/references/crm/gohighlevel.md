# Connect GoHighLevel

Method: a Private Integration Token (PIT) plus GoHighLevel's official MCP server.
Time: about 10 minutes. You need: admin access to the sub-account, a password manager, and a terminal (Claude Code) or the claude.ai app.

Say to the owner: "A sub-account is one business inside your GoHighLevel. The token only opens that one business. Good."

## Step 1. Open the right sub-account
1. Log in to GoHighLevel.
2. Switch into the sub-account (the location) you want the AI to use. If you only see an agency view, use the sub-account switcher at the top and pick the business.
You should see that business's own dashboard, not the agency dashboard.

## Step 2. Find Private Integrations
1. Click Settings (bottom left).
2. Look for Private Integrations in the Settings menu. It is sometimes under Other Settings or Integrations. The label may vary by version.
You should see a page with a Create new integration button.
If you cannot find it, you may be at the agency level. A PIT is made per sub-account, not for the agency. Go back to Step 1.

## Step 3. Create the integration
1. Click Create new integration.
2. Name: type "Claude assistant".
3. Description: "Read access for my AI assistant".

## Step 4. Pick scopes (least privilege)
A scope is a permission. "Readonly" means the AI can look but not change anything. "Write" means it can add or edit. Start with look-only.

Tick these read-only scopes:
- contacts.readonly (view contacts)
- opportunities.readonly (view deals)
- calendars.readonly (view calendars)
- conversations.readonly (view message history)
- locations.readonly (view business settings)

Leave write scopes off for now. Later, if you want the AI to add notes or tasks, come back and tick the matching write scopes. Scopes can be edited later without a new token.
You should see the five scopes ticked. Click Create.

## Step 5. Save the token NOW
The token is shown once. It starts with "pit-".
1. Click the copy button.
2. Open your password manager. Make a new entry called "GoHighLevel PIT, [business name]". Paste the token into the password field.
3. Put today's date in the notes. Rotate this token every 90 days (GoHighLevel's recommendation).
4. Tell me "saved". Only then close the page.
Never paste the token into this chat.

## Step 6. Find the Location ID
1. Settings, then Business Profile. Copy the Location ID shown there.
2. Or read the browser address: the text right after /location/ is the Location ID.
Add it to the same password manager entry. It identifies your business account. Keep it out of public code and screenshots.

## Step 7. Connect to the AI

Official endpoint: https://services.leadconnectorhq.com/mcp/ with headers Authorization: Bearer <PIT> and locationId: <Location ID>. Per HighLevel's docs the locationId header is optional; a location can also be named in a prompt. Source: https://marketplace.gohighlevel.com/docs/other/mcp

### Claude Code
Type this yourself in your own terminal. The token stays out of the chat:
```
read -s GHL_PIT      # paste the token, press Enter (nothing shows)
GHL_LOC="PASTE_LOCATION_ID_HERE"
claude mcp add --transport http gohighlevel https://services.leadconnectorhq.com/mcp/ \
  --header "Authorization: Bearer $GHL_PIT" \
  --header "locationId: $GHL_LOC"
```
You should see "Added HTTP MCP server gohighlevel". Run `claude mcp list`: gohighlevel should show as connected.

### Cursor
Open ~/.cursor/mcp.json in an editor. Type this yourself, replacing the placeholders:
```
{
  "mcpServers": {
    "gohighlevel": {
      "url": "https://services.leadconnectorhq.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_PIT_HERE",
        "locationId": "YOUR_LOCATION_ID_HERE"
      }
    }
  }
}
```
Never commit this file to a repository. Restart Cursor.

### claude.ai custom connector
Settings, Connectors, Add custom connector. Enter the URL https://services.leadconnectorhq.com/mcp/. Custom header fields are not available in every version of the form (verify). If there is no header field, use Claude Code or Cursor.

## Verify it works
Ask: "List the 3 most recent contacts in my GoHighLevel."
Pass: three real contact names from your account. Check one on GoHighLevel's Contacts page.

## If it fails
1. 401: the token is expired, mistyped, or from a different sub-account. Check you copied the whole "pit-" token. If unsure, create a new one (Step 3) and update the connection.
2. Empty results: the Location ID is wrong or belongs to another business. Re-copy it from Business Profile.
3. Agency token by mistake: a PIT must come from inside the sub-account (Step 1).
4. Permission error on one action: a scope is missing. Open the integration, tick the scope, save, retry. No new token needed.
5. Server missing from the list: restart the AI app, then run `claude mcp list` again.

## Hard rules for GoHighLevel
- The AI never sends a message, text, or email to a contact.
- The AI never deletes anything without the owner's exact yes for that item.
- A workflow test-fire is not proof. Open the contact record and check the data landed.
- One write lane means one audit trail. Let one tool (the AI or a workflow) write a given field, not both.
- A custom field key must match exactly (case and underscores). A wrong key silently drops the data.

## What the AI may do by default
- Read contacts, deals, calendars, conversations: yes.
- Draft notes, follow-up texts, and emails for the owner: yes.
- Send anything, delete anything, or change a pipeline stage: only with the owner's yes for that item.

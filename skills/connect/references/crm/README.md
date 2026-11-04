# CRM connection walkthroughs

The AI reads one guide aloud, one step at a time, until the connection is verified. Each step is something the owner clicks or types, then what they should see.

## Index

| CRM | Connection method | File |
|---|---|---|
| GoHighLevel | Official MCP server, sign in with your GoHighLevel login (per-AI address: Claude, OpenAI, Cursor). Token path kept as the fallback. Pairs with the `ghl-assistant` skill. | [gohighlevel.md](gohighlevel.md) |
| HubSpot | Official MCP server, sign in with OAuth | [hubspot.md](hubspot.md) |
| Salesforce | Salesforce hosted MCP server, connected app (verify current status) | [salesforce.md](salesforce.md) |
| Pipedrive | Claude connector (marketplace), sign in | [pipedrive.md](pipedrive.md) |
| Zoho CRM | No official MCP found (verify). API client, or Zapier/Make bridge | [zoho-crm.md](zoho-crm.md) |
| Close | Official remote MCP server, OAuth or API key | [close.md](close.md) |
| Follow Up Boss | API key, community MCP or Zapier/Make bridge | [follow-up-boss.md](follow-up-boss.md) |
| Anything else | REST API, webhook, Zapier or Make, or a custom MCP bridge | [other-crm.md](other-crm.md) |

Doing the setup in a live browser with the owner: [live-browser-walkthrough.md](live-browser-walkthrough.md).

## Which CRM do you use?

Ask the owner this, then open the matching file.

1. Do you log in to a page named HighLevel or LeadConnector (or a white-label name) and see "sub-accounts"? Use GoHighLevel.
2. Do you log in at hubspot.com? Use HubSpot.
3. Do you log in at a salesforce.com address? Use Salesforce.
4. Is your pipeline a row of columns with deal cards, at pipedrive.com? Use Pipedrive.
5. Do you log in at zoho.com and see Leads, Contacts, Deals? Use Zoho CRM.
6. Do you log in at close.com? Use Close.
7. Are you a real estate agent or team on followupboss.com? Use Follow Up Boss.
8. None of these? Use other-crm.md.

If the owner is not sure, ask them to read the web address in the browser bar while logged in to the CRM.

## Standing rules (every guide)

1. Go one step at a time. Wait for the owner to say it is done and what they see before the next step.
2. Never ask the owner to paste a token, key, or password into the chat. Tell them where it goes: a terminal command they type themselves, their password manager, an environment variable, or the tool's own secret field.
3. If a token is shown only once, the owner saves it in their password manager before closing the page. Wait for a "saved" from them.
4. Start with read-only access. Add write access later, when the owner asks for it.
5. Never send a message, text, or email to a contact. Draft it; the owner sends it.
6. Never delete anything, and never change a pipeline stage, without the owner's exact yes for that item.
7. Keep tenant IDs (location, portal, org IDs) out of public code, screenshots, and shared logs.
8. Mark anything you could not confirm as "(verify)" and tell the owner to check the vendor's own help page.
9. End every guide with a real test. The connection is done only when the test returns real data.
10. Plain words. Short sentences. Explain any term in one line.

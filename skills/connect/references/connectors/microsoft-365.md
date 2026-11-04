# Microsoft 365 (Outlook mail, calendar, OneDrive)

## 1. What it unlocks

- Drafts replies to your Outlook email. You review and send.
- Reads tomorrow's calendar for meeting prep.
- Finds and reads files in OneDrive and SharePoint that you can already open.

## 2. Before you start

- A Microsoft 365 work or school account. A personal Outlook.com account may not be supported. If it fails, see section 7.
- Microsoft 365 usually needs a tenant admin (the person who runs your company's Microsoft account) to approve the app once. Without them, you may see "Need admin approval".
- A Claude plan that includes connectors. On Team or Enterprise, a Claude admin may need to turn it on too.
- Time: 3 minutes, plus waiting for approval if needed.

## 3. Claude Code (terminal or desktop app)

The Microsoft 365 connector is hosted by Anthropic. It connects only through claude.ai. You cannot add it with `claude mcp add`.

1. Open https://claude.ai/customize/connectors and sign in.
2. Click **Browse connectors**. Find **Microsoft 365**. Click **Connect**.
3. Microsoft asks you to sign in. Use your work account.
4. If a box says **Need admin approval**, click **Request approval** or send the details to your admin. Stop here until they say yes.
5. If you see a list of permissions, click **Accept**.
6. In Claude Code, make sure you are signed in with the same claude.ai account (`/login` if unsure).
7. Type `/mcp`. Microsoft 365 should appear. If it says it needs authorization, select it and follow the browser prompt.

Check with `claude mcp list`. Manage from the claude.ai connectors page.

## 4. claude.ai (web and desktop chat)

1. Settings, then Connectors (https://claude.ai/customize/connectors).
2. **Browse connectors**, choose **Microsoft 365**, click **Connect**.
3. Sign in with your work account. Click **Accept**.
4. In a chat, click the **+** or tools menu. Turn Microsoft 365 on.

The label may differ by version. Look for "Microsoft 365", "Outlook" or "SharePoint".

## 5. Cursor

Microsoft 365 is not offered as a simple URL for Cursor that was verified. If you use Cursor, set this up through claude.ai instead, or check Cursor Settings, then MCP (or Tools & Integrations), for a Microsoft option. If your admin gives you an MCP address, use **Add new MCP server**, which writes `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "microsoft-365": {
      "url": "https://ADDRESS-FROM-YOUR-ADMIN/mcp"
    }
  }
}
```

## 6. Verify it works

- "What is on my calendar tomorrow?" Pass: real events with correct times.
- "Show the senders and subjects of my 3 newest emails." Pass: messages you recognize.
- "Find a file in OneDrive with the word budget in the name." Pass: a real file name.

## 7. If it fails

- **"Need admin approval".** Ask your Microsoft 365 admin to approve the Claude app for your organization. Send them the name Claude and the screen text. They approve once for everyone.
- **Wrong account.** Disconnect on the connectors page. Connect again with your work address.
- **Personal account fails.** The connector is built for work or school accounts. Use a work account, or forward the mail you need to Gmail.
- **Not showing in Claude Code.** `/login` with the same claude.ai account. Then `/mcp`.
- **Worked yesterday, not today.** Sign-in expired. Reconnect from `/mcp`.

## 8. What the AI may do by default

- Read mail, calendar and files you can already open: yes.
- Draft emails and calendar invites: yes. They wait in Drafts.
- Send mail, send invites, share or delete files: only after you say yes to that exact item.
- Messages to customers always need your tap to send.

# Google Workspace (Gmail, Google Calendar, Google Drive)

## 1. What it unlocks

- Drafts replies in your Gmail inbox. You review and send them.
- Reads tomorrow's calendar for meeting prep.
- Finds and reads files in Google Drive, such as proposals and notes.

## 2. Before you start

- Plan: a Claude plan that includes connectors (Pro, Max, Team or Enterprise).
- A Google account. Work accounts may need an admin to allow Claude. On Team or Enterprise Claude plans, a Claude admin may also need to turn the connector on.
- Time: about 2 minutes per Google tool.
- Know which Google account you want Claude to use. Connect the one you use for work.

## 3. Claude Code (terminal or desktop app)

Gmail and Google Calendar are hosted by Anthropic. They connect only through claude.ai. You cannot add them with `claude mcp add`.

1. Open https://claude.ai/customize/connectors in your browser. Sign in to claude.ai.
2. Click **Browse connectors**. Pick **Gmail**, then click **Connect**.
3. Google asks which account. Choose it, then click **Allow**. You should land back on claude.ai with Gmail marked connected.
4. Repeat for **Google Calendar** and **Google Drive**.
5. Open Claude Code. Make sure you are signed in with the same claude.ai account. Type `/login` if unsure.
6. Type `/mcp`. You should see Gmail, Google Calendar and Google Drive in the list.
7. If one says it needs authorization, select it and follow the browser prompt.

To manage connections later, type `claude mcp list`. Connectors added through claude.ai are managed on the claude.ai page, not with `claude mcp remove`.

## 4. claude.ai (web and desktop chat)

1. Go to Settings, then Connectors (https://claude.ai/customize/connectors).
2. Click **Browse connectors**, choose Gmail, Google Calendar or Google Drive.
3. Click **Connect**. Sign in to Google. Click **Allow**.
4. Open a new chat. Click the **+** or tools menu near the message box.
5. Turn the connector on. A toggle or check mark should show.

The menu label may differ by version. Look for "Connectors", "Tools" or a plug icon.

## 5. Cursor

Google's tools are not offered as a plain URL for Cursor. If you only use Cursor, ask Claude to set up the other surface instead, or look in Cursor Settings, then MCP (or Tools & Integrations), for a Google option. If Cursor offers one, use "Add new MCP server". This writes the file `~/.cursor/mcp.json`. A URL entry looks like this (replace the URL with the one your provider gives you):

```json
{
  "mcpServers": {
    "google-example": {
      "url": "https://PROVIDER-URL-HERE/mcp"
    }
  }
}
```

Cursor opens a browser page to sign in the first time you use it.

## 6. Verify it works

Type these one at a time.

- "What is on my calendar tomorrow?" Pass: real events with correct times.
- "Show me the subjects of my last 3 emails." Pass: subjects you recognize.
- "List 3 recent files in my Google Drive." Pass: real file names.

If Claude says it has no access, go to the next section.

## 7. If it fails

- **Wrong Google account.** Disconnect on the connectors page and connect again. Pick the right account in the Google window.
- **"Admin approval needed".** On Team or Enterprise, your Claude admin must allow the connector. On a Google Workspace account, your Google admin may need to allow it. Send them the connector name.
- **Not showing in Claude Code.** Type `/login`. Use the same claude.ai account as the website. Then type `/mcp`.
- **Worked yesterday, not today.** Your sign-in expired. Type `/mcp`, select the connector and reconnect.
- **Connector is on but Claude does not use it.** In claude.ai, check the toggle in the tools menu for this chat.

## 8. What the AI may do by default

- Read email, calendar and files: yes.
- Draft emails and calendar invites: yes. Drafts stay in your Drafts folder.
- Send email, send invites, share files, move or delete anything: only after you say yes to that exact item.
- Never reads or shares passwords, bank details or ID numbers it finds in a message.

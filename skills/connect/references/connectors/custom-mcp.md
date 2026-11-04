# Any other tool (custom MCP server)

MCP stands for Model Context Protocol. An MCP server is a standard plug that lets Claude use a tool. If your tool is not in the other guides, it may still have one.

## 1. What it unlocks

- Connects Claude to a tool such as your CRM, accounting, calendar booking or project tool.
- Lets Claude read your data there and draft updates.
- One setup works every time you open Claude.

## 2. Before you start

- Find the plug. Two places to look:
  - The Anthropic directory: https://claude.ai/directory. Search for your tool's name.
  - The tool's own help pages. Search "YOUR-TOOL MCP server". You want a web address (a URL) that usually ends in `/mcp`.
- Only use servers from the tool's own maker or a source you trust. An MCP server can read your data.
- Plan: connectors need a Claude plan that includes them. On Team or Enterprise, an admin may need to allow custom connectors.
- Time: 2 to 10 minutes.

## 3. Claude Code (terminal or desktop app)

If the tool is in the directory, add it at https://claude.ai/customize/connectors. It then appears in Claude Code when you are signed in with the same claude.ai account. Type `/mcp` to see it and authorize it.

If you have a URL:

1. Type this in your terminal. Replace `name` with a short word and `URL` with the web address:

```
claude mcp add --transport http name URL
```

   Example: `claude mcp add --transport http notion https://mcp.notion.com/mcp`

2. Add `--scope user` after `mcp add` to make it available in every project.
3. Open Claude Code. Type `/mcp`. Select your server. Choose to sign in.
4. A browser page opens. Sign in to your tool. Click **Allow**.
5. `/mcp` now shows it as connected.

If the tool needs a key instead of a sign-in page, it will tell you to add a header. The key goes in the terminal command, typed by you, not in chat. Store it in your password manager first:

```
claude mcp add --transport http name URL --header "Authorization: Bearer YOUR_KEY"
```

Manage: `claude mcp list`, `claude mcp get name`, `claude mcp remove name`.

Note: Gmail, Google Calendar and Microsoft 365 are hosted by Anthropic. They only connect through claude.ai/customize/connectors.

## 4. claude.ai (web and desktop chat)

1. Settings, then Connectors (https://claude.ai/customize/connectors).
2. Click **Browse connectors**. If your tool is there, click **Connect**, sign in, **Allow**.
3. If not, look for **Add custom connector** (the label may differ by version). Enter a name and the URL. Click **Add**.
4. Sign in to the tool when asked.
5. In a chat, click the **+** or tools menu and turn it on.

## 5. Cursor

1. Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server**. This writes `~/.cursor/mcp.json`. Use `~/.cursor/mcp.json` for every project, or `.cursor/mcp.json` inside one project.
2. Add a block with your name and URL:

```json
{
  "mcpServers": {
    "name": {
      "url": "https://YOUR-TOOL-URL/mcp"
    }
  }
}
```

3. If the tool needs a key, add `"headers": { "Authorization": "Bearer ${env:YOUR_KEY_NAME}" }`. Set the environment variable on your computer. Do not type the key into the file or into chat.
4. Save. Cursor opens a sign-in page on first use. A green dot means it is running. A red dot means it failed. Check for a missing comma in the file.

## 6. Verify it works

Ask Claude something only that tool can answer. Examples:

- "List the 5 newest contacts in my CRM."
- "What invoices are overdue?"

Pass: real records from your account. Also type `/mcp` in Claude Code and check the status says connected.

## 7. If it fails

- **404 or "endpoint not found".** The URL is wrong. Copy it again from the tool's help page. It often ends with `/mcp`.
- **Does not support this type of sign-in.** Some servers need a key or a different setup. Read the tool's help page, or ask Claude to search for the right steps.
- **Wrong account.** Remove and add again. Sign in with the right account.
- **Admin approval needed.** On company plans an admin may block custom connectors. Ask them to allow it.
- **Expired.** Type `/mcp`, select the server, reconnect. If still stuck, `/login`.

## 8. What the AI may do by default

- Read what the connection can see: yes.
- Draft changes and messages: yes, shown to you first.
- Create, edit, send, pay or delete: only after you say yes to that exact action.
- Before adding a new tool, Claude tells you what it can reach and who made it.

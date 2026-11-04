# Notion

## 1. What it unlocks

- Reads your pages and databases, such as client notes, SOPs and project trackers.
- Drafts new pages like meeting notes and checklists.
- Updates task statuses and fields when you ask.

## 2. Before you start

- A Notion account. You choose which workspace to share during sign-in.
- On a company workspace, an admin may need to allow connections.
- A Claude plan that includes connectors.
- Time: 2 minutes. No token to copy. You sign in through your browser.

## 3. Claude Code (terminal or desktop app)

Option A, through claude.ai (works if you already use claude.ai):

1. Go to https://claude.ai/customize/connectors.
2. **Browse connectors**, choose **Notion**, click **Connect**.
3. Notion asks which workspace and pages to share. Choose them. Click **Allow access**.
4. In Claude Code, sign in with the same claude.ai account. Type `/mcp`. Notion should appear.

Option B, direct from the terminal:

```
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

1. Add `--scope user` after `mcp add` to use it in every project.
2. In Claude Code, type `/mcp`. Select **notion**. Choose to authenticate.
3. A browser page opens. Pick your workspace. Click **Allow access**.
4. Back in Claude Code, `/mcp` should show notion as connected.

Manage: `claude mcp list`, `claude mcp get notion`, `claude mcp remove notion`.

## 4. claude.ai (web and desktop chat)

1. Settings, then Connectors (https://claude.ai/customize/connectors).
2. **Browse connectors**, choose **Notion**, click **Connect**.
3. Sign in and click **Allow access** in the Notion window.
4. In a chat, click the **+** or tools menu. Turn Notion on.

The menu label may differ by version. Look for "Connectors" or "Tools".

## 5. Cursor

1. Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server**. This opens `~/.cursor/mcp.json`.
2. Add:

```json
{
  "mcpServers": {
    "notion": {
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```

3. Save. Cursor shows a sign-in link. Click it and choose **Allow access** in Notion. A green dot means it is running.

## 6. Verify it works

Type: "Search Notion for a page about CLIENT-OR-PROJECT-NAME and tell me what it says in two lines."

Pass: a real page from your workspace with matching content. Also try "List the titles of 5 pages in my Notion."

## 7. If it fails

- **Page not found.** Notion only shares the pages you picked at sign-in. Reconnect and choose more pages, or share the page with the connection in Notion.
- **Wrong workspace.** Disconnect in `/mcp` or the connectors page and reconnect. Pick the right workspace.
- **Admin approval needed.** Ask your Notion workspace owner to allow the connection.
- **Sign-in window never opens (terminal).** Copy the link Claude Code shows into your browser by hand.
- **Expired.** Type `/mcp`, select notion, reconnect.

## 8. What the AI may do by default

- Read pages and databases it can access: yes.
- Draft new pages: yes, shown to you first.
- Edit existing pages, change statuses, move or delete pages: only after you say yes to that exact change.
- Pages with client details stay in their own space. Claude does not copy them elsewhere without your say.

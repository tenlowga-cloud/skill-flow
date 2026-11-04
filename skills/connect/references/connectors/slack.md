# Slack

## 1. What it unlocks

- Summarizes a busy channel so you catch up in one minute.
- Finds past decisions and files by searching your workspace.
- Drafts messages and replies for you to review before anything posts.

## 2. Before you start

- A Slack workspace where you are a member.
- Many workspaces require an admin to approve new apps. If you are not an admin, ask yours to approve the Claude connector (see section 7).
- A Claude plan that includes connectors.
- Time: 2 minutes, plus waiting for an admin if needed.

## 3. Claude Code (terminal or desktop app)

Anthropic lists a Slack connector in its directory (https://claude.ai/directory). Add it through claude.ai.

1. Open https://claude.ai/customize/connectors.
2. Click **Browse connectors**, find **Slack**, click **Connect**.
3. Slack opens in your browser. Pick the workspace. Click **Allow**.
4. In Claude Code, make sure you are signed in with the same claude.ai account (`/login` if unsure).
5. Type `/mcp`. You should see Slack listed. If it says it needs authorization, select it and follow the browser prompt.

Direct route (optional, if the directory option is missing): Slack publishes its own MCP address, believed to be `https://mcp.slack.com/mcp`. Check Slack's own help pages before using it.

```
claude mcp add --transport http slack https://mcp.slack.com/mcp
```

Then type `/mcp` to sign in. Add `--scope user` to use it in every project. Manage with `claude mcp list`, `claude mcp get slack`, `claude mcp remove slack`.

## 4. claude.ai (web and desktop chat)

1. Settings, then Connectors (https://claude.ai/customize/connectors).
2. **Browse connectors**, choose **Slack**, click **Connect**.
3. Sign in to Slack, pick your workspace, click **Allow**.
4. In a chat, click the **+** or tools menu and turn Slack on.

The menu label may differ by version. Look for "Connectors" or "Tools".

## 5. Cursor

1. Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server**. This opens `~/.cursor/mcp.json`.
2. Add this block (address as above, unverified, check Slack's help pages):

```json
{
  "mcpServers": {
    "slack": {
      "url": "https://mcp.slack.com/mcp"
    }
  }
}
```

3. Save. Cursor opens a browser page to sign in on first use.

## 6. Verify it works

Type: "Summarize the last day of messages in #CHANNEL-NAME." Use a channel you are in.

Pass: a short summary that matches what you see in Slack. Or type "Search Slack for the word invoice" and check that real messages come back.

## 7. If it fails

- **"Admin approval required".** Your Slack admin must approve the app. Tell them: "Please approve the Claude app so I can connect it." Try again after they confirm.
- **Wrong workspace.** Disconnect and connect again. Choose the right workspace in the Slack window.
- **Cannot see a private channel.** Claude only sees what your account can see. Check you are a member.
- **Not showing in Claude Code.** `/login` with the same claude.ai account, then `/mcp`.
- **Worked before, now errors.** Sign-in expired. Reconnect from `/mcp`.

## 8. What the AI may do by default

- Read channels you can already see: yes.
- Draft messages: yes, shown to you first.
- Post, reply, react, edit or delete: only after you say yes to that exact message and channel.
- Messages to customers or outside people are always your tap to send.

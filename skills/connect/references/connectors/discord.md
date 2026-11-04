# Discord

Discord has no Anthropic-hosted connector that was verified for this guide. Check https://claude.ai/directory first. If Discord is listed there, use that and skip to section 4. Otherwise use the options below.

## 1. What it unlocks

- Reads a server channel so Claude can summarize what your team or community said.
- Drafts posts and replies for you to review.
- Lets you message Claude from Discord, if you use the Claude Code Discord channel plugin.

## 2. Before you start

- A Discord account and a server where you can add a bot. That needs the Manage Server permission, or ask the server owner.
- A bot (a robot account you create) from https://discord.com/developers/applications. The page gives you a **bot token**. It is a secret password.
- Time: 10 minutes. This is the longest guide in the set. Ask Claude to walk you through it live with [browser.md](browser.md).

## 3. Claude Code (terminal or desktop app)

Two routes. Pick one.

### Route A: the Discord plugin for Claude Code

1. In Claude Code, type `/plugin` and look for **discord** in the list. The exact name may differ by version.
2. Install it. Then run its configure command. Look for `/discord:configure`. It asks you to save the bot token.
3. Type the token only into that Claude Code prompt or settings field. Never into the chat message box.
4. Use `/discord:access` to approve who may message the bot.

### Route B: a Discord MCP server

1. Pick a Discord MCP server from a source you trust. Check who made it and how many people use it.
2. Add it using the steps in [custom-mcp.md](custom-mcp.md). Most local ones need your bot token in an environment variable. Put it in your computer's settings, not in chat.
3. Type `/mcp` to see it.

Manage: `claude mcp list`, `claude mcp get <name>`, `claude mcp remove <name>`.

### Create the bot (both routes)

1. Go to https://discord.com/developers/applications. Click **New Application**. Name it.
2. Open **Bot**. Click **Reset Token**. Copy it to your password manager.
3. On the same page, turn on **Message Content Intent**. You should see the switch turn on.
4. Open **OAuth2**, then URL Generator. Tick `bot`. Tick Read Messages and Send Messages. Open the link it gives you and add the bot to your server.

## 4. claude.ai (web and desktop chat)

1. Settings, then Connectors (https://claude.ai/customize/connectors).
2. **Browse connectors**. Look for Discord. If it is there: **Connect**, sign in, **Allow**.
3. If not, use **Add custom connector** only if your Discord tool gives you a web address (URL). See [custom-mcp.md](custom-mcp.md).
4. In a chat, click the **+** or tools menu and turn it on.

## 5. Cursor

Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server**. This writes `~/.cursor/mcp.json`. For a Discord server that has a URL:

```json
{
  "mcpServers": {
    "discord": {
      "url": "https://YOUR-DISCORD-MCP-URL/mcp"
    }
  }
}
```

For a local one, Cursor shows a `command` entry instead. The token goes in an environment variable, never typed in chat.

## 6. Verify it works

Type: "Read the last 5 messages in the #CHANNEL-NAME channel and tell me who wrote them."

Pass: names and text that match Discord. Test posting only if you say so. Say "Draft, do not post, a hello for #CHANNEL-NAME."

## 7. If it fails

- **Bot is in the server but sees nothing.** Turn on Message Content Intent. Give the bot access to that channel.
- **Token invalid.** Reset it in the developer page and update the stored one.
- **Plugin shows "connection closed".** Restart Claude Code. Check the token was saved with the configure command.
- **Someone unknown can message the bot.** Use the access command to restrict it to approved people.
- **Bot missing from the server.** Run the OAuth2 invite link again.

## 8. What the AI may do by default

- Read channels the bot can see: yes.
- Draft messages: yes.
- Post, reply, delete, kick or change roles: only after you say yes to that exact action.
- Posts to your public community are always your tap to send.

# Connector walkthroughs

One guide per tool. Each takes a business owner from zero to a working, tested connection. Claude reads the guide and walks the owner through it one step at a time.

## How Claude should use these files

- Give the owner one step at a time. Wait for them to say it worked before the next step.
- Each step is something they click or type, then what they should see.
- Never ask the owner to paste a token, password or secret into chat. Tell them which window or field it goes in.
- Finish with the "Verify it works" test. A connection is not done until the test passes.
- Default rule: read yes, draft yes, send or delete only after the owner says yes.

## The index

| Tool | What it unlocks | File |
|---|---|---|
| Google Workspace (Gmail, Calendar, Drive) | Reads and drafts email, reads your calendar, finds files | [google-workspace.md](google-workspace.md) |
| GitHub | Reads code, issues and pull requests, drafts replies | [github.md](github.md) |
| Slack | Reads channels, summarizes threads, drafts messages | [slack.md](slack.md) |
| Discord | Reads server channels, drafts posts and replies | [discord.md](discord.md) |
| Notion | Reads and edits pages and databases | [notion.md](notion.md) |
| Microsoft 365 (Outlook, Calendar, OneDrive) | Same as Google, for Microsoft accounts | [microsoft-365.md](microsoft-365.md) |
| Obsidian or local notes | Reads your own notes folder | [obsidian-or-local-notes.md](obsidian-or-local-notes.md) |
| Browser (Chrome extension, browser-use, Playwright) | Clicks through websites with you, live | [browser.md](browser.md) |
| Zoom, Google Meet, recorders | Meeting transcripts for meeting prep | [zoom-and-meetings.md](zoom-and-meetings.md) |
| Any other tool (custom MCP) | Connects any tool that offers an MCP server | [custom-mcp.md](custom-mcp.md) |

## Words used in these guides

- **Connector**: a plug that lets Claude reach one of your tools, such as Gmail.
- **MCP server**: the standard type of plug. Most connectors are MCP servers.
- **Claude Code**: Claude in a terminal window, or in the Claude desktop app's Code tab.
- **claude.ai**: Claude in the web browser or the regular desktop chat app.
- **Sign in / authorize**: a browser page from the tool asks you to click Allow. No password goes to Claude.

## Which surface do I use?

- Same claude.ai account everywhere: add connectors once at https://claude.ai/customize/connectors. They show up in Claude Code and claude.ai.
- Cursor has its own list of connections. Set those up separately in each Cursor guide section.
- If unsure, start with claude.ai. It is the easiest path.

## Menu labels

Apps rename menus often. If a label here does not match your screen, look for the closest wording (for example "Connectors", "Integrations", "Tools").

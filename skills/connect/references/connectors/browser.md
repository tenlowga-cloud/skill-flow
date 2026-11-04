# Browser (Claude in Chrome, browser-use, Playwright)

## 1. What it unlocks

- A live walkthrough in Do mode: Claude sees your browser and does the clicking through a setup page while you watch, narrating each move. You handle every sign-in, Allow screen, secret and payment.
- Fills forms and reads web pages that need your login, such as an admin dashboard.
- Checks that a finished setup really works, for example that a webhook or website page loads.

## What a live browser walkthrough is

Claude opens or controls a browser window. It takes a screenshot, tells you what it sees, and does the click or typing for you. When a page asks for a password, a code or a payment, you type it yourself in the window. Claude never types or reads those.

## 2. Before you start

- Google Chrome installed. A Claude paid plan for the Chrome extension.
- No admin rights, unless your company locks extensions.
- Time: 3 minutes.
- Use your normal Chrome profile only if you want Claude to use your logged-in sessions. For a clean test, use a new Chrome profile.

## 3. Claude Code (terminal or desktop app)

### Option A: Claude in Chrome (best for walking through a setup with you)

1. In desktop Chrome or Edge, open https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn and click **Add to Chrome**. Check the publisher is Anthropic. It needs a paid plan (Pro, Max, Ultra, Team or Enterprise), version 1.0.36 or later for Claude Code, and it does not work on phones or other browsers.
2. Click the puzzle-piece icon, pin the extension, and sign in with the same claude.ai account (and organization) that Claude uses.
3. In your terminal, start Claude Code with `claude --chrome`. Or inside a session type `/chrome`. Sign in with `/login`; an API key or a long-lived token will not connect.
4. You should see `/chrome` report Status: Enabled and Extension: Installed.

### Option B: browser-use

1. Install the browser-use plugin in Claude Code (type `/plugin` and search browser-use). The name may differ by version.
2. The first time it connects, Chrome may show an **Allow** box for remote control. Click **Allow**.
3. Claude can then open tabs, take screenshots and click.

### Option C: Playwright (a testing tool; good for repeatable checks)

```
claude mcp add playwright -- npx @playwright/mcp@latest
```

This needs Node.js installed. It opens its own clean browser, with none of your logins. Type `/mcp` to check it shows up.

Manage: `claude mcp list`, `claude mcp get playwright`, `claude mcp remove playwright`.

## 4. claude.ai (web and desktop chat)

1. Install the Claude in Chrome extension as above.
2. Click the extension icon. A side panel opens. Type or speak the task there.
3. Claude acts on the tab you have open.

Labels may differ by version. Look for "Claude" in your Chrome extensions menu. Anthropic's own page: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

## 5. Cursor

Cursor has its own browser tools. To add Playwright: Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server**. This writes `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Save. A green dot means it is running. Node.js must be installed.

## 6. Verify it works

Type: "Open https://example.com in the browser and tell me the main heading on the page."

Pass: Claude says the heading is "Example Domain". For a real test with you: "Open my Google Calendar tab and tell me today's date shown on it."

## How the AI runs a setup with you

1. Claude opens the setup page and says what it sees.
2. In Do mode it says "Opening Settings, then Integrations" and does it. In Talk mode it says "Click Settings, then Integrations" and you do it.
3. At any password, code or payment screen, Claude stops. You type it yourself.
4. After each step Claude takes a screenshot and confirms it matches what should have happened.
5. At the end it runs the "Verify it works" test from the tool's guide.

## 7. If it fails

- **Extension says not connected.** The usual cause is that the extension and Claude are signed in to different accounts or organizations. Sign out of the extension and back in with the same one, restart Chrome, then run `/chrome` and choose Reconnect extension. Run `/status` in Claude Code to see which organization it uses.
- **Chrome "Allow" box never appears.** Look in the Chrome window behind your terminal. Click **Allow**.
- **Playwright fails to start.** Node.js is missing. Install it from nodejs.org and retry.
- **Page asks to prove you are human.** Do the check yourself in the window, then tell Claude to continue.
- **Company computer blocks extensions.** Ask your IT person, or use Playwright with a clean browser.

## 8. What the AI may do by default

- Look at pages, take screenshots, read what is on screen: yes.
- Click through and fill forms for a setup you asked for: yes, narrating each move (Do mode), or one step at a time with you clicking (Talk mode). Saving a form or flipping a switch needs your yes first.
- Buy, pay, submit a final form, send a message, or delete anything: you do these yourself. Claude stops at that screen and waits for you.
- Passwords, codes and card numbers: you type them. Claude does not.

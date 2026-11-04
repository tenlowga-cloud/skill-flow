# GitHub

## 1. What it unlocks

- Reads your code, issues and pull requests (proposed changes) so it can explain them.
- Drafts issue comments and pull request descriptions for you to review.
- Checks whether tests passed on a change before you approve it.

## 2. Before you start

- A GitHub account with access to the repositories you care about.
- Time: 3 to 5 minutes.
- No admin rights needed for your own repositories. For a company organization, the owner may need to approve token access.
- Decide: GitHub CLI path (simplest, if you have `gh`) or the MCP path (a token).

## 3. Claude Code (terminal or desktop app)

### Simple path: the GitHub CLI

1. Check if you have it. In the terminal type `gh --version`. You should see a version number. If not, install from https://cli.github.com.
2. Type `gh auth login`.
3. Choose **GitHub.com**, then **HTTPS**, then **Login with a web browser**.
4. The terminal shows a short code. Copy it. A browser opens. Type the code there and click **Authorize**.
5. The terminal says you are logged in. Claude Code can now use `gh` to read and work with your repositories.

### MCP path (richer tools)

1. Go to https://github.com/settings/tokens and create a **fine-grained personal access token** (a long password for one app). Pick only the repositories you need. Give read access first.
2. Copy it straight into your password manager. Do not paste it into chat. Claude never needs to see it.
3. In your terminal, type this and put your token where it says YOUR_GITHUB_PAT:

```
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

4. Add `--scope user` after `mcp add` to make it work in every project.
5. In Claude Code, type `/mcp`. You should see **github** listed as connected.

Manage it: `claude mcp list`, `claude mcp get github`, `claude mcp remove github`.

## 4. claude.ai (web and desktop chat)

1. Go to Settings, then Connectors (https://claude.ai/customize/connectors).
2. Click **Browse connectors** and look for **GitHub**. The label may differ by version.
3. Click **Connect**, sign in to GitHub, choose the repositories to share, click **Authorize**.
4. In a chat, click the **+** or tools menu and turn GitHub on.

If GitHub is not in the list, use the Claude Code path above, or the custom connector steps in [custom-mcp.md](custom-mcp.md).

## 5. Cursor

1. Open Cursor Settings, then MCP (or Tools & Integrations).
2. Click **Add new MCP server**. This opens `~/.cursor/mcp.json`.
3. Add this block. Cursor can read the token from an environment variable so you do not type it into the file. Ask Claude how to set `GITHUB_PAT` on your computer.

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer ${env:GITHUB_PAT}" }
    }
  }
}
```

4. Save. A green dot next to github means it is running.

## 6. Verify it works

Type: "List my 5 most recently updated repositories."

Pass: real repository names from your account. Then try "Show open pull requests in REPO-NAME" with a repository you own.

## 7. If it fails

- **"Bad credentials" or 401.** The token is wrong or expired. Make a new one, update the connection, run `claude mcp remove github` then add again.
- **Repository not found.** The token was not given that repository. Edit the token's repository list on GitHub.
- **Header badly formatted.** The word Bearer, a space, then the token. No quotes inside the token. No line breaks.
- **`gh` says not logged in.** Run `gh auth login` again.
- **Organization blocks it.** An organization owner must approve the token. Send them the token name, never the token.

## 8. What the AI may do by default

- Read code, issues and pull requests: yes.
- Draft comments and pull request text: yes.
- Post comments, open pull requests, merge, push or delete anything: only after you say yes to that exact action.
- Never shares your token or prints it.

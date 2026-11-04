# Obsidian or a folder of local notes

An Obsidian vault is just a folder of Markdown files (plain text files ending in `.md`). Any folder of notes works the same way.

## 1. What it unlocks

- Reads your notes to prep for a meeting, a client call or a decision.
- Searches everything you have written, by topic or by person.
- Saves new notes and summaries into the folder, in your format.

## 2. Before you start

- Know where the folder lives on your computer. In Obsidian: Settings, then About, shows the vault path. Or right-click the vault folder and choose to reveal it.
- No admin rights. No account. Nothing leaves your computer except what Claude reads in a chat.
- Time: 2 minutes for Claude Code. 5 for the other surfaces.
- If your notes sit in a sync folder (iCloud, Dropbox, OneDrive), use the local copy.

## 3. Claude Code (terminal or desktop app)

Claude Code reads files directly. No connector needed.

1. Open a terminal. Move into your notes folder. For example type `cd ~/Documents/MyVault` (use your own path).
2. Type `claude` to start Claude Code in that folder.
3. Claude can now read, search and edit files in that folder and below it.
4. Using the desktop app instead: open the Code tab and choose the folder when it asks.
5. To also let Claude see a second folder, type `/add-dir /path/to/other-folder` inside Claude Code.

Optional: put a file named `CLAUDE.md` in the folder. Write a few plain lines about how your notes are organized. Claude reads it first each time.

## 4. claude.ai (web and desktop chat)

Pick one.

**Option A, upload to a Project.** Easiest.
1. In claude.ai, click **Projects**, then **New project**. Name it.
2. Click **Add content** (the label may differ), then upload files or paste text.
3. Open chats inside that Project. Claude can use those files. Re-upload when notes change.

**Option B, Desktop Commander or a filesystem MCP.** Lets chat read your folder live. Needs the Claude desktop app.
1. Open the Claude desktop app. Settings, then Extensions (or Developer, depending on version).
2. Search for **Desktop Commander** or **Filesystem**. Click **Install**.
3. Follow its prompt to allow your notes folder. Allow only that folder.
4. Start a new chat. The tool should show in the tools menu.

## 5. Cursor

1. In Cursor, choose File, then Open Folder. Pick your notes folder. Cursor can then read the files with its built-in tools.
2. Optional: add a filesystem MCP. Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server**. This writes `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "notes": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/your/notes"]
    }
  }
}
```

This needs Node.js installed. Ask Claude to check before you add it.

## 6. Verify it works

Type: "List the 5 most recently edited notes in this folder and give each a one-line summary."

Pass: real file names from your folder, with summaries that match what is in them. Then try: "Find every note that mentions NAME-OF-A-PERSON."

## 7. If it fails

- **"No such file or folder".** The path is wrong. Drag the folder into the terminal window to paste the correct path.
- **Claude only sees part of the notes.** You started it in a sub-folder. Start in the top folder.
- **Desktop Commander cannot see the folder.** Add the folder in its allowed folders setting, then restart the app.
- **Project is out of date.** Re-upload the changed files.
- **Cloud-only files look empty.** Make the folder "available offline" in your sync app, then try again.

## 8. What the AI may do by default

- Read and search your notes: yes.
- Draft new notes and summaries: yes, as new files. It shows you the name first.
- Edit, rename, move or delete existing notes: only after you say yes to that exact file. Keep a backup or version history on.
- Never copies private or client notes to another tool without your yes.

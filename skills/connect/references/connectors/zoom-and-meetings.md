# Zoom, Google Meet and meeting recorders

The goal: after a meeting, the written transcript lands somewhere Claude can read. Then meeting prep can pull what was said last time.

## 1. What it unlocks

- Prepares you for the next meeting using notes and promises from the last one.
- Turns a transcript into a follow-up email draft and a to-do list.
- Finds what a client said weeks ago.

## 2. Before you start

- Pick where transcripts will live. Easiest options, in order:
  1. A recorder app with its own Claude connector (Plaud has one).
  2. Google Drive (Google Meet saves transcripts there).
  3. A local notes folder (see [obsidian-or-local-notes.md](obsidian-or-local-notes.md)).
- Zoom: transcripts need a paid Zoom plan with cloud recording turned on. The host or an account admin may need to switch on "audio transcript" in Zoom settings.
- Google Meet: transcripts need a Google Workspace plan that includes them. Admin may need to allow it.
- Always tell people in the meeting you are recording. Check your local rules.
- Time: 5 to 10 minutes.

## 3. Claude Code (terminal or desktop app)

### Google Meet (transcript goes to Drive)

1. In a Meet call, click the three dots, then **Record meeting** or **Transcript**. Start it. The label may differ by version.
2. After the call, the transcript saves as a document in the host's Drive, in a folder called **Meet Recordings**.
3. Connect Google Drive: follow [google-workspace.md](google-workspace.md).
4. In Claude Code type `/mcp` and check Google Drive is listed.

### Zoom

1. In Zoom on the web, open Settings, then Recording. Turn on **Cloud recording** and **Audio transcript**.
2. After a meeting, the transcript appears in your Zoom recordings list as a `.vtt` file. Download it into your notes folder.
3. Zoom may offer an official connector in the Claude directory at https://claude.ai/directory. If it appears, add it at https://claude.ai/customize/connectors, then `/mcp` in Claude Code.

### Plaud or another recorder

1. If the recorder has a Claude connector, add it at https://claude.ai/customize/connectors. Sign in with the recorder's account and click **Allow**.
2. If not, turn on its auto-export to Google Drive, Notion or a folder. Connect that place using its guide.
3. In Claude Code, type `/mcp`. The recorder should be listed if it has a connector.

## 4. claude.ai (web and desktop chat)

1. Settings, then Connectors (https://claude.ai/customize/connectors).
2. **Browse connectors**. Connect Google Drive, your recorder, or both.
3. In a chat, click the **+** or tools menu and turn them on.

Or: open a Project and upload transcript files there. See [obsidian-or-local-notes.md](obsidian-or-local-notes.md).

## 5. Cursor

Cursor reads transcripts that are in your open folder. Save transcripts to a folder, open it in Cursor. For a recorder with a URL address, Cursor Settings, then MCP (or Tools & Integrations), then **Add new MCP server** writes `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "recorder": {
      "url": "https://RECORDER-MCP-URL-HERE/mcp"
    }
  }
}
```

Use the address from the recorder's own help page.

## 6. Verify it works

1. Hold a short test meeting with yourself. Say a sentence like "The purple kite is due Friday."
2. Wait for the transcript to appear. It can take a few minutes up to an hour.
3. Type: "Find my most recent meeting transcript and tell me what was said about the kite."

Pass: Claude names the right meeting and quotes the sentence.

## 7. If it fails

- **No transcript was created.** Recording or transcript was off. Turn it on before the next call.
- **Transcript is in someone else's Drive.** Meet saves it to the host's Drive. Ask the host to share the folder with you.
- **Claude cannot find it.** The transcript may still be processing. Wait and retry. Check the folder name.
- **Wrong account.** Reconnect with the account that owns the recordings.
- **Admin approval needed.** Your Zoom or Google admin controls transcripts. Ask them to turn them on.

## 8. What the AI may do by default

- Read transcripts it can reach: yes.
- Draft summaries, follow-up emails and to-do lists: yes.
- Send a follow-up, post a summary to a channel, share a recording, or delete a file: only after you say yes to that exact item.
- Client conversations stay in their own place. Claude does not copy them to another tool without your yes.

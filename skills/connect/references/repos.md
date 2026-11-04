# Repos and folders: let the AI see where things live

The flow reads `PROFILE.md`, Where things live. If a repo or folder named there is not readable from the session, nothing built on it works. This guide closes that gap.

## A code repository

**Claude Code on the owner's machine.** Start Claude Code from inside the repo folder (`cd <folder>` then `claude`), or add it to an open session with `/add-dir <path>`. Verify: ask "what is in the README of this repo?" and get real content.

**A repo not on the machine yet.** The owner clones it themselves (the credentials are theirs):

```
git clone <url> <folder>
```

If `git clone` asks for a password, GitHub wants a token or SSH key, not the account password. Easiest: install the GitHub CLI and run `gh auth login`, then clone again. Never paste a token into chat.

**Claude Code in the cloud (claude.ai/code).** The repo is attached to the session or the environment, not cloned by hand. In the session, the owner asks to add the repo by its `owner/name`; the session attaches it if the Claude GitHub App is installed on it. If not, they install the app at https://github.com/apps/claude and choose the repository, then ask again.

**Cursor.** File, Open Folder, pick the repo. Cursor reads `.cursor/rules/` and `AGENTS.md` from it.

**Verify:** read one file the owner named in `PROFILE.md` and quote its first line back.

## A notes vault or folder of Markdown

**Claude Code.** `/add-dir <vault path>` in the session, or start Claude Code in the vault. Add the path to `PROFILE.md`, Where things live, and name the first page to read.

**claude.ai.** Upload the key pages to a Project, or connect the folder through a filesystem connector (`connectors/obsidian-or-local-notes.md`).

**Cloud sessions.** Put the vault in a repository the session can attach, or keep a small `profile/` folder in the kit's repo with the pages the routines need.

**Verify:** read the first page and say what it is about in one line.

## A new repo for the owner's skills, templates or profile

When `blueprint` builds skills and templates that should travel with the owner:

1. Create the repo on their code host (the owner clicks Create; name it, private by default).
2. Clone it next to this kit, add the skills folder, commit, push. The owner runs the push the first time so the credentials are theirs.
3. Add the path to `PROFILE.md` and `STACK.md`.
4. Never commit a profile file with contact details, a client's name or a secret. `profile/*.md` stays gitignored in this kit for that reason; follow the same rule in theirs.

## Rules

- The owner clones and pushes the first time. The AI never holds their credentials.
- One owner per repo in `PROFILE.md`: the code host, the organization, the repo name. Enough to find it, nothing more.
- A repo the AI cannot read is "not connected" in `TOOLS.md`, with the one step that fixes it.

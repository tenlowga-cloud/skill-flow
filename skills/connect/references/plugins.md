# Plugins: install one, start to finish

A plugin is a folder of skills, commands, hooks and agents that Claude Code installs as one unit. Install at user scope unless the owner says the plugin is for one project only.

## impeccable (install for every owner on Claude Code)

What it unlocks: a design bar for anything a person sees. `/impeccable critique` scores a screen, `audit` checks accessibility, performance and responsive behavior, `polish`, `adapt` and `harden` finish it, and it flags generic AI-made patterns before they ship. The flow calls it on every page, app, document or slide a person will look at.

Steps. The owner types each line in Claude Code and waits for it to finish:

1. `/plugin marketplace add pbakaus/impeccable`
   They should see: `Successfully added marketplace: impeccable`.
2. `/plugin install impeccable@impeccable`
   A details pane opens. They pick **Install for you (user scope)**. If the pane says `Run /reload-plugins to apply`, Claude Code runs it; if it warns about the cache, they run `/reload-plugins --force`.
3. Verify: type `/` and look for `/impeccable`. Then `/impeccable init` once in a project with a UI, which writes its design notes file.
4. Record it in `STACK.md`.

Shell path for a setup script: `claude plugin marketplace add pbakaus/impeccable` then `claude plugin install impeccable@impeccable`.

If the marketplace name differs from `impeccable` on their version, read it from `claude plugin marketplace list` and use that name after the `@`.

Other surfaces: claude.ai and Cursor have no plugin install for this. Say what it does and that `pixel-proof` carries the visual check there. The project's own `npx impeccable install` also works from a project root and offers a design hook.

## Any plugin from Anthropic's official marketplace

Claude Code adds that marketplace on the first interactive session. The owner runs `/plugin`, reads the **Discover** tab, and installs by name: `/plugin install <name>@claude-plugins-official`. Read the details pane with them: **Will install** lists what it adds, **Context cost** says what it costs on every turn. Do not install a plugin whose cost outweighs the jobs it serves.

## A plugin from any other marketplace

1. `/plugin marketplace add <owner>/<repo>` (GitHub), or the full git URL, or a local path starting with `./`.
2. `/plugin install <plugin>@<marketplace-name>`.
3. One line: `/plugin install <plugin> --marketplace <owner>/<repo>` does both (Claude Code v2.1.275 or later).

Before installing from a marketplace the owner does not know: open the repo, read what the hooks run. A plugin runs as the owner.

## Manage

- See what is installed: `/plugin`, Installed tab, or `claude plugin list` in the shell.
- Turn one off without removing it: Installed tab, Space on the row, or `claude plugin disable <name>@<marketplace>`.
- Update: Installed tab, Update now, or `claude plugin update <name>@<marketplace>`.
- Remove: Installed tab, Uninstall, or `claude plugin uninstall <name>@<marketplace>`.
- A plugin installed but not working: `/plugin`, Errors tab, then the troubleshooting page it names.

Cloud sessions (claude.ai/code in the browser) do not load the plugins installed on the owner's machine. Say so when the owner works there; the skills in this kit still run when the repo carries them.

## Verify any plugin

Type `/` and find `/<plugin>:<skill>`. Run one skill on a real target. A pass is the skill's own output, not a message that it loaded. Record the plugin in `STACK.md` with the date.

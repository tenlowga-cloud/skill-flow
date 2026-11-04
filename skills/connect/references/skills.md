# Skills: add one the owner needs

A skill is a folder with a `SKILL.md` that tells the AI how to do one kind of job well. Claude Code reads them from `~/.claude/skills/<name>/` (every project) or `.claude/skills/<name>/` (one project). claude.ai takes each skill folder as a zip under Settings, Capabilities, Skills.

## Find one that exists

1. The session's own skill list. It may already be there under a plugin name (`plugin:skill`).
2. Anthropic's official marketplace: `/plugin` in Claude Code, Discover tab, type to search.
3. The owner's own folder from `PROFILE.md`.
4. A public skills repository the owner trusts. Read the `SKILL.md` before installing; a skill can run scripts.

## Install one

- **From a plugin:** `plugins.md`.
- **From a folder or repo:** copy or clone the skill folder to `~/.claude/skills/<name>/`. Keep the folder name equal to the `name` in its frontmatter. Verify: type `/` and find `/<name>`, or ask for the job and watch it load.
- **claude.ai:** zip the folder (the folder, not just the file), upload under Settings, Capabilities, Skills, then start a chat and ask for the job.
- **Cursor, Codex, others:** paste the `SKILL.md` into the rules file the surface reads (`docs/other-ais.md`).

Add it to `ROUTER.md`: one row, when it runs, what it is called. Then `STACK.md`.

## Build one

When nothing fits and the ask keeps coming back, write it. The shape this kit uses:

```
~/.claude/skills/<name>/
  SKILL.md          frontmatter: name, description (when to trigger, in the owner's words, under 1,024 characters)
                    body: what it does, the steps, the gate, what good looks like, under 150 lines
  references/       anything long: templates, checklists, examples
  scripts/          only if a script makes the job reliable; say what it needs to run
```

Rules for a skill written for the owner:

- Reads the profile files by this kit's wording. Never hardcodes a name, path or tool the profile already holds.
- Anything a person other than the owner reads goes through `ghost-mode`. Anything on a screen goes through `impeccable` and `pixel-proof`.
- No secrets, client data or contact details inside the skill.
- Test it once on a real prompt. Fix it until the output matches the owner's bar. Then add it to `ROUTER.md`.

`blueprint` builds the first set. `connect` adds one at a time after that.

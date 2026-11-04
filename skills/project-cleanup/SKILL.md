---
name: project-cleanup
description: Phased cleanup of a codebase or project folder with the same behavior and goals and less clutter. Use when the owner says "clean up this project", "cleanup pass", "declutter", "simplify this codebase", "this project is a mess", "too many files", "condense the docs" or "remove dead code", or asks to audit a project for stale files, redundant docs or unused code (phases 0 and 1 only). Not for new features or one-off edits.
---

# Project Cleanup

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

Same functionality, same goals, less clutter. This is careful demolition with a safety net, not creative work.

Two rules:

1. **Never lose information.** Facts, goals, decisions, credential notes and completed-work records survive every rewrite. Deleting a file is fine; deleting knowledge is not.
2. **Never change behavior.** If a change cannot be proved neutral, do not make it.

If the owner asked only for an audit, stop after Phase 1. If they asked for the cleanup, run through every phase with reversible, evidence-backed changes and no approval ritual between phases. Ask up front, as 1 to 4 short questions in one message (your pick first, marked "(Recommended)"), about any destructive target they have not named or a choice that changes the outcome. Then run. Deleting the owner's work you can't undo is a gate; the gates in `PROFILE.md` apply too. Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`.

When the owner is away, log each phase's evidence in a running report, skip uncertain items, and queue any destructive action that was not clearly authorized. The final summary (short, per the owner's length rule in `VOICE.md`, detail in the report file) lists what was done, skipped and still gated.

## Phase 0: Safety and survey

- **Git.** Check `git status` if the project is under git. Preserve all existing changes and work around them. Do not init git, commit, stash or switch branches unless the request or project workflow includes it. For extra recovery, keep temporary copies of only the files you change.
- **Secrets scan, before any commit.** A committed credential stays in history even after the file is deleted. Look for `.env` files, filenames containing `key`, `secret` or `credential`, and patterns like `api_key`, `token=`, `password` and `-----BEGIN` in config files. Add live credentials to `.gitignore` before any `git add` and flag them in the report. Credential notes in docs (such as "the billing email is X") are facts to keep, not secrets to hide.
- **Scope.** Do not clean or inventory generated or vendored content: `node_modules/`, `venv/`, `__pycache__/`, `dist/`, `build/`, `.cache/`, lockfile-managed vendor dirs, bulk media and data. One line per directory is enough ("assets/ - 400 product images, untouched"). Add ignore rules only if that is in scope. If the project is still too large, pick the highest-impact bounded subtree from the request and record the assumption.
- **Baseline.** Find the test suite, build, lint step or documented manual run, run it, and record the exact result (pass counts, exit codes, output). If none exists, use the cheapest safe smoke check (for example, the script runs `--help`) and state its limits.
- **Golden outputs.** A thin test suite does not prove behavior. For each runnable entry point with sample input (CLI script, report generator), save the exact output outside the project (for example `/tmp/golden/`). After every later change, re-run and diff; anything not byte-identical gets reverted.
- **Inventory.** Classify every source and doc file:
  - Active: referenced, imported or clearly part of the current workflow.
  - Stale: unreferenced, superseded, or an obvious leftover (old drafts, `_v2` twins, dead experiments).
  - Unclassifiable: keep, always.

  Staleness needs evidence: grep for references, trace entry points, compare timestamps. "Looks old" is not evidence.

## Phase 1: Report

Write four lists, one or two lines per entry, then proceed with proved, in-scope items unless a destructive target or scope choice is still gated.

- **DELETE.** Each entry carries a line of proof it is unused ("nothing imports it", "superseded by X"). No proof means CANNOT CLASSIFY.
- **SIMPLIFY (docs).** Each doc with its current length and what to cut or merge. Completed-work records, goals and direction docs are condensed, never dropped; every fact must stay findable.
- **SIMPLIFY (code).** Each refactor, why it is safer or simpler, and how behavior will be proved unchanged.
- **CANNOT CLASSIFY.** Anything uncertain. Default is keep; this list shows where the owner's call is needed.

## Phase 2: Docs

Rewrite the docs shorter and plainer with nothing repeated across files. For every cut, ask whether someone could still find that goal, decision, credential note or completed-work fact afterward. If not, keep it. If commits are part of the delivery, commit docs separately from code so either reverts alone; otherwise leave verified changes local.

## Phase 3: Code

Change one file or module at a time and re-run the Phase 0 verification after each. If anything fails or differs, undo only your own change with a focused patch and record it. Do not fix forward, since a fix is a behavior change. Never disturb unrelated work.

- No new dependencies and no API or behavior changes.
- No improvements beyond the list; note ideas for the wrap-up.
- Dead code goes only if it was on DELETE.
- When commits are authorized, make small commits with clear messages.

## Phase 4: Wrap-up

Run the verification once more; it must match the baseline. Then report files deleted (count and names), lines removed, docs condensed (before and after sizes), refactors applied, and anything flagged but left alone, including deferred ideas.

---
name: pixel-proof
description: "Use when fixing anything visual from a screenshot or verbal UI report: the user pastes a screenshot path and says fix/remove/move/resize this, or reports \"looks broken on my phone\", \"popup shows up at the bottom\", \"text is cut off\", \"spacing is off\", \"it started at -7\". Also use before claiming ANY UI change is done, and when the user comes back with \"try again\", \"still broken\", \"you didn't fix it from the phone view\"."
---

# pixel-proof: no UI fix is done until you've seen the pixels

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

**Core rule:** claim a fix only after YOU rendered the changed page and looked at it, at phone width AND desktop width, on the surface the user actually uses. "The CSS is correct" is a prediction, not proof.

Read `PROFILE.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). If it is missing, say so once and ask the one question you need, or run `setup`.

Quality bar: the quality bar in `PROFILE.md` (default: right the first time, complete, proven, no homework for the owner). A fix that works but looks cluttered, template-made or hard to use is not done. Look at the pixels and score them: one point, less, energy, premium, time back, one tap. Ship at 9 or higher.

If a UI design pass is needed, use the UI design pass in `ROUTER.md`, if the owner has one.

## The loop

### 1. Reproduce before touching code
Open the page in a browser tool (see `TOOLS.md` for what is connected). Find the element from the screenshot in the live DOM. If you can't reproduce it, ask for the URL and steps in one short question. Do not "fix" what you haven't seen.

### 2. Find every occurrence
The screenshot shows one instance. Grep the project for the pattern (class, component, copy string). If it's on five pages, the user means all five.

### 3. Fix
Prefer removing or simplifying over adding. Less UI is the target.

### 4. Prove it (non-negotiable)
- Render on a **preview or staging URL** for the changed branch. A local file proves nothing about production, and that gap causes most "try again" turns.
- Deploying to production just to verify is a gate in `PROFILE.md`. It needs the owner's exact one-time yes and a rollback path. Never deploy to production for a screenshot.
- Hard-reload or cache-bust. Stale cache causes "I just hard refreshed and it started at -7".
- Screenshot at **390x844 (phone)** and **1440x900 (desktop)**. Phone is not optional.
- Compare each screenshot to the original ask, element by element.
- Dynamic behavior (counters, popups, animations, login states): exercise it. Reload N times if flakiness was reported. Click the flow. Check logged-in and logged-out if auth matters.

### 5. Report with evidence
Say what changed, which pages, and what you SAW at both widths ("footer now inside viewport at 390px, screenshot taken"). If anything still looks off, say so yourself. Keep it short; the owner's length rule is in `VOICE.md`. Default when unset: lead with the answer, then the catch, then the next step. Detail goes in the screenshot or a link.

## When you cannot render (no browser tool, embedded iframe, auth wall)

Say exactly that: "Changed X. Could NOT visually verify because Y. Check Z on your phone." Never imply a check that didn't happen. A labeled unverified fix costs one turn. A fake "done" costs three.

## Red flags: stop, you're about to bounce this back

- "The CSS change is trivial, no need to look"
- "I verified locally" (and the user looks at production)
- "The screenshot only showed desktop, so mobile is out of scope"
- "Tests pass" (there are no visual tests)
- "I fixed the instance they pointed at" (without grepping for siblings)
- Claiming a counter or animation works without watching it run

Each one causes a real "try again" or "still broken" turn. All of them mean: open the browser and look.

## Quick reference

| Situation | Minimum proof |
|---|---|
| Static layout/copy change | Screenshots at 390px + 1440px on the preview/staging URL |
| "Broken on my phone" | Reproduce at 390px FIRST, then fix, then re-screenshot |
| Counter/animation/flaky | Watch it run; reload 5-10x if start-state was the bug |
| Popup/modal position | Trigger it at both widths, screenshot open state |
| Multi-page element | Grep count of occurrences = pages verified |
| Can't render surface | Explicit "not visually verified because ___" |

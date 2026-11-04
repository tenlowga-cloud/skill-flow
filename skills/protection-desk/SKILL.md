---
name: protection-desk
description: Fires the moment a quote appears: an insurance quote, illustration, declaration page, rate sheet, renewal notice or pasted premium numbers, as a PDF, an image or text. Runs the Protection Desk workflow end to end (intake and audit, the client-ready deck or document in the owner's brand, the readability and reader gates, the impeccable design pass) and prints the PDF, without being asked. When a cheaper competing quote is in the room, builds the price-versus-cost comparison side by side. If the Protection Desk is not installed, walks the owner through installing it. Use on any quote drop, "turn this quote into a document", "protection review", "preview for this client", "what would this cost", "they found it cheaper", "/protection-desk".
---

# protection-desk

Part of [skill-flow](../../README.md). The `flow` skill decides when this runs; `setup` fills the profile files it reads.

A quote in the owner's hands is a client waiting. This skill turns it into a printed, client-ready document the same hour, following the Protection Desk's own rules. The desk is a separate tool (a folder of Python and Markdown the owner installs once); this skill is the trigger and the bridge.

## 1. Recognize the drop

Any of these, with no other prompt, means run:

- A PDF, image or scan with carrier names, coverage amounts, premiums, riders, deductibles or an illustration table.
- A declaration page, renewal notice or rate sheet.
- Pasted text with a premium and a coverage amount ("$500k, 20 year, $42 a month").
- A call transcript or notes where a client asked what coverage would cost.
- Two quotes, or one quote plus "they found it cheaper", "a competitor quoted", "can you beat this": that is a price-versus-cost comparison (`references/price-vs-cost.md`) on top of the Review.

Say in one line what you see ("a term life quote for two people, one carrier") and that you are starting the desk. Do not ask whether to.

## 1b. Brand first

Read `BRAND.md` from your skill-flow profile folder (`~/.claude/skill-flow/` in Claude Code, else `profile/` in this repo). No `BRAND.md`: run `setup`'s brand intake (`../setup/references/brand-intake.md`) before building anything a client sees; a document in the wrong colors is a document the owner cannot send. Then make sure the desk has a matching brand folder (`brands/<key>/brand.json` filled from `BRAND.md`, `"brand": "<key>"` in `desk.local.json`). The design bar (`references/design-bar.md`) governs how the brand is used on every page.

## 2. Check the desk is installed

Look for the desk folder: `~/.claude/skills/protection-desk/` (Windows: `C:\Users\<you>\.claude\skills\protection-desk`), or the path in `STACK.md`. Inside it, `desk.py` and its own `SKILL.md`.

Not there: go to "Install" below, finish it, then come back. Never improvise a document without the desk; its gates are the point.

The desk is Python on a computer. It runs in Claude Code or in Cowork on the desktop app, not in a web or phone chat. A quote dropped into a web chat: say so in one line, read the quote and report what it contains (carrier, coverage, premium, term, anything odd) so the owner has the picture now, then tell them to open Cowork or Claude Code and drop it again for the document. Never build the document by hand in chat.

## 3. Run the desk's own flow

Open the desk's `SKILL.md` and follow it exactly. It is the authority on the document; this skill only gets you there. In short:

1. **Doctor.** `python desk.py doctor` from inside the desk folder. Every line must say PASS. A FAIL prints its fix; apply it and re-run.
2. **Intake.** Quotes: `python desk.py intake <files> --case <slug>`. Transcript or notes: write the facts file the desk asks for, then intake it. Read the audit it prints to the owner before writing a word: misspelled names, age drift, single versus couple, whose producer is on the paper.
3. **Write.** Author the deck or document config the desk specifies, from the intake only. Problems and solutions lead; products serve them; money appears once, last, small. Every "why it matters" line is the client's own worry or a fact they gave. The value the owner brings (what is handled, what is covered on the day it is used, what the client never has to think about again) is said plainly in the client's terms, not as a feature list. Every dollar figure traces to the intake (a Review) or the desk's own calculators (a Preview). Never do the math yourself. Never mix a quoted number and an estimate in one document. A competing quote: follow `references/price-vs-cost.md` for the side-by-side, the dollarized cost, and the honest psychology.
4. **Build and gate.** `python desk.py build <config> --reader 3`. Gate 1 (readability) must pass. Gate 2 (the fifth-grade reader) gets up to three rounds; rewrite what it flags. A build with `--reader 0` comes out named `_UNREVIEWED` and is not handed to a client.
5. **Design pass.** Render every page to PNG (`pixel-proof`), then run `impeccable` on them per `references/design-bar.md`: critique and score, audit, polish, harden, the AI-tells sweep, the brand check. Under 9 of 10: fix the worst gap, rebuild, re-score. Locked blocks keep their text; the pass styles, never edits. No `impeccable` on this surface: run the critique yourself against the design bar and say so.
6. **Print.** The build writes the color PDF and the print PDF to the desk's out folder. Open the PDF and check every page: no overflow, every number matches the source, disclosure present, brand colors exact, legal name exact. Render it into the chat so the owner sees it, with the design score.
7. **File.** Copy to where `PROFILE.md` says client documents live. Never to a shared drive the owner did not name.
8. **Learn.** `python desk.py learn`.

Then say it back in three lines: the document, the catch (an audit item, a reader flag, a number that needs the owner's eye), the next step.

## 4. Hard stops

- Never invent or round a number. A Review carries only transcribed figures; a Preview carries only engine ranges.
- Never name an insurance company in a Preview.
- Never hand a client an `_UNREVIEWED` document or rename one to hide it. Never hand a client a page that scored under 9 on the design pass or carries an AI tell from the design bar's list.
- Never disparage a competing carrier. A comparison states both quotes' numbers exactly and says so when the cheaper one fits.
- Client files stay in the desk's `work/` folder and the owner's own systems. Nothing from them goes into this kit, a log or a shared room.
- The owner sends the document to the client. You never do.

## Install

The Protection Desk is licensed separately. The owner gets it from its maker as a folder or a repository. Walk the install in teaching mode (`../setup/references/teaching-mode.md`): one step per message, define "terminal" and "Python" the first time, say what they should see after each command, wait for "done". Then:

1. Put the folder at `~/.claude/skills/protection-desk/` and keep that folder name. If it came as a repository, clone it there (`connect/references/repos.md`).
2. Open a terminal in that folder and run `python desk.py doctor`. Walk each FAIL with its printed fix: Python 3.10 or newer, Poppler (`pdftotext`), a PDF renderer (Chrome or Edge), the `claude` command for the reader, `pypdf` for the clean-room test.
3. Run `python tests/test_desk.py` once. It uses synthetic data only and takes about a minute.
4. Copy `desk.local.example.json` to `desk.local.json`; set the brand key and the out folder. Build the brand folder from `BRAND.md` (`../setup/references/brand-intake.md`, "Lock it in"): copy `brands/example/` to `brands/<key>/`, drop in the logo, fill every field in `brand.json`, no placeholder left. Fill the owner's state in `calc/care_costs.json` from a current Cost of Care survey, with the source named, or the first real case will stop and say which state is empty.
5. Build the sample: `python desk.py build examples/sample_deck.json --reader 0 --out out/demo`. Two PDFs with `_UNREVIEWED` in the name appear. Open one; that is the shape.
6. Record the path in `STACK.md` and `TOOLS.md`.

Then re-run step 1 of this skill on the quote that started it.

## For owners outside insurance

If `PROFILE.md` says the owner has nothing to do with insurance or financial protection, a PDF with numbers on it is not a quote drop. Tell `flow` to route it to the skill that fits (a proposal, an invoice, a contract) and mark this skill "do not call" in `ROUTER.md` so it stays quiet.

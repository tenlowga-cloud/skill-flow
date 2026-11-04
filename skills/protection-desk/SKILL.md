---
name: protection-desk
description: Fires the moment a quote appears: an insurance quote, illustration, declaration page, rate sheet, renewal notice or pasted premium numbers, as a PDF, an image or text. Runs the Protection Desk workflow end to end (intake and audit, the client-ready deck or document, the readability and reader gates) and prints the PDF, without being asked. If the Protection Desk is not installed, walks the owner through installing it and running its doctor until every check passes. Use on any quote drop, "turn this quote into a document", "protection review", "preview for this client", "what would this cost", "/protection-desk".
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

Say in one line what you see ("a term life quote for two people, one carrier") and that you are starting the desk. Do not ask whether to.

## 2. Check the desk is installed

Look for the desk folder: `~/.claude/skills/protection-desk/` (Windows: `C:\Users\<you>\.claude\skills\protection-desk`), or the path in `STACK.md`. Inside it, `desk.py` and its own `SKILL.md`.

Not there: go to "Install" below, finish it, then come back. Never improvise a document without the desk; its gates are the point.

## 3. Run the desk's own flow

Open the desk's `SKILL.md` and follow it exactly. It is the authority on the document; this skill only gets you there. In short:

1. **Doctor.** `python desk.py doctor` from inside the desk folder. Every line must say PASS. A FAIL prints its fix; apply it and re-run.
2. **Intake.** Quotes: `python desk.py intake <files> --case <slug>`. Transcript or notes: write the facts file the desk asks for, then intake it. Read the audit it prints to the owner before writing a word: misspelled names, age drift, single versus couple, whose producer is on the paper.
3. **Write.** Author the deck or document config the desk specifies, from the intake only. Every dollar figure traces to the intake (a Review) or the desk's own calculators (a Preview). Never do the math yourself. Never mix a quoted number and an estimate in one document.
4. **Build and gate.** `python desk.py build <config> --reader 3`. Gate 1 (readability) must pass. Gate 2 (the fifth-grade reader) gets up to three rounds; rewrite what it flags. A build with `--reader 0` comes out named `_UNREVIEWED` and is not handed to a client.
5. **Print.** The build writes the color PDF and the print PDF to the desk's out folder. Open the PDF and check every page: no overflow, every number matches the source, disclosure present. Render it into the chat so the owner sees it.
6. **File.** Copy to where `PROFILE.md` says client documents live. Never to a shared drive the owner did not name.
7. **Learn.** `python desk.py learn`.

Then say it back in three lines: the document, the catch (an audit item, a reader flag, a number that needs the owner's eye), the next step.

## 4. Hard stops

- Never invent or round a number. A Review carries only transcribed figures; a Preview carries only engine ranges.
- Never name an insurance company in a Preview.
- Never hand a client an `_UNREVIEWED` document or rename one to hide it.
- Client files stay in the desk's `work/` folder and the owner's own systems. Nothing from them goes into this kit, a log or a shared room.
- The owner sends the document to the client. You never do.

## Install

The Protection Desk is licensed separately. The owner gets it from its maker as a folder or a repository. Then:

1. Put the folder at `~/.claude/skills/protection-desk/` and keep that folder name. If it came as a repository, clone it there (`connect/references/repos.md`).
2. Open a terminal in that folder and run `python desk.py doctor`. Walk each FAIL with its printed fix: Python 3.10 or newer, Poppler (`pdftotext`), a PDF renderer (Chrome or Edge), the `claude` command for the reader, `pypdf` for the clean-room test.
3. Run `python tests/test_desk.py` once. It uses synthetic data only and takes about a minute.
4. Copy `desk.local.example.json` to `desk.local.json`; set the brand key and the out folder. Fill the owner's state in `calc/care_costs.json` from a current Cost of Care survey, with the source named, or the first real case will stop and say which state is empty.
5. Build the sample: `python desk.py build examples/sample_deck.json --reader 0 --out out/demo`. Two PDFs with `_UNREVIEWED` in the name appear. Open one; that is the shape.
6. Record the path in `STACK.md` and `TOOLS.md`.

Then re-run step 1 of this skill on the quote that started it.

## For owners outside insurance

If `PROFILE.md` says the owner has nothing to do with insurance or financial protection, a PDF with numbers on it is not a quote drop. Tell `flow` to route it to the skill that fits (a proposal, an invoice, a contract) and mark this skill "do not call" in `ROUTER.md` so it stays quiet.

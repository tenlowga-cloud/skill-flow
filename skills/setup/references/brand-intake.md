# Brand intake: logo, colors, fonts, guidelines

Everything a client will ever see from this owner (a quote, a proposal, a post, a page) has to look like it came from their business and from the future at the same time. That needs the brand on file before the first document. Teaching mode, one step per message. About eight minutes.

## 1. Ask for what exists

"Do you have any of these? A logo file, brand guidelines (a PDF or page that says your colors and fonts), a website, business cards or a brochure. Send me whatever you have, even one thing. Nothing is fine too; we will build from your website or from scratch."

Where files land: Claude Code and Cowork, into `brand/` inside the profile folder (`~/.claude/skill-flow/brand/`). claude.ai chat: into the skill-flow Project's knowledge. Record the paths in `BRAND.md`, Sources.

## 2. Read the brand

From the guidelines, if any: legal name as it must print, colors with hex values, font names, logo rules, anything forbidden. Quote, do not paraphrase.

From the logo, if no guidelines: sample the main colors (name the hex), note the shape (wordmark, mark, both), note whether a reversed version exists. Say what you found: "Your logo is navy and a warm gold. The navy is #1B2A4A. Is that right, or do you have an exact value?"

From the website, if that is all: read the visible colors and fonts from the page. Mark them "sampled from the website".

Nothing at all: build a starter from the industry and the owner's words ("warm, trustworthy, modern" becomes a palette and a type pair), show it, and mark every value "starter, owner approved" once they say yes. A starter brand is better than a different look on every document.

## 3. Check it against the design bar

Read `skills/protection-desk/references/design-bar.md`. Hold each piece against it:

- **Colors.** Keep the brand's colors; they are the brand. Pick the one that becomes the single accent and the one that becomes the primary. Measure body text contrast on paper; if it fails 7:1, darken the ink shade and say so. Never swap a brand color for a trend.
- **Fonts.** This is where most brands are dated. If the brand font is a system default (Arial, Times New Roman, Calibri, Cambria), a decorative or script face, a 2000s web face, or anything that reads as a template, mark it "upgrade" and recommend a close, licensable sibling from the design bar's type list: same mood, modern cut, real italics, tabular figures for numbers. Show the owner one line in each: "Here is your heading in your current font, and here it is in the one I recommend." Ask one question: keep yours, or upgrade? Record the answer. If the brand font already meets the bar, say so and keep it.
- **Logo.** Check it has a transparent background and a version that works on dark. Missing either: say what is missing and how to get it (ask their designer, or export from the source file). Never redraw a logo.

## 4. Write BRAND.md

Fill `skills/profile/references/BRAND-template.md` into the profile folder (or hand it to the owner for the Project on claude.ai). Every value marked with its source. Show the owner the colors and the type pair rendered once (a small artifact or image: name, tagline, a heading, a line of body text, a number) and ask one question: "Does this look like your business?" Fix what they correct.

## 5. Lock it in

- **Protection Desk:** if installed, create `brands/<key>/` from `brands/example/` with `brand.json` filled from `BRAND.md` (agency name, logo path, palette, the standard panel in the owner's words, the producer block from `PROFILE.md`), set `"brand": "<key>"` in `desk.local.json`, build the sample once and open the PDF with the owner. The desk refuses to build while a placeholder remains, so finish every field.
- **impeccable:** run `/impeccable init` in the owner's project where it exists and point its design notes at `BRAND.md`. On surfaces without it, `BRAND.md` is what `pixel-proof` and the design bar read.
- **prospect-mover, creative-direction, content, blueprint templates:** they read `BRAND.md` by name. Nothing else to do.

Record in `STACK.md`: brand on file, source, fonts kept or upgraded, date.

## Rules

- Never invent a brand value. Sampled is marked sampled; starter is marked starter.
- The owner's legal name prints exactly as the guidelines or their license says. Ask once if unsure.
- Never alter a logo. Never place it on a photo or a gradient.
- One accent color per page. The brand may have five colors; the page uses two and the ink.
- Fonts must be licensable for commercial print and web. Prefer open licenses (Google Fonts, SIL OFL) or fonts the owner already owns.

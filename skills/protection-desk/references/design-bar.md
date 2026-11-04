# The design bar: documents from 2090, in the owner's brand

Every quote, proposal, review, post, one-pager or page a client sees from this kit is held to one bar: it should look like the most expensive firm in the industry sent it from the future, and it should be unmistakably the owner's business. "Good enough" is a fail. "Looks like AI made it" is a fail. The bar is checked, not felt: `impeccable` scores it, `pixel-proof` renders it, and nothing ships under 9 of 10.

`BRAND.md` in the profile folder owns the colors, logo and type. This file owns how they are used.

## What 2090 looks like, concretely

- **Paper and air.** Generous margins, one idea per page or slide, whitespace doing the work borders used to do. No boxed cards with thick colored outlines, no icon tiles, no decorative dividers.
- **One accent.** The brand primary carries structure (headings, rules). One accent color appears once or twice per page, on the number or the action that matters. Everything else is ink on paper.
- **Type that carries authority.** A display face with real character for headings, a quiet text face with true italics for body, tabular figures for every number. Sizes in a clear scale (one display, one heading, one body, one caption). Never more than two families.
- **Numbers as the hero.** A dollar figure gets room, weight and a one-line meaning under it. Tables are rules and alignment, not grids and fills.
- **Editorial, not brochure.** Headlines say the client's problem in their words. Copy is short, specific, human (`ghost-mode`). No stock photos, no clipart, no emoji, no icons unless the brand has its own set.
- **Print and screen both.** US Letter or A4 fixed pages for PDF, phone width for anything on a screen. Fonts embedded. Black ink prints clean in grayscale.
- **The brand everywhere, loudly nowhere.** Logo once on the cover and small in the footer. Legal name exact. Producer block exact. Colors from `BRAND.md`, never a near match.

## AI tells that fail the bar

Any one of these fails the page until fixed:

- Purple-to-blue or multi-stop gradients; glassmorphism; glowing cards.
- Three-column icon-and-blurb rows; rounded tiles with pastel fills.
- Generic hero copy ("Unlock your potential", "Peace of mind for your family"); any sentence a stranger could have written for any business.
- Centered everything; equal-weight everything; no hierarchy.
- System fonts (Arial, Calibri, Times) or the default sans of the renderer.
- Emoji, clipart, stock photos of handshakes or families on beaches.
- A disclosure or footer that drifts in style from the page.
- Em dashes in copy (the kit's voice rule); exclamation marks; "only".

## Type upgrades (when the brand font is dated)

Keep the mood, modernize the cut. All licensable (Google Fonts or SIL OFL) unless noted.

| Brand font reads as | Mood to keep | Recommend for display | Recommend for text |
|---|---|---|---|
| Times New Roman, Georgia, Cambria | classic serif, trusted | Cormorant Garamond, Playfair Display, Fraunces | Source Serif 4, Literata, Newsreader |
| Arial, Helvetica, Calibri, Verdana | plain sans, neutral | Manrope, Space Grotesk, Instrument Sans | Mulish, Source Sans 3, Figtree |
| Montserrat, Raleway, Lato (2010s web) | friendly geometric | Outfit, Plus Jakarta Sans, Sora | Figtree, Nunito Sans, DM Sans |
| A script or decorative face | warmth, personality | keep it for the logo only; headings in Fraunces or Cormorant Garamond | Mulish or Source Serif 4 |
| A condensed or industrial face | strength, trades | Barlow Condensed, Oswald (headings only) | Barlow, IBM Plex Sans |
| Monospace or tech | precision, software | Space Grotesk, IBM Plex Sans | IBM Plex Sans, Mulish |

Numbers always get tabular figures. If the text face has none, numbers go in the display face or in IBM Plex Sans. Inter and Roboto are left off this table on purpose: impeccable's detector flags them as overused, so recommending them would fail the kit's own pass.

Show the owner one line in the old and the new before changing anything. Record kept or upgraded in `BRAND.md`.

## The pass, every document

1. **Build** with the brand (`BRAND.md`, the desk's `brands/<key>/brand.json`).
2. **Render** to PNG per page (`pixel-proof`): phone width too if it will ever be on a screen.
3. **impeccable critique** on the rendered pages (or the HTML before PDF): score, ranked gaps. Under 9: fix the worst gap, rebuild, re-score. Then **audit** (contrast, overflow, orphaned headers, misaligned pairs), **polish**, **harden** (long names, big numbers, missing logo, grayscale print). Where a style fix lives: in the desk, only `brands/<key>/brand.json` (palette, fonts, logo, panel copy) or the desk's own theme or CSS file if the desk exposes one; never its page templates, its locked blocks (disclosure, estimate banner, producer footer) or any copy that came from the intake. Outside the desk, in the owner's `BRAND.md` and the template being built. A gap that cannot be fixed from those places is reported to the owner with the exact file it would need, not patched in a template.
4. **Tells sweep**: read the page as a stranger against the list above. One hit fails.
5. **Brand check**: colors match `BRAND.md` hex for hex; legal name exact; logo untouched; one accent per page.
6. **Record** the score and the fixes in the document's notes file for the owner. The owner sees the PDF rendered in chat, three lines, and the score.

Where `impeccable` is not installed (Cursor, a web chat without the plugin), run the critique yourself against this file's lists, score it honestly, and say in one line that the plugin would have scored it too.

## Where it applies

- Every Protection Desk Preview, Review and deck, and the price-versus-cost comparison (`price-vs-cost.md`).
- Every social post, one-pager, proposal, quote, flier or page `prospect-mover`, `creative-direction`, `blueprint` templates or `content` produce.
- Anything else a person outside the team will see on a page or a screen (`flow` standing trigger).

## What does not move

- Locked blocks (the desk's disclosure, estimate banner, producer footer) keep their text exactly; the design bar styles them, never edits them.
- Numbers come from the desk's intake and engines, never from this pass.
- Brand colors are the brand's. The bar changes how they are used, not what they are.

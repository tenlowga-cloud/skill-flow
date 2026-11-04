# Price versus cost: when a cheaper quote is in the room

The price is what they pay today. The cost is what they pay later if they choose on price alone. They are not the same number, and most people have been taught to look only at the first one. This document is how the owner's quote and the cheaper quote go side by side, with the gap dollarized and the human truth said plainly, without a single manufactured fear.

Runs inside the Protection Desk when the client brings a competing quote, says "I found it cheaper", or the owner says "they have a quote from X". Also feeds `prospect-mover` for the conversation around it.

## Rules before the first word

- **Only transcribed numbers.** Both quotes are read and copied exactly, per the desk's Review regime. Nothing estimated sits beside a quoted figure. Unreadable: ask.
- **Fair to the other quote.** Name its carrier and its numbers exactly. Never disparage a carrier. State differences as facts from the two documents ("their policy renews annually; yours is level for 20 years"), never as opinions about a company.
- **Suitability outranks winning.** If the cheaper quote is the right fit for this client's facts, the comparison says so and the owner hears it first. A comparison that always finds the owner's quote better is a sales sheet, not advice.
- **Say unknown.** A difference you cannot see in the documents (claims service, financial strength) is named as "worth checking" with where to check, never asserted.
- **No urgency that is not true.** Age-based repricing and insurability are real and may be stated plainly. Nothing else is.
- **The owner sends it.** This is a client-facing document: brand locked, design bar passed, owner's yes before it leaves.

## 1. Read both quotes

Intake both through the desk (`desk.py intake <both files> --case <slug>`). Build the comparison table from the intake only:

| Row | Owner's quote | Other quote |
|---|---|---|
| Carrier (exact) | | |
| Product and term or structure | | |
| Coverage amount | | |
| Monthly premium | | |
| Annual premium | | |
| Rate guarantee period | | |
| What happens at the end of the guarantee (renewal terms, verbatim) | | |
| Conversion or extension rights | | |
| Riders included (each, verbatim) | | |
| Exclusions and waiting periods (verbatim) | | |
| Underwriting class assumed | | |
| Carrier financial strength rating, if printed | | |

Every cell is a transcription or "not stated". Then write the **price gap** (monthly and annual difference) as one number. That is the only number the client has been looking at. The rest of the document is about everything else.

## 2. Find the cost

For each row where the quotes differ, ask: what does this difference cost the client in the year it matters? Dollarize only where the desk's engines or the quotes' own numbers allow; otherwise describe the gap in one plain sentence and mark it "not priced".

Typical places the cost hides:

- **The guarantee ends sooner.** A 10-year level term beside a 20-year one: show the renewal premium the cheaper policy prints for year 11, if printed, beside the owner's year-11 premium. If not printed, "the premium at year 11 is not shown; the policy says it is set at renewal."
- **Less coverage.** Same premium, smaller face: the survivor-need gap from the desk's calculator (a Preview-regime number, labeled as such, shown only in the scenario section, never beside quoted figures).
- **A missing rider.** Waiver of premium, child rider, chronic illness, conversion: name what it would have done in the scenario the client already worried about.
- **Renewability or conversion lost.** The right to convert without new underwriting is worth the most to the person whose health changes. Say that in one sentence, with their own words about health or family history if they gave any.
- **Exclusions and waiting periods.** Verbatim, side by side.
- **Class assumed.** A quote priced at Preferred Plus for someone the facts put at Standard is not cheaper; it is unissued. Say so plainly: "this price assumes a health class the application may not reach."

Then one line: **the total cost picture.** Price gap over the guarantee period, against the dollarized or described costs. Honest arithmetic, no rounding in the owner's favor.

## 3. The human truth (the psychology, used honestly)

People do not buy on logic alone, and they should not be sold on fear. Use what is true about how people decide, to help them see the second number.

- **Loss aversion.** A loss hurts about twice as much as a gain feels good. Put the loss in their words: not "you save $14 a month" but "in the year this matters, the difference is [X] that your family does not receive." Then let it sit. One sentence.
- **Future self, present discount.** We treat our future self like a stranger. Make the future concrete and near: a date, an age, a child's grade in school. "In 2036, when Maya is 16" beats "at renewal."
- **Anchoring, reversed.** They anchored on the monthly price. Re-anchor on the number the policy exists for: the coverage amount, or the survivor need. Beside a $500,000 reason, a $14 difference reads differently. Never inflate the anchor.
- **Regret minimization.** The question people ask themselves later is not "did I save money" but "did I make the right call for them." Ask it now, gently, as the client's own question: "Which of these would you want to have chosen, on the day it is used?"
- **The cheapest leaves you with lesser, later.** True in insurance more than most things, because the product is a promise paid in the worst year. Say the plain version once: "The lower price today is real. So is what it leaves out. You are not choosing a price; you are choosing what is there on the day you need it."
- **Certainty.** Tie every claim to a number on the page. Confidence comes from the arithmetic being visible, not from tone.
- **Small yes.** End one step from a decision, not at it: "Want me to show you what the 20-year version costs at your exact class?" The desk's straight-line rules (`references/straight_line.md` in the desk) govern the close: calm, small, honest, no loop on a stated no.

Never: scarcity that is not real, a deadline that is not real, a story about another client that is not theirs, a comparison that hides a row where the other quote wins.

## 4. The document

Build it in the desk as a Review (both sets of numbers are quoted) with the comparison as its own section, in this order:

1. **What you are comparing.** Both quotes named, the price gap as one line, in the client's words why they are looking.
2. **Side by side.** The table from step 1. Rules and alignment, one accent on the row that matters most to this client.
3. **Price and cost.** The step 2 findings, one per short paragraph, each tied to a row above. Dollarized where allowed, labeled where estimated, "not priced" where honest.
4. **The day it is used.** One scenario the client already raised, walked through under each quote. No new worries invented.
5. **What we recommend, and why.** One paragraph. If the cheaper quote fits, this says so.
6. **One next step.** Small, calm.

Design: `design-bar.md`, brand from `BRAND.md`, impeccable pass, 9 of 10 or it does not ship. Voice: `ghost-mode`, then the client-sim gate the desk already runs. Until the desk's deck contract has a native comparison section, the table and findings go in the Review's "Worth Talking About" and scenario sections with both carriers' numbers labeled by quote; never as priced cards for the other carrier.

## 5. The conversation

For the owner, not the client: a half-page talk track per the desk's talk-track rules (local, never filed). Open on the client's reason for looking, show the gap number, show the cost rows, ask the regret question, one small ask. Plus the three objections most likely from this comparison and a one-line, true answer to each.

## What good looks like

Client brings a $38 a month 10-year term beside the owner's $52 a month 20-year term, same face. The document shows the $14 gap once, then the year-11 renewal the cheaper policy prints ($212 a month), the conversion right the cheaper one lacks, and the client's own sentence about their father's heart history. The recommendation says the 20-year fits, and why, in four lines. The owner reads it in two minutes and sends it. The client reads it in three and books the call.

If instead the two quotes are the same term, same riders, same class, and the other carrier is simply $14 cheaper: the document says that, recommends the client take it or asks the owner's carrier to match, and the owner keeps a client who trusts them.

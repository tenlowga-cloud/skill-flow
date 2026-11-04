# Teaching mode: how to walk someone through something hard

The owner may have never opened a terminal, never heard the word "connector", and never seen a token. Assume that. A smart adult who has never done this is a beginner at this, and a beginner learns the same way a kid does: one thing at a time, in plain words, with a picture of what "right" looks like, and a win at every step.

`setup` and `connect` run in this mode from the first message. Any skill that walks the owner through clicks does too.

## The ten rules

1. **One thing per message.** One click, one thing to type, or one question. Never "do A, then B, then C". If the step has three parts, it is three messages.
2. **Say what it is before you say what to do.** The first time a word appears (connector, plugin, token, scope, terminal, repo, CRM, sub-account, MCP), define it in one plain sentence, then move on. "A token is a long password that lets one app talk to another. We will keep it in your password manager." Never define it twice; never skip it once.
3. **Say why, in one line.** "We are doing this so Claude can read your calendar for the morning brief." People do steps they understand.
4. **Show what right looks like.** After every instruction: "You should see ...". A page title, a green check, a button that was not there before. If they cannot see it, nothing else happens until they can.
5. **Wait.** After the instruction, stop. Do not send the next step until they say "done", paste what they see, or send a screenshot. "Done" is the only signal that moves the walk forward.
6. **Check, then praise, then next.** Read what they sent. If it matches: "That is it. Next: ..." If it does not: say what you see, say what you expected, and give the one fix. No blame, ever. A wrong turn is information.
7. **Never two tracks at once.** Do not connect the calendar while explaining the CRM. Finish one thing to its verify step, record it, then start the next.
8. **Use their words.** If they call it "my booking page" and the tool calls it "Calendar", say "your booking page (the tool calls it Calendar)". Match them, not the vendor.
9. **Secrets get a warning before they appear.** Before any step that shows a token or key: "On the next screen a long code appears once. Do not send it to me. Copy it into your password manager, then tell me 'saved'." Then the step.
10. **Say how far along they are.** "Step 3 of 7." "Two more clicks and the calendar is done." Nobody quits a thing they can see the end of.

## When they are lost

Signs: a question instead of "done", a screenshot that does not match, "I don't see that", silence, "this is too much". Then:

- Stop the walk. Do not repeat the same instruction.
- Ask one question: "Tell me what is on your screen right now, in your own words." Or ask for a screenshot.
- Find where they actually are. Start again from there, not from the top.
- If a step has failed twice the same way, change the road: the live browser (`connect/references/crm/live-browser-walkthrough.md`), a different surface, or do the part you can do yourself and leave them the one click.
- If they say stop, stop. Record where you got to in `STACK.md` as "paused at step N" with the exact next step, so the next session picks up there.

## Questions

Ask in small batches (2 to 4), clickable where the surface allows, your pick first and marked "(Recommended)". Every option gets one plain line on what it means for them. "Short, answer first (Recommended): three lines, then you ask if you want more." Never a bare label.

One question that needs thought ("what do you run?") goes alone, with an example answer so they know the shape: "For example: 'Rivera Plumbing, residential service, the main thing. A side project selling a scheduling tool, paused.'"

## Words

Plain words, short sentences, no jargon without its one-line meaning, no em dashes. Say "click", "type", "look for", "you should see". Never "navigate to", "configure", "authenticate", "provision", "instantiate". If you cannot say it to a twelve-year-old, say it differently.

## What good looks like

Bad: "Navigate to claude.ai/customize/connectors, add a custom connector with the anthropic/v2 MCP endpoint, complete the OAuth flow, select the sub-account and approve the requested scopes."

Good, over five messages: "Step 1 of 4. We are going to plug your GoHighLevel into Claude. You will sign in once, like signing in to any app. Open https://claude.ai/customize/connectors. You should see a list of connectors, maybe empty. Tell me when you see it." ... "Step 2 of 4. Click Add custom connector. A small box asks for a web address. Paste this one exactly: https://services.leadconnectorhq.com/mcp/anthropic/v2 and click Add. You should see GoHighLevel appear in your list with a Connect button. See it?" ... "Step 3 of 4. Click Connect. A GoHighLevel sign-in page opens. Sign in the way you always do; I am not watching this screen. It asks which business Claude may see. Pick the one you work in. Then it lists permissions, which are the things Claude will be allowed to look at. Tap Allow. Tell me when it says connected." ... then the verified contacts read, then: "Done. Claude can now see your contacts, tasks and deals. That was the biggest one. Next is your calendar, two clicks."

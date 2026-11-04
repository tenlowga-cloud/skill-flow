# Run the CRM setup in a live browser, together (Do mode)

The default once the browser is proven. Claude drives a browser the owner can watch and does the clicks. The owner handles the parts that involve a login, a consent screen or a secret. Read `skills/setup/references/teaching-mode.md`, "Who does the clicking", first.

## What you can use
- Claude in Chrome extension: the owner installs it and signs in (`skills/setup/references/account-check.md`, section 3b). The AI works in the owner's own Chrome, in a tab group it opens.
- browser-use: the AI controls a Chrome the owner can watch.
- Playwright: the AI opens a visible (not hidden) browser window.
If none works, fall back to Talk mode: the written guide, one step per message.

## Prove it first
Open https://example.com in a new tab, read the main heading back to the owner, close the tab. On Claude Code, `/chrome` shows Enabled. Pass: say "I can drive your browser now, so I will do the clicking and tell you what I am doing. Say 'slow down' any time and I go back to one step at a time." Fail: say why in one line and stay in Talk mode.

## The hard rules
1. The AI never types a password, code, token or card number, and never screenshots or reads a page while a secret is visible.
2. The owner never pastes a token into the chat. It goes straight into the password manager.
3. The AI never clicks Allow, Authorize, Accept, Pay, Send, Delete, Publish or Submit for the owner. The one exception is one save per guide, the one the guide names (save this connector URL, save this scheduled task), said out loud before the click. Account switches are flipped only after the owner's yes for that page.
4. The AI acts only on sites the guide names. When the extension asks permission for a site, the owner decides.
5. The owner's gates hold exactly as before.

## Roles
| The AI does | The owner does |
|---|---|
| Opens each page | Logs in (password, 2-step code) |
| Clicks through menus, tabs and forms the guide names | Reads and approves any Allow or consent screen |
| Fills non-secret fields and saves the one form the guide names | Copies a token straight into the password manager |
| Reads each screen and checks it matches the guide | Pays, accepts terms, or changes a plan |
| Narrates one line per move | Says "done" after each hand-over, or "slow down" |

## The loop
1. Say the step and what it is for in one line: "Step 3 of 7. Adding the connector so Claude can see your calendar."
2. Do it: navigate, click, fill. Narrate each move in plain words.
3. Check the screen against the guide: the page title and main heading, not any secret.
4. Hand over when the next move is a login, a consent screen, a secret, a payment or a gate. Say plainly what is on screen and why you stopped. Wait for "done".
5. If the screen does not match the guide, stop clicking, say what you see, and use the guide's "If it fails" list, in Talk mode for that step.

## When a token appears
1. Say: "A token is on screen. Do not click away yet. I am not looking at this page."
2. Do not capture screenshots or read the page text until the token is gone. Pause capture if the tool allows it.
3. The owner copies the token into the password manager entry and says "saved".
4. Only then continue. If the owner closed it too soon, the guide says how to make a new one.

## Check each screen
- Read titles and headings, not secrets. Skip fields marked as secrets, keys or tokens.
- Do not read cookies, saved passwords or autofill fields.
- Crop out or avoid IDs (location, portal, org) in any screenshot that will be kept or shared.

## After the setup
1. The owner types any connection command in their own terminal, or sets the secret in the connector form, as the guide says.
2. Run the guide's "Verify it works" test prompt. A pass is real names that match the CRM.
3. Close the tabs the AI opened. Do not close tabs the owner opened.

## If the tool cannot see the page
1. Ask the owner to read the heading aloud.
2. Fall back to the written steps, one at a time (Talk mode).
3. Never ask the owner to share their screen with a token visible, and never ask for the token itself.

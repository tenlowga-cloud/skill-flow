# Run the CRM setup in a live browser, together

Use this when the owner would rather be shown than told. The AI drives a browser the owner can see. The owner does the parts that involve a login or a secret.

## What you can use
- Claude in Chrome extension: the owner installs it and signs in. The AI works in the owner's own Chrome.
- browser-use: the AI controls a Chrome the owner can watch.
- Playwright: the AI opens a visible (not hidden) browser window.
If none is installed, fall back to the written guide and read it aloud.

## The two hard rules
1. The AI never types a password or token, and never screenshots a page while a token is visible.
2. The owner never pastes a token into the chat. It goes straight into the password manager.

## Roles
| The AI | The owner |
|---|---|
| Opens each page | Logs in (password, 2-step code) |
| Points at the exact button | Clicks anything with a login, a consent screen, or a secret |
| Reads the screen to check it | Copies the token to the password manager |
| Says what comes next | Says "done" or what they see |

## The loop (repeat for every step)
1. Say the step in one sentence. "Now click Settings at the bottom left."
2. Point at it. Use the tool to highlight or scroll to the button, and say where it is on the screen.
3. Let the owner click when it involves a login, consent, or a secret. The AI may click harmless menu items when the owner agrees.
4. Check the screen. Read the page title and the main heading. Confirm it matches what the guide says you should see.
5. Only then give the next step. If the screen is different, stop, say what you see, and use the guide's "If it fails" list.

## Start
1. Ask: "Is your browser open and logged in to your CRM?" If not, open the CRM login page and wait. The owner logs in; the AI looks away.
2. Open the right guide (see README.md) and follow its steps in order.
3. Say: "I will tell you before each click. If a screen shows a secret, I will not look."

## When a token appears
1. Say: "A token is on screen. Do not click away yet. I am not taking a picture of this page."
2. Do not capture screenshots or read the page text until the token is gone. Pause screen capture if the tool allows it.
3. The owner copies the token into the password manager entry and says "saved".
4. Only then close the page or let the AI continue. If the owner closed it too soon, the guide says how to make a new one.

## Check each screen
- Read titles and headings, not secrets. Skip fields marked as secrets, keys, or tokens.
- Do not read cookies, saved passwords, or autofill fields.
- Crop out or avoid IDs (location, portal, org) in any screenshot that will be kept or shared.

## After the setup
1. The owner types the connection command in their own terminal, or sets the secret in the connector form, as the guide says.
2. Run the guide's "Verify it works" test prompt. A pass is real names that match the CRM.
3. Close the tabs the AI opened. Do not close tabs the owner opened.

## If the tool cannot see the page
1. Ask the owner to read the heading aloud.
2. Fall back to the written steps, one at a time.
3. Never ask the owner to share their screen with a token visible, and never ask for the token itself.

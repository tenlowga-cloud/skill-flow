# Inbox triage rules

Read PROFILE.md (priorities, gates, send window, who counts as a client) and VOICE.md before you start.

## Core rules

1. **A draft is never sent.** The owner taps send. No exceptions unless PROFILE.md gates say a specific kind of message may go automatically, and then only inside the send window.
2. **VOICE.md governs every draft.** Its samples and banned words win over anything here.
3. **One line per thread** in the summary: who, what they want, what you did.
4. **Morning pass lists at most 10 items.** Say how many more are waiting.
5. **Flag first**: anything about money, legal matters, or a client complaint goes at the top of the list, marked FLAG, even if it is not the newest.
6. Never delete. Never unsubscribe on the owner's behalf without a yes. Archive only receipts and newsletters, never a client thread.
7. Never open links or attachments in suspected phishing. Never reply to it.
8. If email is not connected, say so and stop.

## Buckets

| Bucket | What it is | Action |
|---|---|---|
| Reply now | The owner must answer today. A client, a quote, a deadline, a question blocking work. | Draft ready. List first. |
| Reply later | Needs an answer, not urgent. | Draft ready. Say when it can wait until. |
| Waiting on them | The owner wrote last and needs an answer back. | Track. Feeds the follow-up sweep. |
| FYI | Good to know, no action. | One-line summary. Archive after listing. |
| Receipts and notices | Invoices, confirmations, shipping, account alerts. | File under the Receipts label. Mention bills due soon to the bills routine. |
| Newsletters | Bulk mail, promos, digests. | Skip. Add sender to a "maybe unsubscribe" list in the summary. |
| Spam or phishing | Fake invoices, urgent "verify your account", odd senders, mismatched links. | Flag. Move to spam only with the owner's yes. Never click. |

When a thread fits two buckets, take the higher one on the list (Reply now beats FYI).

## Reply now tests (any one is enough)

- From a client or a lead in the CRM.
- Contains a date or deadline within 2 days.
- Asks a direct question to the owner.
- Mentions a problem, a complaint, a refund, a cancellation, or a legal or money term.
- From someone in the VIP list in PROFILE.md.

## Labels or folders the AI may create

Create only these, only if the mail tool allows it. Keep names plain.
- `Reply now`
- `Reply later`
- `Waiting`
- `FYI`
- `Receipts`
- `Newsletters`
- `Flagged`

Do not rename or delete the owner's own labels. Do not touch labels you did not create.

## Summary format sent to the owner

```
Inbox, <time> pass. <n> new. Reply now: <n>. Later: <n>. Waiting: <n>.
FLAG
1. <Name>: <what, one line> [draft ready]
REPLY NOW
2. ...
REPLY LATER
...
FYI: <one line each, max 5>
Not listed: <n> receipts, <n> newsletters, <n> spam.
```

## Follow-up sweep rules

- A thread counts as quiet when the owner sent the last message and 3 business days (Monday to Friday, skip holidays in PROFILE.md) passed with no reply. The default is 3. PROFILE.md may set another number.
- Skip threads marked done, closed, or that the owner replied "no need" to.
- Skip anyone PROFILE.md says not to chase.
- Skip threads where the last message was an out-of-office reply until the return date.
- Max 3 nudges to the same person. After that, tell the owner and stop drafting.
- Each result: who, what was asked, days quiet, draft nudge (see draft-patterns.md). Draft only.
- Oldest first. Quote value or deadline if known.

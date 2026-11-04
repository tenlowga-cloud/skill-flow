# ROUTER

`setup` fills this file. It maps what the owner says or means to the skill, plugin or agent that handles it. The `flow` skill reads it before choosing.

## Routes

One row per request type. "Call" is the skill, plugin or agent name. Notes say when it applies or what to pass.

| When the owner says or means | Call | Notes |
|---|---|---|
| "Write the follow-up email to a client" | the writer agent, then `VOICE.md` check | Owner approves before it sends |

## Do not call

Skills or plugins that are installed but must not run on their own. Say why.

| Name | Why not |
|---|---|
| (retired skill name) | Replaced by a newer skill, kept only for reference |

## Rules

- If two routes fit, pick the one with the narrower scope.
- If none fit, say so and ask one question. Do not guess.
- A route that sends, spends or deletes still stops at the gates in `PROFILE.md`.

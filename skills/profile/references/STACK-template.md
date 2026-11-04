# STACK

`setup`, `connect`, `routines` and `blueprint` fill this file. It is the record of what is installed, connected, scheduled and built, so nothing is recommended twice and nothing is forgotten. Never a token, key or password here.

verified: YYYY-MM-DD

## Account

| Item | State | Date |
|---|---|---|
| Plan | (Free, Pro, Max, Team, Enterprise) | |
| Seat | (Owner or member) | |
| Memory: generate from chats | on | |
| Memory: search past chats | on | |
| Artifacts, analysis, web search, extended thinking, browser, skills, scheduled tasks | on, or "off by choice: <which>" | |
| Waiting on Owner | (none, or the items sent) | |

## Surface

| Surface | Model | Profile folder | Hooks live | Subagents |
|---|---|---|---|---|
| Claude Code | (model) | `~/.claude/skill-flow/` | yes | yes |

## Skills and plugins

| Name | Kind | Source | For | State |
|---|---|---|---|---|
| skill-flow | plugin | marketplace | the flow, setup, routines | installed |
| impeccable | plugin | pbakaus/impeccable | design bar on anything a person sees | installed |
| (owner skill) | skill | `~/.claude/skills/<name>` | (one line) | installed |

## Connections

| Kind | Tool | State | Verified with | Date |
|---|---|---|---|---|
| Calendar | (tool) | connected | "What is on my calendar tomorrow?" returned real events | YYYY-MM-DD |
| CRM | (tool) | not connected | | |

## Recommended and skipped

What `connect` offered that the owner did not take, and why, so it is not offered again without a reason.

| Tool or plugin | Why it was offered | Owner's answer | Date |
|---|---|---|---|

## Routines

| Routine | Scheduler | Cadence | Next run | First good output | State |
|---|---|---|---|---|---|
| Morning brief | cloud scheduled task | weekdays 7:35 | | | scheduled |
| Pre-meeting notes | | | | | waiting on CRM |

## Brand

| Item | Value | Date |
|---|---|---|
| Source | guidelines, logo sampled, website sampled, or starter | |
| Fonts | kept, or upgraded to (names) with the owner's yes | |
| Locked into | Protection Desk brand key (name), impeccable design notes (yes or no) | |

## Phone

| Item | State | Date |
|---|---|---|
| App installed, same account | yes or no | |
| Notifications | on and tested, or the one thing to check | |

## GHL assistant

| Item | Value |
|---|---|
| Sub-account | (name) |
| Last sweep | YYYY-MM-DD HH:MM |
| Waiting on the owner | (a count only; the list itself lives in a GoHighLevel task named "Assistant: waiting on you") |

## Built by blueprint

| Thing | Kind | Where | Triggered by | Date |
|---|---|---|---|---|

## Waiting on the owner

One line each with the exact next step.

- (example) Connect GoHighLevel: claude.ai/customize/connectors, Add custom connector, sign in.

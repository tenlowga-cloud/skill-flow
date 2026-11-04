# TOOLS

`setup` fills this file. Name the tool and what it is for. Never put logins, keys or tokens here.

## AI surfaces and models

Which AI apps the owner uses and what each is best for. Name the model in use.

| Surface | Model in use | Use it for |
|---|---|---|
| Claude Code | (model name) | Building and editing code, long jobs in a repo |

## Model ladder

For each role, the models the owner can run, best first. The flow uses the first one that works on the surface it is on. Leave a row as "session model" when there is only one choice.

| Role | First choice | Then | Then |
|---|---|---|---|
| Planner (plans a big job) | (strongest reasoning model, e.g. Claude Fable 5.1 at high) | (e.g. Claude Opus 5.5) | session model |
| Writer (builds one slice) | (fastest capable model, e.g. Claude Sonnet 5.5) | (e.g. Claude Haiku 5.5) | session model |
| Reviewer (verdict on finished work) | (same as planner) | | session model |

Subagents available: yes or no. With no, the flow plays all three roles in sequence on the session model.

## Connected tools

Which tools the AI can reach. Mark each connected, not connected, or read only.

| Kind | Tool | State | What it is for |
|---|---|---|---|
| Calendar | (calendar app) | connected | Checking availability, booking calls |
| Email | (mail app) | read only | Searching threads, drafting replies |
| CRM | (CRM name) | connected | Leads, pipeline, contact notes |
| Code host | (code host) | connected | Repos, pull requests, issues |
| Chat | (chat app) | connected | Where the team talks |

## Team room

Where agents and people post updates, and the rule for it. One line.

| Room or channel | Who posts there | Rule |
|---|---|---|
| (room name) | The AI lanes and the owner | One or two sentences per post |

## Defaults by job

Which surface or tool a job starts on, so nobody has to ask.

| Job | Starts on |
|---|---|
| Plan a big change | The planner, in Claude Code |
| Draft a client email | The writer, then the owner approves |

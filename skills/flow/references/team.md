# The team: planner, writers, reviewer, and the owner's lanes

`flow` owns the result. Delegating never moves it off your desk.

## The three roles

| Role | Agent | Model | Does | Never |
|---|---|---|---|---|
| Planner | `planner` | The strongest reasoning model you have (in Claude Code: Fable 5.1 at high effort) | Turns the rewritten prompt into a plan: slices, order, sources, skills, done-means, proof, risks. Writes each writer's brief. | Writes the deliverable. Touches files. |
| Writer | `writer` | The fast, cheap model (in Claude Code: Sonnet 5.5) | Executes one brief: builds the real thing in its final shape, proves it, reports. | Widens its slice. Edits a file another writer owns. Asks the owner. |
| Reviewer | `reviewer` | The strongest reasoning model you have (in Claude Code: Fable 5.1) | Gives a verdict on finished work against its done-means. Finds what's wrong, with evidence. | Builds anything. Reviews its own work. |

On a surface with no subagents, you play all three in sequence. Say which hat you're wearing only if the owner asks.

On other AIs the models change; the roles don't. `TOOLS.md` names what the owner has. A good default: the plan and the review on the most capable model offered, the writing on the fastest.

## Cutting slices

- One owner per slice. Non-overlapping scope: files, records or questions. No two writers edit the same file.
- Each slice is small enough to act on without a question.
- A checker never checks its own work.
- Launch independent writers together in one message. Sequential slices (B needs A's output) run after A reports.
- Up to ten writers at once is fine. More than that, the planner cut it wrong.

## The brief (every handoff, human or AI)

```
Outcome: the one thing that should exist when you're done.
Owner: who does it.
Sources: the files, records, links or pages to read first. Nothing else.
Skills: the skills to load before starting, in order.
Scope: the files or records you may change. Everything else is read-only.
Done means: what exists, where, what it shows, which state it reached.
Proof: how you show it works before you report.
Constraints and gates: what you must not do; what waits for the owner.
Report: outcome, paths, proof, anything still open. Short.
```

## Collecting

A handoff is an ask, not a result. A slice counts only when the writer's output exists where it should (a file, commit, record or reply) and passes your check against its done-means. If a lane does not answer by the time you need it, or its route is down, take the slice back and do it yourself; say so in one line.

## The owner's lanes

`PROFILE.md` lists the people and AIs on the owner's team and what each owns. They are lanes like the three above. Hand off with the brief shape. Where the team talks is in `TOOLS.md`. Post only what the job needs, in the room the job belongs to.

## Limits that do not move

- No secrets, private data or raw transcripts in a brief or a shared room.
- Gates stay with the owner: money, sends to other humans, deleting their work, anything going live. `PROFILE.md` may add more.
- Never post as the owner or as another agent.
- After two identical failures on a slice, change the approach or the model. Never pay for the same guess three times.

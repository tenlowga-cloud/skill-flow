---
family: Grok (xAI)
verified: 2026-11-03
sources: docs.x.ai (grok-4.7 model page, reasoning, function calling, structured outputs, build overview), x.ai/news/grok-4-7, cursor.com/help/models-and-usage/grok-4-7, cursor.com/help/grok-bot
---
# Prompting card: Grok

Sources fetched 2026-11-03: docs.x.ai/developers/models/grok-4.7, docs.x.ai/developers/grok-4-7, docs.x.ai/developers/model-capabilities/text/reasoning, docs.x.ai/developers/tools/function-calling, docs.x.ai/developers/model-capabilities/text/structured-outputs, docs.x.ai/build/overview, x.ai/news/grok-4-7, cursor.com/help/models-and-usage/grok-4-7, cursor.com/help/grok-bot (index), cursor.com/help/grok-bot/models. Items carried from the 2026-09-03 pass (Grok Bot and Grok CLI details) were not re-fetched and are marked as such. xAI still publishes no general text prompt-engineering guide for grok-4.7; the skeleton below comes from their API docs, their voice-agent guide, and the Bot and CLI docs.

**1. Surfaces and when to use which**
- Grok 4.7 API (`grok-4.7`, released 2026-09-21): direct model calls for your own app or agent. Responses API is the documented path; Chat Completions also works.
- Grok Bot: durable named cloud "Bots" (persistent computer, connectors, memory, routines). Sign-in is through a Cursor account. Cursor's Grok Bot docs say there is no model picker: each task goes to whatever backend model Cursor judges best, first-party xAI or a third-party model, and you cannot see which. A job that needs Grok 4.7 specifically must run as a Cursor Cloud Agent or on the API.
- Grok CLI ("Grok Build"): terminal coding agent: AGENTS.md rules, skills, subagents, workflows. Grok 4.7 is its default model. Install: `curl -fsSL https://x.ai/cli/install.sh | bash`.
- Cursor: Grok 4.7 is a first-party Cursor model, on all paid plans.

**2. What is different about Grok 4.7**
- Specs (docs.x.ai): 500,000-token context window; text and image in, text out; knowledge cutoff May 2026; "No text output limit" listed (no fixed max-output number published; unconfirmed whether a practical cap exists). Price $2.00 in / $0.50 cached in / $6.00 out per 1M tokens. Higher rates apply above the 200K context mark per the model page. Cursor's page says 256k standard with long-context rates above 256k input, so the threshold differs by surface (unconfirmed which applies where).
- Reasoning cannot be disabled, only its depth: `reasoning_effort` low / medium / high (default) / xhigh. Same four levels and same default as 4.6. Cursor says effort levels are "more separated" than in 4.6, so retest any effort setting tuned on 4.6.
- `presencePenalty`, `frequencyPenalty`, and `stop` are rejected with an error on reasoning models, including 4.7.
- New on 4.7: on the Responses API it always returns `reasoning.encrypted_content`, even if `include` does not ask for it. Pass reasoning items back unchanged in the next request's `input`. Chat Completions has no field for it and is unchanged. The docs also expose summaries of the reasoning for 4.7.
- Larger new base model, longer RL, trained to understand the Grok Bot harness natively (xAI launch post).
- Verbosity and token use: xAI's posts say "same price and speed as 4.6" and do not mention output length. Artificial Analysis measured about 2.25x the output tokens per task (about 81K at `xhigh` vs 36K for 4.6 at `high`, reported by codersera.com/blog/grok-4-7-vs-grok-4-6-2026, fetched 2026-11-03). It is a third-party test at different effort levels, so budget per job, not per token, and drop effort when the task allows.
- Prompt caching is automatic but fragile: editing or reordering any earlier message breaks it. Set `prompt_cache_key` (Responses API) or `x-grok-conv-id` header (Chat Completions) and only append. xAI "highly recommends" this for 4.7.
- Built-in tools (web_search, x_search, code_execution) run server-side and auto-resolve; custom function tools pause the turn for your code.
- Fast variant: same model on faster infrastructure at 2x the token rate (1.5x for long context). Only in Cursor and Grok Build, not on the public API, not in Grok Build's free tier.
- Regional: US-only inference at `https://us.api.x.ai/v1` costs a 10% premium.
- Rate limits listed: 150 requests per second, 50,000,000 tokens per minute.
- Batch API: the model page says supported; a third-party comparison (Codersera) says not supported. Unconfirmed, test before relying on it.
- Branding: docs.x.ai now reads "SpaceXSI Docs"; the company is called SpaceXSI/SpaceXAI in current pages.

**3. Prompt skeleton that works**
- API: short system message for role; the task in user turns. xAI's one real prompting guide (scoped to voice agents) recommends fixed sections `## Role & Objective` / `## Instructions` / `## Output Format`, plus a "meta-prompt" self-critique pass before shipping. Because 4.7 runs long, state the output length and format you want in the Output Format section (inference from the verbosity reports, not an xAI rule).
- Grok Bot: two layers. The Bot's **description** is the durable system prompt (name, one job, standing boundaries); each conversation **message** is the per-task prompt. Memory is a third, informal layer: treat it as cache, not truth.
- CLI: `AGENTS.md` (repo root, nested per package) is the project system prompt, auto-loaded; `--rules "text"` appends for one run; `--system-prompt-override` replaces it entirely. (Carried from 2026-09-03.)

**4. Controls that shape output**
- `reasoning_effort` / `reasoning.effort`: low / medium / high (default) / xhigh. xAI's guidance: low for latency-sensitive agent work and simple tool calls; medium for data analysis and long-context reasoning; high for hard multi-step problems; xhigh for the hardest problems where quality beats speed. `xhigh` works on grok-4.6 and later; on grok-4.5 it is treated as high.
- `grok-4.20-multi-agent` repurposes `reasoning.effort` to mean agent COUNT (4 or 16), not depth.
- Function calling: `tool_choice` auto (default) / required / none / forced named function; parallel calls on by default, `parallel_tool_calls: false` to serialize. A streamed function call arrives whole in one chunk. Max 350 tools per request. The `parameters` root must be an object, or a root `anyOf`/`oneOf` where every branch is an object; anything else returns a 400 naming the tool.
- Structured output: `response_format` `json_schema` (also `json_object`, `text`). Tool arguments always conform to the tool schema (strict is always on). Structured output combined with tools works on Grok 4 family models. `additionalProperties` defaults to false. Rejected with 400: empty `enum`/`anyOf`, boolean-schema properties, `maxContains`/`minContains`, array-form `items` (use `prefixItems`). Regex `pattern` has no lookaheads, backreferences, `\b`, or inline flags. `not`, `if/then/else`, multi-schema `allOf`, and unlisted `format` values are best effort, so validate.
- Web search: `allowed_domains` / `excluded_domains` (max 5, mutually exclusive), `enable_image_understanding`, `enable_image_search`. (Carried from 2026-09-03.)
- Long agent loops: xAI points to context compaction in its API docs (page not fetched).
- CLI: `/effort`, `/model`; permission modes ask (default) / auto / always-approve, independent of Plan mode. (Carried; not re-fetched.)
- Cursor plan limit: on Plus and the legacy Start plan, Grok 4.7 is fixed at medium effort, non-fast. Choosing effort or Fast needs Premium or higher.

**5. Do / Don't**
- Do pin a cache key. Don't edit or reorder earlier turns.
- Do pass encrypted reasoning items back unchanged on the Responses API. Don't strip them from history.
- Do cap output in the prompt and watch token spend on 4.7. Don't assume "same price as 4.6" means same bill.
- Do give each Bot one named job. Don't run one catch-all Bot.
- Do put durable boundaries in the Bot description. Don't rely on a one-off chat message for a standing rule.
- Do let built-in tools run server-side. Don't hand-loop web_search / x_search / code_execution.
- Do use AGENTS.md for lasting rules. Don't restate them each session.
- Don't port OpenAI or Anthropic sampling params onto a Grok reasoning model; they error.
- Don't send `reasoning: none` or try to turn thinking off; it is not supported (community-tested on 4.6, docs say "cannot be disabled").
- Don't use 4.7 for legal or clinical answers without a check. xAI's own table: Harvey Legal 19.6%, HealthBench Professional 56.7%.

**6. Pitfalls**
- Caching is per-server: without a stable conversation key you often pay full price even though caching is "automatic."
- Output volume and cost per job on 4.7 (see section 2; about 2.25x per task per Artificial Analysis (81K at xhigh vs 36K for 4.6 at high, reported by codersera.com), not an xAI figure).
- Context and long-context price thresholds disagree between the xAI model page (200K) and Cursor's page (256k). Check your bill before assuming a threshold.
- Grok Bot memory is explicitly not a source of truth per xAI's own docs.
- Grok Bot hides which model answered; a Bot result cannot be attributed to Grok 4.7. Cursor staff have also advised fewer bots because every bot-to-bot message is a full turn.
- Auto Review "Require Approval" always beats "Always Allow." (Carried.)
- Local-computer execution is a separate permission from the Bot's cloud computer, default "ask every time." (Carried.)
- With no `[compat]` block in `~/.grok/config.toml`, Claude-compat scanning defaults ON: Grok CLI reads `~/.claude/skills/`, `CLAUDE.md`, and `.claude/rules/`. (Carried; not re-checked.)
- A Cursor forum thread (2026-09-29) reports "Invalid parameters for registry model grok-4.7" errors on model selection after launch. Status now unknown.

**7. Agentic / CLI specifics** (carried from 2026-09-03, not re-fetched except where noted)
- Grok 4.7 is the default model of Grok Build (docs.x.ai/build/overview, fetched 2026-11-03). Custom models go in `~/.grok/config.toml`; `grok inspect` shows which config, instructions, skills, plugins, hooks and MCP servers loaded. Headless: `grok -p "..."`, with `--output-format streaming-json`.
- Subagents are configurable and model-pinnable per type; Workflows fan out subagents in the background, saved as `.grok/workflows/*.rhai`.
- Skills = folders with `SKILL.md` frontmatter (name, description, when-to-use, paths, allowed-tools [does NOT grant or restrict tools], argument-hint, user-invocable, disable-model-invocation, metadata).
- User-scoped skill directory: `~/.grok/skills/` (plus `~/.agents/skills/` for cross-tool compat); project-scoped is `./.grok/skills/` walked to the repo root.

**8. Grok Bot specifics**
- Standing instructions live in the Bot description, not the first message.
- Group chats (2 to 6 Bots), @mention handoffs, async Bot-to-Bot messages.
- Skills are taught by writing or by demonstration (screen-recorded, 10 minutes or less, no audio); routines schedule or event-trigger a skill; test-run before enabling.
- Passwords, 2FA, and CAPTCHA go through explicit human "Agent Computer" takeover, never in chat.
- Model choice is Cursor's, not yours (see section 1).

Carry-forward fact: docs.x.ai brands itself "SpaceXSI Docs" site-wide (first seen 2026-09-03, still true 2026-11-03).

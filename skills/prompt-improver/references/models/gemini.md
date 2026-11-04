---
family: Gemini text (Google)
verified: 2026-11-03
sources: aistudio.google.com/docs (models, thinking, prompting strategies, video and audio understanding, media resolution, structured output, Gemini 3.5 Transcribe guide, pricing)
---
# Prompting card: Gemini (text)

Sources fetched 2026-11-03 (docs now live at aistudio.google.com/docs; ai.google.dev redirects there): models list, model pages for gemini-3.8-flash, gemini-3.5-transcribe and gemini-3.1-pro-preview, pricing, thinking, What's new in Gemini 3.8 Flash, prompting strategies, video understanding, audio understanding, Gemini 3.5 Transcribe guide, media resolution, structured output. Image rules are on the image card (Nano Banana). Numbered references [3], [4], [7] point to Google's prompting strategies and thinking docs; lines marked "2026-11-03" come from this refresh.

**1. Models and when to use which**

| Model | ID | Status | Use for |
|---|---|---|---|
| Gemini 3.8 Flash | `gemini-3.8-flash` | Stable, 1,048,576 in / 65,536 out | Main model for watching video and listening to audio (`MM:SS` timestamps, JSON out), long agent and coding work. Text, image, video, audio, PDF in; text out |
| Gemini 3.1 Pro (preview) | `gemini-3.1-pro-preview` | Preview, 1,048,576 in / 65,536 out | Second opinion on a shaky video or reasoning result. Variant `gemini-3.1-pro-preview-customtools` favors custom tools |
| Gemini 3.5 Transcribe | `gemini-3.5-transcribe` (file), `gemini-3.5-transcribe-live` (stream) | Stable | Speaker-labeled transcripts, word timestamps. Audio in, text out |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | Stable | Cheapest high-throughput text and media |
| Gemini 3.6 Flash | `gemini-3.6-flash` | Stable, previous generation | Fallback if 3.8 misbehaves |
| Gemini 3.1 Flash-Lite, Gemini 3 Flash (preview) | `gemini-3.1-flash-lite`, `gemini-3-flash-preview` | Stable / preview | Older cheap tiers; `gemini-3-flash-preview` is the only one that still allows `minimal` thinking |

- Gone or going: `gemini-3-pro-preview` and `gemini-3.1-flash-lite-preview` are shut down. `gemini-2.5-pro` and `gemini-2.5-flash` are deprecated and auto-route on 2026-12-01 (2.5 Pro to `gemini-3.8-flash`, 2.5 Flash to `gemini-3.5-flash-lite`). Preview models get at least 2 weeks' deprecation notice. 2026-11-03
- A newer flagship, `gemini-4-argon` (1M context, 65K/1M output), is on the models list. Its status label is unconfirmed, so treat it as not yet recommended.
- Model IDs churn fast; re-check the models page before hard-coding one.

**Prices per 1M tokens (paid tier, standard), 2026-11-03**

| Model | Input | Output (incl. thinking) |
|---|---|---|
| 3.8 Flash | $0.75 through 2026-12-31, then $1.50 | $3.75 through 2026-12-31, then $7.50 |
| 3.1 Pro preview | $2.00 up to 200k prompt tokens, $4.00 above | $12.00 up to 200k, $18.00 above |
| 3.5 Transcribe | $2.00 audio ($0.003/min) | $12.00 text ($0.002/min); about $0.005/min all in |
| 3.5 Flash-Lite | $0.30 | $2.50 |

3.8 Flash batch and flex are half price; priority costs about 1.8x. Free tier is free but Google trains on what you send, so use a paid-tier project for client calls.

**2. What is different about Gemini text models now**
- Built-in thinking; do not ask for visible chain-of-thought, it mostly wastes tokens [4][7]. "Think very hard before answering" is the one nudge Google allows for heavy reasoning, at extra token cost.
- `thinking_level` goes in `generation_config` and replaced `thinking_budget`. 3.8 Flash: `low | medium | high`, default **medium**; `minimal` returns an error. 3.1 Pro: `low | medium | high`, default **high**. Drop to `low` for simple or latency-sensitive tasks. 2026-11-03
- `max_output_tokens` caps thinking and answer together. Too low a cap truncates the reasoning and the answer. Google suggests at least 32,768 when migrating existing apps (stated on the Gemini 4 page; applies the same logic to 3.8). 2026-11-03
- 3.8 Flash takes smaller reasoning steps, calls tools in loops and checks its own work, so it can burn more tokens on long multi-step jobs. 2026-11-03
- **Temperature: this changed.** For 3.8 Flash Google says remove `temperature`, `top_p` and `top_k` from the config. Models 3.6 and later ignore custom values and send deprecation warnings; Google says a future release will return 400. Older Gemini 3 models (3.1 Pro, 3 Flash): leave them at defaults (temperature 1.0), lowering can loop or degrade reasoning. Whether 3.8 ignores or rejects them today is unconfirmed, so just omit them. 2026-11-03
- Also remove `candidate_count` (unsupported on Gemini 3 and later) and prefilled model turns. 2026-11-03
- Terser by default; ask for tone and length explicitly [4][7].
- `media_resolution`: `low | medium | high | ultra_high` (plus unspecified default); set per file or per part, `ultra_high` only per part and only for images. Google's advice: images `high`, PDFs `medium`, video `low` or `medium` (use `high` for small text), audio leave unspecified. Per frame: video 70 tokens at low, medium and default, 280 at high. 2026-11-03
- Thought signatures carry reasoning state. Stateless calls: resend every thought block unchanged, plus tool-call signatures. Stateful: use `store: true` with `previous_interaction_id` and the server handles it. Google now wants multi-turn on server-side `previous_interaction_id`. For generateContent, every `FunctionResponse` needs `call_id` and `name`. 2026-11-03
- Thought summaries are off; set `thinking_summaries: "auto"` to get them (the array can be empty).
- Enable Search grounding for current or obscure facts; enable code execution for arithmetic and counting [3]. 3.5 Transcribe does not support Search grounding, code execution, function calling, caching or thinking.

**3. Prompt skeleton that works**
- One delimiter style per prompt: XML tags (`<role>`, `<context>`, `<task>`, `<constraints>`) or Markdown headings [3]. Be direct; Google says avoid overly persuasive language.
- Put persona, constraints and output format in the system instruction or at the very top.
- Long context: reference material first, the actual question **last**, bridged with "Based on the information above..." [3][7].
- Few-shot examples: Google says always include them; keep formatting identical across examples; too many can overfit [3].
- For video or audio, put the text prompt **after** the media part. 2026-11-03
- Optional clauses from Google for Flash: say the current date is 2026 (so search uses it), state the knowledge cutoff, and for grounding say "answer only from the context; if it is missing, say it is unavailable."
- Google's Gemini 3 template (still valid):
```
<role>You are Gemini, a specialized assistant for [Domain]. You are precise, analytical, and persistent.</role>
<instructions>1. Plan  2. Execute  3. Validate  4. Format</instructions>
<constraints>Verbosity: [Low/Medium/High]  Tone: [Formal/Casual/Technical]</constraints>
<output_format>1. Executive Summary  2. Detailed Response</output_format>
```
then the user prompt is `<context>...</context><task>...</task>` [3]. (The old closing "think step-by-step" line is unneeded on thinking models.)

**4. Video and audio (the way to use 3.8 Flash)** 2026-11-03
- Ask for moments in `MM:SS` (for example `01:15`). Ask for `MM:SS` in the output and name the JSON field.
- Video: sampled at 1 frame per second, audio at 1 Kbps mono. Fast motion can lose detail. Clip with `start_offset` and `end_offset`, change rate with `fps` (for example 0.5), both in the `processing` object (static mode only).
- Agentic video mode is available on 3.8 Flash: the model jumps around the timeline and loads only what it needs, up to 88% fewer tokens on long video, but can cost more on short clips. No clipping or custom fps in this mode.
- Cost in static mode: about 100 tokens per second of video at low, about 300 at high. A 1M-token window holds up to 3 hours at low or about 1 hour at high. So an hour of high-resolution video sits at the cap: chunk into 10-minute pieces or send audio only.
- Input routes: File API (up to 20 GB paid) for anything over 100 MB or 10 minutes; inline only under 20 MB total; YouTube by public URL only (preview, free; up to 10 videos per request; free tier 8 hours a day). Formats: MP4, MPEG, MOV, AVI, FLV, MPG, WebM, WMV, 3GPP.
- Audio: up to 9.5 hours per prompt; formats WAV, MP3, AIFF, AAC, OGG, FLAC, M4A, Opus, WebM and more; downsampled to 16 Kbps mono. Token rate is stated as 32 per second on the audio and video pages and 25 per second on the media-resolution and Transcribe pricing pages (unconfirmed which; budget for 32).
- Audio can be asked for diarization, timestamps, language and emotion in one prompt with a JSON schema.

**5. Gemini 3.5 Transcribe** 2026-11-03
- Call `gemini-3.5-transcribe` with the audio as input and `generation_config.transcription_config`: `language_codes` (BCP-47, empty means auto-detect and code-switching), `custom_vocabulary` (up to 1,000 terms, about 100 works best), `mode` (`smart` or verbatim, verbatim is default) with `diarization_mode: "speaker"` and `timestamp_granularities: ["word"]`.
- Limits: 1 hour per request, but only 30 minutes with diarization or word timestamps. Up to 8 speakers (3 or more is experimental). 85+ languages.
- Conflicts: custom vocabulary cannot combine with diarization or word timestamps; smart mode cannot either; word timestamps can lower accuracy. The API rejects the bad combos.
- No free-form prompt field. Steering is only language and vocabulary. For questions about the audio, use 3.8 Flash instead. Streaming (`-live`, 10 minutes a session) has no timestamps or diarization.
- Output: text in `response.output_text`; word info (`speaker` like `spk_1`, `start_offset`, `end_offset`) rides on annotations.

**6. Structured output** 2026-11-03
- Set `response_format` to `{type: "text", mime_type: "application/json", schema: <JSON Schema>}` (Pydantic and Zod can generate it). Streams as partial JSON; join the chunks.
- Enforced: types, `enum`, `required`, `properties`, `additionalProperties`, `format` (date-time, date, time), `minimum`/`maximum`, `minItems`/`maxItems`, `prefixItems`. Silently dropped (validate yourself): `minLength`, `maxLength`, `uniqueItems`, `minProperties`, `maxProperties`, `contains`.
- Combines with Search, URL context, code execution, file search and function calling (preview, Gemini 3 series).
- Too big or deep a schema gives 400 `INVALID_ARGUMENT`: flatten, trim enums, shorten names, make recursive fields optional.
- Property ordering behavior is not described on the page (unconfirmed). Put a `description` on each field instead of relying on order.
- For complex JSON use the schema feature, not "reply in JSON" in the prompt [Google].

**7. Controls that shape output**
`thinking_level`, `thinking_summaries`, `max_output_tokens`, `media_resolution`, `response_format`, `processing` (video clip and fps), `transcription_config` (Transcribe), `previous_interaction_id` or echoed thought signatures, `tools: [google_search, url_context, code_execution, function_declarations]` [3][7]. Do not send `temperature`, `top_p`, `top_k`, `candidate_count` to 3.8 Flash.

**8. Do / Don't**
- Do give few-shot examples in one consistent format. Don't mix example formats.
- Do put the question after the context and the text prompt after the media. Don't bury it above a long document.
- Do omit sampling parameters on 3.8 Flash. Don't copy old "temperature 0 for extraction" habits.
- Do keep thought signatures intact in tool chains. Don't drop them; that is a hard failure.
- Do use `low` thinking for simple extraction and `high` for hard reasoning. Don't assume the default is high; it is medium on 3.8 Flash.
- Do chunk long video or send audio only. Don't send an hour of high-resolution video and expect room left for the answer.
- Do ask for the tone you want. Don't assume the default is conversational.

**9. Pitfalls**
- Asking for visible chain-of-thought on a thinking model wastes tokens.
- Temperature below 1.0 can loop on older Gemini 3 models; on 3.8 Flash the setting is ignored or will soon error.
- Setting `thinking_level: "minimal"` on 3.8 Flash or 3.1 Pro errors out.
- Low `max_output_tokens` can eat the whole budget in thinking and return an empty or cut answer.
- Dropping thought signatures breaks function-calling continuity.
- Free-tier keys train Google's models on your input.
- Intro prices on 3.8 Flash double on 2027-01-01.
- For a shaky video review, get a second opinion from 3.1 Pro.

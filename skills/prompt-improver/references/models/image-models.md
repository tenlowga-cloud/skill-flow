---
family: Image models (OpenAI gpt-image, Google Nano Banana / Nano Banana Pro)
verified: 2026-09-03
sources: developers.openai.com (GPT Image Generation Models Prompting Guide), ai.google.dev/gemini-api/docs (image generation and models), Google Cloud Nano Banana prompting guide
---
# Prompting card: Image models

Sources fetched 2026-09-03: OpenAI cookbook "GPT Image Generation Models Prompting Guide" (developers.openai.com), Google Cloud's "ultimate prompting guide for Nano Banana," the dev.to Nano Banana Pro guide by Google AI, and ai.google.dev image-generation and models docs. The shared rules below match both makers' guides; the rest is model-specific mechanics.

## Shared rules (both families)
- Write a scene in full sentences as if briefing a human artist. A keyword list ("cool car, neon, city, night, 8k") is the explicit anti-example in both makers' guides.
- Order: intended use → scene or background → subject → key details (materials, lighting, camera) → constraints.
- Name materials and light precisely ("navy blue tweed," "three-point softbox," "golden-hour backlight"), not adjectives ("cinematic," "masterpiece").
- Frame exclusions positively ("an empty street") rather than as negatives ("no cars").
- Text in image: quote the exact string, name font, size, color, placement; keep it short.
- Restate the invariants on every edit iteration (identity, geometry, layout, brand elements): "change only X; keep everything else the same."
- Edit, don't re-roll: small single-change follow-ups on a clean base beat one long re-prompt.
- Give every reference image an index and a role ("Image 1: product photo; Image 2: style reference") and state the interaction.

## OpenAI gpt-image
**Models and parameters**
- `gpt-image-2`: the default. `quality`: low / medium / high (no `input_fidelity`; output is always high fidelity). `size`: any resolution with max edge under 3840px, both edges multiples of 16, long:short ratio 3:1 or less, 655,360 to 8,294,400 total pixels (above 2560×1440 is experimental). Use for customer-facing, photoreal, editing-heavy, brand-sensitive, text-in-image work.
- `gpt-image-1.5` / `gpt-image-1`: legacy; fixed sizes (1024×1024, 1024×1536, 1536×1024, auto); `input_fidelity` low / high available.
- `gpt-image-1-mini`: cost and throughput first; try `gpt-image-2` at `quality="low"` first, it often matches.
- `background="transparent"` (gpt-image-2, preview) with `output_format="png"` (default) or `"webp"`, never `jpeg`; keep RGBA downstream or the alpha is lost.

**Generate vs edit by use case**
- Infographics and diagrams: generate, `quality=high` for dense labels, name every required component.
- Photorealism: generate; photography language plus explicit texture and imperfection cues; avoid "studio polish" words; include "photorealistic."
- Logos: generate, transparent PNG, clean vector shapes and strong silhouette, `n=4` for variants.
- Ads: generate; write a creative brief not a tech spec; quote the exact tagline; "render exactly once."
- Style transfer: edit plus reference image; describe what stays vs changes.
- Try-on and identity locks: edit; explicitly lock face, body, pose, hair; only garments change.
- Product cutouts: edit, transparent PNG, isolated subject, no halos, label legibility preserved.
- Lighting, weather, object removal: edit; `input_fidelity="high"` on legacy models only when identity must survive.
- Compositing: edit with several inputs, reference each by index and role, state exact placement.

**Do / Don't**
- Do state exclusions and invariants explicitly. Don't assume the model infers what to leave alone across iterations.
- Do use texture and imperfection cues plus "photorealistic." Don't rely on "photo" alone; it trends studio-polished.
- Do start high-volume work at `quality="low"`. Don't default to `high` for everything.
- Do iterate with small single-change follow-ups. Don't pack every change into one prompt if you need to debug a bad result.

**Pitfalls**: detailed camera specs are read loosely (composition level only); `input_fidelity` silently no-ops on gpt-image-2; above 2K is experimental; jpeg cannot carry transparency; RGBA→RGB anywhere downstream discards it.

## Google Nano Banana / Nano Banana Pro
**Models**

| Model | ID | Use for |
|---|---|---|
| Nano Banana 2 (Gemini 3.1 Flash Image) | `gemini-3.1-flash-image` | Default: speed, 4K, world knowledge, multi-reference consistency |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Fastest and cheapest; not for multi-reference or long edit chains |
| Nano Banana Pro (Gemini 3 Pro Image) | `gemini-3-pro-image` | Premium: brand and text accuracy, complex layouts, up to 4K |
| Nano Banana (legacy) | `gemini-2.5-flash-image` | Superseded; move to Nano Banana 2 |

IDs churn; re-check `ai.google.dev/gemini-api/docs/models` before hard-coding.

**Templates**
- Text-to-image: `A photorealistic [shot type] of a [subject] in a [setting]. [Light]. Shot from a [angle] with a [lens type].`
- Edit: `Using the provided image of [subject], please [add/remove/modify] [element]. Ensure the change is [how it integrates].` For localized edits say what stays untouched.
- Text in image: generate the exact text content in a normal chat turn first, then ask for the image; measurably improves legibility.

**Controls**
- `response_format.aspect_ratio`: `1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9` (plus `1:4, 4:1, 1:8, 8:1` on Nano Banana 2 only).
- `response_format.image_size`: `1K / 2K / 4K` (uppercase K required; lowercase is rejected) plus `512px` on Nano Banana 2 only.
- Reference images: up to 14, but the high-fidelity budget differs: Pro 6 objects / 5 characters / 3 style refs; Nano Banana 2 10 objects / 4 characters; legacy about 3.
- `tools: [{"type":"google_search"}]` with optional `search_types: ["web_search","image_search"]`; video-to-image input on `gemini-3.1-flash-image`.
- Thinking is on by default for Gemini 3 image models and cannot be disabled. Edits and follow-ups on `gemini-3-pro-image` / `gemini-3.1-flash-image` must echo back the prior turn's `thoughtSignature` or the call returns 400.
- Editing patterns with Google templates: add/remove, inpainting by semantic mask, style transfer, multi-image composition, face/logo lock, sketch-to-finished, 360° character turnarounds (feed prior frames back as references).

**Do / Don't**
- Do explain the image's purpose. Don't give a bare subject with no context.
- Do iterate conversationally on the existing image, keeping `thoughtSignature`. Don't regenerate from scratch or drop the signature.
- Do quote exact text and describe the font. Don't ask for novel text and a new image in one first shot.

**Pitfalls**: keyword soup; vague style words; dense infographics can mix up facts (human check); lowercase `1k` rejected; dropping `thoughtSignature` is a hard failure.


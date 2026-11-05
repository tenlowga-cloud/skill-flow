---
family: Video models (Kling VIDEO 3.0, Google Veo, xAI Grok Imagine video)
verified: 2026-11-04
sources: kling.ai (Kling AI Prompt Guide), ai.google.dev (Veo guide), docs.x.ai/developers/model-capabilities/video/generation, docs.x.ai/developers/model-capabilities/video/overview, docs.x.ai/developers/model-capabilities/imagine
---
# Prompting card: Video models

Sources fetched 2026-09-03: kling.ai "Kling AI Prompt Guide" (published 2026-08-07) and ai.google.dev's Veo guide. Hosted video tools can route to either engine; write the prompt for the engine that will run.

## Kling VIDEO 3.0
**What it does**: Native Audio (dialogue, ambience, SFX in one generation; 5 languages plus dialects and mixed-language scenes); Multi-Shot (Automatic or Custom shot-level control); References / Elements 3.0 (Element Reference and Video Element Reference for subject consistency); native 4K at 30 credits per second, so plan cost explicitly.

**Prompt skeleton**: Subject (character, product, prop, environment) → Action (visible movement) → Setting (location plus surrounding detail) → Camera (framing, angle, movement) → Lighting and mood (visible atmosphere) → Audio or dialogue. Write vague ideas as visible detail ("swirling blue energy particles with an ethereal glow," not "magic"). Movement cues describe what the viewer sees.

**Camera and motion vocabulary**: close-up (dialogue, emotion, detail), wide shot (setting, scale), push-in (emphasis, tension), pan and tilt (reveal space), tracking shot (movement continuity). Framing: extreme close-up, medium close-up, full body, establishing wide. Composition: centered, rule of thirds, off center. Pacing: slow (calm, suspense), steady (readable action), quick (energy, surprise); use Custom Multi-Shot's duration field for exact shot length, not prose.

**Subject consistency**: Element Reference or Video Element Reference with clean, high-quality source material; keep the character or product description steady in the prompt even as scene, camera, and action change, because description drift breaks consistency as much as a missing reference does. For voice (3.0 Omni) keep speaker name, line, and delivery together.

**Multi-shot**: define the setting first, then organize by shot order. Automatic: describe scene, dialogue, camera coverage, rhythm and let the model assign angles. Custom: set content, duration, shot size or perspective, and camera movement per shot.

**Text rendering**: exact words, placement, surface, camera distance; keep it short when readability matters; support with matching lighting and framing.

**Do / Don't**
- Do give visible pacing and motion cues ("a slow push-in as the character thinks"). Don't describe pacing as an abstract internal state.
- Do label each beat ("Shot 1: wide shot… Shot 2: medium shot…"). Don't write a multi-beat scene as one paragraph and expect inferred breaks.
- Do restate the character or product description across shots even with a reference. Don't assume a reference alone guarantees consistency.
- Do write on-screen text in quotes with placement, surface, and camera distance. Don't leave in-scene text vague.

**Pitfalls and workflow**: vary speed, movement, and framing deliberately and keep a library of what worked; 4K costs 30 credits per second, verify against current plan pricing; choose settings against the current product interface, not article assumptions; campaign consistency needs a reference library and a documented visual direction, not one strong prompt.

## Google Veo (short note)
Five-element structure: subject, action, style, camera positioning, ambiance. Up to 3 reference images; first and last frame interpolation; explicit audio cueing (quoted dialogue, named SFX, ambient description); extension up to 7 seconds per call, repeatable up to 20 times; aspect ratio 16:9 default or 9:16. Full details: Google's Veo guide.

## xAI Grok Imagine video

Fetched 2026-11-04 from docs.x.ai video generation, the video overview, and the Imagine overview. The Kling and Veo sections above were not re-fetched. They stay as of 2026-09-03. xAI has not published a separate video prompting guide on these pages. Do not paste the Kling skeleton onto this model and call it xAI's. The published examples are one full-sentence scene. Image-to-video adds a still and a sentence about the motion.

**Models**
- `grok-imagine-video-1.5`: native 1080p text-to-video and image-to-video, up to 14 reference images, up to 3 voice references, first and last frame, up to 4 keyframes. Use when the clip needs those controls.
- `grok-imagine-video-1.5-lite`: text-to-video and image-to-video, lip-synced speech, 1080p by upscaling 720p. Lowest price per second. Use for a simple clip.
- `grok-imagine-video`: edit and extend, up to 720p.

**Controls**
- `duration`: 1 to 15 seconds. Default 8. Reference-to-video on `grok-imagine-video` allows up to 10 seconds. Editing does not take a custom duration. The edited clip keeps the source length, capped at 8.7 seconds.
- `aspect_ratio`: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `5:2`. Image-to-video matches the still. You do not pick a ratio for that mode.
- `resolution`: `480p` (default), `720p`, `1080p`. `grok-imagine-video` stops at 720p. Reference-to-video on 1.5 stops at 720p.
- Modes on `POST /v1/videos/generations`: text (`prompt` only), image-to-video (`prompt` + `image`), reference-to-video (`reference_images` or `reference_audios`), first and last frame (`last_frame`, optional `image`), keyframes (up to 4 `{image, timestamp_s}`). Edit is `POST /v1/videos/edits`. Extend is `POST /v1/videos/extensions`.
- The call is async. The start response returns `request_id`. Poll `GET /v1/videos/{request_id}` until `status` is `done`, `pending`, or `failed`. Download the URL. It is temporary.
- Price per second, from the overview: 1.5 is $0.08 at 480p, $0.14 at 720p, $0.25 at 1080p. Lite is $0.02, $0.03, and $0.14. Classic video is $0.05 at 480p and $0.07 at 720p.

**Prompt.** One scene in full sentences: what is in the frame, and what the viewer sees move. On image-to-video, the still locks the picture. The prompt should say the motion, not restate a new subject. Text-to-video on 1.5 and lite builds a first frame, then animates it. You still send one request. The intermediate still is not returned.

**Do / Don't**
- Do pin `duration` and `resolution`. The default resolution is `480p`.
- Do use lite for a simple move. Don't pay 1.5 rates unless you need references, voices, pinned frames, or native 1080p.
- Do pass the accepted still as `image` when the frame has to match a photograph you already chose.
- Don't leave the video URL for later. Download it when `status` is `done`.

**Pitfalls**: a longer or more detailed scene takes longer to finish. An empty prompt is rejected. Conflicting modes (for example combining inputs the chosen model does not support) return `invalid_argument`. Submit a new request after a fix. The old one does not resume.

---
family: Video models (Kling VIDEO 3.0, Google Veo)
verified: 2026-09-03
sources: kling.ai (Kling AI Prompt Guide), ai.google.dev (Veo guide)
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

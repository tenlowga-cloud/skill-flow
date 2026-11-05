# prompt-improver references

`models/` holds one prompting card per model family. Each card is the maker's own advice, condensed: controls, pitfalls, do and don't pairs. Its `sources:` line lists where the facts came from, and `verified:` is the date they were last checked.

| Card | Covers |
|---|---|
| `models/claude.md` | Claude Fable, Opus, Sonnet, Haiku |
| `models/openai.md` | GPT-6 Astra (section 9), GPT-5.6 family, Codex, ChatGPT custom instructions |
| `models/grok.md` | Grok 4.7 API, Grok Bot, Grok CLI |
| `models/gemini.md` | Gemini 3.8 Flash, 3.1 Pro, 3.5 Transcribe |
| `models/image-models.md` | OpenAI gpt-image, Nano Banana / Nano Banana Pro, Grok Imagine image |
| `models/video-models.md` | Kling VIDEO 3.0, Veo, Grok Imagine video |

Refresh rule: when a maker ships a new generation, or a card's `verified:` date is older than the model being prompted, re-fetch the maker's guide (public URL only), update the card, and bump the date. Do not fork a card into a project. Keep project-specific deltas in the project's own notes.

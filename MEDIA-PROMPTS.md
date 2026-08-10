# 🖼️🎬 Gauntlet Media Prompts (for Grok image + video gen)

Generate these on **grok.com**. Save into the unzipped `media/` folder using the exact
filenames below. The app auto-shows them — no code changes needed. Missing files fall back
to the animated SVG emblems / skip the video.

**Shared visual style (prepend to every prompt):**
> Cinematic concept art / motion, deep violet (#1a1140) and cyan (#56d4ff) palette with
> electric purple (#8c6eff) accents and ember-gold sparks, dark atmospheric background,
> volumetric haze, soft rim lighting, "arcane-tech codex" aesthetic — glowing circuitry
> mixed with classical forge/alchemy imagery. NO text, NO letters, NO watermarks, NO UI.

---

## 🎬 Between-track videos (3 files) — the chapter breaks
These play fullscreen when you reach a new track (or finish):
- `track1-2.mp4` → plays when you open **Mission 13** (Track 2 start)
- `track2-3.mp4` → plays when you open **Mission 22** (Track 3 start)
- `finale.mp4`     → plays when you complete **Mission 30** (all tasks ticked)

**track1-2.mp4** — *From understanding to building.* A glowing schematic of an abstract AI
"brain" of light dissolves and reforges itself into a roaring forge where raw text-ore is
melted into a tower of stacked transformer rings. Camera pushes in as the forge ignites.
Looping ambient, 6–10s, no text.

**track2-3.mp4** — *From model to agent.* The completed LLM spire opens a luminous eye
(multimodal vision) while a gear of tools clicks into its side; the static tower becomes a
living, thinking agent that reaches out and acts. Camera orbits as the eye + gear awaken.
6–10s, no text.

**finale.mp4** — *The whole gauntlet, complete.* All motifs converge: the shield emblem, the
transformer tower, the multimodal eye, and the agent gear-loop spiral together and launch
into a burst of light. Triumphant, soaring. 8–12s, no text.

> If Grok has no video mode, generate a single hero *image* for each instead and save as
> `track1-2.png` / `track2-3.png` / `finale.png` — the app will still show them (update
> `TRACK_VIDEO` filenames in gauntlet.html if you use .png). Or skip; the SVG emblems cover it.

---

## 🖼️ Per-mission hero images (31 files: 00.png … 30.png)
Shown in the mission hero banner + cinematic divider (falls back to SVG if missing).

### Track 1 — Understand & Direct AI Engineering
- **00** A lone engineer at a glowing crossroads inside a vast dark library of living
  code-streams; three luminous paths diverge into the dark; a faint shield emblem glows in
  the sky. Sense of beginning a journey.
- **01** A constellation of glowing nodes connected by threads of light forming a living web;
  attention flowing between orbiting spheres; one node flares brighter as it gathers light.
- **02** A towering spire of stacked glowing rings self-assembling in mid-air, each ring a
  transformer block locking into place; construction energy crackling upward.
- **03** A single bolt of light fracturing into many smaller diverging sparks — a probability
  cloud of possible next tokens; sense of sampling / branching futures.
- **04** A river of glowing glyph-characters flowing into a narrowing funnel, a waterfall of
  scrolling text being compressed into a context window; counts shimmering as they enter.
- **05** A star-map of meaning: points of light in a dark void connected by faint lines into
  clusters — a vector space of concepts; one point pulsing as "you are here".
- **06** A hooded seeker holds a lantern that pulls the *right* glowing tomes from endless
  shelves in a vast library; irrelevant books dim; relevant ones lift toward the light.
- **07** A gear of light merging with a wrench and a floating interface panel; hands of energy
  operating tools; the moment a model learns to act on the world.
- **08** Several small shield-emblems orbit and coordinate around a central glowing core, a
  command constellation; lines of intent flowing between them.
- **09** Modular glowing panels snapping together like living architecture, a clean framework
  assembling from parts; contrast of lean vs heavy.
- **10** A great scale of judgment with a glowing checkmark seal; a quality gauge tipping
  toward "pass"; proof etched in light.
- **11** A rough stone statue being polished and refined by beams of alignment light; a wild
  form becoming a precise, trustworthy figure.
- **12** (Boss) A massive blazing shield emblem; the engineer stands before a gate of pure
  light — the final trial of understanding; triumphant, daunting.

### Track 2 — Build the Full LLM
- **13** A cold empty forge with raw "text ore" waiting; a single spark ascending toward the
  anvil — the beginning of creating a model from nothing.
- **14** Scattered floating letters (a, b, c, ≡) coalescing into an ordered glowing grid — a
  vocabulary being born; alphabet resolving into structure.
- **15** A conveyor of sliding token-windows passing through a luminous machine; batches of
  context flowing in rhythm; data pipeline in motion.
- **16** The full GPT spire now complete and towering, every transformer block lit, a cathedral
  of computation; awe-inspiring scale.
- **17** A roaring forge with loss-sparks falling like embers; a furnace of learning; the model
  tempering as the fire cools; heat and focus.
- **18** A quill of light writes streaming text flowing from a model's maw; autocomplete
  cascading forward; the moment of generation.
- **19** A magnifier of light inspects generated text on a bench; quality being measured; a
  careful evaluator's eye.
- **20** A wild glyph-beast being shaped into a polite glowing chat-bubble assistant; formatting
  and instruction taming chaos.
- **21** (Boss) A trained LLM core orbiting a server-pillar, launching into the world; the
  shipped model ascending; completion.

### Track 3 — Multimodal + Agent
- **22** A luminous eye merging with a page of flowing text — vision and language fusing into
  one stream of understanding.
- **23** A glowing JSON block with executable function tags pulsing; a structured tool-call
  taking shape; precision and schema.
- **24** A circular gear-loop with a pulse of light traveling thought → action → observation →
  thought; the agent reasoning cycle as a living ring.
- **25** An image projecting beams of light that land and arrange themselves into a text-space —
  a projector aligning pixels with words; bridge of modalities.
- **26** Rows of glowing cards, each a synthetic query paired with its tool-call — training data
  as a library of examples; pattern and repetition.
- **27** A test arena where an agent-spirit leaps through gates of evaluation; a scoreboard of
  passing runs glowing; proving ground.
- **28** An agent holds a memory-lantern (retrieval) in one hand and a tool in the other, acting
  with both; wisdom + capability combined.
- **29** An agent-entity *sees* an image through an eye and *acts* through a gear at once — the
  multimodal agent demo as one unified being.
- **30** (Boss) A fully assembled multimodal-agent emblem — eye + gear + shield — launching in a
  burst of light; the grand finale; everything you built, whole.

---

**Tips:** Images 16:9; videos 6–12s. Name files exactly as listed. Drop them in `media/`.
The app shows them in the hero + cinematic divider + track breaks; missing files fall back
gracefully to the animated SVG emblems.

# 🎬 ONE-SHOT GROK PROMPT — generate all gauntlet media, then zip

Copy everything below into Grok (image/video mode). After it returns the files, use the
companion `zip_media.sh` (or `zip_media.bat`) to package them — most generators can't zip
their own outputs, so that step is separate.

────────────────────────────────────────────────────────
You are generating concept art + short videos for an interactive coding workbook called
"The Agent Engineer's Gauntlet". Use ONE consistent art style for EVERYTHING:

STYLE (apply to all): Cinematic concept art / motion, deep violet (#1a1140) and cyan
(#56d4ff) palette with electric purple (#8c6eff) accents and ember-gold sparks, dark
atmospheric background, volumetric haze, soft rim lighting, "arcane-tech codex" aesthetic —
glowing circuitry mixed with classical forge/alchemy imagery. NO text, NO letters, NO
watermarks, NO UI elements.

Generate these 35 assets:

IMAGES (16:9, save as the exact filename):
00.png — lone engineer at a glowing crossroads inside a vast dark library of living
  code-streams; three luminous paths diverge into the dark; a faint shield emblem glows
  in the sky. Beginning of a journey.
01.png — constellation of glowing nodes connected by threads of light forming a living
  web; attention flowing between orbiting spheres; one node flares brighter as it gathers.
02.png — towering spire of stacked glowing rings self-assembling mid-air, each ring a
  transformer block locking into place; construction energy crackling upward.
03.png — a single bolt of light fracturing into many smaller diverging sparks — a
  probability cloud of possible next tokens; branching futures.
04.png — river of glowing glyph-characters flowing into a narrowing funnel, a waterfall of
  scrolling text compressed into a context window; counts shimmering as they enter.
05.png — star-map of meaning: points of light in a dark void connected by faint lines into
  clusters — a vector space of concepts; one point pulsing as "you are here".
06.png — hooded seeker holds a lantern that pulls the right glowing tomes from endless
  shelves; irrelevant books dim, relevant ones lift toward the light.
07.png — gear of light merging with a wrench and a floating interface panel; hands of
  energy operating tools; a model learning to act on the world.
08.png — several small shield-emblems orbit and coordinate around a central glowing core, a
  command constellation; lines of intent flowing between them.
09.png — modular glowing panels snapping together like living architecture; a clean
  framework assembling from parts; lean vs heavy contrast.
10.png — great scale of judgment with a glowing checkmark seal; a quality gauge tipping
  toward "pass"; proof etched in light.
11.png — rough stone statue polished and refined by beams of alignment light; a wild form
  becoming a precise, trustworthy figure.
12.png — (boss) massive blazing shield emblem; engineer stands before a gate of pure light;
  final trial of understanding; triumphant, daunting.
13.png — cold empty forge with raw "text ore" waiting; a single spark ascending toward the
  anvil — creating a model from nothing.
14.png — scattered floating letters (a, b, c, ≡) coalescing into an ordered glowing grid —
  a vocabulary being born.
15.png — conveyor of sliding token-windows passing through a luminous machine; batches of
  context flowing in rhythm; data pipeline in motion.
16.png — full GPT spire complete and towering, every transformer block lit, a cathedral of
  computation; awe-inspiring scale.
17.png — roaring forge with loss-sparks falling like embers; a furnace of learning; the
  model tempering as fire cools; heat and focus.
18.png — quill of light writes streaming text flowing from a model's maw; autocomplete
  cascading forward; the moment of generation.
19.png — magnifier of light inspects generated text on a bench; quality being measured; a
  careful evaluator's eye.
20.png — wild glyph-beast shaped into a polite glowing chat-bubble assistant; instruction
  taming chaos.
21.png — (boss) trained LLM core orbiting a server-pillar, launching into the world; the
  shipped model ascending; completion.
22.png — luminous eye merging with a page of flowing text — vision and language fusing into
  one stream of understanding.
23.png — glowing JSON block with executable function tags pulsing; a structured tool-call
  taking shape; precision and schema.
24.png — circular gear-loop with a pulse of light traveling thought → action → observation →
  thought; the agent reasoning cycle as a living ring.
25.png — an image projecting beams of light that land and arrange into a text-space; a
  projector aligning pixels with words; bridge of modalities.
26.png — rows of glowing cards, each a synthetic query paired with its tool-call; training
  data as a library of examples; pattern and repetition.
27.png — test arena where an agent-spirit leaps through gates of evaluation; a scoreboard of
  passing runs glowing; proving ground.
28.png — agent holds a memory-lantern (retrieval) in one hand and a tool in the other, acting
  with both; wisdom + capability combined.
29.png — agent-entity sees an image through an eye and acts through a gear at once; the
  multimodal agent demo as one unified being.
30.png — (boss) fully assembled multimodal-agent emblem — eye + gear + shield — launching in
  a burst of light; the grand finale.

VIDEOS (6–12s each, save as the exact filename):
intro.mp4 — opening title: a glowing forge hall in deep violet/cyan, floating code glyphs
  drifting upward like embers, a massive stone shield emblem etched with circuit traces at
  center; slow camera push-in; looping ambient; no text.
track1-2.mp4 — from understanding to building: a glowing schematic of an abstract AI brain of
  light dissolves and reforges into a roaring forge where raw text-ore is melted into a tower
  of stacked transformer rings; camera pushes in as the forge ignites; 6–10s; no text.
track2-3.mp4 — from model to agent: the completed LLM spire opens a luminous eye (multimodal
  vision) while a gear of tools clicks into its side; the static tower becomes a living,
  thinking agent that reaches out and acts; camera orbits as eye + gear awaken; 6–10s; no text.
finale.mp4 — the whole gauntlet complete: shield emblem, transformer tower, multimodal eye,
  and agent gear-loop spiral together and launch into a burst of light; triumphant, soaring;
  8–12s; no text.

Return all 35 files. Then zip them into "gauntlet-media.zip" if your environment supports
packaging; otherwise list the 35 filenames so I can zip them locally.
────────────────────────────────────────────────────────

NOTE: If Grok returns the files but can't make the zip, run this in the folder where you
saved them (see zip_media.sh / zip_media.bat included with these prompts):
  zip gauntlet-media.zip 00.png 01.png ... 30.png intro.mp4 track1-2.mp4 track2-3.mp4 finale.mp4

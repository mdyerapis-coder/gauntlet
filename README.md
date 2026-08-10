# 🛡️ The Agent Engineer's Gauntlet — *Apprenticeship Edition*
### For builders who direct AI to write the code (like HADA, HPS, llmfit were built)

You're `mdyerapis-coder`. Your repos (HADA, HPS, Pantheon, llmfit) were mostly **AI-written
under your direction.** That's a real skill — but it caps out if you can only *prompt* and
not *direct with understanding.* This gauntlet closes that gap.

**The model is apprenticeship, not copy-paste.** AI is your coding partner / junior dev.
Your responsibility ramps across the 13 missions:

- **Observe & explain** (00–04): AI writes it, you *read what it produced* and explain it.
  You learn the shape of the thing you've been orchestrating.
- **Direct the change** (05–09): you tell AI *what to modify* and *why*; AI writes it; you
  verify. You're the engineer giving the brief.
- **Architect it** (10–12): you sketch the design in plain words; AI implements; you own
  the eval + deploy decision. That's the HPS/HADA role, done deliberately.

Every mission gives you a **🤖 prompt to hand your AI coder** (me, Claude, Codex — whoever
writes your scripts), a **👀 what to watch for** so you understand the output, and a
**✍️ your move** that forces *you* to make the next call. No mission ends at "paste this."

The companion codex (`pdfs/`, 66 files from Raschka's *Build a Large Language Model From
Scratch*) is your **solution reference** — open it when you want to see clean, runnable
code for what you just directed. It's real, not guessed.

## 🎮 How to play
1. Work **one mission at a time.** Tick `[ ]` boxes.
2. For each 🤖 prompt: paste it to your AI coder, get the script, **run it**, read the output.
3. Fill the **✍️ your move** — this is the part only you can do. Don't skip it.
4. Keep `loot.md`: what AI produced, what surprised you, what you'd change in HADA/HPS.
5. Each mission ends in a **🏆 Done when** gate. Clear it before advancing.

## 🗺️ 13 missions
- **00.** Orientation — name the gap, set up your AI-coding arena
- **01.** Attention — get AI to build it; you trace the data flow
- **02.** Build the GPT — AI assembles it; you map the block diagram
- **03.** Decoding & sampling — AI generates; you tune the knobs and explain why
- **04.** Tokens & context — AI counts cost; you find your own context-stuffing
- **05.** Vectors & memory — you *direct* AI to add retrieval to a thing you built
- **06.** RAG from scratch — you brief AI; you pick the chunks that break it
- **07.** Tool use — you design the tool contract; AI wires the loop
- **08.** Orchestration patterns — you map HADA/Pantheon to named patterns
- **09.** Frameworks — you choose one; AI builds; you decide framework-vs-lean
- **10.** Evals — you write the pass/fail; AI runs the suite
- **11.** Fine-tune & align — you spec the model+data; AI trains LoRA/DPO
- **12.** Boss fight — you architect; AI builds; you ship + eval + serve on OVH2

## 🛠️ Track 2 — Build the Full LLM (missions 13–21)
Track 1 taught you to *understand and direct* AI engineering. Track 2 makes you *build
the thing itself*: a complete, tiny-but-real LLM you train from scratch, guided by the
Raschka codex PDFs in `pdfs/`. AI writes the scripts; you run, read, and own them.
- **13.** Intro & setup — config + corpus
- **14.** Tokenizer from scratch (char-level)
- **15.** Dataset & DataLoader (sliding context windows)
- **16.** The full GPT-style model
- **17.** Training loop (loss curve you watch fall)
- **18.** Generate text (sampling on your own weights)
- **19.** Evaluate it (accuracy + perplexity vs random)
- **20.** Instruction-tune it (make it an agent brain)
- **21.** Boss fight — ship your LLM as a serving endpoint

## 🤖 Track 3 — Multimodal + Agent (missions 22–30)
Track 2 built the model. Track 3 makes it *multimodal and agentic* — the kind of system you orchestrate in HADA/Pantheon, now built by you. Frozen vision encoder + trainable projector, a real tool-call loop, RAG memory, and a served agent app.
- **22.** Multimodal: image→text fusion architecture
- **23.** Tool schema & function calling
- **24.** Agent loop with tools (thought→action→observation)
- **25.** Train the multimodal projector
- **26.** Build tool-calling training data
- **27.** Evaluate the agent
- **28.** RAG-backed agent
- **29.** Multimodal + agent demo
- **30.** Boss fight — ship the agent as a serving endpoint

## 🏅 Progress certificate
The app's **🏅 Export certificate** button reads your real tick-box progress and downloads a self-contained `gauntlet-certificate-YYYY-MM-DD.html` showing per-track and overall completion.

## 📦 In the box
- `pdfs/` — 66 Raschka code companion PDFs (ch2–7 + standalone-model bonus). Your codex.
- Companions: `~/linux-learning-workbooks/` (fundamentals), `~/hermes-stack-workbooks/`
  (production deploy). This gauntlet is the AI-engineering rung between them.

Start at `00-orientation---name-the-gap.md`. Your AI coder is ready when you are.

# 🛡️ Mission 00 — Orientation: Name the Gap

**🎯 Your job:** You direct AI to build things (that's how HADA/HPS happened). This
gauntlet makes you a *better director* — so you can tell your AI coder not just "build X"
but "build X *this way* because of Y." First, map the territory.

**🧠 Why:** Your repos treat "the model" as a black box. When an agent loops or a prompt
silently degrades, you can only re-prompt. Understanding the internals turns re-prompting
into *directing.*

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch03/01_main-chapter-code/ch03.pdf` — just the first page.
      Register that the real, runnable attention code is sitting in this folder for you.
- [ ] **Read (free, 10 min):** https://www.anthropic.com/engineering/building-effective-agents
      — note which patterns your HADA/Pantheon already use. One line each.
- [ ] **Audit your own repos for implicit model assumptions** (you directed these — what did
      you assume about the model without checking?):
  - [ ] HADA — assumes model behavior anywhere without verifying?
  - [ ] HPS — deploys models; does anything reason about token cost / context limits?
  - [ ] llmfit — matches hardware; does it reason about *quality* or just fit?
  - [ ] Pantheon — "Gods share one brain" — real retrieval/memory, or context-stuffing?
- [ ] **Set up your AI-coding arena** (so future missions have a place to run what AI writes):
      `python3 -m venv ~/ai-eng && source ~/ai-eng/bin/activate && pip install torch transformers sentence-transformers tiktoken`
- [ ] **Create `loot.md`** with one paragraph: *"Orchestration is ___. Engineering is ___."*

**🤖 Prompt to give your AI coder:** none this mission — setup only. (Future missions use these.)

**👀 What to watch for:** when `pip install torch` finishes, run
`python -c "import torch, transformers; print('arena ready', torch.__version__)"` — if it
prints a version, your arena works and AI can write+run code here.

**✍️ Your move:** In `loot.md`, name **≥2 implicit model assumptions** in your own repos.
This is the gap you're here to close. No AI can do this for you — only you know what you built.

**🏆 Done when:** `loot.md` has your gap paragraph + ≥2 repo assumptions, and
`import torch` works in `~/ai-eng`.

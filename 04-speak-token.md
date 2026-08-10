# 🛡️ Mission 04 — Tokens & Context: AI Counts Cost, You Find Your Own Leak

**🎯 Your job:** Models read *tokens,* not text. AI computes the cost math; **you hunt for
where your own repos stuff context** and would silently truncate. The director's job is
spotting the leak, then briefing AI to fix it (Mission 05/06).

**🧠 Why:** Pantheon's "shared brain" and HADA's evidence archives are big. Context ≠ memory
— it's a fixed buffer that drops the oldest tokens. This is the silent killer of agent loops.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch02/01_main-chapter-code/ch02.pdf` + `pdfs/ch02/05_bpe-from-scratch/bpe-from-scratch.pdf`.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write tokens.py: use tiktoken. (1) tokenize a paragraph with gpt2-BPE
      > vs cl100k_base, print counts. (2) Take 100 lines of a real Go file and report token
      > count + estimated $ cost at $0.50/1M tokens. (3) Send a prompt longer than the model
      > max context and catch the truncation/error."
- [ ] **Run it.** Note Go code tokens vs prose, the $ cost of one full-file read, and the
      truncation behavior.
- [ ] **👀 What to watch for:** code tokenizes ~3–4× denser than prose; long context = slow
      AND pricey (quadratic attention from Mission 01). That's why chunking exists.
- [ ] **Extend preview:** `pdfs/ch05/09_extending-tokenizers/extend-tiktoken.pdf` (adding
      domain vocab — relevant if HPS ever needs it).

**✍️ Your move:** In `loot.md`, list **2 specific places in HADA/Pantheon where you
context-stuff today** (point at real files/behaviors you directed). For each, write one
sentence: *"Replace with retrieval (Mission 06) because ___."* You found the leak; next
missions fix it under your direction.

**🏆 Done when:** AI's token script runs (counts + cost + truncation shown), and `loot.md`
names 2 real context-stuffing spots in your repos with a retrieval-based fix rationale.

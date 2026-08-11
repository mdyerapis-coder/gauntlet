# 🛡️ Mission 04 — Tokens & Context: AI Counts Cost, You Find Your Own Leak

**🎯 Your job:** Models read *tokens,* not text. AI computes the cost math; **you hunt for
where your own repos stuff context** and would silently truncate. The director's job is
spotting the leak, then briefing AI to fix it (Mission 05/06).

**🧠 Why:** Pantheon's "shared brain" and HADA's evidence archives are big. Context ≠ memory
— it's a fixed buffer that drops the oldest tokens. This is the silent killer of agent loops.

**🧩 In plain English:** A model never reads letters or whole words — it reads **tokens**,
chunks of text (often pieces of words) pulled from a fixed vocabulary it learned during
training. The **context window** is the model's entire short-term memory: a hard cap on how
many tokens it can look at in a single call. It is *not* smart storage that keeps the
important bits — it's a fixed-size buffer, and once you're past the cap, the oldest tokens
either get silently dropped or the call errors out, whether or not they mattered. And
tokens aren't free: every one costs real money and real compute, and (because of the
attention math from Mission 01) cost grows faster than linearly as the context gets longer.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch02/01_main-chapter-code/ch02.pdf` — how raw text actually
      becomes token IDs — plus `pdfs/ch02/05_bpe-from-scratch/bpe-from-scratch.pdf`, which
      builds the tokenizer itself from nothing, chunk-merging rule by chunk-merging rule.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write tokens.py: use tiktoken. (1) tokenize a paragraph with gpt2-BPE
      > vs cl100k_base, print counts. (2) Take 100 lines of a real Go file and report token
      > count + estimated $ cost at $0.50/1M tokens. (3) Send a prompt longer than the model
      > max context and catch the truncation/error."
- [ ] **Run it.** Note Go code tokens vs prose, the $ cost of one full-file read, and the
      truncation behavior.
- [ ] **👀 What to watch for:** code tokenizes ~3–4× denser than prose; long context = slow
      AND pricey (quadratic attention from Mission 01). That's why chunking exists.
- [ ] **Extend preview:** `pdfs/ch05/09_extending-tokenizers/extend-tiktoken.pdf` — teaching
      a tokenizer new domain-specific vocabulary (relevant if HPS ever needs it).

**✍️ Your move:** In `loot.md`, list **2 specific places in HADA/Pantheon where you
context-stuff today** (point at real files/behaviors you directed). For each, write one
sentence: *"Replace with retrieval (Mission 06) because ___."* You found the leak; next
missions fix it under your direction.

**🏆 Done when:** AI's token script runs (counts + cost + truncation shown), and `loot.md`
names 2 real context-stuffing spots in your repos with a retrieval-based fix rationale.

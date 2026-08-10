# 🛡️ Mission 05 — Vectors & Memory: You *Direct* AI to Add Retrieval

**🎯 Your job (tier up: Direct the change):** No more just observing. You tell AI *what to
build and why*; AI writes it; you verify. Real "memory" for agents = embeddings + nearest
search. This is how Pantheon's brain *should* work and how HADA could recall evidence
without bloating context (your Mission 04 leak).

**🧠 Why:** You've been directing AI to build things your whole stack is made of. This
mission practices directing AI on the *retrieval primitive* — and verifying it actually works.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch02/03_bonus_embedding-vs-matmul/embeddings-and-linear-layers.pdf`
      (embeddings = learned lookup tables).
- [ ] **🤖 Prompt to give your AI coder (you brief it — note the *why*):**
      > "In ~/ai-eng, write memory.py using sentence-transformers (all-MiniLM-L6-v2). (1)
      > Embed 5 sentences: 2 similar pairs + 1 outlier. Print cosine sim — similar should be
      > ~0.7+, outlier ~0.2. (2) Build a from-scratch vector search over 10 docs (no libs):
      > rank by cosine to a query, return top-3. (3) Rebuild the same with chromadb and assert
      > top-3 matches. (4) Show that embedding the same text with TWO different models gives a
      > meaningless similarity."
- [ ] **Run it.** Confirm similar≈high, outlier≈low, library matches scratch, cross-model sim is junk.
- [ ] **👀 What to watch for:** same-model embedding is non-negotiable; chromadb should match
      your scratch top-3 exactly (if not, AI has a bug — your call to send back).

**✍️ Your move:** In `loot.md`, write the **4-step design to turn HADA's `evidence/` into
retrievable memory**: chunk → embed → index → retrieve-on-demand. For each step, write one
line on *what you'd tell AI to do.* You're architecting the brief, not coding it.

**🏆 Done when:** AI's memory script runs and matches library↔scratch, and `loot.md` has
your 4-step HADA-memory brief.

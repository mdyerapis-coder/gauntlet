# 🛡️ Mission 01 — Attention: Get AI to Build It, You Trace It

**🎯 Your job:** Attention is the engine of every LLM you orchestrate. You won't hand-code
it — you'll **direct your AI coder to build it**, then *you* trace what it produced. The
skill is reading AI's code, not writing it from scratch.

**🧠 Why:** HADA's release gate and Pantheon's "Gods" all sit on attention. When context is
mis-weighted, the bug is here. If you can read the attention code your AI wrote, you can
tell it *how to fix it* — that's directing, not copy-pasting.

**🧩 In plain English:** Read this: *"The trophy didn't fit in the suitcase because it was
too big."* What does "it" refer to — the trophy or the suitcase? You resolved that instantly,
without thinking, by relating "it" back to the right earlier word. Attention is the
mechanical version of that trick. For every word, the model scores how relevant every
*other* word is to it, turns those raw scores into percentages that add up to 100%
(that's all **softmax** is — "turn scores into percentages"), then blends the words
together weighted by those percentages. A **causal mask** is just a rule that says: when
predicting word 5, you're not allowed to peek at words 6, 7, 8 — only look backward, the
way you'd read a sentence left to right without a spoiler.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch03/01_main-chapter-code/ch03.pdf` §3.1–3.3 — the real,
      runnable version of the attention math you're about to direct your AI coder to write.
      Don't copy it — just see the shape so you recognize it in what AI produces.
- [ ] **Bonus:** `pdfs/ch03/02_bonus_efficient-multihead-attention/mha-implementations.pdf`
      — same mechanism, several implementations, one clearly faster. Why naive attention is
      slow (you'll feel this in Mission 04's cost math).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write attention.py implementing single-head scaled dot-product
      > attention in PyTorch: q,k,v → scores = q@k.T/sqrt(d) → softmax → weighted sum of v.
      > Add a 3-token demo with random vectors, print the attention weights, and assert each
      > row sums to ~1. Also add a causal (lower-triangular) mask variant and show future
      > tokens get weight 0."
- [ ] **Run it.** Did weights sum to 1? Did the masked future token read 0? If not, **your
      move** below.
- [ ] **👀 What to watch for:** the softmax over the *last* dimension; the mask must be
      added *before* softmax as -inf. If AI got it wrong, that's your teaching moment.

**✍️ Your move:** Open the file AI wrote. In `loot.md`, **explain in 4 bullet lines** what
each line of the attention function does (in your own words). Then, if the demo had a bug,
write the *one-line fix* you'd tell AI to make. You directed a fix you understand.

**🏆 Done when:** AI's script runs, weights behave (sum-to-1, future=0), and `loot.md` has
your 4-line explanation + (if needed) your directed fix.

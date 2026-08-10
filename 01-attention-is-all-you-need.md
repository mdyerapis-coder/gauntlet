# 🛡️ Mission 01 — Attention: Get AI to Build It, You Trace It

**🎯 Your job:** Attention is the engine of every LLM you orchestrate. You won't hand-code
it — you'll **direct your AI coder to build it**, then *you* trace what it produced. The
skill is reading AI's code, not writing it from scratch.

**🧠 Why:** HADA's release gate and Pantheon's "Gods" all sit on attention. When context is
mis-weighted, the bug is here. If you can read the attention code your AI wrote, you can
tell it *how to fix it* — that's directing, not copy-pasting.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch03/01_main-chapter-code/ch03.pdf` §3.1–3.3 (real attention
      code). Don't copy — just see the shape.
- [ ] **Bonus:** `pdfs/ch03/02_bonus_efficient-multihead-attention/mha-implementations.pdf`
      (why naive attention is slow — you'll feel this in Mission 04's cost math).
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

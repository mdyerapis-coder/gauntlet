# 🛡️ Mission 02 — Build the GPT: AI Assembles, You Map It

**🎯 Your job:** Get AI to assemble a full GPT block stack. You produce the **architecture
map** — the thing HPS deploys and llmfit selects. Knowing the block diagram lets you tell
AI *why* a served model misbehaves.

**🧠 Why:** You provision/serve these. Understanding the internal diagram means you can
brief AI precisely ("add a LayerNorm before the residual," not "fix it").

**🧩 In plain English:** A GPT model is really just: a lookup table that turns each token
into a list of numbers (a vector), then that vector passed through the *same kind* of block
— attention (Mission 01) plus a small extra neural net — repeated N times back to back,
then one final lookup table run in reverse to turn the last vector back into "which token
comes next." Two details make stacking that many blocks actually work: **LayerNorm**, which
just rescales the numbers at each step so they don't explode or shrink to nothing after
passing through dozens of blocks, and a **residual connection** (`x + sublayer(x)`) — a
shortcut wire that carries the original input past a block untouched and adds it back on
top of whatever the block computed. Without that shortcut, stacking many blocks tends to
lose the signal entirely.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch04/01_main-chapter-code/ch04.pdf` §4.1–4.3 — the full
      block-by-block build, the same one your AI coder is about to reproduce below.
- [ ] **Bonus:** `pdfs/ch04/02_performance-analysis/flops-analysis.pdf` — how parameter
      count turns into actual compute cost. This is what llmfit *should* reason about.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, build gpt_model.py: token + positional embeddings, N transformer
      > blocks (reuse attention.py's attention + an MLP), final LayerNorm + linear head to
      > vocab. Print total parameter count. Do one forward pass on a 5-token sentence and
      > assert output shape is (1, 5, vocab)."
- [ ] **Run it.** Confirm output shape. Read the param count.
- [ ] **👀 What to watch for:** residual connections (x + sublayer(x)) and where LayerNorm
      sits (pre- vs post-). These details change behavior — note which AI chose.

**✍️ Your move:** In `loot.md`, draw the **block-stack map in ASCII** (embed → [block ×N →]
→ head) and write the param count. Then: *if you were deploying this via HPS, what's one
config knob you'd expose to the manifest?* (e.g. N blocks, context length). You're
architecting the deploy surface, not coding it.

**🏆 Done when:** AI's model forward-passes, and `loot.md` has your ASCII map + the one
deploy knob you'd expose.

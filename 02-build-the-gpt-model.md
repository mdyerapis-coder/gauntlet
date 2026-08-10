# 🛡️ Mission 02 — Build the GPT: AI Assembles, You Map It

**🎯 Your job:** Get AI to assemble a full GPT block stack. You produce the **architecture
map** — the thing HPS deploys and llmfit selects. Knowing the block diagram lets you tell
AI *why* a served model misbehaves.

**🧠 Why:** You provision/serve these. Understanding the internal diagram means you can
brief AI precisely ("add a LayerNorm before the residual," not "fix it").

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch04/01_main-chapter-code/ch04.pdf` §4.1–4.3.
- [ ] **Bonus:** `pdfs/ch04/02_performance-analysis/flops-analysis.pdf` — how params → compute.
      This is what llmfit *should* reason about.
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

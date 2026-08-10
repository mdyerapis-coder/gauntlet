# 🛡️ Mission 16 — The Full Model (GPT-style)

**🎯 Your job:** Assemble the complete model you scaffolded in Mission 13: token embedding + positional embedding + N transformer blocks (your Mission 01 attention + MLP) + LayerNorm + output head. This is the real thing, not a toy.

**🧠 Why:** Track 1 Mission 02 built a model you could forward-pass. Here you wire it to *your* config and tokenizer so it's trainable on *your* corpus. This is the heart of the LLM you're building.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch04/01_main-chapter-code/ch04.pdf` (full GPT implementation) + `pdfs/ch03/01_main-chapter-code/ch03.pdf` (attention).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write model.py importing ModelConfig from config.py. Build TinyGPT: TokenEmbedding(vocab) + PosEmbedding(context_len), a TransformerBlock (pre-LN: LayerNorm -> MultiHeadAttention(from attention.py/Track1) -> residual -> LayerNorm -> MLP -> residual), repeated n_layers times, then final LayerNorm + Linear(d_model, vocab) head. Use config d_model=64, n_heads=4, n_layers=4. Forward(x) returns logits (B, T, vocab). Print total param count and confirm a (2,32) input yields (2,32,vocab) logits."
- [ ] **Run it.** Confirm output shape and a small param count (CPU-trainable, <1M params).
- [ ] **👀 What to watch for:** pre-LayerNorm ordering and the residual connections. A shape mismatch here breaks training — read the error, tell AI the fix.
- [ ] **✍️ Your move:** in `loot.md`, paste the param count and draw the block stack in ASCII (embed → [block ×4] → head).

**🏆 Done when:** `model.py` forward-passes to correct shape, params are CPU-friendly, and `loot.md` has the count + ASCII diagram.

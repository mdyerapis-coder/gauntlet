# 🛡️ Mission 15 — Dataset & DataLoader

**🎯 Your job:** Turn your tokenized corpus into training batches — sliding context windows the model learns to predict. This is the "input pipeline" every LLM needs.

**🧠 Why:** Track 1 Mission 03/04 showed context windows are finite and costly. Here you *build* the windowing. Getting strides/offsets right is the difference between stable training and garbage.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch02/04_bonus_dataloader-intuition/dataloader-intuition.pdf` and `pdfs/ch02/01_main-chapter-code/ch02.pdf` (data sampling).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write dataset.py: load models/vocab.json + data/tiny.txt, tokenize the whole corpus, and build a DataLoader that yields random (context, target) batches where context is context_len=32 tokens and target is the next token. Use a simple iterable dataset with shuffle. Print one batch's shape (batch, 32) and show the context+target for one example (decode both)."
- [ ] **Run it.** Confirm batch shape `(B, 32)` and that target[i] == context[i+1] (shifted by one).
- [ ] **👀 What to watch for:** the target is always the input shifted by one position — that's the next-token prediction objective. If they don't line up, training will fail silently.
- [ ] **✍️ Your move:** in `loot.md`, write the batch shape and confirm (in your own words) *why target is input shifted by one.*

**🏆 Done when:** `dataset.py` yields correctly-shifted (context, target) batches and `loot.md` explains the shift.

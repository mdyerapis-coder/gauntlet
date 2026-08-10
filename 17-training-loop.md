# 🛡️ Mission 17 — Training Loop

**🎯 Your job:** Write the training loop that turns your data into a trained model. Cross-entropy loss on next-token prediction, an optimizer, and a loss curve you watch fall.

**🧠 Why:** This is where "understanding" becomes "a model exists." You'll own the hyperparameters (lr, epochs, batch) and learn to read a loss curve — the single most useful training signal.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch05/01_main-chapter-code/ch05.pdf` §5 (training loop, loss, evaluation).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write train.py: load config, vocab, dataset. Instantiate TinyGPT, AdamW(lr=3e-3), CrossEntropyLoss. Train for ~20 epochs on batches of 16 with context_len=32. Every epoch print avg loss. Save the best checkpoint to models/tinyllm.pt when loss improves. Keep it CPU-friendly (should finish in a few minutes)."
- [ ] **Run it.** Watch loss fall. If it explodes/NaN, that's your teaching moment.
- [ ] **👀 What to watch for:** loss should decrease steadily. NaN = lr too high or a bug in attention scaling. A flat loss = data/label misalignment (revisit Mission 15 shift).
- [ ] **✍️ Your move:** in `loot.md`, record start vs end loss and one line: *"Loss dropped from X to Y, which means the model learned ___."*

**🏆 Done when:** training runs, loss decreases, `models/tinyllm.pt` is saved, and `loot.md` has start/end loss + your interpretation.

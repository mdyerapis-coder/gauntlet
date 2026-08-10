# 🛡️ Mission 18 — Generate Text (Sampling)

**🎯 Your job:** Load your trained checkpoint and make it *write*. You already studied sampling in Track 1 Mission 03 — now you drive it on your own model.

**🧠 Why:** A model that doesn't generate is just a loss number. Generation is the proof. You'll reuse temperature/top-p from Mission 03, now on weights *you* trained.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch05/01_main-chapter-code/ch05.pdf` (text generation / sampling).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write generate.py: load models/tinyllm.pt + vocab, take a prompt string, encode it, and autoregressively sample the next token (temp=0.8, top-p=0.9) for 50 steps using your generate logic. Decode and print the full output. Also add a 'greedy' (temp=0) mode flag."
- [ ] **Run it** on a short prompt from your corpus. Compare temp=0.8 vs greedy outputs.
- [ ] **👀 What to watch for:** early training → gibberish; later → it repeats corpus phrases. That's expected for a 64-dim model on 20KB. The point is *it learned the distribution*.
- [ ] **✍️ Your move:** in `loot.md`, paste one generated sample and one sentence: *"This shows the model learned ___ but not ___."*

**🏆 Done when:** `generate.py` produces text from your trained model in both sampling modes, and `loot.md` has a sample + honest assessment.

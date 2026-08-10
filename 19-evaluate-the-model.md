# 🛡️ Mission 19 — Evaluate the Model

**🎯 Your job:** Prove your LLM actually learned, with metrics — not vibes. Perplexity + a tiny next-token-accuracy test. (Track 1 Mission 10 was eval for agents; here it's eval for the model itself.)

**🧠 Why:** You shipped HADA with evidence gates. Your own LLM deserves the same rigor. A number you can watch improve across training runs is how you know a change helped.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch05/01_main-chapter-code/ch05.pdf` §5.1 (evaluating generative models) + `pdfs/ch07/03_model-evaluation/llm-instruction-eval-ollama.pdf`.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write eval.py: load models/tinyllm.pt + tokenizer + a held-out slice of data/tiny.txt. Compute (a) next-token accuracy: over N positions, how often does argmax(logits) equal the true next token? (b) a simple perplexity proxy = exp(avg cross-entropy). Print both. Also save results to models/eval.json."
- [ ] **Run it** on the trained checkpoint. You should see accuracy > random (random = 1/vocab) and a finite perplexity.
- [ ] **👀 What to watch for:** accuracy barely above random on a 20KB corpus is *normal* for tiny models. The value is the *comparison* across runs, not the absolute number.
- [ ] **✍️ Your move:** in `loot.md`, record accuracy + perplexity and one sentence: *"Compared to random (1/V), my model does ___% better, meaning it learned ___."*

**🏆 Done when:** `eval.py` reports accuracy + perplexity vs random baseline, and `loot.md` interprets the gap.

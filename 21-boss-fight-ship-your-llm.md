# 🛡️ Mission 21 — Boss Fight: Ship Your LLM

**🎯 Your job (capstone of Track 2):** Wrap your trained model in a tiny serving app so it runs like a real endpoint — the thing HPS would deploy. Generate, evaluate, and expose it. Ties Track 1 Mission 12 (serve on OVH2) to a model *you* built.

**🧠 Why:** Building a model in a notebook is a demo; serving it is engineering. This closes Track 2: you go from "I trained weights" to "I run an LLM."

## 🛠️ Activity
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write serve.py: a minimal HTTP server (stdlib http.server) exposing POST /generate {prompt, temp} -> {text}. It loads models/tinyllm-instruct.pt + tokenizer on startup. Add a tiny HTML form at GET / for trying it in-browser. Bind 127.0.0.1:8001. Print 'LLM ready'."
- [ ] **Run it** (background) and curl `/generate` with a prompt. Confirm it returns generated text.
- [ ] **Eval gate:** run `eval.py` on the instruct checkpoint; require accuracy > random before calling it done.
- [ ] **📦 Package:** copy `models/`, `tokenizer.py`, `config.py`, `serve.py`, `generate.py` into a `my-llm/` folder as your shippable artifact.
- [ ] **✍️ Your move:** write `MY-LLM.md`: what it does, how to run it, its eval numbers, and what you'd add (bigger corpus, BPE, more layers) to make it real. This is Track 2's completion certificate.

**🏆 Done when:** `serve.py` generates via HTTP, eval passes the random baseline, and `MY-LLM.md` documents your shipped model. You built a full LLM from scratch.

🎉 **Track 2 complete, Engineer.** You directed AI to build the tokenizer, data, model, training, eval, and serving of a real (tiny) LLM. That's the whole stack — from orchestrator to model-maker.

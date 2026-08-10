# 🛡️ Mission 30 — Boss Fight: Ship the Agent

**🎯 Your job (capstone of Track 3):** Package everything into one runnable agent app — multimodal input, tool use, RAG memory, evaluation — and serve it like Track 2's boss fight. This is the agent you orchestrate in HADA, now self-contained and built by you.

**🧠 Why:** You've gone from prompting models to *building the model, its tools, its memory, and its serving.* That's the full vertical. This mission proves it composes and ships.

## 🛠️ Activity
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write agent_serve.py: an HTTP server (stdlib) POST /ask {image?, question} -> runs rag_agent/demo_mm_agent pipeline and returns {answer, tool_calls, retrieved}. Add a browser form at GET /. Bind 127.0.0.1:8002. Print 'Agent ready'."
- [ ] **Run it** (background) and curl `/ask` with a question (and optional image). Confirm a structured response.
- [ ] **Eval gate:** run `eval_agent.py` (Mission 27); require the tool-use pass rate to be recorded (even if <100%).
- [ ] **📦 Package:** copy `models/`, `*.py`, `agent_serve.py`, `MY-LLM.md` into `my-agent/` as your shippable artifact.
- [ ] **✍️ Your move:** write `MY-AGENT.md`: what it does, how to run, eval numbers, and what you'd add (bigger vision model, real RAG embeddings, more tools) to make it production-grade. This is Track 3's completion certificate.

**🏆 Done when:** `agent_serve.py` serves the full pipeline, eval is recorded, and `MY-AGENT.md` documents your shipped multimodal agent. 

🎉 **All three tracks complete, Engineer.** You directed AI to build a tokenizer, a trained LLM, a multimodal fusion, tool-use, an agent loop, RAG memory, evals, and two serving apps. From orchestrator to model-maker to agent-builder — that's the whole stack, and you own every layer.

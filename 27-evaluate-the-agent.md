# 🛡️ Mission 27 — Evaluate the Agent

**🎯 Your job:** Prove your agent (Mission 24) works with a real eval — not just one happy-path trace. Build a small agent-eval suite: does it call the right tool, use the observation, and stop?

**🧠 Why:** Track 1 Mission 10 was agent evals abstractly; here you write the suite for *your* agent. Evidence gates (your HADA/HPS style) start with a test like this.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch06/01_main-chapter-code/ch06.pdf` (agent eval ideas) + `pdfs/ch07/03_model-evaluation`.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write eval_agent.py: define 5 test questions (some need tools, some don't). For each, run agent_loop, and check: (a) correct final answer, (b) if a tool was needed, was it called?, (c) did it terminate within max turns? Score pass/fail per case. Print a summary table + overall pass rate. Save to models/agent_eval.json."
- [ ] **Run it.** You won't get 100% on a tiny model — that's fine. The *suite* is the deliverable.
- [ ] **👀 What to watch for:** separate "called right tool" from "right answer." A model can get lucky; the tool-use signal is what you're really measuring.
- [ ] **✍️ Your move:** in `loot.md`, record pass rates and one sentence: *"My agent fails most on ___ because ___."*

**🏆 Done when:** `eval_agent.py` scores the agent on 5 cases with a summary table, and `loot.md` names the failure mode.

# 🛡️ Mission 12 — Boss Fight: You Architect, AI Builds, You Ship + Eval + Serve

**🎯 Your job (capstone):** Everything comes together. You **architect** a small but real AI
service; AI builds it; **you** run the eval gate and make the ship/no-ship call — the HPS/HADA
role, done deliberately.

**🧠 Why:** This connects `linux-learning-workbooks` (deploy) + `hermes-stack-workbooks`
(production) to the AI engineering you just learned. You close the loop: architect → build →
prove → serve.

## 🛠️ Activity
- [ ] **You architect (pick one):**
  - (a) RAG Q&A over `~/hermes-stack-workbooks/` + `~/linux-learning-workbooks/`
  - (b) A "release-evidence checker" agent inspired by HADA's gate
  - (c) An `llmfit`-style "which model fits my box" advisor with a tool call
- [ ] **🤖 Prompt to give your AI coder:** "Build <my pick> in ~/ai-eng, reusing rag.py /
      memory.py / tool loop from earlier missions. Keep it framework-lean (HPS spirit)."
- [ ] **You run the Mission 10 eval** — must pass ≥80% before serving. You decide ship/no-ship.
- [ ] **Serve:** wrap in FastAPI or a systemd service on OVH2 (linux-workbooks cover this).
      Add auth / network allowlist — a live box is not a sandbox.
- [ ] **Observe:** log token usage + latency per call; tie back to Mission 04 cost math.

**✍️ Your move:** Write **`BOSS-FIGHT.md`**: architecture you designed, eval score (your gate),
how to run, what you'd add next. This is your gauntlet-completion certificate — authored by you.

**🏆 Done when:** A working service runs on OVH2, passes your eval ≥80%, is network-hardened,
and `BOSS-FIGHT.md` documents it. You went from directing scripts to architecting systems.

🎉 **Gauntlet complete, Engineer.** You now direct AI on AI-engineering — not by copy-paste,
but by understanding what you're asking for.

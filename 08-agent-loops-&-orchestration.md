# 🛡️ Mission 08 — Orchestration Patterns: You Map HADA/Pantheon

**🎯 Your job:** Step back to *patterns.* You've directed AI to build multi-agent systems;
now **name what you built** and find where it leaks. Deliberate design beats instinct at scale.

**🧠 Why:** Anthropic's patterns will feel familiar — that's the point. You'll see your own
decisions reflected and spot the gaps to brief AI on next time.

## 🛠️ Activity
- [ ] **Read (free):** https://www.anthropic.com/engineering/building-effective-agents —
      prompt chaining, routing, parallelization, orchestrator-worker, evaluator-optimizer.
- [ ] **Map YOUR repos (you know them best):**
  - [ ] HADA → which pattern? (likely orchestrator + evaluator-optimizer w/ evidence gate)
  - [ ] Pantheon → which pattern? (likely routing across specialist "Gods")
  - [ ] Agent Forge → delegation = orchestrator-worker?
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, build a minimal orchestrator-worker: one manager prompt splits a task
      > into 2 subtasks, 2 worker calls, 1 merge call. Print each step. No framework."
- [ ] **Run it.** See the manager→worker→merge flow your own systems do at scale.
- [ ] **Free ref:** https://github.com/microsoft/ai-agents-for-beginners (10 hands-on lessons).

**✍️ Your move:** In `loot.md`, write **one real failure mode** of your orchestration that
this mission's patterns would now let you fix (e.g. no evaluator step, unbounded worker
retries, context overflow manager↔worker). This is the brief you'd give AI next time.

**🏆 Done when:** AI's mini-orchestrator runs, and `loot.md` maps HADA/Pantheon/Agent Forge
to named patterns + ≥1 concrete fix you'd direct.

# 🛡️ Mission 08 — Orchestration Patterns: You Map HADA/Pantheon

**🎯 Your job:** Step back to *patterns.* You've directed AI to build multi-agent systems;
now **name what you built** and find where it leaks. Deliberate design beats instinct at scale.

**🧠 Why:** Anthropic's patterns will feel familiar — that's the point. You'll see your own
decisions reflected and spot the gaps to brief AI on next time.

**🧩 In plain English:** Once you have more than one AI call working together, you're doing
"orchestration," and it turns out there are only a handful of named shapes it takes: a
straight pipeline where one call's output feeds the next (**prompt chaining**), a
switchboard that routes different requests to different specialists (**routing**), several
calls fired at once and combined (**parallelization**), a manager that splits work across
workers and merges their results (**orchestrator-worker**), and a generate→critique→improve
loop (**evaluator-optimizer**). None of this is new theory — it's a vocabulary for systems
you've *already built by instinct.* Naming the pattern you're already running is usually the
fastest way to notice the pattern you're missing.

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

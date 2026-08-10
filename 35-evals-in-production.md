# 🛡️ Mission 35 — Evals in Production (Guardrails)

**🎯 Your job:** Keep the model honest after deploy. Add a live eval gate + a regression check so a bad model version can't silently ship (the evidence-gate discipline from Track 1 Mission 10, now operational).

**🧠 Why:** You ship with evidence gates (HADA/HPS). This mission wires that gate into CI/CD: every new checkpoint must pass evals before it goes live.

## 🛠️ Activity
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write gate.py: load eval_agent.py (Mission 27) results + a thresholds file (min tool-pass-rate, max toxicity-ish heuristic). Exit non-zero if any threshold fails. Also write a guardrail check that rejects outputs containing a blocklist of unsafe patterns. Print PASS/FAIL with reasons."
- [ ] **Run it** against your instruct checkpoint. Confirm it prints PASS (or FAIL with a clear reason).
- [ ] **👀 What to watch for:** a gate that always passes is worse than no gate. Make at least one threshold meaningful (e.g. tool-pass-rate >= 0.6).
- [ ] **✍️ Your move:** in `loot.md`, state your two thresholds and one sentence: *"A deploy gate earns trust only if ___."*

**🏆 Done when:** `gate.py` enforces eval + guardrail thresholds with PASS/FAIL, and `loot.md` records them.

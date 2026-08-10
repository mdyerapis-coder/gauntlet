# 🛡️ Mission 32 — Observability: Logs, Metrics, Traces

**🎯 Your job:** Make the deployed model *visible*. Add structured logs, a token/latency metric, and a trace id per request — the three pillars, applied to your own serving app.

**🧠 Why:** Hermes and HPS are observed systems; you can't operate what you can't see. This mission makes your model service debuggable, the way your real infra is.

## 🛠️ Activity
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write observe.py: extend deploy.py with (1) JSON structured logs (ts, trace_id, model, tokens_in, tokens_out, ms), (2) a /metrics endpoint returning request count + avg latency + error rate as plain text, (3) a per-request trace_id (uuid) threaded through logs. Keep it stdlib. Print a sample log line on one request."
- [ ] **Run it**, send 2–3 requests, and read the `/metrics` output + logs.
- [ ] **👀 What to watch for:** latency should be *measured*, not guessed. If a request is slow, the metric tells you where (token gen vs model load).
- [ ] **✍️ Your move:** in `loot.md`, paste one structured log line and one sentence: *"The metric that matters most for my model is ___ because ___."*

**🏆 Done when:** `observe.py` emits structured logs + `/metrics`, and `loot.md` shows a log line + your key metric.

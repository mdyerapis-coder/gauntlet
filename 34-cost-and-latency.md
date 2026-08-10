# 🛡️ Mission 34 — Cost & Latency Engineering

**🎯 Your job:** Make the model *cheap and fast* enough to run in prod. Quantize, batch, cache, and measure — the levers that turn a demo into a service.

**🧠 Why:** llmfit matches models to hardware for a reason — cost/latency decide whether a feature lives. You'll learn the knobs on your own model.

## 🛠️ Activity
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write optimize.py: add (1) a KV-cache across turns in generate.py so repeated context isn't re-computed, (2) a simple response cache keyed by normalized prompt (TTL optional), (3) a benchmark that reports tokens/sec and p95 latency over 20 requests. Print before/after numbers."
- [ ] **Run it.** Compare latency with vs without the cache.
- [ ] **👀 What to watch for:** caching changes *correctness* if prompts aren't normalized — two prompts that mean the same must hit the same cache key, or you serve stale/wrong text.
- [ ] **✍️ Your move:** in `loot.md`, record before/after latency and one sentence: *"The biggest win was ___; the risk I'd watch is ___."*

**🏆 Done when:** `optimize.py` adds KV/response cache + benchmark, shows a speedup, and `loot.md` reports it.

# 🛡️ Mission 07 — Tool Use: You Design the Contract, AI Wires the Loop

**🎯 Your job:** Function calling is how agents *act* — the backbone of every HADA/Agent
Forge tool step. You design the **tool contract** (what the tool is, what args it takes);
AI wires the execute→feed-back loop.

**🧠 Why:** Your agents already call tools. Designing the contract yourself means you can
spec it precisely and validate it — the discipline HPS wants at a provisioning boundary.

**🧩 In plain English:** Function calling ("tool use") just means the model can, instead of
only outputting prose, output a structured *request* — something like
`{"tool": "get_weather", "args": {"city": "Perth"}}`. Your code reads that request, decides
whether it's valid, actually runs the real function if so, and feeds the result back in so
the model can use it in its next answer. The critical, easy-to-miss point: the model never
*does* anything itself. It only ever asks. Your code is the one deciding whether to trust
and execute that ask — which is exactly why designing the contract (name, arguments, what
counts as valid) is your job, not something to leave to whatever the model happens to emit.

## 🛠️ Activity
- [ ] **Read (free):** https://platform.openai.com/docs/guides/function-calling (protocol is
      provider-agnostic).
- [ ] **Design the contract yourself** (no AI yet): pick ONE tool your stack needs — e.g.
      `verify_artifact(path)` for HADA, or `host_status(ip)` for HPS. Write its name + args +
      what it returns.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, implement the tool contract I designed: <paste your contract>. Build a
      > loop: model emits JSON {tool, args} → parse + validate (reject unknown tool / missing
      > args) → execute → append result → ask model to answer. Use a real chat model via my
      > provider or mock the JSON if no model access."
- [ ] **Run it.** Does validation reject a bad call? Does the loop recover?
- [ ] **👀 What to watch for:** validation MUST happen before execution (security); malformed
      JSON is the common failure — your brief should require a retry path.

**✍️ Your move:** In `loot.md`, write the **contract you designed** + one sentence on how
this loop maps onto HADA's tool-execution (tool → execute → verify → continue). You designed
the spec; AI implemented it. That's directing.

**🏆 Done when:** AI's tool loop runs with validation, and `loot.md` has your tool contract +
the HADA mapping.

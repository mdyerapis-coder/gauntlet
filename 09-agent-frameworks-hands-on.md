# 🛡️ Mission 09 — Frameworks: You Choose One, AI Builds, You Decide Lean-vs-Framework

**🎯 Your job:** You built agents by directing AI (07/08). Now use a framework to see what it
abstracts. **You pick which one**; AI builds; **you decide** when to use it vs roll lean (HPS
spirit).

**🧠 Why:** HPS/HADA are framework-free by design. Knowing what smolagents/langchain/llamaindex
hide lets you choose deliberately — prototype with framework, ship lean.

## 🛠️ Activity — you choose one (or all three, they're small):
- [ ] **smolagents:** https://github.com/huggingface/smolagents — `pip install smolagents`,
      build a CodeAgent with one tool. Compare to your Mission 07 loop.
- [ ] **LangChain:** https://python.langchain.com/docs/tutorials — tool-calling chain; note
      what it handles (retries, parsing, memory).
- [ ] **LlamaIndex:** https://docs.llamaindex.ai — RAG agent over `~/hermes-stack-workbooks`;
      compare to your Mission 06 from-scratch RAG.
- [ ] **🤖 Prompt to give your AI coder:** "Build a working agent with <chosen framework>
      that does <one task from your stack>. Keep it runnable in ~/ai-eng."

**✍️ Your move:** In `loot.md`, write **what the framework hid that you built by hand in 06/07**
(retries? parsing? memory?) and **your rule of thumb**: when would YOU tell AI to use a
framework vs roll lean for an HPS production deploy? You made the architectural call.

**🏆 Done when:** A framework agent runs, and `loot.md` contrasts framework-vs-lean with your
own deploy rule of thumb.

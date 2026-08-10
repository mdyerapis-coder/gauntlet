# 🛡️ Mission 28 — RAG-Backed Agent

**🎯 Your job:** Give your agent a memory. Combine Track 1 Mission 06 (RAG) with your Mission 24 agent loop: the agent can *retrieve* from a doc store before answering, and call tools too.

**🧠 Why:** Real agents (HADA) blend retrieval + tools + reasoning. This mission fuses three things you've built into one system — the integration is the engineering.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch06/01_main-chapter-code/ch06.pdf` (RAG + agents) + your Mission 06 notes.
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write rag_agent.py: index data/tiny.txt (or a small facts file) with a simple TF-IDF/keyword retriever into a 'context' string. Extend agent_loop so before answering, it retrieves top-k chunks and injects them as context. Add a 'lookup' pseudo-tool the model can call to fetch more. Print a question that needs retrieval, showing the retrieved context + final answer."
- [ ] **Run it** on a question whose answer is in the doc but not memorizable from 20KB. Confirm retrieval context appears in the prompt.
- [ ] **👀 What to watch for:** retrieval without a *citation check* can hallucinate. Note in loot.md whether the agent actually used the retrieved text or ignored it.
- [ ] **✍️ Your move:** in `loot.md`, paste the retrieved context + answer and one sentence: *"Retrieval helped / didn't help because ___."*

**🏆 Done when:** `rag_agent.py` retrieves context into the agent loop and answers a doc-based question, and `loot.md` assesses whether retrieval was used.

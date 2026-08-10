# 🛡️ Mission 24 — Agent Loop With Tools

**🎯 Your job:** Close the loop. Build the reasoning cycle: model emits a tool call → you execute it → you feed the result back → repeat until the model answers. This is the agent you orchestrate in HADA, now running on *your* model.

**🧠 Why:** Track 1 Mission 08 mapped orchestration patterns. Here you *implement* the core one: thought → action → observation, bounded by a max-iteration guard. Owning this loop means you can debug agent failures at the source.

## 🛠️ Activity
- [ ] **Open the codex:** re-read `pdfs/ch06/01_main-chapter-code/ch06.pdf` (the agent chapter) and your Mission 23 `tools.py`.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write agent_loop.py: import TinyGPT generate (generate.py), tools.py. Loop up to 5 turns: (1) prompt model with system + conversation; (2) if it emits a <tool> block, parse+dispatch and append the result as an 'observation'; (3) else treat output as final answer and stop. Print each turn. Use a toy question needing the calculator tool."
- [ ] **Run it** on a question like 'What is 17 * 23, then add 5?'. Confirm it calls the tool, gets the observation, and gives the final answer.
- [ ] **👀 What to watch for:** without the iteration cap the loop can spin forever. The guard is a safety feature, not optional.
- [ ] **✍️ Your move:** in `loot.md`, paste the turn-by-turn trace and one sentence: *"The loop terminated because ___."*

**🏆 Done when:** `agent_loop.py` solves a tool-needing question via the thought→action→observation cycle, and `loot.md` has the trace.

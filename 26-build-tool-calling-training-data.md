# 🛡️ Mission 26 — Build Tool-Calling Training Data

**🎯 Your job:** Make your instruction model actually *emit* tool calls. Write a synthetic data generator that produces (query → tool-call) pairs in the format Mission 23 defined, then fine-tune on it.

**🧠 Why:** A model only calls tools if it was trained to. This closes the loop between "I defined a tool format" (23) and "the model uses it" (24). You become the data engineer, not just the architect.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch07/01_main-chapter-code/ch07.pdf` §7 (instruction data, tool calls).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write tool_data.py: generate 20 synthetic (user query, expected <tool>name args</tool>) pairs using your tools.py schemas (weather, calculator). Write them as instruction-format text to data/tool_instr.txt with a clear system prefix. Print 3 examples."
- [ ] **Run it.** Inspect the format matches what `parse_tool_call` expects in Mission 23.
- [ ] **👀 What to watch for:** the training text format MUST match the inference format exactly, or the model learns a dialect no parser understands. Diff them.
- [ ] **✍️ Your move:** in `loot.md`, paste one generated pair and one sentence: *"Train/infer format match matters because ___."*

**🏆 Done when:** `tool_data.py` emits matched-format pairs, and `loot.md` shows one + the match rationale.

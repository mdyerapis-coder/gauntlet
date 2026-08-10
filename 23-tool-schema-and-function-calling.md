# 🛡️ Mission 23 — Tool Schema & Function Calling

**🎯 Your job:** Give your LLM hands. Define a JSON tool schema and the parse/dispatch loop that turns the model's text output into a real function call. (Track 1 Mission 07 was tool use at the agent level; here it's *inside* the model you built.)

**🧠 Why:** This is the bridge from "chatbot" to "agent." You already saw tool contracts in Mission 07 — now you implement the *mechanism* the model speaks: a structured tool-call format it emits, and your code that executes it.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch07/01_main-chapter-code/ch07.pdf` (instruction finetuning w/ tools) + revisit `pdfs/ch06` tool patterns.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write tools.py: define TWO tools as JSON schemas — get_weather(city) and calculator(expr). Write parse_tool_call(text) that extracts a <tool>name args JSON</tool> block the model emits, and dispatch(name, args) that calls the real python function. Add a system prompt string instructing the model to emit that block. Print a parsed call for a sample model output."
- [ ] **Run it** with a hand-written sample model output containing a tool block. Confirm dispatch calls the real function and returns its result.
- [ ] **👀 What to watch for:** the format the model emits must be *unambiguously parseable* (hence the XML-ish tags). This is why real APIs use strict schemas, not free text.
- [ ] **✍️ Your move:** in `loot.md`, show one parsed tool call + result and one sentence: *"Strict tool format matters because ___."*

**🏆 Done when:** `tools.py` parses + dispatches a tool call to a real function, and `loot.md` shows it.

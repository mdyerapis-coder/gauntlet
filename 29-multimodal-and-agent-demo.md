# 🛡️ Mission 29 — Multimodal + Agent Demo

**🎯 Your job:** Wire it all together: an agent that can *see* an image (Mission 22/25) and *act* with tools (23/24) in one demo. This is the capstone integration before the boss fight.

**🧠 Why:** Each prior mission was a part. This proves the parts compose — the defining test of good architecture. If fusion + tools fight each other, you've found a real design flaw to fix.

## 🛠️ Activity
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write demo_mm_agent.py: load TinyGPT + vision_fuse projector + tools. Flow: user gives an image + a question (e.g. 'how many red shapes? then multiply by 3'). Encode image to tokens, prepend to the prompt, run agent_loop with the calculator tool. Print image tokens count, the tool call, the observation, and the final answer."
- [ ] **Run it.** Even if answers are rough (tiny model), confirm the *pipeline* flows: image → tokens → tool → answer.
- [ ] **👀 What to watch for:** token ordering. Image tokens must sit where the model expects them (you fixed this in 22). A misplaced image block silently breaks grounding.
- [ ] **✍️ Your move:** in `loot.md`, paste the pipeline trace and one sentence: *"Image+tool composition worked because ___ / broke because ___."*

**🏆 Done when:** `demo_mm_agent.py` runs the full image→reason→tool→answer pipeline, and `loot.md` has the trace + assessment.

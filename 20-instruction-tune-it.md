# 🛡️ Mission 20 — Instruction-Tune It (Make It an Agent Brain)

**🎯 Your job:** Turn your base LLM into something that follows instructions — the bridge from "text completer" to "agent you can prompt." LoRA-style or full fine-tune on a tiny instruction set.

**🧠 Why:** This is the leap your whole stack implies — HADA/Pantheon are *orchestrators* around a model that follows instructions. Here you make the follower. Ties Track 1 Mission 11 (fine-tune) to your own weights.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch07/01_main-chapter-code/ch07.pdf` (instruction finetuning) + `pdfs/ch06/01_main-chapter-code/ch06.pdf`.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write instruct.py: build a tiny instruction dataset (10 examples: 'Task: summarize. Input: <line>. Output: <shorter line>') from data/tiny.txt. Load models/tinyllm.pt, fine-tune for a few epochs with a masked loss on the response portion only. Save models/tinyllm-instruct.pt. Print loss at start vs end."
- [ ] **Run it.** Load the instruct checkpoint in `generate.py` with an instruction-style prompt and compare to the base model's output.
- [ ] **👀 What to watch for:** instruction tuning on 10 examples is a demo, not magic — expect subtle shifts, not transformation. The architecture (loss on response only) is the real lesson.
- [ ] **✍️ Your move:** in `loot.md`, write one instruction prompt and contrast base vs instruct output in one sentence.

**🏆 Done when:** `instruct.py` trains a response-masked checkpoint, you compared base vs instruct outputs, and `loot.md` documents the difference.

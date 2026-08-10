# 🛡️ Mission 03 — Decoding & Sampling: AI Generates, You Tune the Knobs

**🎯 Your job:** Generation is a distribution → text. The knobs (temperature, top-p,
repetition penalty) decide whether your agents sound sane or unhinged. AI builds the
generator; **you tune and explain why** each knob does what it does.

**🧠 Why:** Pantheon's "Gods" go wild/repetitive? Usually sampling, not prompts. Agent
*tool-call* steps want temp≈0. Knowing this lets you tell AI *which setting* for which step.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch05/01_main-chapter-code/ch05.pdf` (generation/eval, §5.1).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, load gpt2 via transformers. Write generate.py that takes a prompt and
      > temperature, runs greedy (argmax) and multinomial sampling, and prints output at
      > temp 0.2 / 0.8 / 1.2. Also print the raw logits shape for one step."
- [ ] **Run it.** Watch deterministic → creative → chaotic across the three temps.
- [ ] **👀 What to watch for:** greedy = temp→0 = the *most likely* path. That's what eval
      AND tool-calls should use. Multinomial = "roll the dice" scaled by temp.
- [ ] **Preview serving:** skim `pdfs/ch05/11_qwen3/standalone-qwen3-plus-kvcache.pdf` —
      KV-cache is what makes generation fast at serve time (revisit Mission 12).

**✍️ Your move:** In `loot.md`, define **temperature / top-p / repetition penalty /
max_tokens in one line each**, and state **which temp you'd set for a HADA tool-call step
vs a Pantheon creative "God," and why.** You're setting policy AI will implement.

**🏆 Done when:** AI's generator runs at 3 temps, and `loot.md` has your 4 definitions + the
temp policy for tool-calls vs creative Gods.

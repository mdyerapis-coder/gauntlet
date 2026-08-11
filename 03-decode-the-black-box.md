# 🛡️ Mission 03 — Decoding & Sampling: AI Generates, You Tune the Knobs

**🎯 Your job:** Generation is a distribution → text. The knobs (temperature, top-p,
repetition penalty) decide whether your agents sound sane or unhinged. AI builds the
generator; **you tune and explain why** each knob does what it does.

**🧠 Why:** Pantheon's "Gods" go wild/repetitive? Usually sampling, not prompts. Agent
*tool-call* steps want temp≈0. Knowing this lets you tell AI *which setting* for which step.

**🧩 In plain English:** After all that attention math, the model doesn't spit out a word —
it spits out a probability for *every* word in its vocabulary ("35% chance the next word is
'cat', 12% chance it's 'dog', ..."). Something still has to pick one. **Greedy** decoding
always takes the single highest-probability word — safe, deterministic, but repetitive.
**Sampling** rolls a weighted die over those probabilities instead. **Temperature** is the
dial that reshapes that die: low temperature (near 0) squashes it toward "always pick the
favorite" (≈greedy); high temperature flattens it toward "anything goes" (more surprising,
sometimes incoherent). **Top-p** just trims the die down to only the top slice of likely
words before you roll, so it can never land on something absurd no matter how high the
temperature is.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch05/01_main-chapter-code/ch05.pdf` (generation/eval, §5.1)
      — the same greedy-vs-sampling code your AI coder is about to write below.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, load gpt2 via transformers. Write generate.py that takes a prompt and
      > temperature, runs greedy (argmax) and multinomial sampling, and prints output at
      > temp 0.2 / 0.8 / 1.2. Also print the raw logits shape for one step."
- [ ] **Run it.** Watch deterministic → creative → chaotic across the three temps.
- [ ] **👀 What to watch for:** greedy = temp→0 = the *most likely* path. That's what eval
      AND tool-calls should use. Multinomial = "roll the dice" scaled by temp.
- [ ] **Preview serving:** skim `pdfs/ch05/11_qwen3/standalone-qwen3-plus-kvcache.pdf` — a
      **KV-cache** is just re-using the attention math you already computed for earlier
      tokens instead of redoing it every step; it's what makes generation fast at serve time
      (revisit Mission 12).

**✍️ Your move:** In `loot.md`, define **temperature / top-p / repetition penalty /
max_tokens in one line each**, and state **which temp you'd set for a HADA tool-call step
vs a Pantheon creative "God," and why.** You're setting policy AI will implement.

**🏆 Done when:** AI's generator runs at 3 temps, and `loot.md` has your 4 definitions + the
temp policy for tool-calls vs creative Gods.

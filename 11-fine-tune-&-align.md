# 🛡️ Mission 11 — Fine-Tune & Align: You Spec Model+Data, AI Trains

**🎯 Your job:** Make a model *yours.* You specify the **base model + training data + eval**;
AI does the LoRA/DPO training. Tie the base-model pick back to what llmfit would allow.

**🧠 Why:** llmfit matches hardware to models, but what if you need a model fluent in your
domain (HPS provisioning, HADA release policy)? You architect the fine-tune; AI executes.

**🧩 In plain English:** Fine-tuning takes an already-trained general model and nudges its
weights toward a specific task or style using your own examples, instead of training
something from zero. **LoRA** is a cheap way to do that: instead of updating all of the
model's parameters (expensive — you'd need to store a full new copy), you freeze the
original weights and train a small set of new ones bolted alongside them, often well under
1% of the original parameter count. **DPO** is a fine-tuning method that skips the extra
step of training a separate "reward model" — instead it learns directly from pairs of (a
good response, a bad response) to the same prompt, nudging the model toward the good one.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch06/01_main-chapter-code/ch06.pdf` (classification finetune)
      + `pdfs/ch07/01_main-chapter-code/ch07.pdf` (instruction finetune). For DPO:
      `pdfs/ch07/04_preference-tuning-with-dpo/dpo-from-scratch.pdf`.
- [ ] **You write the spec (no AI yet):** pick a base model *llmfit would allow on your HW*,
      a tiny instruction set (e.g. "given a release log, decide pass/fail"), and the Mission-10
      eval that proves it worked.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng (pip install peft), load <base model>, attach LoRA to attention, train on
      > <my tiny set>, print trainable-param % (should be <<100%), and run my eval.py. If no
      > GPU, simulate the training loop and report the expected param savings."
- [ ] **Run it.** Confirm LoRA trains far fewer params than full finetune.
- [ ] **👀 What to watch for:** DPO needs (chosen, rejected) pairs, not a reward model —
      see `create-preference-data-ollama.pdf`. Match the method to your data.

**✍️ Your move:** In `loot.md`, write the **fine-tune spec for one of your repos**: base model
(tied to llmfit), data source (e.g. HADA release decisions), eval (your Mission 10 gate). You
authored the brief; AI trains.

**🏆 Done when:** AI's LoRA trains (or simulates with reported savings), and `loot.md` has your
repo-specific fine-tune spec (model + data + eval).

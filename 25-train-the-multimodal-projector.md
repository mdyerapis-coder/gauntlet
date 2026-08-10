# 🛡️ Mission 25 — Train the Multimodal Projector

**🎯 Your job:** Actually train the projector from Mission 22 on an image↔caption pair set, so your model learns to align pixels with words. Frozen vision, trainable projector — the standard recipe.

**🧠 Why:** Building the shape (Mission 22) proves you understand fusion. *Training* it proves the alignment works. This is exactly how CLIP-style and LLaVA-style models bootstrap multimodality cheaply.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch05/01_main-chapter-code/ch05.pdf` (training) + `pdfs/ch06` multimodal references.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write train_mm.py: make a tiny dataset of 5 (image, caption) pairs (generate simple PIL images + captions). Load vision_fuse.py encoder+projector. Train the projector (frozen ViT) with a contrastive or caption-MSE loss for a few epochs so image tokens predict caption tokens. Save models/projector.pt. Print loss start vs end."
- [ ] **Run it.** Loss should drop. The projector is tiny, so CPU training is fast.
- [ ] **👀 What to watch for:** only the projector's params should require grad. If ViT trains too, you'll overfit 5 images instantly and learn nothing general.
- [ ] **✍️ Your move:** in `loot.md`, record loss start vs end and one sentence: *"Frozen encoder + trained projector works because ___."*

**🏆 Done when:** `train_mm.py` trains only the projector, loss falls, `models/projector.pt` saved, and `loot.md` explains the frozen/trainable split.

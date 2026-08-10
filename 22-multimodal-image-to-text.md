# 🛡️ Mission 22 — Multimodal: Image→Text Pipeline

**🎯 Your job:** Extend your LLM into a multimodal model. You won't train a vision tower from scratch (that needs GPUs), but you'll *build the architecture* that fuses an image encoder with your text model — and wire in a pretrained vision encoder so it runs on CPU.

**🧠 Why:** Modern agents (and your HADA/Pantheon work) aren't text-only. Understanding the fusion point — where pixels become tokens your LLM can attend to — is the real lesson. You build the connector; the vision weights are frozen pretrained.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch06/01_main-chapter-code/ch06.pdf` (optional: any `pdfs/standalone/` vision references).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write vision_fuse.py: load a pretrained torchvision ViT-tiny image encoder (frozen), and a small Linear 'projector' mapping its embedding dim to your ModelConfig.d_model=64. Write encode_image(path)->tensor(1, n_patches, 64) and a function to prepend image tokens to a text token sequence so your TinyGPT can attend over both. Print shapes for a sample image + a caption prompt."
- [ ] **Run it** on a tiny test image (create one with PIL if needed). Confirm image tokens have shape (1, n_patches, 64) and concatenate with text tokens.
- [ ] **👀 What to watch for:** the projector is the *only* thing you'd train in a real multimodal setup. Frozen vision + trainable projector is the standard LoRA-era recipe.
- [ ] **✍️ Your move:** in `loot.md`, write the image-token count vs text-token count and one sentence: *"The projector matters because ___."*

**🏆 Done when:** `vision_fuse.py` produces fused (image+text) token sequences of shape (1, n_img+n_txt, 64), and `loot.md` records it.

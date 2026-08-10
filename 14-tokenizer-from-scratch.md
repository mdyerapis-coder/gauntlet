# 🛡️ Mission 14 — Tokenizer From Scratch

**🎯 Your job:** A model reads tokens, not text. Build your own tokenizer over your corpus so you *own* the vocabulary. (Track 1 Mission 04 covered BPE theory; here you make one that fits your model.)

**🧠 Why:** llmfit matches models to hardware, but the tokenizer decides your vocab size and sequence length — both feed directly into the config you set in Mission 13. Understanding it means you can debug "unknown token" and length issues yourself.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch02/05_bpe-from-scratch/bpe-from-scratch.pdf` and `pdfs/ch02/01_main-chapter-code/ch02.pdf` §2 (tokenization).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write tokenizer.py: a character-level tokenizer for data/tiny.txt. It should learn the unique chars, build char→id and id→char maps, and expose encode(text)->list[int] and decode(list[int])->str. Save the vocab (chars + special <pad>/<eos>) to models/vocab.json. Print vocab size. Then encode+decode a sample line and assert round-trips exactly."
- [ ] **Run it.** Vocab size should be small (chars only, ~30–60). Confirm a string encodes then decodes back identically.
- [ ] **👀 What to watch for:** char-level is the simplest possible tokenizer and perfect for a tiny model. Word/subword (BPE) scales better but needs more data — note this tradeoff in loot.md.
- [ ] **✍️ Your move:** in `loot.md`, write the vocab size and one sentence: *"I used char-level because ___; I'd switch to BPE if ___."*

**🏆 Done when:** `tokenizer.py` round-trips text, `models/vocab.json` exists, and `loot.md` records vocab size + your tokenizer rationale.

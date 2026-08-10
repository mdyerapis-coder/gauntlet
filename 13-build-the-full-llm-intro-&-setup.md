# 🛡️ Mission 13 — Build the Full LLM: Intro & Setup

**🎯 Your job:** This starts Track 2. Track 1 (00–12) taught you to *understand and direct* AI engineering. Track 2 makes you *build the thing itself* — a complete, tiny-but-real LLM you train from scratch. AI writes the scripts; you run them, read them, and own the design decisions.

**🧠 Why:** You orchestrate models daily (HADA, Pantheon, llmfit). Here you become the person who *made one*. By Mission 24 you'll have a trained model that generates text and chats — not a black box, something you built.

## 🛠️ Activity
- [ ] **Open the codex map:** skim `pdfs/setup/02_installing-python-libraries/python_environment_check.pdf` and `pdfs/ch02/01_main-chapter-code/ch02.pdf` (first page). This track follows Raschka's *Build a LLM From Scratch*, which these PDFs are the runnable companion to.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, create a project scaffold for building a tiny LLM from scratch: folders data/ and models/, a config.py with a ModelConfig dataclass (vocab_size, d_model=64, n_heads=4, n_layers=4, context_len=32, dropout=0.1), and a requirements note (torch, numpy, tiktoken). Also write data/make_corpus.py that generates a ~20KB lowercase text corpus (a fable or repeated simple sentences) into data/tiny.txt. Print confirmation."
- [ ] **Run it.** Confirm `config.py`, `data/tiny.txt` (~20KB) exist.
- [ ] **👀 What to watch for:** the config is the *contract* for every later mission. Keep d_model small (64) so CPU training finishes in minutes.
- [ ] **✍️ Your move:** in `loot.md`, write one sentence: *"My tiny LLM's job is ___ (e.g. complete fable text / answer 3 toy questions)."* This scopes the whole track.

**🏆 Done when:** `config.py` + `data/tiny.txt` exist, and `loot.md` states your LLM's one-line purpose.

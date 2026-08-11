# 🛡️ Mission 10 — Evaluations: You Write the Pass/Fail, AI Runs the Suite

**🎯 Your job (top tier: Architect):** The most underrated AI-engineering skill. You write
the **evaluation spec** (questions + pass/fail); AI builds + runs the suite. Evals turn
"vibes" into signal — and HADA's evidence gate is really an eval you already believe in.

**🧠 Why:** You've been patching agents by feel. Writing the eval yourself means you can tell
AI *how to prove* an agent works, then trust the result.

**🧩 In plain English:** An eval is just a test suite, except the thing under test is a
model or an agent instead of ordinary code: a fixed list of questions with known-good
answers, run automatically every time something changes, and scored (pass/fail, or graded
by a second model acting as judge — "LLM-as-judge"). Without one, "did that prompt tweak
actually help?" gets answered by vibes. With one, it gets answered by a number that either
moved or didn't. Today you write the questions and the bar yourself, *before* any AI
touches it — that's the part only you can do, because only you know what "correct" means
for your system.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch07/03_model-evaluation/llm-instruction-eval-ollama.pdf` (and
      the `-openai.pdf` variant). See how the book evaluates instruction-following.
- [ ] **You write the eval spec (no AI yet):** take your Mission 06 RAG bot. Write 5 questions
      with known answers from your docs. Define: correct / partial / wrong. Set a pass bar (≥80%).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write eval.py that runs my 5 questions against rag.py, scores each
      > correct/partial/wrong, computes accuracy %, and also runs an LLM-as-judge grade.
      > Print both my manual key vs judge, and flag disagreements."
- [ ] **Run it.** Does it pass your bar? Do you + the judge agree?
- [ ] **Correlation:** skim `pdfs/ch07/03_model-evaluation/scores/correlation-analysis.pdf`
      — why you check whether an automated judge's grades actually track a human's.

**✍️ Your move:** In `loot.md`, **design one eval for a real HADA/HPS step** — e.g. "does the
release gate reject a tampered artifact?" Write the pass/fail criterion *you* would accept.
You specified the proof; that's the engineer's job.

**🏆 Done when:** AI's eval suite runs on your RAG bot, and `loot.md` has a real HADA/HPS eval
spec with a pass criterion you wrote.

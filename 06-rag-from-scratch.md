# 🛡️ Mission 06 — RAG From Scratch: You Brief AI, You Pick the Breaking Chunks

**🎯 Your job:** RAG = give the model *only relevant chunks* instead of the whole archive.
Direct AI to build the pipeline; **you choose the query that breaks it** — that's how you
learn what retrieval can and can't do.

**🧠 Why:** Fixes the Mission 04 leak for real. HADA evidence + Pantheon brain are retrieval
problems. You'll direct the build, then stress-test it yourself.

## 🛠️ Activity
- [ ] **Reuse loot:** AI's `memory.py` from Mission 05 is your retrieval engine.
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write rag.py: chunk a folder of markdown (e.g. ~/hermes-stack-workbooks)
      > into ~200-token pieces, embed+index via memory.py, retrieve top-3 for a question, and
      > prompt gpt2-small (or a chat model) with ONLY those chunks to answer. Print the answer
      > + which chunks were used."
- [ ] **Run it** on a question whose answer lives deep in the docs.
- [ ] **👀 What to watch for:** token cost vs full-context; does it actually use the right chunk?
- [ ] **Your stress test:** pick a question whose answer is *split across two chunks* or
      *buried under a near-miss chunk*. Watch it fail or hallucinate confidently.

**✍️ Your move:** In `loot.md`, record (a) the token savings vs dumping the whole doc, and
(b) the exact query you chose that broke retrieval + *why* it broke (e.g. "answer spanned
chunk boundary," "a distractor chunk scored higher"). You diagnosed a real RAG failure mode.

**🏆 Done when:** AI's RAG runs, you measured savings, and `loot.md` documents a real
retrieval failure you deliberately triggered + its cause.

# 🛡️ Mission 31 — Ship to Production (OVH2 / HPS-style)

**🎯 Your job:** Take your Track 2/3 artifacts and actually deploy them — a real serving endpoint behind a process manager, the way HPS provisions machines and Hermes deploys agents. This is where "it runs on my laptop" becomes "it's live."

**🧠 Why:** You build infra (HADA, HPS, Pantheon). Deployment is the verdict — everything before was practice. Owning the deploy path means you can ship your own models, not just train them.

## 🛠️ Activity
- [ ] **Open the codex:** `pdfs/ch06/01_main-chapter-code/ch06.pdf` (deployment patterns) + re-read `pdfs/ch05` (serving).
- [ ] **🤖 Prompt to give your AI coder:**
      > "In ~/ai-eng, write deploy.py: a production-ish server for models/tinyllm-instruct.pt using stdlib http.server behind a tiny process wrapper. Bind 0.0.0.0:8000, add a /health endpoint, basic request logging, and a graceful shutdown. Print 'listening'. (No docker needed; mention what HPS would add: manifest-driven provisioning, SHA-256 gating.)"
- [ ] **Run it** (background) and `curl /health`. Confirm it returns ok.
- [ ] **👀 What to watch for:** binding 0.0.0.0 exposes it to the network — fine locally, but in prod you'd gate it (HPS does SHA-256 gating). Note that in loot.md.
- [ ] **✍️ Your move:** in `loot.md`, write one line: *"To make this prod-safe I'd add ___ (auth / rate limit / TLS)."*

**🏆 Done when:** `deploy.py` serves `/health` + `/generate` and `loot.md` lists your prod-hardening plan.

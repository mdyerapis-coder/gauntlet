# 🛡️ The Agent Engineer's Gauntlet — One-Click Edition

Download, unzip, **double-click `gauntlet.html`**. That's it. No terminal, no pip,
no signing in, works offline for the workbook. For the **built-in AI Coder** (Run with
AI / Expand gauntlet), follow the one-time setup below.

## What you get
- **`gauntlet.html`** — the whole interactive gauntlet in one file. Open in any browser.
  Click a mission → tick boxes (saved in your browser) → copy-button on every 🤖 prompt.
- **`gauntlet-proxy.py`** — tiny same-origin CORS proxy (no deps) so the AI Coder can
  reach OpenCode Zen / cloud models from the browser without CORS blocks.
- **`pdfs/`** — 66 Raschka code companion PDFs (*Build a Large Language Model From Scratch*).
- `build_html.py`, `gauntlet.py`, mission `.md` — sources, if you want the terminal CLI.

## 🔌 One-time AI Coder setup (OpenCode Zen, free)
1. Start the proxy (from this unzipped folder):
   ```
   python3 gauntlet-proxy.py
   ```
   It prints `http://localhost:8000` and forwards `/zen/*` → `https://opencode.ai/zen/*`.

   **Or just double-click a launcher:** `start.command` (macOS/Linux), `start.sh` (Linux),
   or `start.bat` (Windows) — each starts the proxy and opens `gauntlet.html` for you.
2. Open `gauntlet.html`, click **⚙ AI Coder** (top-right).
3. Provider: **OpenCode**. It auto-fills:
   - Base URL: `http://localhost:8000/zen/v1`
   - Model: `deepseek-v4-flash-free`  (a free Zen coder model)
4. Paste your **Zen API key** (from opencode.ai/zen → your account) into the key field.
5. Save. Now every mission's **▶ Run with AI** generates real code via the free model.

> No key? You can still use the workbook fully offline — the AI Coder is optional.
> Prefer a cloud model instead? Pick OpenRouter / Anthropic / OpenAI in the gear and
> enter that provider's key + model.

## How to use
- Click **▶ Play guided tour** or any mission card.
- Hand the 🤖 prompts to the AI Coder (or your own agent). It writes the scripts.
  You do the **✍️ Your move** parts — that's where the learning is.
- **✨ Expand gauntlet** lets the AI draft a new mission and append it.

🎉 Good luck, Engineer.

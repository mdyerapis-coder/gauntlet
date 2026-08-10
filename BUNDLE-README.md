# 🛡️ The Agent Engineer's Gauntlet — One-Click Edition

Download, unzip, **double-click `gauntlet.html`**. That's it. No terminal, no pip,
no signing in, works offline.

## What you get
- **`gauntlet.html`** — the whole interactive gauntlet in one file. Open it in any
  browser (Chrome, Safari, Firefox, Edge). Click a mission → tick boxes → progress
  saves in your browser automatically. Copy-button on every 🤖 AI-coder prompt.
- **`pdfs/`** — 66 Raschka code companion PDFs (*Build a Large Language Model From
  Scratch*). The "codex" — open them when a mission points you to one. They're real,
  runnable notebooks.

## How to use
1. Unzip this folder anywhere.
2. Double-click `gauntlet.html`.
3. Click **▶ Play guided tour** or any mission card.
4. Hand the 🤖 prompts to *your* AI coder (Claude, Codex, OpenCode, me). It writes the
   scripts. You do the **✍️ Your move** parts — that's where the learning is.
5. Your ticks are saved locally. To reset: the **Reset progress** button.

## The model
AI writes the scripts (like HADA/HPS were built). You **direct & understand**. Missions
ramp your responsibility: observe → direct → architect. No passive copy-paste.

## Build it yourself (optional)
The HTML is generated from the mission `.md` files:
```
python3 build_html.py   # regenerates gauntlet.html from *.md
```
The `.md` files and `gauntlet.py` CLI are included too if you prefer the terminal.

🎉 Good luck, Engineer.

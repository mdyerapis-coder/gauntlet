#!/usr/bin/env python3
"""
🛡️  The Agent Engineer's Gauntlet — runnable CLI application
===========================================================
Turns the AI/Agent-engineering workbook into an interactive, progress-tracking
app. AI writes the scripts (like HADA/HPS were built); YOU direct and understand.

No external dependencies — pure Python stdlib. Runs on any box with Python 3.8+.

USAGE
  python3 gauntlet.py                 # dashboard: missions + progress
  python3 gauntlet.py show <n>        # read a mission (checkboxes reflect state)
  python3 gauntlet.py check <n> <t>   # tick task t in mission n  (t = task #)
  python3 gauntlet.py uncheck <n> <t> # untick
  python3 gauntlet.py prompt <n>      # print only the 🤖 AI-coder prompt (copy-ready)
  python3 gauntlet.py pdf <n>         # list/open the codex PDF(s) for a mission
  python3 gauntlet.py next            # jump to the first incomplete mission
  python3 gauntlet.py progress        # overall completion %
  python3 gauntlet.py play            # interactive mode (menu-driven)
  python3 gauntlet.py reset           # wipe progress (keeps workbook + pdfs)
"""

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

WORKBOOK = Path(__file__).resolve().parent
STATE = WORKBOOK / ".gauntlet-state.json"
TASK_RE = re.compile(r"^(\s*)-\s*\[([ xX])\]\s*(.*)$")
NUM_RE = re.compile(r"^(\d{2})-.*\.md$")
PDF_RE = re.compile(r"pdfs/[^\s`\"'\)]+?\.pdf")

C = {
    "bold": "\033[1m", "dim": "\033[2m", "red": "\033[31m", "green": "\033[32m",
    "yellow": "\033[33m", "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m",
    "reset": "\033[0m",
}
USE_COLOR = sys.stdout.isatty()


def c(name, s):
    return f"{C[name]}{s}{C['reset']}" if USE_COLOR else s


# ---------------------------------------------------------------- state -----
def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except Exception:
            pass
    return {"current": "00", "checked": {}}


def save_state(s):
    STATE.write_text(json.dumps(s, indent=2))


# -------------------------------------------------------------- missions ----
def mission_files():
    return sorted([p for p in WORKBOOK.glob("*.md") if NUM_RE.match(p.name)])


def parse_mission(path):
    text = path.read_text(encoding="utf-8")
    num = path.name[:2]
    m = re.search(r"^#\s*(.*)$", text, re.M)
    title = m.group(1).strip() if m else path.name
    # strip the emoji prefix from the title for display
    title_clean = re.sub(r"^🛡️\s*", "", title)
    tasks = [i for i, line in enumerate(text.splitlines())
             if TASK_RE.match(line)]
    pdfs = sorted(set(PDF_RE.findall(text)))
    return {"num": num, "path": path, "title": title_clean, "text": text,
            "tasks": tasks, "pdfs": pdfs}


def missions():
    return [parse_mission(p) for p in mission_files()]


# --------------------------------------------------------------- render -----
def render_mission(m, state):
    text = m["text"]
    checked = set(state["checked"].get(m["num"], []))
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        tm = TASK_RE.match(line)
        if tm and i in m["tasks"]:
            idx = m["tasks"].index(i)
            mark = "x" if i in checked else " "
            box = c("green", "✔") if mark == "x" else c("dim", "☐")
            indent = tm.group(1)
            out.append(f"{indent}{box} {tm.group(3)}")
        else:
            out.append(line)
    return "\n".join(out)


def extract_prompts(m):
    """Pull the 🤖 AI-coder prompt block(s) out of a mission.

    A prompt block is the checkbox line containing the 🤖 marker, followed by
    blockquote (`>`) lines (and only those). It stops at the next checkbox,
    a `**` heading, or a non-quoted line.
    """
    lines = m["text"].splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "🤖" in line and TASK_RE.match(line):
            buf = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.lstrip().startswith(">"):
                    buf.append(nxt.lstrip("> ").rstrip())
                    j += 1
                # allow a single blank line inside the quote block
                elif buf and not nxt.strip():
                    # peek next; if it's a quote continue, else break
                    if j + 1 < len(lines) and lines[j + 1].lstrip().startswith(">"):
                        j += 1
                        continue
                    else:
                        break
                else:
                    break
            body = "\n".join(buf).strip()
            if body:
                blocks.append(body)
            i = j
        else:
            i += 1
    return blocks


# ---------------------------------------------------------------- commands --
def cmd_dashboard(state):
    ms = missions()
    total_tasks = sum(len(m["tasks"]) for m in ms)
    done_tasks = sum(len([t for t in state["checked"].get(m["num"], []) if t in m["tasks"]])
                     for m in ms)
    print(c("bold", "\n🛡️  THE AGENT ENGINEER'S GAUNTLET") + c("dim", "  (apprenticeship edition)"))
    print(c("dim", "─" * 60))
    for m in ms:
        n_done = len([t for t in state["checked"].get(m["num"], []) if t in m["tasks"]])
        n = len(m["tasks"])
        pct = (n_done / n * 100) if n else 0
        bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
        mark = c("green", "✔") if pct == 100 else (c("yellow", "▶") if m["num"] == state["current"] else c("dim", " "))
        print(f"{mark} {m['num']} {bar} {pct:3.0f}%  {c('bold', m['title'])}")
    print(c("dim", "─" * 60))
    overall = (done_tasks / total_tasks * 100) if total_tasks else 0
    print(f"Overall: {c('cyan', f'{overall:.0f}%')}  ({done_tasks}/{total_tasks} tasks)")
    print(c("dim", f"Next: run `python3 gauntlet.py show {state['current']}` or `play`"))
    print()


def cmd_show(state, num):
    m = next((x for x in missions() if x["num"] == num), None)
    if not m:
        print(c("red", f"No mission {num}")); return
    state["current"] = num
    save_state(state)
    print(render_mission(m, state))
    # footer: prompts + pdfs
    prompts = extract_prompts(m)
    if prompts:
        print(c("magenta", "\n🤖  AI-CODER PROMPT(S) — copy to your coder:"))
        for p in prompts:
            print(c("dim", "┌" + "─" * 58))
            for line in p.splitlines():
                print(c("cyan", "│ ") + line)
            print(c("dim", "└" + "─" * 58))
    if m["pdfs"]:
        print(c("blue", "\n📚  CODEX PDF(S):"))
        for p in m["pdfs"]:
            print(f"   {WORKBOOK / p}")
    print(c("yellow", f"\n🏆  Done when: ") + extract_done(m))
    print(c("dim", f"\nTick tasks: python3 gauntlet.py check {num} <task#>", ))


def extract_done(m):
    mm = re.search(r"🏆\s*(.*)", m["text"])
    if not mm:
        return ""
    # grab until next blank or heading
    rest = m["text"][mm.start():]
    lines = rest.splitlines()[1:]
    out = []
    for ln in lines:
        if re.match(r"^#|\*\*|🛡️", ln) or (not ln.strip() and out):
            break
        if ln.strip():
            out.append(ln.strip())
    return " ".join(out)


def cmd_prompt(num):
    m = next((x for x in missions() if x["num"] == num), None)
    if not m:
        print(c("red", f"No mission {num}")); return
    prompts = extract_prompts(m)
    if not prompts:
        print(c("dim", "No AI-coder prompt in this mission (setup/reading only)."))
        return
    for p in prompts:
        print(p)
        print()


def cmd_pdf(num, open_it=False):
    m = next((x for x in missions() if x["num"] == num), None)
    if not m:
        print(c("red", f"No mission {num}")); return
    if not m["pdfs"]:
        print(c("dim", "No PDF referenced.")); return
    for p in m["pdfs"]:
        full = WORKBOOK / p
        print(str(full))
        if open_it and shutil.which("xdg-open"):
            os.system(f'xdg-open "{full}" >/dev/null 2>&1 &')


def cmd_check(state, num, task):
    m = next((x for x in missions() if x["num"] == num), None)
    if not m:
        print(c("red", f"No mission {num}")); return
    if task < 1 or task > len(m["tasks"]):
        print(c("red", f"Mission {num} has {len(m['tasks'])} tasks (1-{len(m['tasks'])})"))
        return
    line_idx = m["tasks"][task - 1]
    cur = state["checked"].setdefault(num, [])
    if line_idx in cur:
        print(c("dim", f"Task {task} already ticked."))
    else:
        cur.append(line_idx)
        save_state(state)
        print(c("green", f"✔ Mission {num} task {task} ticked."))


def cmd_uncheck(state, num, task):
    m = next((x for x in missions() if x["num"] == num), None)
    if not m:
        print(c("red", f"No mission {num}")); return
    if task < 1 or task > len(m["tasks"]):
        print(c("red", "Task out of range")); return
    line_idx = m["tasks"][task - 1]
    cur = state["checked"].get(num, [])
    if line_idx in cur:
        cur.remove(line_idx)
        save_state(state)
        print(c("yellow", f"☐ Mission {num} task {task} unticked."))
    else:
        print(c("dim", "Was not ticked."))


def cmd_next(state):
    ms = missions()
    for m in ms:
        n_done = len([t for t in state["checked"].get(m["num"], []) if t in m["tasks"]])
        if n_done < len(m["tasks"]):
            print(c("yellow", f"Next incomplete: {m['num']} — {m['title']}"))
            print(c("dim", f"  python3 gauntlet.py show {m['num']}"))
            return
    print(c("green", "🎉 All missions complete, Engineer."))


def cmd_progress(state):
    ms = missions()
    total = sum(len(m["tasks"]) for m in ms)
    done = sum(len([t for t in state["checked"].get(m["num"], []) if t in m["tasks"]]) for m in ms)
    print(f"{c('cyan', f'{(done/total*100 if total else 0):.0f}%')}  ({done}/{total} tasks across {len(ms)} missions)")


# ------------------------------------------------------------- interactive ---
def cmd_play(state):
    ms = missions()
    by_num = {m["num"]: m for m in ms}
    cur = state["current"]
    print(c("bold", "\n🛡️  GAUNTLET — interactive mode") + c("dim", "  (type ? for help, q to quit)\n"))
    while True:
        m = by_num.get(cur)
        if not m:
            cur = ms[0]["num"]; m = by_num[cur]
        n_done = len([t for t in state["checked"].get(cur, []) if t in m["tasks"]])
        print(c("bold", f"[{cur}] {m['title']}") + c("dim", f"   ({n_done}/{len(m['tasks'])} tasks)"))
        # show tasks compactly
        for i, li in enumerate(m["tasks"], 1):
            line = m["text"].splitlines()[li]
            tm = TASK_RE.match(line)
            done = li in state["checked"].get(cur, [])
            box = c("green", "✔") if done else c("dim", " ")
            print(f"  {box} {i}. {tm.group(3)[:70]}")
        cmd = input(c("cyan", "\ngauntlet> ")).strip()
        if cmd in ("q", "quit", "exit"):
            print(c("dim", "Progress saved. Keep building, Engineer.")); break
        if cmd in ("?", "h", "help"):
            print(c("dim", "  <n>      show mission n (e.g. 3)\n"
                          "  c <t>    tick task t here\n"
                          "  u <t>    untick task t\n"
                          "  p        print AI-coder prompt\n"
                          "  pdf      show codex PDF paths\n"
                          "  next     jump to first incomplete\n"
                          "  q        quit"))
            continue
        if cmd == "next":
            for x in ms:
                if len([t for t in state["checked"].get(x["num"], []) if t in x["tasks"]]) < len(x["tasks"]):
                    cur = x["num"]; state["current"] = cur; save_state(state); break
            continue
        if cmd == "p":
            for p in extract_prompts(m):
                print(c("cyan", p)); print()
            continue
        if cmd == "pdf":
            for p in m["pdfs"]:
                print(WORKBOOK / p)
            continue
        if cmd.startswith("c "):
            try:
                t = int(cmd.split()[1]); cmd_check(state, cur, t)
            except Exception:
                print(c("red", "usage: c <task#>")); continue
            continue
        if cmd.startswith("u "):
            try:
                t = int(cmd.split()[1]); cmd_uncheck(state, cur, t)
            except Exception:
                print(c("red", "usage: u <task#>")); continue
            continue
        if cmd.isdigit():
            target = f"{int(cmd):02d}"
            if target in by_num:
                cur = target; state["current"] = cur; save_state(state)
            else:
                print(c("red", f"No mission {target}"))
            continue
        print(c("dim", "unknown command — ? for help"))


def cmd_reset():
    if STATE.exists():
        STATE.unlink()
    print(c("yellow", "Progress reset. Workbook + pdfs untouched."))


# ------------------------------------------------------------------ main ----
def main():
    ap = argparse.ArgumentParser(description="The Agent Engineer's Gauntlet CLI")
    ap.add_argument("cmd", nargs="?", default="dashboard",
                    choices=["dashboard", "show", "check", "uncheck", "prompt",
                             "pdf", "next", "progress", "play", "reset"])
    ap.add_argument("num", nargs="?", default=None)
    ap.add_argument("task", nargs="?", type=int, default=None)
    ap.add_argument("--open", action="store_true", help="open PDFs (needs xdg-open)")
    args = ap.parse_args()

    state = load_state()
    cmd = args.cmd

    if cmd == "dashboard":
        cmd_dashboard(state)
    elif cmd == "show":
        if not args.num:
            print(c("red", "usage: show <n>")); return
        cmd_show(state, f"{int(args.num):02d}")
    elif cmd == "check":
        if not args.num or args.task is None:
            print(c("red", "usage: check <n> <task#>")); return
        cmd_check(state, f"{int(args.num):02d}", args.task)
    elif cmd == "uncheck":
        if not args.num or args.task is None:
            print(c("red", "usage: uncheck <n> <task#>")); return
        cmd_uncheck(state, f"{int(args.num):02d}", args.task)
    elif cmd == "prompt":
        if not args.num:
            print(c("red", "usage: prompt <n>")); return
        cmd_prompt(f"{int(args.num):02d}")
    elif cmd == "pdf":
        if not args.num:
            print(c("red", "usage: pdf <n> [--open]")); return
        cmd_pdf(f"{int(args.num):02d}", args.open)
    elif cmd == "next":
        cmd_next(state)
    elif cmd == "progress":
        cmd_progress(state)
    elif cmd == "play":
        cmd_play(state)
    elif cmd == "reset":
        cmd_reset()


if __name__ == "__main__":
    main()

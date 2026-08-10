#!/usr/bin/env python3
"""Build a single self-contained gauntlet.html from the mission .md files.

Output: gauntlet.html  (one file, offline, no CDN, no Python needed to run).
Open it by double-clicking -> interactive gauntlet with localStorage progress.
"""
import json
import re
import html
from pathlib import Path

WORK = Path(__file__).resolve().parent
NUM_RE = re.compile(r"^(\d{2})-.*\.md$")
TASK_RE = re.compile(r"^(\s*)-\s*\[([ xX])\]\s*(.*)$")
PDF_RE = re.compile(r"pdfs/[^\s`\"'\)]+?\.pdf")
PROMPT_RE = re.compile(r"🤖")


def md_inline(s: str) -> str:
    # escape first
    s = html.escape(s, quote=False)
    # code spans
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    # bold
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # italic
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    # links [text](url)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\1" target="_blank" rel="noopener">\2</a>', s)
    return s


def md_to_html(text: str, task_ids: dict):
    """Convert mission markdown to HTML. Checkbox lines become interactive
    inputs keyed by their (0-based) order in task_ids."""
    lines = text.splitlines()
    out = []
    i = 0
    in_ul = False
    in_code = False
    code_buf = []
    task_counter = [0]

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            close_ul()
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            close_ul()
            lvl = len(m.group(1))
            content = md_inline(m.group(2))
            out.append(f"<h{lvl}>{content}</h{lvl}>")
            i += 1
            continue
        # blockquote
        if line.lstrip().startswith(">"):
            close_ul()
            out.append("<blockquote>" + md_inline(line.lstrip()[1:].strip()) + "</blockquote>")
            i += 1
            continue
        # checkbox / list item
        tm = TASK_RE.match(line)
        if tm:
            if not in_ul:
                out.append('<ul class="tasks">')
                in_ul = True
            raw = tm.group(3)
            # strip leading emoji headers like **Open the codex:** and 🤖
            label = md_inline(raw)
            tid = task_counter[0]
            task_counter[0] += 1
            task_ids[id(line)] = tid  # not used; we assign in order below
            out.append(
                f'<li class="task"><label><input type="checkbox" data-task="{tid}">'
                f'<span>{label}</span></label></li>'
            )
            i += 1
            continue
        # plain list item
        if re.match(r"^\s*[-*]\s+", line):
            if not in_ul:
                out.append('<ul class="tasks">')
                in_ul = True
            out.append("<li>" + md_inline(line.lstrip()[2:].strip()) + "</li>")
            i += 1
            continue
        # blank
        if not line.strip():
            close_ul()
            i += 1
            continue
        # paragraph
        close_ul()
        out.append("<p>" + md_inline(line) + "</p>")
        i += 1
    close_ul()
    if in_code and code_buf:
        out.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
    return "\n".join(out)


def extract_prompts(text: str):
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        if PROMPT_RE.search(lines[i]) and TASK_RE.match(lines[i]):
            buf = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.lstrip().startswith(">"):
                    buf.append(nxt.lstrip()[1:].strip())
                    j += 1
                elif buf and not nxt.strip():
                    if j + 1 < len(lines) and lines[j + 1].lstrip().startswith(">"):
                        j += 1
                        continue
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


def extract_done(text: str):
    m = re.search(r"🏆\s*(.*)", text)
    if not m:
        return ""
    rest = text[m.start():]
    out = []
    started = False
    for ln in rest.splitlines()[1:]:
        if re.match(r"^#|\*\*|🛡️", ln):
            break
        if ln.strip():
            started = True
            out.append(ln.strip())
        elif started:
            break
    return " ".join(out)


def build():
    missions = []
    for p in sorted(WORK.glob("*.md")):
        if not NUM_RE.match(p.name):
            continue
        text = p.read_text(encoding="utf-8")
        num = p.name[:2]
        tm = re.search(r"^#\s*(.*)$", text, re.M)
        title = re.sub(r"^🛡️\s*", "", tm.group(1).strip()) if tm else p.name
        task_ids = {}
        body_html = md_to_html(text, task_ids)
        # count checkboxes == number of data-task inputs
        n_tasks = body_html.count('data-task=')
        missions.append({
            "num": num,
            "title": title,
            "html": body_html,
            "nTasks": n_tasks,
            "prompts": extract_prompts(text),
            "pdfs": sorted(set(PDF_RE.findall(text))),
            "done": extract_done(text),
        })
    data = json.dumps(missions, ensure_ascii=False)
    html_doc = TEMPLATE.replace("/*__MISSIONS__*/", data)
    out = WORK / "gauntlet.html"
    out.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {out}  ({out.stat().st_size//1024} KB, {len(missions)} missions)")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>🛡️ The Agent Engineer's Gauntlet</title>
<style>
  :root{
    --bg:#0d1117; --panel:#161b22; --panel2:#1c2330; --line:#2b3340;
    --txt:#e6edf3; --dim:#8b949e; --accent:#58a6ff; --green:#3fb950;
    --yellow:#d29922; --magenta:#bc8cff; --cyan:#39c5cf; --red:#f85149;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--txt);
    font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  header{padding:18px 22px;border-bottom:1px solid var(--line);
    background:linear-gradient(180deg,#11161f,#0d1117);position:sticky;top:0;z-index:5}
  header h1{margin:0;font-size:19px}
  header .sub{color:var(--dim);font-size:13px;margin-top:2px}
  .wrap{max-width:920px;margin:0 auto;padding:18px 16px 80px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-top:14px}
  .card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 15px;cursor:pointer;transition:.15s}
  .card:hover{border-color:var(--accent);transform:translateY(-2px)}
  .card .num{color:var(--dim);font-size:12px;letter-spacing:.08em}
  .card .t{font-weight:600;margin:4px 0 8px}
  .ring{height:8px;background:#0b0f14;border-radius:6px;overflow:hidden}
  .ring > i{display:block;height:100%;background:linear-gradient(90deg,var(--cyan),var(--green));width:0}
  .card .pct{font-size:12px;color:var(--dim);margin-top:6px}
  .back{color:var(--accent);cursor:pointer;display:inline-block;margin:6px 0 12px;font-size:14px}
  .mission h1,.mission h2,.mission h3{margin-top:18px}
  .mission p{color:#cdd6e0}
  .mission code{background:#0b0f14;padding:1px 6px;border-radius:5px;color:var(--cyan);font-size:13px}
  .mission pre{background:#0b0f14;border:1px solid var(--line);border-radius:10px;padding:12px;overflow:auto}
  .mission pre code{background:none;color:#cdd6e0;padding:0}
  .mission blockquote{margin:8px 0;padding:6px 12px;border-left:3px solid var(--magenta);
    background:rgba(188,140,255,.07);color:#d7c9f5;border-radius:0 8px 8px 0}
  ul.tasks{list-style:none;padding-left:0;margin:8px 0}
  ul.tasks li.task{padding:5px 0;border-bottom:1px dashed var(--line)}
  ul.tasks li.task label{display:flex;gap:10px;align-items:flex-start;cursor:pointer}
  ul.tasks li.task input{margin-top:5px;width:17px;height:17px;accent-color:var(--green);flex:0 0 auto}
  ul.tasks li.task.done span{color:var(--dim);text-decoration:line-through}
  ul.tasks li.task span{color:#d7dee6}
  .panel{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:14px;margin:16px 0}
  .panel h4{margin:0 0 8px;color:var(--magenta);font-size:14px}
  .prompt{background:#0b0f14;border:1px solid var(--line);border-radius:8px;padding:10px 12px;
    white-space:pre-wrap;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;color:#cdd6e0}
  button{cursor:pointer;border:1px solid var(--line);background:var(--panel);color:var(--txt);
    border-radius:8px;padding:7px 13px;font-size:13px;transition:.15s}
  button:hover{border-color:var(--accent)}
  button.primary{background:var(--accent);color:#04101f;border-color:var(--accent);font-weight:600}
  .pdflink{display:block;color:var(--cyan);text-decoration:none;padding:3px 0;font-size:13px}
  .pdflink:hover{text-decoration:underline}
  .done-box{background:rgba(63,185,80,.08);border:1px solid var(--green);border-radius:10px;
    padding:12px;margin:16px 0;color:#bff0c4}
  .toolbar{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
  .hidden{display:none}
  .banner{background:rgba(88,166,255,.08);border:1px solid var(--accent);border-radius:10px;
    padding:12px 14px;margin:12px 0;color:#cfe3ff;font-size:14px}
  footer{color:var(--dim);font-size:12px;text-align:center;margin-top:30px}
  kbd{background:#0b0f14;border:1px solid var(--line);border-radius:5px;padding:1px 6px;font-size:12px}
</style>
</head>
<body>
<header>
  <h1>🛡️ The Agent Engineer's Gauntlet</h1>
  <div class="sub">Apprenticeship edition — AI writes the scripts, <b>you</b> direct &amp; understand. Click a mission to play.</div>
</header>
<div class="wrap">
  <div id="home">
    <div class="banner">Progress saves in this browser (localStorage). Nothing leaves your machine.
      To reset: clear site data or click <kbd>Reset</kbd> below.</div>
    <div class="toolbar">
      <button class="primary" id="playBtn">▶ Play guided tour</button>
      <button id="resetBtn">Reset progress</button>
      <span id="overall" style="align-self:center;color:var(--dim)"></span>
    </div>
    <div class="grid" id="grid"></div>
    <footer>Built from your mission workbooks. Codex PDFs (Raschka, <i>Build a LLM From Scratch</i>) ship in the bundle.</footer>
  </div>

  <div id="mission" class="mission hidden"></div>
</div>

<script>
const MISSIONS = /*__MISSIONS__*/;
const KEY = "gauntlet.progress.v1";
let progress = {};
try { progress = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch(e){ progress = {}; }

function save(){ localStorage.setItem(KEY, JSON.stringify(progress)); }
function doneCount(m){ const p = progress[m.num]||[]; return p.length; }
function pct(m){ return m.nTasks? Math.round(doneCount(m)/m.nTasks*100):0; }

function renderHome(){
  document.getElementById("mission").classList.add("hidden");
  document.getElementById("home").classList.remove("hidden");
  const grid = document.getElementById("grid");
  grid.innerHTML = "";
  let total=0, done=0;
  MISSIONS.forEach(m=>{
    total += m.nTasks; done += doneCount(m);
    const p = pct(m);
    const card = document.createElement("div");
    card.className="card";
    card.innerHTML = `<div class="num">MISSION ${m.num}</div>
      <div class="t">${m.title}</div>
      <div class="ring"><i style="width:${p}%"></i></div>
      <div class="pct">${doneCount(m)}/${m.nTasks} tasks · ${p}%</div>`;
    card.onclick = ()=>openMission(m.num);
    grid.appendChild(card);
  });
  document.getElementById("overall").textContent =
    `Overall: ${total? Math.round(done/total*100):0}%  (${done}/${total})`;
}

function openMission(num){
  const m = MISSIONS.find(x=>x.num===num);
  if(!m) return;
  document.getElementById("home").classList.add("hidden");
  const el = document.getElementById("mission");
  el.classList.remove("hidden");
  let html = `<div class="back" onclick="renderHome()">← All missions</div>`;
  html += `<h1>${m.title}</h1>`;
  html += m.html;
  // AI prompts panel
  if(m.prompts.length){
    html += `<div class="panel"><h4>🤖 AI-CODER PROMPT${m.prompts.length>1?"S":""} — copy to your coder</h4>`;
    m.prompts.forEach((p,idx)=>{
      html += `<div class="prompt" id="prompt${idx}">${escapeHtml(p)}</div>`;
      html += `<button onclick="copyPrompt(${idx})" style="margin:6px 0 12px">Copy prompt ${idx+1}</button>`;
    });
    html += `</div>`;
  }
  // PDFs
  if(m.pdfs.length){
    html += `<div class="panel"><h4>📚 Codex PDFs</h4>`;
    m.pdfs.forEach(p=>{ html += `<a class="pdflink" href="${p}" target="_blank" rel="noopener">📄 ${p}</a>`; });
    html += `</div>`;
  }
  // Done when
  if(m.done){ html += `<div class="done-box"><b>🏆 Done when:</b> ${escapeHtml(m.done)}</div>`; }
  html += `<div class="toolbar"><button class="primary" onclick="nextMission('${m.num}')">Next mission →</button>
           <button onclick="renderHome()">← Home</button></div>`;
  el.innerHTML = html;
  // wire checkboxes
  el.querySelectorAll('input[data-task]').forEach(inp=>{
    const tid = inp.getAttribute('data-task');
    const checked = (progress[m.num]||[]).includes(tid);
    inp.checked = checked;
    if(checked) inp.closest('li.task').classList.add('done');
    inp.onchange = ()=>{
      progress[m.num] = progress[m.num]||[];
      if(inp.checked){ if(!progress[m.num].includes(tid)) progress[m.num].push(tid);
        inp.closest('li.task').classList.add('done'); }
      else { progress[m.num] = progress[m.num].filter(x=>x!==tid);
        inp.closest('li.task').classList.remove('done'); }
      save();
    };
  });
  window.scrollTo(0,0);
}

function copyPrompt(idx){
  const txt = document.getElementById("prompt"+idx).innerText;
  navigator.clipboard.writeText(txt).then(()=>{
    event.target.textContent = "✓ Copied!";
    setTimeout(()=>event.target.textContent=`Copy prompt ${idx+1}`,1400);
  }).catch(()=>{ alert(txt); });
}

function nextMission(num){
  const i = MISSIONS.findIndex(x=>x.num===num);
  if(i<0) return renderHome();
  const nx = MISSIONS[i+1];
  if(nx) openMission(nx.num); else { alert("🎉 Gauntlet complete, Engineer."); renderHome(); }
}

function resetProgress(){
  if(confirm("Reset all progress? (keeps the workbook)")){
    progress = {}; save(); renderHome();
  }
}

function playTour(){
  // open first incomplete, or 00
  let m = MISSIONS.find(x=>doneCount(x)<x.nTasks) || MISSIONS[0];
  openMission(m.num);
  window.scrollTo(0,0);
}

function escapeHtml(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}

document.getElementById("resetBtn").onclick = resetProgress;
document.getElementById("playBtn").onclick = playTour;
renderHome();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    build()

#!/usr/bin/env python3
"""Build a single self-contained gauntlet.html from the mission .md files.

Output: gauntlet.html  (one file, offline, no CDN, no Python needed to run).
Now ships with an integrated AI Coder (Run-with-AI + Expand-gauntlet) that can
target OpenCode's local OpenAI-compatible endpoint or any cloud provider.
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
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\1" target="_blank" rel="noopener">\2</a>', s)
    return s


def md_to_html(text: str):
    lines = text.splitlines()
    out = []
    i = 0
    in_ul = False
    in_code = False
    code_buf = []
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if in_ul:
                out.append("</ul>"); in_ul = False
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
                code_buf = []; in_code = False
            else:
                in_code = True
            i += 1; continue
        if in_code:
            code_buf.append(line); i += 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            if in_ul: out.append("</ul>"); in_ul = False
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{md_inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if line.lstrip().startswith(">"):
            if in_ul: out.append("</ul>"); in_ul = False
            out.append("<blockquote>" + md_inline(line.lstrip()[1:].strip()) + "</blockquote>"); i += 1; continue
        tm = TASK_RE.match(line)
        if tm:
            if not in_ul:
                out.append('<ul class="tasks">'); in_ul = True
            label = md_inline(tm.group(3))
            out.append(f'<li class="task"><label><input type="checkbox" data-task="{len([1 for x in out if "data-task=" in x])}"><span>{label}</span></label></li>')
            i += 1; continue
        if re.match(r"^\s*[-*]\s+", line):
            if not in_ul:
                out.append('<ul class="tasks">'); in_ul = True
            out.append("<li>" + md_inline(line.lstrip()[2:].strip()) + "</li>"); i += 1; continue
        if not line.strip():
            if in_ul: out.append("</ul>"); in_ul = False
            i += 1; continue
        if in_ul: out.append("</ul>"); in_ul = False
        out.append("<p>" + md_inline(line) + "</p>"); i += 1
    if in_ul: out.append("</ul>")
    if in_code and code_buf:
        out.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
    return "\n".join(out)


def extract_prompts(text: str):
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        if PROMPT_RE.search(lines[i]) and TASK_RE.match(lines[i]):
            buf = []; j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.lstrip().startswith(">"):
                    buf.append(nxt.lstrip()[1:].strip()); j += 1
                elif buf and not nxt.strip():
                    if j + 1 < len(lines) and lines[j + 1].lstrip().startswith(">"):
                        j += 1; continue
                    break
                else:
                    break
            body = "\n".join(buf).strip()
            if body: blocks.append(body)
            i = j
        else:
            i += 1
    return blocks


def extract_done(text: str):
    m = re.search(r"🏆\s*(.*)", text)
    if not m: return ""
    out = []; started = False
    for ln in text[m.start():].splitlines()[1:]:
        if re.match(r"^#|\*\*|🛡️", ln): break
        if ln.strip():
            started = True; out.append(ln.strip())
        elif started: break
    return " ".join(out)


def build():
    missions = []
    for p in sorted(WORK.glob("*.md")):
        if not NUM_RE.match(p.name): continue
        text = p.read_text(encoding="utf-8")
        num = p.name[:2]
        tm = re.search(r"^#\s*(.*)$", text, re.M)
        title = re.sub(r"^🛡️\s*", "", tm.group(1).strip()) if tm else p.name
        body_html = md_to_html(text)
        n_tasks = body_html.count('data-task=')
        missions.append({
            "num": num, "title": title, "html": body_html, "nTasks": n_tasks,
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
  /* AI coder */
  .gear{position:absolute;right:18px;top:16px}
  .ai-result{background:#0b0f14;border:1px solid var(--line);border-radius:10px;padding:12px;margin-top:10px;
    white-space:pre-wrap;font-size:13px;max-height:420px;overflow:auto}
  .codeblk{background:#0b0f14;border:1px solid var(--line);border-radius:8px;padding:10px;margin:8px 0;
    white-space:pre-wrap;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px}
  .status{font-size:12px;color:var(--yellow);margin-left:8px}
  .modal{position:fixed;inset:0;background:rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;z-index:20}
  .modal .box{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px;width:min(520px,92vw);max-height:88vh;overflow:auto}
  .modal label{display:block;font-size:12px;color:var(--dim);margin:12px 0 4px}
  .modal input,.modal select{width:100%;background:#0b0f14;border:1px solid var(--line);color:var(--txt);
    border-radius:8px;padding:8px 10px;font-size:13px}
  .modal .hint{font-size:11px;color:var(--dim);margin-top:4px}
  .modal .row{display:flex;gap:10px;margin-top:16px;justify-content:flex-end}
</style>
</head>
<body>
<header>
  <h1>🛡️ The Agent Engineer's Gauntlet</h1>
  <div class="sub">Apprenticeship edition — AI writes the scripts, <b>you</b> direct &amp; understand. Click a mission to play.</div>
  <button class="gear" id="aiGear" title="Configure AI coder">⚙ AI Coder</button>
</header>
<div class="wrap">
  <div id="home">
    <div class="banner">Progress saves in this browser (localStorage). The built-in <b>AI Coder</b> can run prompts and expand the gauntlet — configure it via ⚙ (top-right) to point at OpenCode or a cloud model. Keys stay on your machine.</div>
    <div class="toolbar">
      <button class="primary" id="playBtn">▶ Play guided tour</button>
      <button id="expandBtn">✨ Expand gauntlet (AI)</button>
      <button id="resetBtn">Reset progress</button>
      <span id="overall" style="align-self:center;color:var(--dim)"></span>
    </div>
    <div class="grid" id="grid"></div>
    <footer>Built from your mission workbooks. Codex PDFs (Raschka, <i>Build a LLM From Scratch</i>) ship in the bundle.</footer>
  </div>

  <div id="mission" class="mission hidden"></div>
</div>

<!-- AI settings modal -->
<div id="aiModal" class="modal hidden">
  <div class="box">
    <h3 style="margin-top:0">⚙ AI Coder settings</h3>
    <label>Provider preset</label>
    <select id="aiProvider">
      <option value="opencode">OpenCode (local, OpenAI-compatible)</option>
      <option value="openrouter">OpenRouter (broad model selection)</option>
      <option value="anthropic">Anthropic (Claude, direct)</option>
      <option value="openai">OpenAI</option>
      <option value="local">Other local OpenAI-compatible (LM Studio / Ollama)</option>
    </select>
    <div class="hint">OpenCode Zen (hosted, OpenAI-compatible): Base URL <code>https://opencode.ai/zen/v1</code>. Get a key from your Zen account (opencode.ai/zen). For a local OpenCode server, use <code>http://localhost:&lt;port&gt;/v1</code> with no key.</div>
    <label>Base URL</label>
    <input id="aiBase" placeholder="https://opencode.ai/zen/v1">
    <label>API key (Zen key from opencode.ai/zen; blank for local OpenCode)</label>
    <input id="aiKey" type="password" placeholder="sk-... or empty for localhost">
    <label>Model</label>
    <input id="aiModel" placeholder="anthropic/claude-3.5-sonnet">
    <div class="hint">OpenRouter model list: openrouter.ai/models. OpenCode uses whatever model you configured in its provider.</div>
    <div class="row">
      <button id="aiCancel">Cancel</button>
      <button class="primary" id="aiSave">Save</button>
    </div>
  </div>
</div>

<script>
const MISSIONS = /*__MISSIONS__*/;
const KEY = "gauntlet.progress.v1";
const AIKEY = "gauntlet.ai.v1";
const ADDEDKEY = "gauntlet.added.v1";
let progress = {};
let ai = {};
let CUR = null;
try { progress = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch(e){ progress = {}; }
try { ai = JSON.parse(localStorage.getItem(AIKEY) || "{}"); } catch(e){ ai = {}; }

function save(){ localStorage.setItem(KEY, JSON.stringify(progress)); }
function saveAI(){ localStorage.setItem(AIKEY, JSON.stringify(ai)); }
function mergeAdded(){
  try {
    const added = JSON.parse(localStorage.getItem(ADDEDKEY) || "[]");
    added.forEach(m => MISSIONS.push(m));
  } catch(e){}
}
function doneCount(m){ return (progress[m.num]||[]).length; }
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
  CUR = m;
  document.getElementById("home").classList.add("hidden");
  const el = document.getElementById("mission");
  el.classList.remove("hidden");
  let html = `<div class="back" onclick="renderHome()">← All missions</div>`;
  html += `<h1>${m.title}</h1>`;
  html += m.html;
  if(m.prompts.length){
    html += `<div class="panel"><h4>🤖 AI-CODER PROMPT${m.prompts.length>1?"S":""}</h4>`;
    m.prompts.forEach((p,idx)=>{
      html += `<div class="prompt" id="prompt${idx}">${escapeHtml(p)}</div>`;
      html += `<div style="margin:6px 0 12px">
        <button onclick="copyPrompt(${idx})">Copy prompt ${idx+1}</button>
        <button class="primary" onclick="runWithAI(${idx})">▶ Run with AI</button>
        <span class="status" id="aiStatus${idx}"></span></div>`;
      html += `<div class="ai-result hidden" id="aiResult${idx}"></div>`;
    });
    html += `</div>`;
  }
  if(m.pdfs.length){
    html += `<div class="panel"><h4>📚 Codex PDFs</h4>`;
    m.pdfs.forEach(p=>{ html += `<a class="pdflink" href="${p}" target="_blank" rel="noopener">📄 ${p}</a>`; });
    html += `</div>`;
  }
  if(m.done){ html += `<div class="done-box"><b>🏆 Done when:</b> ${escapeHtml(m.done)}</div>`; }
  html += `<div class="toolbar"><button class="primary" onclick="nextMission('${m.num}')">Next mission →</button>
           <button onclick="renderHome()">← Home</button></div>`;
  el.innerHTML = html;
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

/* ---------------- AI Coder ---------------- */
function aiConfigured(){
  if(!ai.baseUrl) return false;
  if(ai.provider==='opencode' || ai.provider==='local') return true; // local may need no key
  return !!ai.apiKey;
}
async function runAI(system, user, onText, onError){
  if(!aiConfigured()){
    onError("Open ⚙ AI Coder and set a provider/endpoint first.");
    return;
  }
  const status = document.createElement("span");
  try {
    let body, headers={}, url;
    if(ai.provider==='anthropic'){
      url = ai.baseUrl.replace(/\/$/,'') + "/messages";
      body = JSON.stringify({model:ai.model||"claude-3-5-sonnet-20241022", max_tokens:2000, system, messages:[{role:"user",content:user}]});
      headers = {"content-type":"application/json","x-api-key":ai.apiKey,
                 "anthropic-version":"2023-06-01","anthropic-dangerous-direct-browser-access":"true"};
    } else {
      url = ai.baseUrl.replace(/\/$/,'') + "/chat/completions";
      body = JSON.stringify({model:ai.model||"gpt-4o", messages:[{role:"system",content:system},{role:"user",content:user}], max_tokens:2000});
      headers = {"content-type":"application/json"};
      if(ai.apiKey) headers["authorization"] = "Bearer " + ai.apiKey;
    }
    const res = await fetch(url, {method:"POST", headers, body});
    if(!res.ok){ const t = await res.text(); onError("API error "+res.status+": "+t.slice(0,200)); return; }
    const j = await res.json();
    let text = (ai.provider==='anthropic')
      ? (j.content||[]).map(c=>c.text||"").join("")
      : (j.choices&&j.choices[0]&&j.choices[0].message&&j.choices[0].message.content) || "";
    onText(text);
  } catch(e){
    onError("Request failed: "+e.message+". Check the endpoint/key, and that CORS is allowed (OpenRouter/local OK).");
  }
}
function renderAIText(container, text){
  // split into code blocks + prose
  const parts = text.split(/```/);
  let html = "";
  parts.forEach((part,i)=>{
    if(i%2===1){
      const nl = part.indexOf("\n");
      const code = nl>=0? part.slice(nl+1): part;
      const id = "cb"+Math.random().toString(36).slice(2);
      html += `<div class="codeblk" id="${id}">${escapeHtml(code)}</div>
        <button onclick="copyText('${id}')" style="margin-bottom:8px">Copy code</button>`;
    } else if(part.trim()){
      html += `<div style="color:#cdd6e0">${escapeHtml(part.trim())}</div>`;
    }
  });
  container.innerHTML = html;
}
function copyText(id){
  const t = document.getElementById(id).innerText;
  navigator.clipboard.writeText(t).then(()=>{}).catch(()=>alert(t));
}
const AI_SYS = "You are the user's AI coding partner for 'The Agent Engineer's Gauntlet', an AI-engineering workbook. The user directs you; they are learning by understanding what you produce. Write minimal, runnable code (Python/PyTorch/etc as asked) with brief comments. Prefer a small working script over exposition. If a task needs a model, use a tiny one (e.g. gpt2) and note it.";
function runWithAI(idx){
  const el = document.getElementById("aiResult"+idx);
  const st = document.getElementById("aiStatus"+idx);
  el.classList.remove("hidden");
  st.textContent = "generating…";
  el.innerHTML = "<i style='color:var(--dim)'>thinking…</i>";
  const prompt = CUR.prompts[idx];
  runAI(AI_SYS, prompt,
    (text)=>{ renderAIText(el, text); st.textContent=""; },
    (err)=>{ el.innerHTML = "<span style='color:var(--red)'>"+escapeHtml(err)+"</span>"; st.textContent=""; }
  );
}

/* ---------------- Expand gauntlet ---------------- */
const EXPAND_SYS = "You extend 'The Agent Engineer's Gauntlet', an AI-engineering workbook for a builder who directs AI to write code. Produce ONE new mission in the same voice and format. Return ONLY minified JSON: {\"title\":\"Mission NN — <name>\",\"md\":\"<full markdown with ## 🛠️ Activity, checkboxes - [ ], 🤖 Prompt to give your AI coder: as a > quoted line, 👀 What to watch for, ✍️ Your move, and 🏆 Done when>\",\"prompts\":[\"<the quoted prompt text>\"],\"done\":\"<done text>\"}. Keep it concrete and runnable.";
function nextNum(){
  let max=12;
  MISSIONS.forEach(m=>{ const n=parseInt(m.num,10); if(n>max) max=n; });
  return String(max+1).padStart(2,"0");
}
async function expandGauntlet(){
  const st = document.getElementById("overall");
  st.textContent = "AI is drafting a new mission…";
  runAI(EXPAND_SYS, "Add a new mission that builds on the previous ones (e.g. agent security, observability, or multimodal). Make it genuinely useful.",
    (text)=>{
      try {
        const m = text.match(/\{[\s\S]*\}/);
        const obj = JSON.parse(m[0]);
        const num = nextNum();
        const newMission = {
          num, title: obj.title || ("Mission "+num),
          html: jsMdToHtml(obj.md||""),
          nTasks: (obj.md.match(/-\s*\[ \]/g)||[]).length,
          prompts: obj.prompts||[],
          pdfs: [], done: obj.done||""
        };
        MISSIONS.push(newMission);
        const added = JSON.parse(localStorage.getItem(ADDEDKEY)||"[]");
        added.push(newMission); localStorage.setItem(ADDEDKEY, JSON.stringify(added));
        st.textContent = "";
        renderHome();
        alert("✨ Added: "+newMission.title+"\n\nThe gauntlet just expanded. Open it from the home grid.");
      } catch(e){
        st.textContent = "";
        alert("Couldn't parse the AI's mission. Raw response:\n\n"+text.slice(0,800));
      }
    },
    (err)=>{ st.textContent=""; alert(err); }
  );
}

/* minimal JS markdown->html (for AI-generated missions) */
function jsMdToHtml(md){
  const lines = md.split("\n"); let out=[], inUl=false, inCode=false, cb=[];
  const inline=s=>{ s=escapeHtml(s);
    s=s.replace(/`([^`]+)`/g,"<code>$1</code>");
    s=s.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>");
    s=s.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g,"<em>$1</em>");
    return s; };
  lines.forEach(line=>{
    if(line.trim().startsWith("```")){
      if(inUl){out.push("</ul>");inUl=false;}
      if(inCode){out.push("<pre><code>"+escapeHtml(cb.join("\n"))+"</code></pre>");cb=[];inCode=false;}
      else inCode=true; return;
    }
    if(inCode){cb.push(line);return;}
    let hm=line.match(/^(#{1,4})\s+(.*)$/);
    if(hm){ if(inUl){out.push("</ul>");inUl=false;} out.push("<h"+hm[1].length+">"+inline(hm[2])+"</h"+hm[1].length+">"); return; }
    if(line.lstrip===undefined) {}
    if(line.trim().startsWith(">")){ if(inUl){out.push("</ul>");inUl=false;} out.push("<blockquote>"+inline(line.trim().slice(1).trim())+"</blockquote>"); return; }
    let tm=line.match(/^(\s*)-\s*\[([ xX])\]\s*(.*)$/);
    if(tm){ if(!inUl){out.push('<ul class="tasks">');inUl=true;}
      out.push('<li class="task"><label><input type="checkbox" data-task="'+out.filter(x=>x.includes("data-task=")).length+'"><span>'+inline(tm[3])+'</span></label></li>'); return; }
    if(!line.trim()){ if(inUl){out.push("</ul>");inUl=false;} return; }
    if(inUl){out.push("</ul>");inUl=false;}
    out.push("<p>"+inline(line)+"</p>");
  });
  if(inUl)out.push("</ul>");
  if(inCode&&cb.length)out.push("<pre><code>"+escapeHtml(cb.join("\n"))+"</code></pre>");
  return out.join("\n");
}

function nextMission(num){
  const i = MISSIONS.findIndex(x=>x.num===num);
  if(i<0) return renderHome();
  const nx = MISSIONS[i+1];
  if(nx) openMission(nx.num); else { alert("🎉 Gauntlet complete, Engineer."); renderHome(); }
}
function resetProgress(){
  if(confirm("Reset all progress? (keeps the workbook)")){ progress={}; save(); renderHome(); }
}
function openAIModal(){
  document.getElementById("aiProvider").value = ai.provider||"opencode";
  document.getElementById("aiBase").value = ai.baseUrl||"";
  document.getElementById("aiKey").value = ai.apiKey||"";
  document.getElementById("aiModel").value = ai.model||"";
  document.getElementById("aiModal").classList.remove("hidden");
}
function applyPreset(){
  const p=document.getElementById("aiProvider").value;
  const presets={
    opencode:{base:"https://opencode.ai/zen/v1",model:"deepseek-v4-flash-free"},
    openrouter:{base:"https://openrouter.ai/api/v1",model:"anthropic/claude-3.5-sonnet"},
    anthropic:{base:"https://api.anthropic.com/v1",model:"claude-3-5-sonnet-20241022"},
    openai:{base:"https://api.openai.com/v1",model:"gpt-4o"},
    local:{base:"http://localhost:1234/v1",model:"local-model"}
  };
  const pr=presets[p];
  document.getElementById("aiBase").value=pr.base;
  document.getElementById("aiModel").value=pr.model;
}
function saveAISettings(){
  ai = {
    provider: document.getElementById("aiProvider").value,
    baseUrl: document.getElementById("aiBase").value.trim(),
    apiKey: document.getElementById("aiKey").value.trim(),
    model: document.getElementById("aiModel").value.trim()
  };
  saveAI();
  document.getElementById("aiModal").classList.add("hidden");
  const ok = aiConfigured();
  document.getElementById("overall").textContent = ok ? "AI coder ready ✓" : "AI not configured";
}

function escapeHtml(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}

document.getElementById("resetBtn").onclick = resetProgress;
document.getElementById("playBtn").onclick = playTour;
document.getElementById("expandBtn").onclick = expandGauntlet;
document.getElementById("aiGear").onclick = openAIModal;
document.getElementById("aiCancel").onclick = ()=>document.getElementById("aiModal").classList.add("hidden");
document.getElementById("aiSave").onclick = saveAISettings;
document.getElementById("aiProvider").onchange = applyPreset;
function playTour(){
  let m = MISSIONS.find(x=>doneCount(x)<x.nTasks) || MISSIONS[0];
  openMission(m.num); window.scrollTo(0,0);
}
mergeAdded();
renderHome();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    build()

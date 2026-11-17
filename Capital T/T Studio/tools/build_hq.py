#!/usr/bin/env python3
"""Build hq/launch-hq.html (the Launch HQ page) from tools/leads_data.py.

    python3 tools/build_hq.py

The page is self-contained: data is embedded as JSON, no external scripts.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import leads_data as D  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "hq" / "launch-hq.html"

SHEET_URL = "https://docs.google.com/spreadsheets/d/1ZFc6ZsEfIY8zdxbtppggHs5MAA2vIeqfk7vwN4soW_8/edit"
REPO = "https://github.com/capitalT07/Ugc"
BRANCH = "claude/1k-2k-business-7-days-w9vmgs"
PROJECT_DIR = "Capital%20T/T%20Studio"
BLOB = f"{REPO}/blob/{BRANCH}/{PROJECT_DIR}"

TYPE_SHORT = {D.T_BRAND: "Brand", D.T_MOSTAQL: "Mostaql", D.T_UPWORK: "Upwork",
              D.T_AGENCY: "Agency", D.T_HIRING: "Company hiring", D.T_JOB: "Job"}
GROUP = {D.T_BRAND: "brands", D.T_MOSTAQL: "mostaql", D.T_UPWORK: "upwork",
         D.T_AGENCY: "partners", D.T_HIRING: "partners", D.T_JOB: "partners"}
MONEY_CHECKPOINT = {
    "2026-11-17": "Setup day. No revenue expected.",
    "2026-11-18": "First quotes out; aim for one Starter paid (EGP 3,500 / $120).",
    "2026-11-19": "First deposit landed (≥ EGP 3,500); booked ≥ $300.",
    "2026-11-20": "First client previews delivered.",
    "2026-11-21": "Booked ≥ $700; landed ≥ $300.",
    "2026-11-22": "$1,000 booked, ≥ $500 landed. Stretch: $1,000 kept.",
}


def direction(text):
    m = re.search(r"[A-Za-z؀-ۿ]", text)
    return "rtl" if m and "؀" <= m.group(0) <= "ۿ" else "ltr"


def cash_short(cash):
    return cash.split(":")[0].strip().lower()


def payload():
    leads = []
    for i, raw in enumerate(D.LEADS, start=1):
        if not raw["rank"]:
            continue
        leads.append({
            "id": f"L{i:03d}", "rank": raw["rank"], "name": raw["company"], "priority": raw["priority"],
            "type": TYPE_SHORT[raw["type"]], "group": GROUP[raw["type"]],
            "service": raw["service"], "price": raw["price"], "films": raw["films"],
            "cash": cash_short(raw["cash"]), "cashFull": raw["cash"],
            "idea": raw["opportunity"], "why": raw["why"], "check": raw["note"],
            "source": raw["source"], "reach": raw["contact_method"],
            "message": raw["message"], "dir": direction(raw["message"]),
        })
    leads.sort(key=lambda l: l["rank"])
    days = [dict(d, money=MONEY_CHECKPOINT[d["date"]]) for d in D.DAILY_PLAN]
    stats = {
        "prospects": sum(1 for l in D.LEADS if l["type"] != D.T_PLATFORM),
        "drafted": sum(1 for l in D.LEADS if l["message"]),
    }
    return {"leads": leads, "days": days, "stats": stats}


TEMPLATE = r"""<title>UGC Studio Launch HQ</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=IBM+Plex+Mono:wght@500&family=Inter:wght@400;500;600&display=swap">
<style>
/* Layout: a production call sheet, phone first. One column; from 980px a left rail (today, packages, six-day sheet) beside the lead list. */
:root{
  --bg:#F2F4F7; --surface:#FFFFFF; --ink:#141820; --muted:#5A6371; --line:#DDE2E9;
  --accent:#0A7480; --accent-ink:#FFFFFF; --accent-soft:#E1F0F1;
  --rec:#D1283E; --good:#1D7A4C; --good-soft:#E3F3EA; --warn:#965800; --warn-soft:#FBF0DC;
  --slow:#5A6371; --slow-soft:#ECEFF3; --mark:#FFEFAD; --mark-ink:#584400; --chip:#E9EDF2;
  --font-display:"Cairo","Segoe UI",system-ui,sans-serif;
  --font-body:"Inter","Cairo",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --font-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --radius:10px;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0D1015; --surface:#151A21; --ink:#E7EBF1; --muted:#9BA5B3; --line:#29303A;
  --accent:#3DB8C3; --accent-ink:#04292D; --accent-soft:#11323A;
  --rec:#FF5D72; --good:#52C78F; --good-soft:#123326; --warn:#F2A955; --warn-soft:#3A2A12;
  --slow:#9BA5B3; --slow-soft:#20262F; --mark:#4B3D0C; --mark-ink:#FFE8A6; --chip:#1E242D;
  color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0D1015; --surface:#151A21; --ink:#E7EBF1; --muted:#9BA5B3; --line:#29303A;
  --accent:#3DB8C3; --accent-ink:#04292D; --accent-soft:#11323A;
  --rec:#FF5D72; --good:#52C78F; --good-soft:#123326; --warn:#F2A955; --warn-soft:#3A2A12;
  --slow:#9BA5B3; --slow-soft:#20262F; --mark:#4B3D0C; --mark-ink:#FFE8A6; --chip:#1E242D;
  color-scheme:dark}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 var(--font-body);
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:20px 56px}
a{color:var(--accent)}
.wrap{max-width:1180px;margin:0 auto;display:grid;gap:24px}
.top{display:flex;flex-wrap:wrap;gap:14px 24px;align-items:flex-end;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:18px}
.eyebrow{font:500 12px/1 var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:8px}
.rec{width:9px;height:9px;border-radius:50%;background:var(--rec);display:inline-block;animation:pulse 2s ease-in-out infinite}
@keyframes pulse{50%{opacity:.35}}
@media (prefers-reduced-motion:reduce){.rec{animation:none}}
h1{font:700 clamp(28px,5vw,38px)/1.1 var(--font-display);margin:8px 0 6px;text-wrap:balance}
.sub{color:var(--muted);margin:0}
.btns{display:flex;flex-wrap:wrap;gap:8px}
.btn{appearance:none;border:1px solid var(--line);background:var(--surface);color:var(--ink);font:600 14px/1 var(--font-body);
  padding:11px 14px;border-radius:8px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:6px}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.btn:focus-visible,.chip:focus-visible,.toggle:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.stats{display:flex;flex-wrap:wrap;gap:8px 26px;font-variant-numeric:tabular-nums;color:var(--muted);font-size:13px;align-items:baseline}
.stats b{font:700 19px/1 var(--font-display);color:var(--ink);margin-right:5px}
.stats .asof{font:500 12px var(--font-mono)}
.cols{display:grid;gap:30px}
@media (min-width:980px){.cols{grid-template-columns:minmax(0,380px) minmax(0,1fr);align-items:start}}
.rail{display:grid;gap:30px;min-width:0}
section{min-width:0}
h2{font:700 20px/1.2 var(--font-display);margin:0 0 12px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
h2 small{font:500 12px/1 var(--font-mono);color:var(--muted);letter-spacing:.04em}
.steps{list-style:none;margin:0;padding:0;display:grid;gap:10px;counter-reset:step}
.steps li{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:14px 14px 14px 54px;position:relative;counter-increment:step}
.steps li::before{content:counter(step);position:absolute;left:14px;top:14px;width:26px;height:26px;border-radius:50%;
  background:var(--accent);color:var(--accent-ink);font:700 14px/26px var(--font-display);text-align:center}
.steps strong{display:block}
.steps .time{font:500 12px var(--font-mono);color:var(--muted)}
.steps p{margin:4px 0 0;font-size:14px}
.also{font-size:13px;color:var(--muted);margin:10px 0 0}
.rules{background:var(--accent-soft);border-radius:var(--radius);padding:12px 14px;font-size:14px;margin-top:12px}
.rules ul{margin:6px 0 0;padding-left:18px;display:grid;gap:3px}
.pk{display:grid;gap:10px}
.pk .p{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:12px 14px;display:grid;gap:3px}
.pk .p.feature{border:2px solid var(--accent)}
.pk .name{font-weight:600;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.pk .name em{font:500 11px/1.8 var(--font-mono);font-style:normal;color:var(--accent);text-transform:uppercase;letter-spacing:.06em}
.pk .price{font:700 18px/1.25 var(--font-display);font-variant-numeric:tabular-nums}
.pk .price span{font:400 13px var(--font-body);color:var(--muted)}
.pk .small{font-size:13px;color:var(--muted)}
.call{border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);overflow:hidden}
.call .row{display:grid;grid-template-columns:62px minmax(0,1fr);gap:12px;padding:12px 14px;border-top:1px solid var(--line)}
.call .row:first-child{border-top:0}
.call .row.is-today{background:var(--accent-soft)}
.call .d{font:500 12px/1.3 var(--font-mono);color:var(--muted)}
.call .d b{display:block;font:700 19px/1.1 var(--font-display);color:var(--ink)}
.call .obj{font-weight:600;margin:0}
.call .tg{font:500 12px/1.5 var(--font-mono);color:var(--muted);margin:2px 0 0}
.call .money{font-size:13px;margin:4px 0 0}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.chip{appearance:none;border:1px solid var(--line);background:var(--surface);color:var(--ink);font:500 13px/1 var(--font-body);padding:9px 12px;border-radius:999px;cursor:pointer}
.chip[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.chip .n{font-family:var(--font-mono);opacity:.7;margin-left:4px}
.leads{display:grid;gap:12px}
.lead{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:14px;display:grid;gap:9px;min-width:0}
.lead .hd{display:flex;align-items:flex-start;gap:10px}
.lead .rk{font:500 13px/1.75 var(--font-mono);color:var(--muted);min-width:26px}
.lead h3{font:700 17px/1.35 var(--font-display);margin:0;flex:1;min-width:0;overflow-wrap:anywhere}
.pill{font:600 11px/1 var(--font-body);padding:6px 8px;border-radius:999px;white-space:nowrap}
.pill.A{background:var(--ink);color:var(--bg)}
.pill.B{background:var(--chip);color:var(--ink)}
.tags{display:flex;flex-wrap:wrap;gap:6px}
.tag{font:500 12px/1 var(--font-body);background:var(--chip);color:var(--ink);padding:6px 8px;border-radius:6px}
.tag.fast{background:var(--good-soft);color:var(--good)}
.tag.medium{background:var(--warn-soft);color:var(--warn)}
.tag.slow{background:var(--slow-soft);color:var(--slow)}
.lead p{margin:0}
.lead .offer{font-weight:600}
.lead .offer span{font-weight:400;color:var(--muted)}
.lead .idea{font-size:14px}
.lead .check{font-size:13px;color:var(--warn)}
.msg{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:12px 14px;font:15px/1.75 var(--font-body);white-space:pre-wrap;overflow-wrap:anywhere;margin:0}
.msg[dir="rtl"]{font-family:var(--font-display);font-size:16px}
.msg.clamp{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
.msg mark{background:var(--mark);color:var(--mark-ink);border-radius:4px;padding:0 3px}
.lead .ft{display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center}
.toggle{appearance:none;background:none;border:0;color:var(--accent);font:600 13px var(--font-body);cursor:pointer;padding:6px 0}
.lead a.src{font-size:13px;font-weight:600;text-decoration:none}
.lead a.src:hover{text-decoration:underline}
.copied{font:500 12px var(--font-mono);color:var(--good)}
.empty{color:var(--muted)}
footer{color:var(--muted);font-size:13px;border-top:1px solid var(--line);padding-top:16px;display:grid;gap:6px}
</style>

<div class="wrap">
  <header class="top">
    <div>
      <div class="eyebrow"><span class="rec" aria-hidden="true"></span><span id="dayline">Tue 17 Nov · Day 1 of 6</span></div>
      <h1>UGC Studio Launch HQ</h1>
      <p class="sub">T Studio · Arabic UGC ads from Cairo. Goal: $1,000 by Sunday 22 Nov, counted only when it reaches you.</p>
    </div>
    <div class="btns">
      <a class="btn primary" href="__SHEET__" target="_blank" rel="noopener">Open the CRM sheet</a>
      <a class="btn" href="__REPO__" target="_blank" rel="noopener">All files on GitHub</a>
    </div>
  </header>

  <div class="stats" aria-label="Status">
    <span><b>__PROSPECTS__</b>prospects researched</span>
    <span><b>__DRAFTED__</b>messages drafted</span>
    <span><b>0</b>sent</span>
    <span><b>$0</b>collected</span>
    <span class="asof">as of Tue 17 Nov · live numbers are in the sheet</span>
  </div>

  <div class="cols">
    <div class="rail">
      <section aria-labelledby="h-today">
        <h2 id="h-today">Today's three actions <small>TUE 17 NOV</small></h2>
        <ol class="steps">
          <li><strong>Find creators who film and edit</strong><span class="time">30 min</span>
            <p>You don’t need to know anyone. On Khamsat’s UGC videos category, shortlist 8–10 Egyptian creators and message the best 5 through Khamsat. Their samples are the audition. <a href="https://khamsat.com/video-design/ugc-videos" target="_blank" rel="noopener">Khamsat UGC videos</a> · <a href="__BLOB__/docs/09-creator-roster.md#hiring-on-khamsat" target="_blank" rel="noopener">Checklist and message</a></p></li>
          <li><strong>Set up T Studio</strong><span class="time">40 min</span>
            <p>Instagram @tstudioo.ugc and TikTok @tstudio_ugc are created ✅; still to do: profile photo and bio on both, a matching Gmail, WhatsApp Business with the 3 packages (<a href="__BLOB__/docs/01-business-decision.md#whatsapp-business-copy-and-paste" target="_blank" rel="noopener">text to paste</a>), check you can receive InstaPay, and check your card or PayPal can pay in dollars on Khamsat.</p></li>
          <li><strong>Send the first batch</strong><span class="time">1.5 h</span>
            <p>Leads 1–12 below (tap “Today’s batch”). Fill in the highlighted parts, approve, send, then set each to <em>Sent</em> in the sheet’s Pipeline tab.</p></li>
        </ol>
        <p class="also">Also today: read the <a href="__BLOB__/docs/10-studio-basics.md" target="_blank" rel="noopener">30-minute studio basics guide</a>, and send applications 14, 19, 20, 25 and 30 if they're still open. You don’t film or edit: creators do, and you check every video.</p>
        <div class="rules">
          <strong>Before any message goes out</strong>
          <ul>
            <li>Open the source and check it is still open or active.</li>
            <li>Replace <mark>[OBSERVATION]</mark> with one real detail from their last 3 posts.</li>
            <li>Replace <mark>[PORTFOLIO]</mark> and <mark>[NAME]</mark>. No portfolio yet? Drop that line from brand DMs.</li>
            <li>Mostaql money is held 14 working days: booked, not cash.</li>
          </ul>
        </div>
      </section>

      <section aria-labelledby="h-pk">
        <h2 id="h-pk">What you sell</h2>
        <div class="pk">
          <div class="p"><div class="name">Starter</div><div class="price">EGP 3,500 <span>· $120</span></div><div class="small">1 video: our script and hooks, filmed and edited by a creator. 100% upfront.</div></div>
          <div class="p feature"><div class="name">Creative Test <em>Lead with this</em></div><div class="price">EGP 9,000 <span>· $330</span></div><div class="small">3 videos, 3 concepts, 30 days of paid ads. 100% upfront.</div></div>
          <div class="p"><div class="name">Content Sprint</div><div class="price">EGP 14,000 <span>· $520</span></div><div class="small">5 videos + 5 alternate hooks. 50% deposit, 50% before final files.</div></div>
        </div>
        <p class="also">Creators are paid EGP 1,000–2,000 per finished video from the client’s payment, never before. Organic posting on their accounts has no time limit; paid-ads use is priced by period; never unlimited for free. First order paid by Sun 22 Nov gets 2 extra hooks. Final files only after full payment.</p>
      </section>

      <section aria-labelledby="h-call">
        <h2 id="h-call">Six-day call sheet <small>EGYPT WEEKEND FRI–SAT</small></h2>
        <div class="call" id="call"></div>
      </section>
    </div>

    <section aria-labelledby="h-leads">
      <h2 id="h-leads">Top 30 leads <small>RANKED · NOTHING SENT YET</small></h2>
      <div class="filters" role="group" aria-label="Filter leads">
        <button class="chip" type="button" id="f-today" data-f="today" aria-pressed="true">Today’s batch</button>
        <button class="chip" type="button" id="f-all" data-f="all" aria-pressed="false">All 30</button>
        <button class="chip" type="button" id="f-brands" data-f="brands" aria-pressed="false">Brands</button>
        <button class="chip" type="button" id="f-mostaql" data-f="mostaql" aria-pressed="false">Mostaql</button>
        <button class="chip" type="button" id="f-upwork" data-f="upwork" aria-pressed="false">Upwork</button>
        <button class="chip" type="button" id="f-partners" data-f="partners" aria-pressed="false">Agencies &amp; partners</button>
      </div>
      <div class="leads" id="leads"></div>
    </section>
  </div>

  <footer>
    <span>Research Nov 15–16, 2026. Every lead has its source link; handles I couldn’t confirm are left out. Messages are drafts: nothing has been sent.</span>
    <span>Full details, all 94 prospects and the scripts: <a href="__BLOB__/crm/top30.md" target="_blank" rel="noopener">top30.md</a> · <a href="__BLOB__/README.md" target="_blank" rel="noopener">README</a></span>
  </footer>
</div>

<script id="hq-data" type="application/json">__DATA__</script>
<script>
(function(){
  var DATA = JSON.parse(document.getElementById('hq-data').textContent);
  var CASH = {fast:'Fast pay', medium:'Medium pay', slow:'Slow pay'};

  function el(tag, cls, text){ var n=document.createElement(tag); if(cls) n.className=cls; if(text!=null) n.textContent=text; return n; }
  function fillMessage(node, text){
    text.split(/(\[[^\]]+\])/g).forEach(function(part){
      if(/^\[[^\]]+\]$/.test(part)){ node.appendChild(el('mark', null, part)); }
      else if(part){ node.appendChild(document.createTextNode(part)); }
    });
  }
  function selectText(node){
    try{ var r=document.createRange(); r.selectNodeContents(node); var s=window.getSelection(); s.removeAllRanges(); s.addRange(r); }catch(e){}
  }
  function copy(text, node, note){
    function done(msg){ note.textContent = msg; setTimeout(function(){ note.textContent=''; }, 2500); }
    function fallback(){
      var ok=false, ta=document.createElement('textarea');
      ta.value=text; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.opacity='0';
      document.body.appendChild(ta); ta.select();
      try{ ok=document.execCommand('copy'); }catch(e){}
      ta.remove();
      if(ok){ done('Copied'); } else { node.classList.remove('clamp'); selectText(node); done('Selected: use your copy command'); }
    }
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(function(){ done('Copied'); }, fallback);
    } else { fallback(); }
  }

  var list=document.getElementById('leads');
  DATA.leads.forEach(function(l){
    var card=el('article','lead'); card.dataset.group=l.group; card.dataset.rank=l.rank;
    var hd=el('div','hd');
    hd.appendChild(el('span','rk', String(l.rank).padStart(2,'0')));
    hd.appendChild(el('h3', null, l.name));
    hd.appendChild(el('span','pill '+l.priority, 'Priority '+l.priority));
    card.appendChild(hd);

    var tags=el('div','tags');
    tags.appendChild(el('span','tag', l.type));
    var c=el('span','tag '+l.cash, CASH[l.cash]||l.cash); c.title=l.cashFull; tags.appendChild(c);
    tags.appendChild(el('span','tag', l.films));
    card.appendChild(tags);

    var offer=el('p','offer', l.service+' '); offer.appendChild(el('span', null, '· '+l.price)); card.appendChild(offer);
    card.appendChild(el('p','idea', l.idea));
    if(l.check){ card.appendChild(el('p','check', 'Check first: '+l.check)); }

    var msg=el('p','msg clamp'); msg.setAttribute('dir', l.dir); msg.id='msg-'+l.id; fillMessage(msg, l.message);
    card.appendChild(msg);

    var ft=el('div','ft');
    var b=el('button','btn primary','Copy message'); b.type='button';
    var note=el('span','copied'); note.setAttribute('role','status');
    b.addEventListener('click', function(){ copy(l.message, msg, note); });
    var t=el('button','toggle','Show all'); t.type='button'; t.setAttribute('aria-controls', msg.id); t.setAttribute('aria-expanded','false');
    t.addEventListener('click', function(){ var open=msg.classList.toggle('clamp')===false; t.textContent=open?'Show less':'Show all'; t.setAttribute('aria-expanded', String(open)); });
    var a=el('a','src','Open source ↗'); a.href=l.source; a.target='_blank'; a.rel='noopener';
    ft.appendChild(b); ft.appendChild(t); ft.appendChild(a); ft.appendChild(note);
    card.appendChild(ft);
    list.appendChild(card);
  });

  var chips=[].slice.call(document.querySelectorAll('.chip'));
  function count(f){ return DATA.leads.filter(function(l){ return match(l,f); }).length; }
  function match(l,f){ return f==='all' || (f==='today' ? l.rank<=12 : l.group===f); }
  chips.forEach(function(ch){ ch.appendChild(el('span','n', String(count(ch.dataset.f)))); });
  function apply(f){
    chips.forEach(function(ch){ ch.setAttribute('aria-pressed', String(ch.dataset.f===f)); });
    [].forEach.call(list.children, function(card){
      var l=DATA.leads[[].indexOf.call(list.children, card)];
      card.hidden=!match(l,f);
    });
  }
  chips.forEach(function(ch){ ch.addEventListener('click', function(){ apply(ch.dataset.f); }); });
  apply('today');

  var today=null;
  try{ today=new Intl.DateTimeFormat('en-CA',{timeZone:'Africa/Cairo',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date()); }catch(e){}
  var call=document.getElementById('call');
  DATA.days.forEach(function(d, i){
    var row=el('div','row'); if(d.date===today){ row.classList.add('is-today'); }
    var dd=el('div','d'); var big=el('b', null, d.day); dd.appendChild(big); dd.appendChild(document.createTextNode(d.date.slice(8)+' Nov'));
    var body=el('div');
    body.appendChild(el('p','obj', d.objective));
    body.appendChild(el('p','tg', d.msgs+' messages · '+d.apps+' applications'+(d.creators? ' · '+d.creators+' creators' : '')));
    body.appendChild(el('p','money', d.money));
    row.appendChild(dd); row.appendChild(body); call.appendChild(row);
    if(d.date===today){
      var label=new Date(d.date+'T12:00:00').toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short'});
      document.getElementById('dayline').textContent=label+' · Day '+(i+1)+' of '+DATA.days.length;
    }
  });
})();
</script>
"""


def main():
    data = json.dumps(payload(), ensure_ascii=False).replace("</", "<\\/")
    html = (TEMPLATE.replace("__DATA__", data).replace("__SHEET__", SHEET_URL)
            .replace("__REPO__", f"{REPO}/tree/{BRANCH}/{PROJECT_DIR}").replace("__BLOB__", BLOB)
            .replace("__PROSPECTS__", str(payload()["stats"]["prospects"]))
            .replace("__DRAFTED__", str(payload()["stats"]["drafted"])))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(html.encode('utf-8')) // 1024} KB)")


if __name__ == "__main__":
    main()

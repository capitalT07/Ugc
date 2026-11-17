#!/usr/bin/env python3
"""Build the CRM files from tools/leads_data.py.

    python3 tools/build_crm.py

Writes:
  crm/leads.csv            every lead, the 20 requested fields + extras
  crm/top30.md             ranked top 30 with ready-to-edit messages
  crm/pipeline.csv         outreach status, one row per contactable lead
  crm/daily_scoreboard.csv targets vs actuals, Nov 17-22
  crm/revenue_ledger.csv   one row per deal; money by stage (header only)
  crm/creators.csv         creator roster (header only)
  crm/UGC-CRM.xlsx         all of the above in one workbook with formulas

CSV files are UTF-8 with a BOM so Excel shows Arabic correctly.
"""
import csv
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlparse

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, str(Path(__file__).resolve().parent))
import leads_data as D  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "crm"

LEAD_COLUMNS = [
    ("id", "ID"),
    ("rank", "Top-30 rank"),
    ("company", "1. Company"),
    ("website", "2. Website"),
    ("instagram", "3. Instagram"),
    ("tiktok", "4. TikTok"),
    ("facebook", "5. Facebook"),
    ("country", "6. Country"),
    ("industry", "7. Industry"),
    ("size", "8. Size (evidence only)"),
    ("why", "9. Why they need it"),
    ("opportunity", "10. Content opportunity"),
    ("contact_person", "11. Contact person (public)"),
    ("contact_method", "12. Contact method"),
    ("source", "13. Source URL"),
    ("date_found", "14. Date found"),
    ("signal", "15. Hiring signal"),
    ("service", "16. Recommended service"),
    ("price", "17. Suggested price"),
    ("message", "18. Opening message"),
    ("priority", "19. Priority"),
    ("status", "20. Follow-up status"),
    ("type", "Type"),
    ("cash", "Cash speed"),
    ("films", "Who films"),
    ("note", "Verify / notes"),
    ("ads_library", "Meta Ads Library search"),
]
URL_KEYS = {"website", "instagram", "tiktok", "facebook", "source", "ads_library"}
ALLOWED_PLACEHOLDERS = {"[OBSERVATION]", "[PORTFOLIO]", "[NAME]", "[first name]"}

PIPELINE_HEADERS = ["Lead ID", "Rank", "Company", "Priority", "Type", "Channel", "Stage",
                    "Date sent", "Last touch", "Next action", "Next action date",
                    "Quote amount", "Currency", "Notes"]
DAILY_HEADERS = ["Date", "Day", "Main objective",
                 "Target: messages sent", "Actual: messages sent",
                 "Target: applications", "Actual: applications",
                 "Target: creators contacted", "Actual: creators contacted",
                 "Prospects researched", "Messages drafted", "Messages approved",
                 "Responses", "Positive responses", "Calls / meetings", "Quotes sent",
                 "Contracts signed", "Videos delivered", "Notes"]
LEDGER_HEADERS = ["Deal ID", "Date opened", "Client", "Lead ID", "Package",
                  "Currency (USD/EGP)", "Quote amount", "Signed amount", "Deposit received",
                  "Delivered value", "Balance received", "Available to withdraw (on platform)",
                  "Landed in Egyptian bank (EGP)", "Creator pay paid (EGP)", "Fees paid",
                  "Payment method", "Notes"]
CREATOR_HEADERS = ["Creator ID", "Name", "City", "Languages / dialects", "Casting notes",
                   "Niches", "Instagram / TikTok", "Sample link", "Audition status",
                   "ID checked, 18+ (Y/N)", "Release signed (Y/N)", "Rate per video (EGP)",
                   "Payment method", "Jobs assigned", "Owed (EGP)", "Paid (EGP)",
                   "Balance (EGP)", "Notes"]


# ---------------------------------------------------------------- helpers
def ads_library_url(name, country):
    if not country:
        return ""
    return ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
            f"&country={country}&q={quote(name)}&search_type=keyword_unordered&media_type=all")


def channel_for(lead):
    t = lead["type"]
    if t == D.T_MOSTAQL:
        return "Mostaql proposal"
    if t == D.T_UPWORK:
        return "Upwork proposal"
    if t == D.T_AGENCY:
        return "Email / LinkedIn / site form"
    if t in (D.T_HIRING, D.T_JOB):
        return "Application / LinkedIn"
    if "LinkedIn" in lead["contact_method"] and not lead["instagram"]:
        return "LinkedIn"
    return "Instagram DM" if lead["instagram"] else "Instagram DM (find account first)"


def next_action_date(lead):
    rank, prio = lead["rank"], lead["priority"]
    if rank and rank <= 20:
        return "2026-11-17"
    if rank:
        return "2026-11-18"
    if prio == "B":
        return "2026-11-19"
    return "2026-11-20"


def prepare():
    leads = []
    for i, raw in enumerate(D.LEADS, start=1):
        lead = dict(raw)
        lead["id"] = f"L{i:03d}"
        lead["ads_library"] = ads_library_url(
            re.sub(r"\s*\(.*\)$", "", lead["company"]), lead.pop("ads_country"))
        leads.append(lead)
    return leads


def validate(leads):
    errors = []
    ranks = sorted(l["rank"] for l in leads if l["rank"])
    if ranks != list(range(1, 31)):
        errors.append(f"top-30 ranks must be exactly 1..30, got {ranks}")
    for l in leads:
        tag = f"{l['id']} {l['company']}"
        if l["priority"] not in ("A", "B", "C"):
            errors.append(f"{tag}: bad priority {l['priority']!r}")
        if not l["source"]:
            errors.append(f"{tag}: missing source URL")
        for key in URL_KEYS:
            url = l[key]
            if url:
                p = urlparse(url)
                if p.scheme != "https" or not p.netloc or " " in url:
                    errors.append(f"{tag}: bad {key} URL {url!r}")
        contactable = l["type"] != D.T_PLATFORM and not l["status"].startswith("Skip")
        if contactable and not l["message"]:
            errors.append(f"{tag}: contactable lead has no message")
        if l["rank"] and not l["message"]:
            errors.append(f"{tag}: top-30 lead has no message")
        for ph in re.findall(r"\[[^\]]+\]", l["message"]):
            if ph not in ALLOWED_PLACEHOLDERS:
                errors.append(f"{tag}: unknown placeholder {ph}")
        for key in ("why", "opportunity", "service", "price", "industry"):
            if not l[key]:
                errors.append(f"{tag}: empty {key}")
    if errors:
        raise SystemExit("Validation failed:\n  " + "\n  ".join(errors))


def pipeline_rows(leads):
    rows = []
    for l in sorted(leads, key=lambda x: (x["rank"] or 999, x["priority"], x["id"])):
        if l["type"] == D.T_PLATFORM:
            continue
        drafted = bool(l["message"])
        rows.append({
            "Lead ID": l["id"], "Rank": l["rank"] or "", "Company": l["company"],
            "Priority": l["priority"], "Type": l["type"], "Channel": channel_for(l),
            "Stage": "Drafted" if drafted else "Not a fit",
            "Date sent": "", "Last touch": "",
            "Next action": "Verify source, fill placeholders, approve, send" if drafted else l["status"],
            "Next action date": next_action_date(l) if drafted else "",
            "Quote amount": "", "Currency": "", "Notes": "",
        })
    return rows


def daily_rows(leads):
    researched = sum(1 for l in leads if l["type"] != D.T_PLATFORM)
    drafted = sum(1 for l in leads if l["message"])
    rows = []
    for d in D.DAILY_PLAN:
        row = {h: "" for h in DAILY_HEADERS}
        row.update({"Date": d["date"], "Day": d["day"], "Main objective": d["objective"],
                    "Target: messages sent": d["msgs"], "Target: applications": d["apps"],
                    "Target: creators contacted": d["creators"]})
        if d["date"] == D.BUILD_DATE:
            row["Prospects researched"] = researched
            row["Messages drafted"] = drafted
            row["Notes"] = "Research Nov 15-16; database and messages delivered Nov 17"
        rows.append(row)
    return rows


def write_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for r in rows:
            w.writerow(r)


# ---------------------------------------------------------------- markdown
def md_escape_cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def write_top30(leads, path):
    top = sorted((l for l in leads if l["rank"]), key=lambda l: l["rank"])
    out = [
        "# Top 30 leads, ranked",
        "",
        f"Built {D.BUILD_DATE} from `tools/leads_data.py`. Research date {D.DATE_FOUND}. Nothing here has been sent.",
        "",
        "Before you send any message:",
        "",
        "1. Open the source link. For Mostaql and Upwork, confirm the project is still open. For brands, find the official account and check it links to their site.",
        "2. Replace `[OBSERVATION]` with one specific thing you saw in their last 3 posts. I could not open Instagram, TikTok or Facebook from my environment, so this part is yours.",
        "3. Replace `[PORTFOLIO]` and `[NAME]` (and `[first name]` where shown). The studio name, T Studio, is already filled in.",
        "4. Send, then set the lead's stage to **Sent** in the Pipeline sheet.",
        "",
        "Ranking: fresh hiring signal and direct payment first, then fit with faceless or roster production, then budget.",
        "Mostaql money is held 14 working days, so Mostaql wins count as booked, not cash, for Nov 22.",
        "",
        "| # | Lead | Type | Offer | Price | Channel | Cash speed |",
        "|---|---|---|---|---|---|---|",
    ]
    for l in top:
        out.append("| {} | {} | {} | {} | {} | {} | {} |".format(
            l["rank"], md_escape_cell(l["company"]), md_escape_cell(l["type"]),
            md_escape_cell(l["service"]), md_escape_cell(l["price"]),
            md_escape_cell(channel_for(l)), md_escape_cell(l["cash"].split(":")[0])))
    out.append("")
    for l in top:
        out += [f"## {l['rank']}. {l['company']}  ·  priority {l['priority']}", ""]
        facts = [
            ("Type", l["type"]), ("Hiring signal", l["signal"]), ("Country", l["country"]),
            ("Industry", l["industry"]), ("Evidence of size", l["size"]),
            ("Why they need it", l["why"]), ("Video idea", l["opportunity"]),
            ("Offer", f"{l['service']}: {l['price']}"), ("Who films", l["films"]),
            ("Contact", l["contact_person"] or "-"), ("How to reach", l["contact_method"]),
        ]
        for label, value in facts:
            if value:
                out.append(f"- **{label}:** {value}")
        links = [("Source", l["source"]), ("Website", l["website"]), ("Instagram", l["instagram"]),
                 ("Facebook", l["facebook"]), ("Meta Ads Library search", l["ads_library"])]
        link_text = " · ".join(f"[{name}]({url})" for name, url in links if url and not (name == "Website" and url == l["source"]))
        if link_text:
            out.append(f"- **Links:** {link_text}")
        if l["note"]:
            out.append(f"- **Check first:** {l['note']}")
        out += ["", "**Opening message**", ""]
        out += [("> " + line) if line else ">" for line in l["message"].split("\n")]
        out += [""]
    path.write_text("\n".join(out), encoding="utf-8")


# ---------------------------------------------------------------- workbook
HEAD_FILL = PatternFill("solid", fgColor="1F2937")
HEAD_FONT = Font(bold=True, color="FFFFFF")
INPUT_FILL = PatternFill("solid", fgColor="FFF4C2")
TOTAL_FILL = PatternFill("solid", fgColor="E5E7EB")
LINK_FONT = Font(color="1D4ED8", underline="single")
WRAP = Alignment(wrap_text=True, vertical="top")


def style_header(ws, ncols, widths=None):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill, cell.font = HEAD_FILL, HEAD_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[1].height = 32
    if widths:
        for c, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(c)].width = w


def put_link(cell, url):
    if url:
        cell.value = url
        cell.hyperlink = url
        cell.font = LINK_FONT


def build_workbook(leads, pipe_rows, d_rows, path):
    wb = Workbook()
    dash = wb.active
    dash.title = "Dashboard"
    ws_leads = wb.create_sheet("Leads")
    ws_top = wb.create_sheet("Top 30")
    ws_pipe = wb.create_sheet("Pipeline")
    ws_daily = wb.create_sheet("Daily")
    ws_led = wb.create_sheet("Revenue Ledger")
    ws_cre = wb.create_sheet("Creators")
    ws_pack = wb.create_sheet("Packages")
    ws_hunt = wb.create_sheet("Hunting Links")
    ws_list = wb.create_sheet("Lists")

    # ---- Lists (validation sources)
    ws_list["A1"], ws_list["C1"] = "Pipeline stages", "Currencies"
    for i, s in enumerate(D.PIPELINE_STAGES, start=2):
        ws_list.cell(row=i, column=1, value=s)
    for i, c in enumerate(("USD", "EGP"), start=2):
        ws_list.cell(row=i, column=3, value=c)
    style_header(ws_list, 3, [28, 4, 14])
    stage_ref = f"Lists!$A$2:$A${len(D.PIPELINE_STAGES) + 1}"

    # ---- Pipeline
    ws_pipe.append(PIPELINE_HEADERS)
    for r in pipe_rows:
        ws_pipe.append([r[h] for h in PIPELINE_HEADERS])
    style_header(ws_pipe, len(PIPELINE_HEADERS), [8, 6, 34, 8, 22, 22, 20, 12, 12, 34, 14, 12, 10, 30])
    dv_stage = DataValidation(type="list", formula1=f"={stage_ref}", allow_blank=True)
    dv_cur = DataValidation(type="list", formula1="=Lists!$C$2:$C$3", allow_blank=True)
    ws_pipe.add_data_validation(dv_stage)
    ws_pipe.add_data_validation(dv_cur)
    dv_stage.add("G2:G500")
    dv_cur.add("M2:M500")
    ws_pipe.freeze_panes = "D2"
    ws_pipe.auto_filter.ref = f"A1:{get_column_letter(len(PIPELINE_HEADERS))}{len(pipe_rows) + 1}"
    in_pipeline = {r["Lead ID"] for r in pipe_rows}

    # ---- Leads
    keys = [k for k, _ in LEAD_COLUMNS]
    ws_leads.append([h for _, h in LEAD_COLUMNS])
    status_col = keys.index("status") + 1
    for row_i, l in enumerate(leads, start=2):
        for col_i, key in enumerate(keys, start=1):
            cell = ws_leads.cell(row=row_i, column=col_i)
            if key in URL_KEYS:
                put_link(cell, l[key])
            elif key == "status" and l["id"] in in_pipeline:
                cell.value = (f'=IFERROR(INDEX(Pipeline!$G$2:$G$500,MATCH($A{row_i},Pipeline!$A$2:$A$500,0)),'
                              f'"Not in pipeline")')
            else:
                cell.value = l[key] if l[key] is not None else ""
            if key in ("why", "opportunity", "message", "size", "note", "service", "contact_method"):
                cell.alignment = WRAP
    widths = {"id": 7, "rank": 6, "company": 30, "website": 28, "instagram": 28, "tiktok": 18, "facebook": 24,
              "country": 16, "industry": 24, "size": 32, "why": 44, "opportunity": 44, "contact_person": 26,
              "contact_method": 30, "source": 32, "date_found": 11, "signal": 30, "service": 26, "price": 24,
              "message": 70, "priority": 8, "status": 22, "type": 22, "cash": 30, "films": 28, "note": 40,
              "ads_library": 30}
    style_header(ws_leads, len(keys), [widths[k] for k in keys])
    ws_leads.freeze_panes = "D2"
    ws_leads.auto_filter.ref = f"A1:{get_column_letter(len(keys))}{len(leads) + 1}"
    prio_letter = get_column_letter(keys.index("priority") + 1)
    type_letter = get_column_letter(keys.index("type") + 1)

    # ---- Top 30
    top_headers = ["Rank", "Company", "Priority", "Type", "Offer", "Price", "Who films",
                   "How to reach", "Opening message", "Source", "Check first"]
    ws_top.append(top_headers)
    for l in sorted((x for x in leads if x["rank"]), key=lambda x: x["rank"]):
        ws_top.append([l["rank"], l["company"], l["priority"], l["type"], l["service"], l["price"],
                       l["films"], l["contact_method"], l["message"], "", l["note"]])
        r = ws_top.max_row
        put_link(ws_top.cell(row=r, column=10), l["source"])
        for c in (5, 7, 8, 9, 11):
            ws_top.cell(row=r, column=c).alignment = WRAP
    style_header(ws_top, len(top_headers), [6, 30, 8, 22, 26, 24, 26, 30, 80, 30, 40])
    ws_top.freeze_panes = "C2"

    # ---- Daily
    ws_daily.append(DAILY_HEADERS)
    for r in d_rows:
        ws_daily.append([r[h] for h in DAILY_HEADERS])
    total_row = len(d_rows) + 2
    ws_daily.cell(row=total_row, column=1, value="TOTAL")
    last_num_col = DAILY_HEADERS.index("Videos delivered") + 1
    for c in range(4, last_num_col + 1):
        L_ = get_column_letter(c)
        cell = ws_daily.cell(row=total_row, column=c, value=f"=SUM({L_}2:{L_}{total_row - 1})")
        cell.font = Font(bold=True)
    for c in range(1, len(DAILY_HEADERS) + 1):
        ws_daily.cell(row=total_row, column=c).fill = TOTAL_FILL
    for r in range(2, total_row):
        for c in (5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
            ws_daily.cell(row=r, column=c).fill = INPUT_FILL
    style_header(ws_daily, len(DAILY_HEADERS), [11, 6, 44] + [11] * (len(DAILY_HEADERS) - 4) + [40])
    ws_daily.freeze_panes = "D2"

    def daily_ref(header):
        return f"=Daily!{get_column_letter(DAILY_HEADERS.index(header) + 1)}{total_row}"

    # ---- Revenue Ledger
    ws_led.append(LEDGER_HEADERS)
    style_header(ws_led, len(LEDGER_HEADERS), [9, 11, 26, 8, 18, 10, 11, 11, 11, 11, 11, 14, 14, 14, 10, 18, 36])
    ws_led.add_data_validation(dv_cur_led := DataValidation(type="list", formula1="=Lists!$C$2:$C$3", allow_blank=True))
    dv_cur_led.add("F2:F500")
    for r in range(2, 101):
        for c in range(7, 16):
            ws_led.cell(row=r, column=c).number_format = "#,##0"
    ws_led.freeze_panes = "D2"

    # ---- Creators
    ws_cre.append(CREATOR_HEADERS)
    owed_c, paid_c, bal_c = (CREATOR_HEADERS.index(h) + 1 for h in ("Owed (EGP)", "Paid (EGP)", "Balance (EGP)"))
    for r in range(2, 22):
        o, p = get_column_letter(owed_c), get_column_letter(paid_c)
        ws_cre.cell(row=r, column=1, value=f"C{r - 1:02d}")
        ws_cre.cell(row=r, column=bal_c, value=f'=IF(AND({o}{r}="",{p}{r}=""),"",N({o}{r})-N({p}{r}))')
    style_header(ws_cre, len(CREATOR_HEADERS), [8, 20, 12, 20, 22, 20, 26, 26, 14, 10, 10, 10, 16, 20, 10, 10, 10, 30])
    ws_cre.freeze_panes = "C2"

    # ---- Packages
    ws_pack.append(["Package", "Deliverables", "USD", "EGP", "Usage", "Revisions", "Delivery",
                    "Payment terms", "Creator pay (EGP, est.)"])
    for p in D.PACKAGES:
        ws_pack.append([p["name"], p["deliverables"], p["usd"], p["egp"], p["usage"], p["revisions"],
                        p["delivery"], p["terms"], p["creator_cost_egp"]])
    ws_pack.append([])
    ws_pack.append(["Extras", "USD", "EGP"])
    extras_head = ws_pack.max_row
    for name, usd, egp in D.EXTRAS:
        ws_pack.append([name, usd, egp])
    for c in range(1, 4):
        ws_pack.cell(row=extras_head, column=c).font = Font(bold=True)
    for row in ws_pack.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = WRAP
    style_header(ws_pack, 9, [24, 44, 8, 9, 30, 16, 22, 24, 18])

    # ---- Hunting links
    ws_hunt.append(["Search", "Link", "What to look for"])
    for name, url, what in D.HUNTING_LINKS:
        ws_hunt.append([name, "", what])
        put_link(ws_hunt.cell(row=ws_hunt.max_row, column=2), url)
    style_header(ws_hunt, 3, [48, 60, 48])

    # ---- Dashboard
    led = "'Revenue Ledger'"
    cur = f"{led}!$F$2:$F$500"

    def usd(col):
        rng = f"{led}!${col}$2:${col}$500"
        return f'=SUMPRODUCT(({cur}="USD")*({rng}))+SUMPRODUCT(({cur}="EGP")*({rng}))/$B$4'

    potential = (f'=SUMPRODUCT(({cur}="USD")*({led}!$H$2:$H$500="")*({led}!$G$2:$G$500))'
                 f'+SUMPRODUCT(({cur}="EGP")*({led}!$H$2:$H$500="")*({led}!$G$2:$G$500))/$B$4')

    dash["A1"] = "UGC studio dashboard"
    dash["A1"].font = Font(bold=True, size=14)
    dash["A2"] = "Money counts only when it reaches you. Quotes are potential, not revenue. Enter deals in 'Revenue Ledger'."
    dash["A4"], dash["B4"] = "FX: EGP per 1 USD (edit me)", D.FX_EGP_PER_USD
    dash["B4"].fill = INPUT_FILL
    dash["A6"], dash["B6"], dash["C6"], dash["D6"] = "Money", "USD equiv.", "EGP equiv.", "How it is counted"
    money = [
        ("1. Potential revenue (open quotes)", potential, "Quote amount on deals with no signed amount yet"),
        ("2. Signed contracts (count)", f'=COUNTIF({led}!$H$2:$H$500,">0")', "Deals with a signed amount"),
        ("3. Booked revenue (signed value)", usd("H"), "Signed amount"),
        ("4. Deposits actually received", usd("I"), "Deposit received"),
        ("5. Completed work (delivered value)", usd("J"), "Delivered value"),
        ("6. Final balances received", usd("K"), "Balance received"),
        ("7. Available to withdraw (platforms)", usd("L"), "Cleared on Mostaql/Upwork/etc., not yet withdrawn"),
        ("8. Landed in Egyptian bank", f"=SUM({led}!$M$2:$M$500)/$B$4", "Landed in Egyptian bank (EGP)"),
        ("Cash collected (4 + 6)", "=B10+B12", "Deposits + balances"),
        ("Creator pay paid", f"=SUM({led}!$N$2:$N$500)/$B$4", "Creator pay paid (EGP)"),
        ("Fees paid", usd("O"), "Platform and transfer fees"),
        ("KEPT (cash - creators - fees)", "=B15-B16-B17", "What you actually keep"),
        ("Progress to $1,000 kept", "=B18/1000", ""),
        ("Progress to $2,000 kept", "=B18/2000", ""),
    ]
    for i, (label, formula, how) in enumerate(money, start=7):
        dash.cell(row=i, column=1, value=label)
        dash.cell(row=i, column=2, value=formula)
        dash.cell(row=i, column=4, value=how)
        if label.startswith("2."):
            dash.cell(row=i, column=2).number_format = "0"
        elif label.startswith("Progress"):
            dash.cell(row=i, column=2).number_format = "0%"
        else:
            dash.cell(row=i, column=2).number_format = '"$"#,##0'
            dash.cell(row=i, column=3, value=f"=B{i}*$B$4").number_format = '"EGP "#,##0'
    for c in range(1, 5):
        dash.cell(row=18, column=c).font = Font(bold=True)
        dash.cell(row=18, column=c).fill = TOTAL_FILL

    dash["A23"], dash["B23"], dash["C23"] = "Activity (from Daily)", "Target", "Actual"
    activity = [
        ("Messages sent", "Target: messages sent", "Actual: messages sent"),
        ("Applications", "Target: applications", "Actual: applications"),
        ("Creators contacted", "Target: creators contacted", "Actual: creators contacted"),
        ("Prospects researched", None, "Prospects researched"),
        ("Messages drafted", None, "Messages drafted"),
        ("Messages approved", None, "Messages approved"),
        ("Responses", None, "Responses"),
        ("Positive responses", None, "Positive responses"),
        ("Calls / meetings", None, "Calls / meetings"),
        ("Quotes sent", None, "Quotes sent"),
        ("Contracts signed", None, "Contracts signed"),
        ("Videos delivered", None, "Videos delivered"),
    ]
    for i, (label, target, actual) in enumerate(activity, start=24):
        dash.cell(row=i, column=1, value=label)
        if target:
            dash.cell(row=i, column=2, value=daily_ref(target))
        dash.cell(row=i, column=3, value=daily_ref(actual))

    start = 24 + len(activity) + 2
    dash.cell(row=start, column=1, value="Pipeline by stage")
    dash.cell(row=start, column=2, value="Leads")
    for i, stage in enumerate(D.PIPELINE_STAGES, start=start + 1):
        dash.cell(row=i, column=1, value=stage)
        dash.cell(row=i, column=2, value=f'=COUNTIF(Pipeline!$G$2:$G$500,A{i})')

    dash["F6"], dash["G6"] = "Leads by priority", "Count"
    for i, p in enumerate(("A", "B", "C"), start=7):
        dash.cell(row=i, column=6, value=p)
        dash.cell(row=i, column=7, value=f'=COUNTIF(Leads!${prio_letter}$2:${prio_letter}$500,F{i})')
    dash["F11"], dash["G11"] = "Leads by type", "Count"
    types = [D.T_BRAND, D.T_AGENCY, D.T_MOSTAQL, D.T_UPWORK, D.T_HIRING, D.T_JOB, D.T_PLATFORM]
    for i, t in enumerate(types, start=12):
        dash.cell(row=i, column=6, value=t)
        dash.cell(row=i, column=7, value=f'=COUNTIF(Leads!${type_letter}$2:${type_letter}$500,F{i})')

    for cell_ref in ("A6", "B6", "C6", "D6", "A23", "B23", "C23", f"A{start}", f"B{start}", "F6", "G6", "F11", "G11"):
        dash[cell_ref].font = Font(bold=True)
    for col, w in zip("ABCDEFG", (40, 14, 16, 48, 3, 30, 8)):
        dash.column_dimensions[col].width = w

    wb.active = 0
    wb.save(path)


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(exist_ok=True)
    leads = prepare()
    validate(leads)

    write_csv(OUT / "leads.csv", [h for _, h in LEAD_COLUMNS],
              [{h: (l[k] if l[k] is not None else "") for k, h in LEAD_COLUMNS} for l in leads])
    write_top30(leads, OUT / "top30.md")
    pipe = pipeline_rows(leads)
    write_csv(OUT / "pipeline.csv", PIPELINE_HEADERS, pipe)
    days = daily_rows(leads)
    write_csv(OUT / "daily_scoreboard.csv", DAILY_HEADERS, days)
    write_csv(OUT / "revenue_ledger.csv", LEDGER_HEADERS, [])
    write_csv(OUT / "creators.csv", CREATOR_HEADERS, [])
    build_workbook(leads, pipe, days, OUT / "UGC-CRM.xlsx")

    by_type = {}
    for l in leads:
        by_type[l["type"]] = by_type.get(l["type"], 0) + 1
    prospects = sum(v for k, v in by_type.items() if k != D.T_PLATFORM)
    print(f"Leads: {len(leads)} rows ({prospects} prospects + {by_type.get(D.T_PLATFORM, 0)} platforms)")
    for k, v in sorted(by_type.items(), key=lambda kv: -kv[1]):
        print(f"  {v:3d}  {k}")
    print("Priority:", {p: sum(1 for l in leads if l["priority"] == p) for p in "ABC"})
    print(f"Messages drafted: {sum(1 for l in leads if l['message'])}; pipeline rows: {len(pipe)}")
    print(f"Wrote {', '.join(sorted(p.name for p in OUT.iterdir()))}")


if __name__ == "__main__":
    main()

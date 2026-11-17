# UGC studio launch · Nov 17–22, 2026

**Status, Tue Nov 17:** research done; 94 prospects and 6 creator platforms in the CRM; 88 outreach messages drafted. **Nothing has been sent, no deals, no revenue yet.**

**Work from these two links (both private to you):**
- **Launch HQ page**, phone-friendly, with copy buttons for every top-30 message: https://claude.ai/artifact/8H4xJs28pTWZxocBQUGHAW
- **CRM Google Sheet** (your live tracker): https://docs.google.com/spreadsheets/d/1SY54jhhQfHfHGCB_F2n_78gnFDvXCowGhhpnUA55PxU/edit

**The business:** an Arabic-first UGC studio in Cairo. You sell, script, direct, edit and film faceless footage; creators from a small roster film the on-camera parts. Short-form editing for brands and agencies is the second service. Goal: $1,000 (stretch $2,000) by Sunday Nov 22, counted only when it reaches you.

## Today's three actions

1. **Recruit (20 min).** Send the recruiting message in [docs/09-creator-roster.md](docs/09-creator-roster.md) to 10 people you know. Ask for the 20-second audition by tomorrow.
2. **Film your first faceless sample (1–2 h).** The app demo, concept #3 in [docs/04-portfolio-scripts.md](docs/04-portfolio-scripts.md). Order one basic item from a local brand for the unboxing (#2).
3. **Send the first batch (1.5 h).** From [crm/top30.md](crm/top30.md), fill `[OBSERVATION]`, approve, send: Mostaql proposals **2, 3, 11, 12**; brand DMs **1, 4, 5, 9, 10**; partner messages **6, 7, 8**. Then set each to *Sent* in Pipeline.

## Files

| File | What it's for |
|---|---|
| [crm/top30.md](crm/top30.md) | The 30 best leads, ranked, each with facts, a video idea, a price and a ready message |
| [crm/UGC-CRM.xlsx](crm/UGC-CRM.xlsx) | Workbook: Dashboard (the 8 money stages), Leads, Top 30, Pipeline, Daily, Revenue Ledger, Creators, Packages, Hunting Links |
| `crm/*.csv` | The same sheets as CSV (UTF-8; Arabic intact) |
| [docs/01-business-decision.md](docs/01-business-decision.md) | Why this model; TikTok audit worksheet for you to fill |
| [docs/02-offer-and-pricing.md](docs/02-offer-and-pricing.md) | Packages, editing rates, rights, extras, creator costs, revenue math |
| [docs/03-market-evidence.md](docs/03-market-evidence.md) | Prices, demand, platforms, sources; findings vs assumptions |
| [docs/04-portfolio-scripts.md](docs/04-portfolio-scripts.md) | Six concept ads with hooks, full scripts (AR/EN, FR for two), shot lists, CapCut steps |
| [docs/05-sales-system.md](docs/05-sales-system.md) | Templates for every channel, follow-ups, objection replies, quote and payment messages |
| [docs/06-payments-and-agreement.md](docs/06-payments-and-agreement.md) | Payment options from Egypt, client agreement (EN/AR), invoice, scam checklist |
| [docs/07-delivery-workflow.md](docs/07-delivery-workflow.md) | Offer-to-repeat-order steps, brief form, QA checklist, optional n8n flow |
| [docs/08-six-day-plan.md](docs/08-six-day-plan.md) | Day-by-day plan with targets, your tasks and mine |
| [docs/09-creator-roster.md](docs/09-creator-roster.md) | Recruiting, audition, scorecard, creator pay, creator release (EN/AR), filming brief |
| `tools/leads_data.py`, `tools/build_crm.py` | Source of all lead data and the script that builds the CRM files |
| `hq/launch-hq.html`, `tools/build_hq.py` | The Launch HQ page and the script that builds it from the same data |

## Placeholders in messages

| Placeholder | Replace with |
|---|---|
| `[OBSERVATION]` | One specific thing you saw in their last 3 posts (I couldn't open social feeds) |
| `[PORTFOLIO]` | Your Canva portfolio link (until it's live, see [docs/08](docs/08-six-day-plan.md#before-the-first-portfolio-piece-is-ready)) |
| `[NAME]`, `[STUDIO]`, `[first name]` | Your name, your studio name, the recipient's first name |

## Using the CRM

- **Status lives in Pipeline**, money in **Revenue Ledger** (one row per deal: quote, signed, deposit, delivered, balance, available to withdraw, landed in bank, creator pay, fees), activity in **Daily**. The Dashboard adds it up in USD and EGP (FX cell is editable).
- Recalculation was tested in LibreOffice with sample deals; totals matched hand calculations.
- **Track live work in the Google Sheet.** It was created from the workbook on Nov 17; rebuilding the repo files does not change it.
- **Rebuilding** (`python3 tools/build_crm.py` and `python3 tools/build_hq.py` after editing `tools/leads_data.py`) overwrites `crm/` and `hq/`.
- **Creator personal data** (names, phones, IDs) goes in your private sheet only, never in this repository.

## Verified and not verified

- **Verified from sources (linked per row):** every lead, price range, platform fee and hold, and the TikTok case studies.
- **Not verified:** whether each project is still open; brand handles not named in a source (left blank); live link checks. My environment's network policy blocked TikTok, Instagram, Facebook, X, Reddit and Upwork pages.
- **Estimates:** posting dates from project IDs, creator pay, reply rates, hours per package. Each is labelled where it's used.

## What I need from you

1. Your TikTok numbers and the TikTok One check (worksheet in [docs/01](docs/01-business-decision.md#tiktok-audit-worksheet)).
2. Studio name, and which bank or wallet receives InstaPay.
3. Replies from leads and creators as they come in, so I can adjust messages, quotes and scripts.
4. Approval of each outreach batch before anything is sent.

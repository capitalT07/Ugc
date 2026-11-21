# T Studio: UGC studio launch · Nov 17–22, 2026

Part of [Capital T](../../README.md), the group of T businesses.

**Status, Sat Nov 21: research week (Nov 22–28) before selling.** Brand sales messages are paused and the $1,000-by-Nov-22 goal is dropped. The CRM still holds 94 prospects and 71 drafted messages for later. **Nothing has been sent, no deals, no revenue yet.** Decision on Sat Nov 28: keep, narrow or change the offer ([research/](research/00-context.md)).

**How we got here:** every decision since Nov 15, and why, is in [docs/00-session-log.md](docs/00-session-log.md).

**Work from these two links (both private to you):**
- **Launch HQ page**, phone-friendly, with copy buttons for every top-30 message: https://claude.ai/artifact/8H4xJs28pTWZxocBQUGHAW
- **CRM Google Sheet "T Studio CRM"** (your live tracker): https://docs.google.com/spreadsheets/d/1ZFc6ZsEfIY8zdxbtppggHs5MAA2vIeqfk7vwN4soW_8/edit

**The business:** T Studio, an Arabic-first UGC studio in Cairo. **You** sell, cast creators, brief them and check every video; **creators** film and edit; **I** write the scripts and hooks. You don't need to film or edit. The first goal was $1,000 by Sunday Nov 22; on Nov 21 you chose to research the market first.

## Today's three actions

Research week, Nov 22–28. Brand sales are paused; these replace the selling steps until the decision on Sat Nov 28.

1. **Interviews (30 min to send).** Pick 10–12 people from the [interview kit](research/01-interview-kit.md#4-who-to-ask-suggested-you-choose), approve the message, and send it yourself. These are questions, not a pitch.
2. **Creators (15 min).** Message the 5 shortlisted Khamsat creators through Khamsat ([message](docs/09-creator-roster.md#hiring-on-khamsat)). Don't order anything. Their prices and answers go into the research.
3. **Replies (5 min each).** Paste or screenshot every reply to Claude. After 2 days, send one polite follow-up to anyone silent.

**Also, when you have time:**
- finish both profiles: bio with `📩 Tstudio.eg@gmail.com`, a logo, business account;
- ask your bank whether your Banque Misr Visa pays in dollars;
- read [docs/10-studio-basics.md](docs/10-studio-basics.md).

## Files

| File | What it's for |
|---|---|
| [crm/top30.md](crm/top30.md) | The 30 best leads, ranked, each with facts, a video idea, a price and a ready message |
| [crm/UGC-CRM.xlsx](crm/UGC-CRM.xlsx) | Workbook: Dashboard (the 8 money stages), Leads, Top 30, Pipeline, Daily, Revenue Ledger, Creators, Packages, Hunting Links |
| `crm/*.csv` | The same sheets as CSV (UTF-8; Arabic intact) |
| [docs/00-session-log.md](docs/00-session-log.md) | Session record, Nov 15–17: timeline, decisions and why, problems and fixes, open items |
| [docs/01-business-decision.md](docs/01-business-decision.md) | Why this model; studio name, handles and accounts |
| [docs/02-offer-and-pricing.md](docs/02-offer-and-pricing.md) | Packages, who does what, rights, extras, creator costs, revenue math |
| [docs/03-market-evidence.md](docs/03-market-evidence.md) | Prices, demand, platforms, sources; findings vs assumptions |
| [docs/04-portfolio-scripts.md](docs/04-portfolio-scripts.md) | Six concept scripts with hooks (AR/EN, FR for two), shot lists, the editing spec for creators, how to get the first samples |
| [docs/05-sales-system.md](docs/05-sales-system.md) | Templates for every channel, follow-ups, objection replies, quote and payment messages |
| [docs/06-payments-and-agreement.md](docs/06-payments-and-agreement.md) | Payment options from Egypt, client agreement (EN/AR), invoice, scam checklist |
| [docs/07-delivery-workflow.md](docs/07-delivery-workflow.md) | Offer-to-repeat-order steps, brief form, QA checklist, optional n8n flow |
| [docs/08-six-day-plan.md](docs/08-six-day-plan.md) | Day-by-day plan with targets, your tasks and mine |
| [docs/09-creator-roster.md](docs/09-creator-roster.md) | Recruiting creators who film and edit, audition, scorecard, pay, concept-ad swap, release (EN/AR), production brief |
| [docs/10-studio-basics.md](docs/10-studio-basics.md) | 30-minute guide: hooks, what good filming and editing look like, how to explain the process |
| [site/index.html](site/index.html) | T Studio landing page: creators first, then businesses; Arabic and English; concept ads only, labelled |
| [research/](research/00-context.md) | Research week: context draft, interview kit, competitors and demand, customer insight; positioning, offer and the decision follow by Nov 28 |
| [docs/11-ai-video-prompts.md](docs/11-ai-video-prompts.md) | Optional: Higgsfield prompts for AI product clips (no AI people, labelled AI), cost, how to use |
| `tools/leads_data.py`, `tools/build_crm.py` | Source of all lead data and the script that builds the CRM files |
| `hq/launch-hq.html`, `tools/build_hq.py` | The Launch HQ page and the script that builds it from the same data |
| [CLAUDE.md](../../CLAUDE.md) | Rules and build steps that any new Claude session reads first |

## Placeholders in messages

| Placeholder | Replace with |
|---|---|
| `[OBSERVATION]` | One specific thing you saw in their last 3 posts (I couldn't open social feeds) |
| `[PORTFOLIO]` | Your Canva portfolio link (until it's live, see [docs/08](docs/08-six-day-plan.md#before-the-first-samples-are-ready)) |
| `[NAME]`, `[first name]` | Your name, the recipient's first name. The studio name, T Studio, is already filled in |

## Using the CRM

- **Status lives in Pipeline**, money in **Revenue Ledger** (one row per deal: quote, signed, deposit, delivered, balance, available to withdraw, landed in bank, creator pay, fees), activity in **Daily**. The Dashboard adds it up in USD and EGP (FX cell is editable).
- Recalculation was tested in LibreOffice with sample deals; totals matched hand calculations.
- **Track live work in the Google Sheet "T Studio CRM".** It was created from the rebuilt workbook on Nov 17; rebuilding the repo files does not change it. The first sheet, "UGC CRM", and an outdated draft of "T Studio CRM" were never edited and are in your Drive trash (Google deletes trashed files after 30 days).
- **Rebuilding** (`python3 tools/build_crm.py` and `python3 tools/build_hq.py` after editing `tools/leads_data.py`) overwrites `crm/` and `hq/`.
- **Creator personal data** (names, phones, IDs) goes in your private sheet only, never in this repository.

## Verified and not verified

- **Verified from sources (linked per row):** every lead, price range, platform fee and hold, and the TikTok case studies.
- **Not verified:** whether each project is still open; brand handles not named in a source (left blank); live link checks. My environment's network policy blocked TikTok, Instagram, Facebook, X, Reddit and Upwork pages.
- **Estimates:** posting dates from project IDs, creator pay, reply rates, hours per package. Each is labelled where it's used.

## What I need from you

1. Whether your Banque Misr Visa can pay in dollars on Khamsat (ask the bank), and when WhatsApp Business works again, so its number can go on the landing page. The handles, Gmail and InstaPay are done.
2. Replies from leads and creators as they come in, so I can adjust messages, quotes and scripts.
3. Approval of each outreach batch before anything is sent.

# CLAUDE.md

Guidance for Claude sessions in this repository. Before doing anything, read `README.md` (status and today's actions), `docs/00-session-log.md` (what was decided and why) and `docs/08-six-day-plan.md` (the day-by-day plan).

## The project

T Studio is an Arabic-first UGC ad studio in Cairo, launched on Nov 17, 2026. Goal: $1,000 (stretch $2,000) by Sunday Nov 22, 2026, counted only when the money reaches the owner's account.

- **The owner** sells, casts creators, briefs them, checks every video, and handles clients and money. They are not on camera, and their personal TikTok is not used for the business.
- **Creators** film and edit each video. They are paid EGP 1,000–2,000 per finished video out of the client's payment.
- **Claude** writes the scripts and hooks, drafts messages and keeps the docs and CRM current.

Never write, in any language, that the owner films or edits. Editing-only work is not offered.

## Rules from the owner's brief (every session)

- Nothing is sent, posted or applied for without the owner's explicit approval of the exact text. Claude drafts; the owner sends.
- No made-up leads, contacts, prices, testimonials, statistics, job posts or results, and no guaranteed results.
- Give a source for each fact. Keep findings apart from assumptions and label estimates.
- A quote or promise is not revenue. Money stages are tracked separately in the Revenue Ledger.
- Never say a client was contacted, an order secured or a payment received unless the owner said so.
- No passwords. No mass or unsolicited messaging; follow each platform's and subreddit's rules. No buying followers, and no VPNs to get around monetisation rules.
- No private personal data in this repo: creator names, phone numbers and IDs stay in the owner's private sheet.
- AI presenters only if a client asks, always labelled as AI, never scripted as a real customer.

## How the files are built

`tools/leads_data.py` is the single source for leads, messages, packages, pipeline stages, the daily plan and hunting links. After editing it, run:

- `python3 tools/build_crm.py` → `crm/` (CSVs, `top30.md`, `UGC-CRM.xlsx`). It stops with an error if the top-30 ranks aren't exactly 1–30, a source is missing, a URL isn't https, a lead that can be contacted (or any top-30 lead) has no message, a message uses an unknown placeholder, or `why`, `opportunity`, `service`, `price` or `industry` is empty.
- `python3 tools/build_hq.py` → `hq/launch-hq.html`.

Never edit `crm/` or `hq/` by hand; rebuilding overwrites them. The only placeholders allowed in messages are `[OBSERVATION]`, `[PORTFOLIO]`, `[NAME]` and `[first name]`; the studio name is written out. Messages to Egyptian brands are in Egyptian Arabic; English and French are used where they fit.

## Live data and the published page

- **Google Sheet "T Studio CRM"** in the owner's Drive is where live work is tracked: https://docs.google.com/spreadsheets/d/1ZFc6ZsEfIY8zdxbtppggHs5MAA2vIeqfk7vwN4soW_8/edit. Rebuilding the repo doesn't update it. Never replace, overwrite or trash it without asking: the owner enters data there.
- **Launch HQ** (private page, built from `hq/launch-hq.html`): https://claude.ai/artifact/8H4xJs28pTWZxocBQUGHAW. To update it from a new conversation, read it first, then publish with its `url` so the link stays the same.

## Environment and git

- This cloud environment's network policy blocks TikTok, Instagram, Facebook, X, Reddit and Upwork pages, and a request to allow them was rejected. Use web search (it refuses searches limited to reddit.com), and ask the owner for anything only they can see (feeds, DMs, replies).
- Work on `claude/1k-2k-business-7-days-w9vmgs`, which is the repo's default branch. Commit and push there after each finished step, since a session can stop on a usage limit. No pull request unless the owner asks.

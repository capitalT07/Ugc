# Session log: Nov 15–17, 2026

The record of the first working session on T Studio: what you asked for, what we decided and why, what was built, what went wrong and what's next. Times are Cairo time (UTC+2), taken from the chat record, git and Google Drive. For today's to-do list, see the [README](../README.md).

## Summary

- **Goal:** collect $1,000 (stretch $2,000) by Sunday Nov 22, 2026 from an online service business. Money counts only when it reaches your account.
- **Business:** T Studio, an Arabic-first UGC ad studio in Cairo. You sell, cast creators, brief them and check every video; creators film and edit; I write the scripts and hooks.
- **Built:** 94 researched prospects and 6 creator platforms, 71 drafted messages, a ranked top 30, three packages, ten guides, a CRM (repo files and a Google Sheet) and the Launch HQ page.
- **Status on Tue Nov 17, evening:** nothing sent, no replies, no deals, $0 collected.
- **Next:** find creators on Khamsat, set up T Studio's accounts, and send leads 1–12 once you approve them ([README](../README.md#todays-three-actions)).

## Timeline

| When | What happened |
|---|---|
| **Sun Nov 15**, 13:12 | You sent the master brief: compare four business models, research the market live, build a lead database, an offer, portfolio scripts, a sales system, trackers, payment options and a day-by-day plan, under strict rules on honesty, approval and money. |
| 13:12–13:15 | My environment's network policy blocked TikTok, Instagram, Facebook, Reddit and Upwork, and my request to allow them (with X and LinkedIn) was rejected. Your TikTok profile couldn't be opened either, so it was never audited. From here on, lead facts come from search-indexed pages. |
| 13:12–13:24 | 86 web searches: prices, platforms and payouts, open Mostaql and Upwork projects, companies hiring, Egyptian brands and agencies. 2 were refused because the search tool can't search Reddit. |
| 13:28 | I proposed the first plan: a UGC and short-form editing service. |
| 15:18–15:23 | You didn't approve it and asked whether your face would be in the videos, then about AI-generated presenters. I ran 6 searches on AI ads (results, platform labels, the US FTC rule, tool prices) and asked how you wanted the videos made. |
| **Mon Nov 16**, 06:48 | You asked about getting other people to film instead of you. The next search hit the weekly usage limit and work stopped. |
| 22:23–22:26 | You wrote again and work resumed. You chose a roster of creators, with you directing and editing, and I proposed the second plan: a UGC studio with a creator roster, editing as a second service, a private Launch HQ page and a private Google Sheet. |
| **Tue Nov 17**, 11:04–11:12 | You approved the plan. My first reply failed because the account was out of usage credits for that model; you said "Try again", switched models and said it again, and work resumed at 11:12. |
| 11:28–11:41 | Three commits: lead database and CRM; offer, sales system and creator kit; portfolio scripts, payments, delivery workflow and the six-day plan. The first push was refused; the repo was already connected, and the push at 11:33 worked. |
| 11:43–11:47 | Google Sheet "UGC CRM" created from the workbook (11:43); Launch HQ published, version 1 (11:46); committed (11:47). |
| 13:30–13:36 | You said your TikTok is about fitness and running and doesn't suit the business, and suggested the name T Studio. Two searches found no Cairo business or UGC agency using it. You chose "T Studio" with a UGC tag and approved the change. |
| 13:39 | Launch HQ version 2. Commit: the studio is named T Studio and your personal TikTok is out of all messages and plans. |
| 16:51–16:59 | You pointed out that the messages promised filming, hooks and editing you don't know how to do. Two searches checked how UGC creators deliver edited videos and what freelance editors charge. You chose: creators film and edit, and approved that plan. |
| 17:14–17:23 | New sheet "T Studio CRM" created (17:14) and the old "UGC CRM" moved to Drive trash (17:16). A last check found five leftover editing lines; I fixed them, created the sheet again (17:23) and moved the outdated copy to trash. |
| 17:23–17:24 | Launch HQ version 3. Commit: creators film and edit; studio basics guide added. |
| 17:31–17:39 | You asked me to document the session and chose a file in the project plus a guide for future sessions. Commit at 17:39: this log and `CLAUDE.md`. |
| 17:44 | The chat-history check came back. I corrected this log's times and counts (97 searches, not about 55; the AI research was on Nov 15). |
| 18:17–18:26 | You asked what to do now. I set out tonight's order and added WhatsApp Business text to paste (commit at 18:26). |
| 18:37 | You said you don't know anyone to send the recruiting message to. Five searches found creators, many of them Egyptian, selling edited UGC videos on Khamsat, most from about $25 a video. Decision 7: hire creators there first. The docs, Launch HQ and the CRM files were updated. |

## Decisions and why

### 1. Business model: a UGC studio, Arabic-first

- **Options:** A UGC studio, B short-form editing, C content systems, D automations.
- **Chosen:** A. Editing (B) was the second service at first and was dropped this week by decision 4. Final scores: A 40, B 28, C 34, D 29 ([01](01-business-decision.md)).
- **Why:** live demand (22 Arabic UGC and Reels projects on Mostaql, an Upwork post for Arabic-speaking creators, an Egyptian company hiring a UGC specialist, an Egyptian brand growing on TikTok ads), first customers possible within days, and cash possible inside the week from direct clients. Content systems and automations take weeks to sell.

### 2. You stay off camera

- **You asked:** whether your face would be in the videos; then about AI presenters; then about other people filming.
- **Chosen:** real creators film. AI is only a tool, and an AI presenter is used only if a client asks, labelled as AI.
- **Why:** research found human-made ads did better in the short term (Ipsos, May 2026); TikTok and Meta require labels on realistic AI people; the US FTC bans testimonials from people who don't exist ([03](03-market-evidence.md#5-ai-ugc-checked-nov-15)).

### 3. Your TikTok stays personal; the studio is T Studio

- **You said:** your TikTok is about fitness and running, so it doesn't suit the business, and you suggested "T Studio".
- **Chosen:** your account is never linked; your training and running still count as "I train and run myself" with fitness brands. The studio is T Studio with a UGC tag; suggested handles `@tstudio.ugc` or `@tstudio.eg` (you check availability). Two web searches found no Cairo business or UGC agency already using the name.

### 4. Creators film and edit; you run the studio

- **You said:** the messages claimed filming, hooks and editing you don't know how to do.
- **Chosen:** creators film and edit; you sell, cast, brief and check quality; I write scripts and hooks. Editing-only work isn't offered this week.
- **Why:** it stops promising work you can't deliver; creators editing their own videos is normal in UGC ([03](03-market-evidence.md#8-who-makes-the-videos-checked-nov-17)); and your time drops to about 2.5 hours per Creative Test.
- **Effect:** every message rewritten, 23 leads skipped, a new top 30, and the guide [10](10-studio-basics.md) so you can judge hooks and videos.

### 5. Prices and creator pay

- **Packages:** Starter $120 / EGP 3,500 (1 video); Creative Test $330 / EGP 9,000 (3 videos); Content Sprint $520 / EGP 14,000 (5 videos and 5 extra hooks) ([02](02-offer-and-pricing.md)).
- **Creators** get EGP 1,000–2,000 per finished video (planning figure EGP 1,200), paid from the client's payment, so you never pay upfront.
- **What you keep:** about 70% on dollar clients, about 55% on Egyptian ones. 2 Content Sprints and 1 Creative Test from dollar clients leave about $1,012. Egypt alone would need about EGP 96,000 in sales, so dollar clients (agencies, Gulf brands, Upwork) come first.

### 6. Money counts only when it reaches you

- Mostaql holds earnings for 14 working days, Fiverr for 14 days, and UGC MENA pays only above $100 after brand approval, so marketplace money can't be withdrawn by Nov 22.
- Only direct clients (InstaPay, bank transfer, Payoneer, PayPal) can pay you inside the week. The CRM tracks 8 money stages separately, from quote to money in your Egyptian bank ([06](06-payments-and-agreement.md)).

### 7. Creators come from Khamsat, not from people you know

- **You said:** you don't know anyone you'd send the recruiting message to.
- **Chosen:** hire creators who already sell edited UGC in Khamsat's UGC videos category. Shortlist with a checklist (Egyptian Arabic, a real person on camera, edited samples, up to $35 a video, some reviews), message the best 5 through Khamsat, and order and pay only there, after the client has paid you. Instagram and TikTok DMs and Collabstr are backups ([09](09-creator-roster.md#hiring-on-khamsat)).
- **Why:** they already film and edit; samples and reviews are public; most prices start around $25, about EGP 1,460 with the fee, inside the planned EGP 1,000–2,000; and Khamsat holds the payment and guarantees orders for 14 days. Their samples replace the free audition ([03](03-market-evidence.md#9-finding-creators-without-contacts-checked-nov-17)).

## What exists now

| What | Where |
|---|---|
| Today's actions, status and the list of all files | [README](../README.md) |
| Ten guides | [01 decision](01-business-decision.md) · [02 offer](02-offer-and-pricing.md) · [03 evidence](03-market-evidence.md) · [04 scripts](04-portfolio-scripts.md) · [05 sales](05-sales-system.md) · [06 payments](06-payments-and-agreement.md) · [07 delivery](07-delivery-workflow.md) · [08 plan](08-six-day-plan.md) · [09 creators](09-creator-roster.md) · [10 basics](10-studio-basics.md) |
| Leads and trackers | [crm/top30.md](../crm/top30.md), [crm/UGC-CRM.xlsx](../crm/UGC-CRM.xlsx) and the CSVs in `crm/` |
| Your live tracker: Google Sheet "T Studio CRM" | https://docs.google.com/spreadsheets/d/1ZFc6ZsEfIY8zdxbtppggHs5MAA2vIeqfk7vwN4soW_8/edit |
| Launch HQ page (private, version 3) | https://claude.ai/artifact/8H4xJs28pTWZxocBQUGHAW |
| Source data and build scripts | `tools/leads_data.py`, `tools/build_crm.py`, `tools/build_hq.py` |
| Guidance for future Claude sessions | [CLAUDE.md](../CLAUDE.md) |
| In your Drive trash, never opened (Google deletes them about Dec 17) | "UGC CRM" (first sheet) and an outdated copy of "T Studio CRM" |

**Commits** on `claude/1k-2k-business-7-days-w9vmgs`, the repo's default branch:

| Time (Nov 17) | Commit |
|---|---|
| 11:28 | Add lead database, CRM trackers and build script |
| 11:33 | Add offer and pricing, sales system and creator roster kit |
| 11:41 | Add portfolio scripts, payments, delivery workflow and six-day plan |
| 11:47 | Add Launch HQ page and link the CRM sheet |
| 13:39 | Name the studio T Studio and keep the personal TikTok out |
| 17:24 | Switch to creators who film and edit; add studio basics guide |
| 17:39 | Document the session; add CLAUDE.md for future sessions |
| 17:44 | Add exact times to the session log; correct search counts and dates |
| 18:26 | Add WhatsApp Business text to paste: description, catalogue, greeting, away |

## Research and its limits

- **Done:** 90 web searches on Sun Nov 15 (2 more were refused: the search tool can't search Reddit), 1 on Mon Nov 16 that hit the usage limit, and 9 on Tue Nov 17 (the studio name, how UGC creators deliver edited videos, freelance editor prices, and where to find creators without contacts). Sources are linked in [03](03-market-evidence.md) and next to every lead.
- **Main findings:** beginner UGC sells for $75–300 a video worldwide; Egyptian nano creators charge EGP 500–1,500; Mostaql budgets are mostly $25–100; Mostaql and Fiverr hold earnings about 14 days; InstaPay is instant.
- **Not checked:** social feeds, profiles and the Meta Ads Library (blocked); whether each project is still open; brand handles not named in a source (left blank); live links (format checked only).
- **Estimates, labelled where used:** reply and closing rates, creator pay, hours per package, posting dates.

## Rules this session followed

| Rule from your brief | How it was kept |
|---|---|
| Nothing sent without your approval | 0 sent. All 71 messages are drafts; each batch waits for your OK. |
| No made-up leads, prices, testimonials or results | Every lead has a source link; unconfirmed handles are blank; guesses are labelled (for example, "Converted" = Convertedin). No results promised. |
| Findings apart from assumptions, with sources | [03](03-market-evidence.md) lists both; estimates are labelled. |
| An unpaid promise isn't revenue | The CRM counts money only when it lands. |
| No mass or unsolicited messages; follow platform rules | Each message is written for one lead from a source about that lead; 36 of them also need your own observation of the lead's latest posts. |
| No passwords, no VPNs, no bought followers | None asked for or suggested. |
| No private personal data | Only public business contacts; creators' personal details stay out of the repo. |
| Never claim contact, orders or payments that didn't happen | Everywhere the status reads: nothing sent, $0. |
| Honesty about who makes the videos | Fixed in decision 4: no message says you film or edit. |

## Problems and fixes

| Problem | Fix |
|---|---|
| Social platforms blocked by my environment; the request to open them was rejected; Reddit closed to the search tool | Facts from search-indexed pages; an `[OBSERVATION]` slot in 36 messages for you; hunting links in the CRM (Reddit included) for you to use |
| Your TikTok profile couldn't be opened, so it was never audited | Not needed once you kept it out of the business (decision 3) |
| Mon 06:48: a search hit the weekly usage limit and work stopped | Work resumed when you wrote again at 22:23 |
| Tue 11:04: my first reply after your approval failed (out of usage credits for that model) | You switched models and said "Try again"; work resumed at 11:12 |
| The first push to GitHub was refused (Tue 11:28) | Checked the access setup; the repo was already connected and the push at 11:33 worked |
| Your personal TikTok was in the pitches | Removed (decision 3) |
| Messages promised filming, hooks and editing you can't do yet | Creators film and edit; every message rewritten (decision 4) |
| Today's plan assumed you knew people to recruit | Creators come from Khamsat first (decision 7) |
| A README link broke when a heading was renamed | Fixed; every link is checked after each change |
| The Egypt-only sales figure said EGP 100,000 | Corrected to about EGP 96,000 |
| Lead 10 appeared twice in Launch HQ's applications | Fixed |
| A last check found five leftover editing lines (one brand was still offered editing; one Upwork message said "I can do") | Fixed; sheet uploaded again; the outdated copy moved to trash |
| Comment alerts for Launch HQ couldn't be switched on | The page works normally; if you leave a comment there, tell me in chat |

## Numbers on Nov 17

- 100 CRM rows: 94 prospects and 6 creator platforms.
- 71 messages drafted; 23 leads skipped: 15 editing-only, 6 want Saudi or UAE-permit creators, 1 full-time on-camera job, 1 job that needs a paid AI tool.
- Top 30: 12 priority A (today's batch, leads 1–12) and 18 priority B.
- Sent 0 · replies 0 · deals 0 · collected $0.

## Open items

- **Today:** the three actions in the [README](../README.md#todays-three-actions), plus 30 minutes with [10](10-studio-basics.md).
- **I need from you:** the T Studio handles you secure, the bank or wallet that receives InstaPay, whether your card or PayPal can pay on Khamsat, the creators' replies, approval of each batch, and replies from creators and leads as they come in.
- **When replies arrive, I will:** adjust messages and quotes, write the script and brief for each order, and update the CRM only with what really happened.
- **Before applying to any project:** open its page and confirm it's still open.

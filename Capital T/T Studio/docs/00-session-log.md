# Session log: Nov 15–17, 2026

The record of the first working session on T Studio: what you asked for, what we decided and why, what was built, what went wrong and what's next. Times are Cairo time (UTC+2), taken from the chat record, git and Google Drive. For today's to-do list, see the [README](../README.md).

## Summary

- **Goal:** collect $1,000 (stretch $2,000) by Sunday Nov 22, 2026 from an online service business. Money counts only when it reaches your account.
- **Business:** T Studio, an Arabic-first UGC ad studio in Cairo. You sell, cast creators, brief them and check every video; creators film and edit; I write the scripts and hooks.
- **Built:** 94 researched prospects and 6 creator platforms, 71 drafted messages, a ranked top 30, three packages, ten guides, a CRM (repo files and a Google Sheet) and the Launch HQ page.
- **Status on Sat Nov 21, 17:00 (paused):** research week (Nov 22–28) before selling. Brand sales messages are paused and the $1,000-by-Nov-22 goal is dropped. T Studio's TikTok, Instagram, Gmail and landing page exist; InstaPay receiving works; WhatsApp Business is waiting. Nothing has been sent: no replies, no deals, $0 collected as far as I know.
- **Next:** approve and send the buyer interviews and the 5 Khamsat creator messages ([interview kit](../research/01-interview-kit.md)); paste replies to me as they arrive; decision on Sat Nov 28 ([README](../README.md#todays-three-actions)).

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
| 18:37 | You said you don't know anyone to send the recruiting message to. Five searches found creators, many of them Egyptian, selling edited UGC videos on Khamsat, most from about $25 a video. Decision 7: hire creators there first. |
| 18:44 | Launch HQ version 4. Commit: creators come from Khamsat; README, plan, creator guide, costs, evidence and CRM Hunting Links updated. |
| 18:45 | You asked me to document this; this update to the log. |
| 19:16–19:18 | You named Capital T the group for all T businesses (T for Tahan). Decision 8: a "Capital T" folder with "T Studio" inside, in Google Drive (the CRM sheet moved in, same link) and in the repo (`Capital T/T Studio/`), plus text for a Claude project named Capital T. |
| 19:30–19:53 | You asked me to add two skill packs and use them. Decision 9: 17 Higgsfield skills and last30days added to `.claude/skills/`, without the two that make AI people look like real customers. last30days found nothing from here (sources blocked). I wrote AI product-clip prompts in [11](11-ai-video-prompts.md). |
| 19:57 | You created T Studio's accounts: TikTok `@tstudio_ugc` and Instagram `@tstudioo.ugc`. Docs, plan and Launch HQ (version 6) updated. I sent the profile setup: display name "T Studio · UGC ads", bio, logo, business account. |
| 20:05 | You asked me to document the session and pause; we'll continue later. This update. |
| **Fri Nov 20**, ~18:55–19:00 | You asked for a page to bring in creators for businesses and said you couldn't choose the details while driving. Your screen recording of a studio's TikTok carousel showed the structure you liked. I chose the defaults (decision 10), built `site/index.html` and published it as a private page (commit at 19:00). |
| **Sat Nov 21**, ~07:57 | You asked what to do. The sheet still showed nothing sent, so I set out the last day and said plainly that $1,000 by Sunday was very unlikely; the realistic target was a first paid order. |
| ~08:00–08:07 | You asked to open Khamsat from here. It was blocked, so I asked to allow `khamsat.com` only; you approved. I read the human-UGC listings and Khamsat's terms ([03](03-market-evidence.md#9-finding-creators-without-contacts-checked-nov-17)) and shortlisted five creators in chat; their names stay out of the repo. |
| 08:29 | You gave the T Studio Gmail and confirmed InstaPay receiving works. WhatsApp Business is waiting (a WhatsApp problem). You don't know if your Banque Misr Visa pays in dollars. I turned the landing page buttons into email links and kept your InstaPay address out of the repo. |
| ~16:10 | You said you'd rushed into T Studio and wanted to research what the market needs, how to provide it and how to be different, using the ai-business-skills pack, and asked whether UGC is a service that solves a problem. An agent read the pack's research skills; you chose a research week of about 7 days, creators still messaged, brand sales paused (the Sunday goal dropped) and 8–10 buyer interviews. Decision 11. |
| 16:20–16:45 | Research day 1: five skills installed; `mostaql.com` and `wuzzuf.net` allowed after your approval (Wuzzuf then blocked automated visits). Committed: the T Studio context draft, the interview kit, 176 Khamsat buyer reviews coded by theme, 11 recent Mostaql UGC projects and a first competitor table ([research](../research/02-competitors.md)). |
| 16:47 | Status docs and Launch HQ (version 8) switched to the research week. Commit at 16:47. |
| ~17:00 | You asked whether the Capital T project can see this chat. It can't: chats are separate. What it can use is saved in the repo and Drive. I listed five files to add to its knowledge. You asked me to document this and pause; this update. |

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

### 8. Capital T is the group; T Studio is its first business

- **You said:** create a folder named Capital T for the group of all T businesses (T stands for Tahan) and put this project in it, in Drive, the repo and Claude.
- **Chosen:** the same layout everywhere: **Capital T → T Studio**. Drive: folders "Capital T" and "T Studio", with the "T Studio CRM" sheet moved in (same link, nothing copied). Repo: every T Studio file under `Capital T/T Studio/`; `CLAUDE.md` and a Capital T README stay at the top. Claude: I can't create Claude projects, so [claude-project-instructions.md](../../claude-project-instructions.md) holds the text for you to paste into a project named Capital T.
- **Why:** later businesses get their own folder next to T Studio without mixing files.

### 9. Skills added: Higgsfield prompts and last30days, without fake AI people

- **You asked:** to read two public skill packs (higgsfield-claude-skills and last30days), put them in the project and use them.
- **Chosen (your pick):** the 15 Higgsfield prompt skills and its 2 browser-automation skills, plus last30days, in `.claude/skills/`. Left out: `ugc-hot-girl` and `ugc-video-auto`, which make AI people designed to pass as real customers. That breaks decision 2 and is a fake-testimonial risk.
- **Used:** last30days ran with no keys and no browser cookies and found 0 results, because Reddit, Hacker News and its keyless web search are blocked here, so nothing was added to [03](03-market-evidence.md). The Higgsfield skills produced 3 prompts for AI product clips (no people, made from a real product photo, labelled AI) in [11](11-ai-video-prompts.md).
- **Why:** AI product shots can make a creator's video look richer at low cost, but Higgsfield's paid plans aren't worth buying before a client pays. The browser skills only work on your computer.

### 10. Landing page: creators first, defaults chosen for you

- **You said:** you want a page that gets creators to make videos for businesses. You don't have time to choose the details, and the client's look isn't yours to decide.
- **Chosen:** creators first, businesses second. A light, Arabic-first page with English under each heading. Proof is concept ads only, each labelled "Concept ad · not sponsored", since there's no client work yet. Packages from [02](02-offer-and-pricing.md). Contact buttons read "Coming soon" until the Gmail existed; on Nov 21 they became email links to `Tstudio.eg@gmail.com` (WhatsApp Business is waiting). No copied look or logos from other studios.
- **Why:** creators are the bottleneck, so the first button is for them; showing no fake results keeps the rules.

### 11. A research week before selling (Nov 22–28)

- **You said:** you rushed in; before continuing you want to know what the market needs, how to provide it and how to be different, using the ai-business-skills pack. You asked whether UGC is a service that solves a problem.
- **My answer:** yes, for brands already paying for ads (their videos wear out fast); a nice-to-have for brands that don't run ads. The risk to test: a brand can hire the same creator directly for $25–50, so T Studio must sell what the brand can't easily do alone.
- **Chosen (your picks):** about a week of research; brand sales messages paused and the $1,000-by-Nov-22 goal dropped; the 5 Khamsat creators still messaged; 8–10 buyer interviews that you approve and send. Five of the pack's skills installed (context, customer insight, competitor research, positioning, offer design); its root `CLAUDE.md`, outside connectors and installers left out ([notes](../../../.claude/skills/AI-BUSINESS-SKILLS-NOTES.md)).
- **Day 1 findings:** managed Arabic UGC already exists (Stllr, UGC MENA, influUGC, Fiverr studios), so "we do UGC" isn't a difference; Mostaql UGC projects are budgeted $50–250; Khamsat buyers praise reliability, quality and speed far more than scripts. Leading gaps to test: G1, ad-ready Egyptian-dialect videos with scripts written to sell; G2, a creative supply for performance agencies ([02](../research/02-competitors.md#e-early-read-where-t-studio-could-be-different-hypotheses-for-the-interviews-not-decisions)).
- **Decision date:** Sat Nov 28: keep, narrow or change the offer, against thresholds agreed before the answers arrive ([01](../research/01-interview-kit.md#6-what-would-change-our-mind-agreed-before-the-answers-come-in)).

## What exists now

| What | Where |
|---|---|
| Today's actions, status and the list of all files | [README](../README.md) |
| Ten guides | [01 decision](01-business-decision.md) · [02 offer](02-offer-and-pricing.md) · [03 evidence](03-market-evidence.md) · [04 scripts](04-portfolio-scripts.md) · [05 sales](05-sales-system.md) · [06 payments](06-payments-and-agreement.md) · [07 delivery](07-delivery-workflow.md) · [08 plan](08-six-day-plan.md) · [09 creators](09-creator-roster.md) · [10 basics](10-studio-basics.md) |
| Leads and trackers | [crm/top30.md](../crm/top30.md), [crm/UGC-CRM.xlsx](../crm/UGC-CRM.xlsx) and the CSVs in `crm/` |
| Your live tracker: Google Sheet "T Studio CRM" (Drive folder Capital T → T Studio) | https://docs.google.com/spreadsheets/d/1ZFc6ZsEfIY8zdxbtppggHs5MAA2vIeqfk7vwN4soW_8/edit |
| Launch HQ page (private, version 8) | https://claude.ai/artifact/8H4xJs28pTWZxocBQUGHAW |
| Research week files (context, interview kit, competitors, customer insight) | [research/](../research/00-context.md) |
| Skills in the repo | `.claude/skills/` (Higgsfield prompts, last30days, five ai-business-skills research skills) |
| Source data and build scripts | `tools/leads_data.py`, `tools/build_crm.py`, `tools/build_hq.py` |
| Guidance for future Claude sessions | [CLAUDE.md](../../../CLAUDE.md) |
| In your Drive trash, never opened (Google deletes them about Dec 17) | "UGC CRM" (first sheet) and an outdated copy of "T Studio CRM" |

**Commits** on `claude/1k-2k-business-7-days-w9vmgs`, the repo's default branch:

| Time (Cairo; Nov 17 unless dated) | Commit |
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
| 18:44 | Find creators on Khamsat instead of people the owner knows |
| 18:45 | Log Launch HQ version 4 and the Khamsat commit in the session log |
| 19:18 | Move T Studio into Capital T/T Studio |
| 19:53 | Add Higgsfield prompt skills and last30days research skill |
| 19:57 | Record T Studio's TikTok and Instagram handles |
| 20:01 | Session log: accounts created, pause for the evening |
| Nov 20, 19:00 | Add T Studio landing page for creators and businesses |
| Nov 21, 08:29 | Turn on landing page email contact; record Gmail, InstaPay status and Khamsat findings |
| Nov 21, 16:40 | Add research skills and start the T Studio research week |
| 16:41 | Add the interview kit and the customer-insight log |
| 16:45 | Research week day 1: competitors and demand signals |
| 16:47 | Switch status docs and Launch HQ to the research week |

## Research and its limits

- **Done:** 90 web searches on Sun Nov 15 (2 more were refused: the search tool can't search Reddit), 1 on Mon Nov 16 that hit the usage limit, and 9 on Tue Nov 17 (the studio name, how UGC creators deliver edited videos, freelance editor prices, and where to find creators without contacts). Sources are linked in [03](03-market-evidence.md) and next to every lead.
- **Sat Nov 21:** 10 web searches (bank card limits, competitors, salaries), plus direct reads of Khamsat (30 listings, 21 listing pages, 176 buyer reviews, its terms, buyer requests) and Mostaql (11 UGC projects). Wuzzuf blocked automated visits. Findings in [research/02](../research/02-competitors.md).
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

- **This week:** the research-week actions in the [README](../README.md#todays-three-actions); decision on Sat Nov 28.
- **Optional:** add `README.md`, `docs/00-session-log.md`, `research/00-context.md`, `research/01-interview-kit.md` and `research/02-competitors.md` to the knowledge of your claude.ai project "Capital T" (the project can't see this chat), and again after big changes. No InstaPay address or people's names in project files.
- **I need from you:** which 10–12 people to interview (pick from the kit), your OK on the interview messages, every reply from buyers and creators (paste or screenshot), whether your Banque Misr Visa pays in dollars, and when WhatsApp Business works again.
- **When replies arrive, I will:** adjust messages and quotes, write the script and brief for each order, and update the CRM only with what really happened.
- **Before applying to any project:** open its page and confirm it's still open.

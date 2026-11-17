"""Lead, package and plan data for the UGC studio CRM.

This file is the single source of truth. Edit it, then run:

    python3 tools/build_crm.py

Rules this data follows:
- Every fact comes from the source URL on the row (research done 2026-11-15/16).
- Handles, websites and contacts I could not confirm are left blank and flagged.
- Messages contain placeholders you must fill before sending:
  [OBSERVATION] one specific thing you saw in their last 3 posts
  [PORTFOLIO]   your portfolio link
  [NAME]        your name
Studio name: T Studio (sign-off "T Studio · Arabic UGC ads").
- Nothing here has been sent. Every message needs your approval first.
"""

DATE_FOUND = "2026-11-15"
BUILD_DATE = "2026-11-17"
FX_EGP_PER_USD = 54  # early Nov 2026 market range was about 53.9-55.5

# ---------------------------------------------------------------- constants
CASH_DIRECT = "Fast: client pays you directly (InstaPay, bank transfer, Payoneer)"
CASH_MOSTAQL = "Slow: Mostaql holds earnings 14 working days after delivery"
CASH_UPWORK = "Medium: Upwork holds fixed-price funds a few days after approval, then local-bank withdrawal"
CASH_JOB = "Salary job: not cash this week"
CASH_NA = "n/a: creator-side platform, not a client"

F_YOU = "Creator films and edits (faceless: hands, product, screen)"
F_NECK = "Creator films and edits (on camera or neck-down)"
F_ROSTER = "Creator films and edits (on camera)"
F_EDIT = "Editing only: no editor on the team yet"
F_AI = "AI presenter, disclosed as AI"
F_NA = "n/a"

T_BRAND = "Brand"
T_AGENCY = "Agency (white-label partner)"
T_MOSTAQL = "Open project: Mostaql"
T_UPWORK = "Open project: Upwork"
T_HIRING = "Company hiring"
T_JOB = "Job / role"
T_PLATFORM = "Platform (recruit creators)"

ST_DRAFTED = "Message drafted, not sent"
ST_SKIP_SAUDI = "Skip: wants a Saudi/Gulf creator"
ST_SKIP_EDIT = "Skip for now: editing-only work, no editor on the team"

MOSTAQL_METHOD = "Mostaql proposal (needs a verified Mostaql account)"
UPWORK_METHOD = "Upwork proposal (costs Connects; profile must be approved)"
FIND_ACCOUNT = "Find the official Instagram/TikTok (search the name, check it links to their site) -> DM"

NEWEST_MOSTAQL = "Among the newest Mostaql IDs found (128xxxx). Open the page and confirm it is still open."
WEEKS_MOSTAQL = "Mostaql ID 127xxxx: a few weeks old, may already be awarded. Check the page."
OLD_MOSTAQL = "Older Mostaql project (ID 1229157 was April 2026). Probably closed; check before spending time."


def upwork_age(estimate):
    return (f"Upwork job ID suggests it was posted around {estimate} "
            "(my estimate from the ID sequence). Check it is still open.")


def L(**kw):
    """One lead row with defaults."""
    row = dict(
        rank=None, priority="C", type=T_BRAND, signal="None found", company="",
        website="", instagram="", tiktok="", facebook="", country="Egypt",
        industry="", size="Unknown", why="", opportunity="", contact_person="",
        contact_method=FIND_ACCOUNT, source="", date_found=DATE_FOUND, service="",
        price="", message="", status=ST_DRAFTED, cash=CASH_DIRECT, films="",
        note="", ads_country="EG",
    )
    unknown = set(kw) - set(row)
    if unknown:
        raise KeyError(f"unknown lead fields: {sorted(unknown)}")
    row.update(kw)
    return row


# ---------------------------------------------------------------- leads
LEADS = [
    # ===================== TOP 30 (ranked) =====================
    L(rank=1, priority="A", company="Cotmasr", industry="Apparel: Egyptian-cotton basics",
      size="42K organic TikTok followers; growth mainly from paid TikTok ads; reported 14x ROAS and -11.3% CPA (TikTok case study, self-reported)",
      signal="None found, but a proven paid-ads spender",
      why="They grow through paid TikTok ads, and paid ads wear out creatives fast. New hooks and new faces are their bottleneck.",
      opportunity="Creative Test: 'blind touch test' (3 tees, only one is Egyptian cotton), fabric close-ups, 3-outfit fit check. 3 hooks each for Spark Ads.",
      contact_person="Mahmoud Reda, founder (named in the TikTok case study)",
      source="https://ads.tiktok.com/business/en/inspiration/cotmasr-tiktok-success-stories",
      service="Creative Test (3 UGC ads, 30-day paid usage), then Sprint",
      price="EGP 9,000 (Sprint EGP 14,000)", films=F_ROSTER,
      note="Website and handles not confirmed by me; find them first. The case study says they sell on their own website.",
      message=(("أهلاً فريق Cotmasr 👋 قريت قصتكم على TikTok for Business، وإن أغلب نموكم جاي من الإعلانات المدفوعة. الإعلانات دي بتستهلك كريتيفز بسرعة، فعندي فكرة جاهزة: «اختبار اللمس بعين مقفولة» — ٣ تيشيرتات، واحد بس منهم قطن مصري من Cotmasr، والشخص لازم يعرفه باللمس. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة: بنكتب السكريبت والهوكات، وبنختار صانع محتوى يصوّر ويعمل المونتاج، وبنراجع كل فيديو قبل التسليم. أبعتلكم ٣ هوكات مكتوبة للفكرة دي النهارده؟\n"
               "نماذج: [PORTFOLIO]\n"
               "— [NAME]، T Studio"))),

    L(rank=14, priority="B", type=T_MOSTAQL, company="Mostaql client: office-supplies store",
      website="https://mostaql.com/project/1288390-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D8%B1%D9%8A%D9%84%D8%B2-%D8%AA%D8%B3%D9%88%D9%8A%D9%82%D9%8A",
      country="See project page", industry="E-commerce: office supplies",
      signal="Confirmed open project (Mostaql)",
      why="Wants UGC unboxing videos and real in-office product use. Budget $50-100, 30 days.",
      opportunity="3 faceless videos: ASMR unboxing, 'my desk before/after', '3 tools that saved me time'. Hands only, natural light.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1288390-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D8%B1%D9%8A%D9%84%D8%B2-%D8%AA%D8%B3%D9%88%D9%8A%D9%82%D9%8A",
      service="UGC, faceless (creator films and edits)", price="Bid $100 for 3 videos (top of their budget)",
      cash=CASH_MOSTAQL, films=F_YOU, ads_country=None,
      note=NEWEST_MOSTAQL + " Confirm the store can ship to you in Egypt. Low margin after creator pay and Mostaql's commission: worth it mainly for a first review.",
      message=(("السلام عليكم، قرأت إنك محتاج فيديوهات Unboxing واستخدام حقيقي للأدوات المكتبية في مكتب. ده نوع المحتوى اللي صانع المحتوى بتاعنا بيصوّره بالأيدي من غير وش ويعمله مونتاج: إضاءة طبيعية، صوت ASMR للفتح، ولقطات قريبة للتفاصيل، وإحنا بنراجع كل فيديو قبل التسليم.\n"
               "اقتراحي ٣ فيديوهات (١٥–٣٠ ثانية، 9:16):\n"
               "١) Unboxing هادي بصوت الطلبية.\n"
               "٢) «مكتبي قبل وبعد» بالأدوات.\n"
               "٣) «٣ أدوات وفّرتلي وقت» مع كابشن عربي.\n"
               "التسليم: أول فيديو خلال ٤٨ ساعة من وصول المنتجات، وجولة تعديل لكل فيديو. نماذج: [PORTFOLIO]"))),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: TikTok/Reels editing",
      website="https://mostaql.com/project/1285320-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-tiktok-%D9%88-reels",
      country="See project page", industry="Short-form editing",
      signal="Confirmed open project (Mostaql), listed as open",
      why="Needs TikTok/Reels editing with Arabic captions and a strong hook in the first 3 seconds. CapCut or Premiere. Budget $50-100, 30 days.",
      opportunity="Edit with a 1-second on-screen hook, synced Arabic captions, fast cuts. Offer 3 written hooks for one of their raw videos.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1285320-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-tiktok-%D9%88-reels",
      service="Skip for now", price="n/a",
      cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=NEWEST_MOSTAQL,
      message=("")),

    L(rank=3, priority="A", company="Gym Apparel", website="https://gymapparel.net",
      industry="Activewear", size="About 210 Trustpilot reviews",
      why="Reviewers praise fabric and fit at affordable prices. Video proves those claims better than photos.",
      opportunity="'Squat-proof + sweat test' ad and a 3-outfit gym fit check (neck-down, can be faceless).",
      contact_person="Brand Instagram (their Trustpilot replies send customers to Instagram)",
      contact_method="Instagram DM (handle not confirmed); website contact",
      source="https://uk.trustpilot.com/review/gymapparel.net",
      service="Creative Test", price="EGP 9,000", films=F_NECK,
      note="Some reviews complain about delivery and refunds. Don't mention them; lead with the fabric and fit praise.",
      message=(("أهلاً فريق Gym Apparel 👋 قريت تقييماتكم على Trustpilot، وأكتر حاجة الناس بتمدحها الخامة والمقاس بسعر معقول — ودي بالظبط الحاجات اللي الفيديو بيثبتها أحسن من الصور.\n"
               "فكرة إعلان: «Squat-proof test» تحت إضاءة قوية + «Sweat test» بعد ٣٠ دقيقة تمرين، وفي الآخر فيت تشيك لـ٣ أطقم. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة: بنكتب السكريبت والهوكات، وبنختار صانع محتوى يصوّر ويعمل المونتاج، وبنراجع كل فيديو قبل التسليم. أبعتلكم السكريبت + ٣ هوكات؟ نماذج: [PORTFOLIO]"))),

    L(rank=4, priority="A", company="Sigma Fit", website="https://sigmafiteg.com",
      instagram="https://www.instagram.com/sigmafitegypt/", industry="Activewear (men, women, kids)",
      size="Founded 2016/2017; men, women and kids ranges (Egypt Innovate, CB Insights)",
      why="Online-first activewear brand whose own blog pitches Egyptian-cotton fitness wear 'without paying a fortune'. That claim is made for comparison videos.",
      opportunity="'1 hour of training: Sigma Fit cotton tee vs imported polyester' comparison; kids' range parent-POV video.",
      contact_person="Brand Instagram", contact_method="Instagram DM; website contact",
      source="https://egyptinnovate.com/en/entities/profile/sigma-fit-1",
      service="Creative Test", price="EGP 9,000", films=F_NECK,
      note="Instagram handle taken from an Instagram post embedded in an Egyptian Streets article.",
      message=(("أهلاً Sigma Fit 👋 قريت مقالتكم عن إزاي تجيب لبس رياضي قطن مصري بجودة عالية من غير ما تدفع ثروة — الرسالة دي تنفع إعلان UGC قوي.\n"
               "فكرة: «ساعة تمرين بتيشيرت Sigma Fit قصاد تيشيرت بوليستر مستورد» — نفس التمرين ونفس الشخص، ونشوف الفرق في الراحة على الكاميرا. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة: بنكتب السكريبت والهوكات، وبنختار صانع محتوى يصوّر ويعمل المونتاج، وبنراجع كل فيديو قبل التسليم. أبعتلكم السكريبت و٣ هوكات؟ [PORTFOLIO]"))),

    L(rank=2, priority="A", type=T_HIRING, company="Convertedin (job post says 'Converted')",
      industry="Marketing software for e-commerce",
      size="$3M seed (2022); job post claims 800+ e-commerce clients",
      signal="Hiring signal: 'UGC Specialist' role for Egypt/KSA/UAE (posting date not shown)",
      why="They are hiring someone to source and scale UGC across Egypt, KSA and UAE, so they need creators now.",
      opportunity="White-label Arabic UGC for their merchants while they hire: we script and check, our creators film and edit. Pilot on one merchant.",
      contact_person="Hiring team on the job post; founders Mohamed Atef, Mohamed Fergany, Mustafa Raslan (2022 press)",
      contact_method="LinkedIn (company page or founders); reply via the job post",
      source="https://www.founditgulf.com/job/ugc-specialist-converted-egypt-42303127",
      service="White-label UGC partnership",
      price="Pilot: Creative Test $330 / EGP 9,000 per merchant", films=F_ROSTER,
      note="'Converted' = Convertedin is my inference from the job text (e-commerce marketing OS, 800+ clients). Confirm before sending.",
      message=(("Hi [first name], I saw your team is hiring a UGC Specialist to scale creator content across Egypt, KSA and UAE. While you hire, T Studio can cover it white-label: we write Arabic scripts and hooks, Egyptian creators film and edit each video, and we check every video before delivery, with 3 hooks per ad in about 5 days.\n"
               "An idea for your own acquisition ads: a real store owner checking yesterday's sales, filmed UGC-style.\n"
               "Could we run one paid pilot for one of your merchants this week? Samples: [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(rank=5, priority="A", type=T_AGENCY, company="Growthmerce", country="Egypt (Cairo)",
      industry="Performance marketing / media buying for e-commerce",
      size="2-9 staff; founded 2026; $1,000+ minimum project (Clutch)",
      why="Media buyers need new creatives every week; a small team rarely has its own creators.",
      opportunity="White-label Arabic UGC for their e-commerce clients: scripted by us, filmed and edited by our creators.",
      contact_person="Via Clutch profile", contact_method="Clutch contact; LinkedIn; website form",
      source="https://clutch.co/profile/growthmerce",
      service="White-label UGC partnership", price="Test: Starter EGP 3,500; then Creative Test EGP 9,000",
      films=F_ROSTER,
      message=(("Hi Growthmerce team, I saw on Clutch that you run Meta, TikTok and Snap ads for e-commerce brands. When a client runs out of creatives, T Studio can be your white-label UGC supplier in Cairo: we write the Arabic scripts and hooks, Egyptian creators film and edit each video, and we check every video before it reaches you. 3 hooks per ad, about 5 days, your branding only and no contact with your clients.\n"
               "Want to test it on one client with a single video for EGP 3,500? Samples: [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(rank=6, priority="A", type=T_AGENCY, company="AdBuyers", country="Egypt (Maadi, Cairo)",
      industry="Performance marketing for Gulf and Arab e-commerce", size="Founded 2022 (Sortlist)",
      why="Runs Meta, Google, TikTok and Snap for Gulf and Arab stores. Gulf campaigns go through Arabic creatives fast.",
      opportunity="White-label UGC in neutral Arabic for their Gulf clients: scripted by us, filmed and edited by our creators.",
      contact_person="Via Sortlist profile", contact_method="Sortlist contact; LinkedIn; website",
      source="https://www.sortlist.co.uk/agency/adbuyers",
      service="White-label UGC partnership", price="Starter $120; Creative Test $330",
      films=F_ROSTER,
      message=(("Hi AdBuyers team, I saw you run Meta, TikTok and Snap campaigns for e-commerce brands across the Gulf. Those campaigns go through Arabic creatives fast, so here's an offer: T Studio supplies white-label UGC in neutral Arabic. We write the scripts and hooks, our creators film and edit, and we check every video before delivery: 3 hooks per ad, under your name.\n"
               "Happy to start small with one paid video. Samples: [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(rank=7, priority="A", company="Nspired", website="https://nspiredbeauty.com",
      instagram="https://www.instagram.com/nspired.beauty/", industry="Fragrance (inspired-by scents)",
      size="Online store + branches; EGP 485 (50ml) / 795 (100ml) (Made in Egypt review, Nov 2026)",
      why="They already pay for advertising (a CGI ad campaign on Ads of the World). Real human reactions are what CGI can't show.",
      opportunity="'Compliment test' (wear it for a day, count compliments) + 'which scent are you' series. Never name the designer originals.",
      contact_person="Brand Instagram", contact_method="Instagram DM; website contact",
      source="https://enterpriseam.com/egypt/2026/11/02/making-scents-of-local-brands/",
      service="Creative Test", price="EGP 9,000", films=F_ROSTER,
      note="CGI campaign: https://www.adsoftheworld.com/campaigns/nspired-perfume-cgi . Don't name luxury originals in ads (trademark risk).",
      message=("أهلاً فريق Nspired 👋 شفت حملة الـCGI بتاعتكم على Ads of the World — شكلها قوي. "
               "الحاجة الوحيدة اللي الـCGI مش بيقدر يعملها: رد فعل حقيقي.\n"
               "فكرة: «اختبار المجاملات» — حد يرش Nspired ويكمل يومه عادي، ويعد كام مرة اتقاله «ريحتك حلوة»، "
               "والرقم يظهر آخر الفيديو. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم ٣ هوكات للفكرة؟ [PORTFOLIO]")),

    L(rank=8, priority="A", company="Mr.Beard", website="https://mrbeard-egypt.com",
      industry="Men's grooming: beard care",
      size="Started 2020; says it sells across the Middle East; EDA-approved, ISO 22716 facility (own claims)",
      why="Beard kits are made for demo videos: routine, unboxing, before/after.",
      opportunity="'60-second beard routine' with the Master's Beard Kit (lower-face close-ups), kit unboxing ASMR, '3 beard-oil mistakes'.",
      contact_person="Website contact / brand Instagram", contact_method="Website contact; Instagram DM (handle not confirmed)",
      source="https://mrbeard-egypt.com/pages/about-us",
      service="Creative Test", price="EGP 9,000", films=F_NECK,
      message=(("أهلاً Mr.Beard 👋 الـMaster's Beard Kit عندكم معمول عشان يتصور: من فتح العلبة لأول استخدام في ٦٠ ثانية.\n"
               "فكرة إعلان: «روتين الدقن في دقيقة» بلقطات قريبة من غير ما نحتاج وش كامل، وهوك: «٣ غلطات بيعملها أغلب الرجالة مع زيت الدقن». [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة: بنكتب السكريبت والهوكات، وبنختار صانع محتوى يصوّر ويعمل المونتاج، وبنراجع كل فيديو قبل التسليم. أبعتلكم السكريبت و٣ هوكات؟ [PORTFOLIO]"))),

    L(rank=10, priority="A", type=T_MOSTAQL, company="Mostaql client: online store (reels ads)",
      website="https://mostaql.com/project/1285106-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D9%88%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%85%D8%AD%D8%AA%D8%B1%D9%81-%D9%84%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%B1%D9%8A%D9%84%D8%B2-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A%D8%A9-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A",
      country="See project page", industry="E-commerce: reels ads",
      signal="Confirmed open project (Mostaql)",
      why="Wants a content creator and editor to produce reels ads for an online store.",
      opportunity="Creative Test structure: 3 ads, 3 selling angles, 2 alternate hooks each, Arabic script.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1285106-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D9%88%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%85%D8%AD%D8%AA%D8%B1%D9%81-%D9%84%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%B1%D9%8A%D9%84%D8%B2-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A%D8%A9-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A",
      service="UGC (creator films and edits)", price="Bid $90-150 for 3 videos (budget not shown in search)",
      cash=CASH_MOSTAQL, films=F_ROSTER, ads_country=None,
      note=NEWEST_MOSTAQL + " Budget and product not visible in search; read the page first.",
      message=(("السلام عليكم، قرأت إنك محتاج صانع محتوى ومونتير لفيديوهات ريلز إعلانية لمتجرك. إحنا ستوديو صغير: بنكتب السكريبت والهوكات بالعربي، وصانع محتوى من فريقنا بيصوّر (لقطات منتج وأيدي، أو قدام الكاميرا حسب المنتج) ويعمل المونتاج بهوك في أول ثانيتين وكابشن عربي، وإحنا بنراجع كل فيديو قبل التسليم.\n"
               "اقتراحي كبداية: ٣ فيديوهات بـ٣ زوايا بيع مختلفة، وكل فيديو بهوكين بديلين عشان تختبرهم في الإعلانات.\n"
               "محتاج أعرف: المنتج، والسعر، والجمهور المستهدف. نماذج: [PORTFOLIO]"))),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: UGC editing",
      website="https://mostaql.com/project/1283316-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%84%D8%B5%D9%86%D8%A7%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc",
      country="See project page", industry="Short-form editing (UGC)",
      signal="Confirmed open project (Mostaql)",
      why="Wants an editor for UGC content.",
      opportunity="UGC-style editing: 1-second hook, synced captions, product b-roll, 2 hook variants per video.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1283316-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%84%D8%B5%D9%86%D8%A7%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc",
      service="Skip for now", price="n/a",
      cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=NEWEST_MOSTAQL,
      message=("")),

    L(status="Skip for now: needs a paid AI tool and editing", priority="C", type=T_UPWORK, company="Upwork client: e-commerce brand (AI UGC ads)",
      country="Worldwide applicants", industry="E-commerce ads",
      signal="Confirmed open project, posted 2026-11-12 (Upwork)",
      why="Wants short AI-generated UGC-style ads for an e-commerce brand. AUD 50 per completed video, possible ongoing work.",
      opportunity="Disclosed AI presenter with our script; needs a paid AI tool and someone to edit. Only if the client asks for AI; follow TikTok/Meta AI-label rules.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-video-creation_~022120669148158840379/",
      service="Skip for now", price="n/a",
      cash=CASH_UPWORK, films=F_NA, ads_country=None,
      note="Needs a paid AI tool (about $39-110/month). Take it only if the first order covers the tool. Never script the avatar as a real customer.",
      message=("")),

    L(rank=11, priority="A", company="Bobana", website="https://bobana-eg.com",
      instagram="https://www.instagram.com/bobana.egypt", facebook="https://www.facebook.com/Bobana.Egypt",
      industry="Hair care: curly hair",
      why="Egyptian Streets calls Bobana a staple on curly-hair feeds and featured it in 'TikTok Made Me Buy It'. Their buyers already shop from video.",
      opportunity="Wash-day routine with the Moisturizing Curly Routine Bundle; 'day 1 vs day 3 curls' hold test (really filmed over 3 days).",
      contact_person="Brand Instagram / Facebook page", contact_method="Instagram DM; Facebook message",
      source="https://egyptianstreets.com/2025/08/24/tiktok-made-me-buy-it-egyptian-products-that-actually-live-up-to-the-hype/",
      service="Creative Test", price="EGP 9,000", films="Creator with curly hair films and edits",
      note="Instagram and Facebook links come from the footer of bobana-eg.com product pages.",
      message=("أهلاً Bobana 💛 شفت إن Egyptian Streets حطوكم في «TikTok Made Me Buy It» — يعني جمهوركم أصلاً بيشتري من الفيديو.\n"
               "فكرة: «يوم الغسيل» بالـMoisturizing Curly Routine Bundle خطوة بخطوة على الشاشة، وفي الآخر «الكيرلي يوم ١ قصاد يوم ٣» "
               "عشان نثبت الثبات. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة، وبنختار صانعة محتوى شعرها كيرلي فعلاً تجرب المنتجات. أبعتلكم السكريبت و٣ هوكات؟ [PORTFOLIO]")),

    L(rank=13, priority="B", company="Haxel", industry="Activewear (gym, yoga, running lines)",
      why="Rebranded from Nexus, with separate gym, yoga and running lines. A new name needs a burst of content to introduce it.",
      opportunity="'One set, three sports': same creator runs, does yoga and lifts in one Haxel set; line-by-line fit checks.",
      source="https://www.cairo360.com/?p=1794812",
      service="Creative Test", price="EGP 9,000", films=F_NECK,
      note="Website and handle not confirmed. Flair Magazine says it has been 'taking over the gym feeds'.",
      message=(("أهلاً Haxel 👋 شفت إنكم اتحولتوا من Nexus لـHaxel وبقى عندكم خطوط للجيم واليوجا والجري. الاسم الجديد محتاج دفعة محتوى تعرّف الناس عليه.\n"
               "فكرة: «طقم واحد — ٣ رياضات»: نفس الشخص بيجري، بيعمل يوجا، وبيرفع حديد بنفس الطقم، والكاميرا بتركز على الحركة والخامة. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة: بنكتب السكريبت والهوكات، وبنختار صانع محتوى يصوّر ويعمل المونتاج، وبنراجع كل فيديو قبل التسليم. أبعتلكم السكريبت؟ [PORTFOLIO]"))),

    L(rank=15, priority="B", company="Nuit Fragrances", instagram="https://www.instagram.com/nuitfragrances/",
      industry="Fragrance (original scents)", size="EGP 380-550 per 50ml (Enterprise listing); best-seller 'Rum'",
      why="Founder-led short videos built their following (Enterprise, Nov 2026). Customer-voice UGC is the next layer beside the founder.",
      opportunity="'Rum: first spray to 8 hours later' wear test; 'describe it in one word' reactions.",
      contact_person="Salma Elkhamisy, founder (public interviews)", contact_method="Instagram DM; founder on LinkedIn",
      source="https://enterpriseam.com/egypt/2026/11/02/making-scents-of-local-brands/",
      service="Starter, then Creative Test", price="EGP 3,500 Starter / EGP 9,000 Creative Test", films=F_ROSTER,
      message=("أهلاً أستاذة سلمى 👋 قريت مراجعة Enterprise عن Nuit، وإن الفيديوهات القصيرة اللي بتحكي فيها عن الروايح هي اللي عملت المتابعين. "
               "صوت المؤسِّسة قوي — والخطوة الجاية إن يبقى جنبه صوت العملاء.\n"
               "فكرة: «Rum — من أول رشة لحد ٨ ساعات» كاختبار ثبات حقيقي في يوم عادي، وفي الآخر الشخص يوصف الريحة بكلمة واحدة. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلك السكريبت؟ [PORTFOLIO]")),

    L(rank=12, priority="A", company="The Hair Addict", industry="Hair tools: 'Curl Fuser' diffuser",
      signal="Hiring signal: social media specialist and content creator job (Wuzzuf, date not shown)",
      why="They're hiring a content creator, so content is a priority, and their Curl Fuser diffuser already gained social-media fame.",
      opportunity="'Curl Fuser vs air-dry' on the same head (half and half); 'fits any dryer?' test. Offer a batch while they hire.",
      contact_person="Hiring contact on Wuzzuf; brand Instagram", contact_method="Instagram DM; Wuzzuf application",
      source="https://wuzzuf.net/jobs/p/kusoinhlgyvx-social-media-specialist-and-content-creator-the-hair-addict-cairo-egypt",
      service="Creative Test (freelance, while they hire)", price="EGP 9,000", films="Creator with curly hair films and edits",
      note="Curl Fuser coverage: Egyptian Streets 'TikTok Made Me Buy It' (Aug 2025).",
      message=("أهلاً The Hair Addict 👋 شفت إنكم بتدوروا على Content Creator على Wuzzuf. لحد ما تلاقوا الشخص المناسب، نقدر نغطي دفعة محتوى بالقطعة.\n"
               "فكرة للـCurl Fuser: «ديفيوزر قصاد تنشيف عادي» على نفس الشعر — نص بنص — والفرق في شكل الكيرلي يبان في ٣ ثواني. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة، وبنختار صانعة محتوى شعرها كيرلي فعلاً. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(rank=16, priority="B", company="FitXpert", industry="Software for fitness coaches and nutrition centres",
      size="Seven-figure investment from Foras Investment (Jan 2026)",
      why="Fresh funding for regional expansion. Coaches buy after they see the product working.",
      opportunity="Screen-recorded demo with Egyptian voice-over: 'a coach builds a client plan in 3 minutes'. No shipping needed.",
      contact_person="Founders Salah Selim and Mostafa Mahmoud (press)", contact_method="LinkedIn message",
      source="https://www.wamda.com/2026/01/fitxpert-secures-seven-figure-backing-scale-fitness-nutrition-saas-platform",
      service="Creative Test (app demos)", price="EGP 9,000 / $330", films=F_YOU,
      message=("أهلاً أستاذ صلاح 👋 مبروك على استثمار Foras في يناير. مع توسع FitXpert في المنطقة، أكتر محتوى بيقنع المدربين هو إنهم يشوفوا البرنامج شغال.\n"
               "فكرة: ديمو قصير بتسجيل شاشة وتعليق صوتي بالمصري: «إزاي مدرب يعمل خطة تمرين وتغذية لعميل في ٣ دقايق»، "
               "بهوك: «لسه بتبعت الدايت PDF على واتساب؟»\n"
               "أنا نفسي بتمرن وبجري، وعندنا ستوديو UGC صغير في القاهرة اسمه T Studio. أبعتلك السكريبت؟ [PORTFOLIO]")),

    L(rank=17, priority="B", company="Mavin Wear", website="https://global.mavin-wear.com",
      industry="Activewear", contact_person="Fady Bakri, owner (per Cairo360; single source)",
      why="Owned by a fitness influencer. UGC from other lifters adds proof beyond the founder's own audience.",
      opportunity="'Heavy session test' for compression pieces; training suit 'gym to street' transition.",
      source="https://cairo360.com/?p=1801513",
      service="Creative Test", price="EGP 9,000", films=F_NECK,
      message=("أهلاً فريق Mavin Wear 👋 «Local roots, global vision» — شفتها على موقعكم. البراند معروف من جمهور المؤسس، "
               "والخطوة اللي بتكبّر الثقة إن ناس تانية تتمرن بيه وتتكلم عنه.\n"
               "فكرة: «Heavy session test» لقطع الكومبريشن — سِت تقيل، لقطات قريبة للحركة والخامة، وفي الآخر تحويلة «من الجيم للشارع» بالترينينج سوت. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت و٣ هوكات؟ [PORTFOLIO]")),

    L(rank=18, priority="B", company="Kijaqo", website="https://kijaqo.com", instagram="https://www.instagram.com/kijaqo/",
      industry="Tracksuits: heavyweight Egyptian cotton",
      why="It's November: heavyweight cotton tracksuits are a winter product, and fabric weight is something video shows better than photos.",
      opportunity="'Scale test' (Kijaqo hoodie vs a regular one on a kitchen scale), texture close-ups, cosy winter fit check.",
      source="https://cairoscene.com/Listicles/7-Local-Brands-for-Fiercely-Chill-Athleisure",
      service="Creative Test", price="EGP 9,000", films=F_NECK,
      message=("أهلاً Kijaqo 👋 داخلين على الشتا، والترينينجات القطن التقيل بتاعتكم منتج شتوي بامتياز. الوزن والخامة حاجات الصور مش بتوصلها، الفيديو بيوصلها.\n"
               "فكرة: «اختبار الميزان» — هودي Kijaqo قصاد هودي عادي على ميزان المطبخ، بعدها لقطات قريبة للخامة، وفيت تشيك شتوي. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت و٣ هوكات؟ [PORTFOLIO]")),

    L(rank=9, priority="A", type=T_AGENCY, company="Hypebox", website="https://hypebox.me/services/ugc",
      country="UAE (Dubai) / Lebanon", industry="UGC and social agency",
      size="Says 500+ creators; 4.8/5 on Clutch (listing)",
      why="UGC agency serving the UAE and Lebanon; Egyptian-dialect creators at Egyptian costs widen their bench.",
      opportunity="Egyptian-dialect creators who film and edit, managed by us, for their Egypt/Gulf campaigns.",
      contact_person="Website contact form", contact_method="Website form; LinkedIn",
      source="https://hypebox.me/services/ugc", service="White-label UGC (creator supply)",
      price="Starter $120; Creative Test $330", films=F_ROSTER, ads_country="AE",
      message=(("Hi Hypebox team, I run T Studio, a small UGC studio in Cairo. If your Arabic campaigns need Egyptian-dialect creators, we can supply them white-label: we write the scripts and hooks, our creators film and edit, and we check every video before it reaches you. 3 hooks per ad, about 5 days.\n"
               "Happy to start with one paid video for a current campaign. Samples: [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: real estate",
      website="https://mostaql.com/project/1277585-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%85%D8%AD%D8%AA%D8%B1%D9%81-%D9%88%D9%85%D8%AA%D8%AE%D8%B5%D8%B5-%D9%81%D9%8A-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%85%D9%82%D8%A7%D8%B7%D8%B9-tiktok-%D9%88reels",
      country="See project page", industry="Real estate: short-form",
      signal="Confirmed project (Mostaql), ongoing scope",
      why="Ongoing: 12-16 TikTok/Reels videos a month, 30-60s, 9:16.",
      opportunity="Monthly editing retainer: price/area hook in the first 2 seconds, room labels on screen, contact CTA.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1277585-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%85%D8%AD%D8%AA%D8%B1%D9%81-%D9%88%D9%85%D8%AA%D8%AE%D8%B5%D8%B5-%D9%81%D9%8A-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%85%D9%82%D8%A7%D8%B7%D8%B9-tiktok-%D9%88reels",
      service="Skip for now", price="n/a",
      cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=WEEKS_MOSTAQL,
      message=("")),

    L(rank=19, priority="B", type=T_UPWORK, company="Upwork client: UGC Meta video ads",
      country="See post", industry="Paid social ads",
      signal="Open project (Upwork)",
      why="Wants UGC video ads for Meta. Details only on the post.",
      opportunity="3-ad Creative Test with 3 hooks each for Reels and Feed (9:16 and 4:5).",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-Meta-Video-Ads_~022113138996341048866/",
      service="UGC Creative Test", price="$330 for 3 ads (adjust to their budget)",
      cash=CASH_UPWORK, films=F_ROSTER, ads_country=None,
      note=upwork_age("late Oct 2026") + " Details were not visible in search; read the post first.",
      message=(("Hi, for Meta UGC ads the first 2 seconds usually decide performance, so every ad we deliver comes with 3 alternate hooks you can test as separate creatives. T Studio writes the script and hooks, casts a creator who fits your customer, and the creator films and edits it for Reels and Feed (9:16 and 4:5). We check every video before delivery.\n"
               "Can you share the product and who buys it? I'll reply with 3 hook ideas before you hire. Samples: [PORTFOLIO]"))),

    L(rank=20, priority="B", type=T_UPWORK, company="Upwork client: plant identification & care app",
      country="See post", industry="Mobile app",
      signal="Open project, posted 2026-10-20 (Upwork)",
      why="Wants UGC creators for short-form app videos; initial budget $100 per creator.",
      opportunity="No-shipping app demo: 'I scanned every plant on my balcony' (screen + hands + real plants).",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-Video-Creators-Wanted-for-Plant-Identification-Plant-Care-Mobile-App_~022112531947020738585/",
      service="UGC app demo", price="$100 (their budget) for 1-2 videos",
      cash=CASH_UPWORK, films=F_YOU, ads_country=None,
      note="About 4 weeks old; check it is still open.",
      message=(("Hi, an idea for your plant app: 'I scanned every plant on my balcony and found out which one I've been killing.' Screen recording plus hands and real plants, no shipping needed. We write the hook; a creator from our team films it faceless in natural light and edits it with captions in English or Arabic, and we check it before delivery.\n"
               "First video within 48 hours of approval. Samples: [PORTFOLIO]"))),

    L(rank=21, priority="B", company="Nileton", industry="Active-casual apparel",
      size="EGP 235-500 price range (Enterprise, Oct 2026); 214 products listed on Jumia",
      why="Low-price basics sell on value, and 'full outfit under EGP 1,000' videos make that obvious.",
      opportunity="'Gym outfit under EGP 1,000' haul; product videos for their Jumia and Noon listings.",
      contact_method=FIND_ACCOUNT + "; Jumia/Noon store pages",
      source="https://enterpriseam.com/egypt/2026/10/26/basics-egp-priced/",
      service="Starter, then Creative Test", price="EGP 3,500 / 9,000", films=F_NECK,
      note="Website URL not confirmed (Enterprise says they sell on their own site).",
      message=("أهلاً Nileton 👋 قريت في Enterprise إن أسعاركم من ٢٣٥ لـ٥٠٠ جنيه — ده سعر يتعمل عليه فيديو لوحده.\n"
               "فكرة: «طقم جيم كامل بأقل من ١٠٠٠ جنيه» — هول سريع بالأسعار على الشاشة وفيت تشيك، وينفع كمان كفيديو لصفحات المنتجات على Jumia وNoon. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(rank=22, priority="B", company="Brüz", industry="Healthy snacks: tahini nutrition bars",
      size="10g protein, 210 kcal per bar (product listing)",
      why="A snack brand with Egyptian flavours (Tahini Coffee Chocolate, Harankash Cranberry Cashews). People want to see someone taste it first.",
      opportunity="'First bite' taste test (3 people, 3 flavours), 'what's in my gym bag', pre-workout snack.",
      source="https://cairoscene.com/Buzz/Tahini-Nutrition-Bars-Br-z-Gives-Health-Snacks-an-Egyptian-Twist",
      service="Starter, then Creative Test", price="EGP 3,500 / 9,000", films=F_ROSTER,
      note="Instagram handle not confirmed; launch date unclear. Check they're still selling.",
      message=("أهلاً Brüz 👋 بار بطحينة ونكهات زي «Tahini Coffee Chocolate» و«هرانكش بالكرانبري» — دي نكهات الناس محتاجة تشوف حد بيدوقها قبل ما تشتري.\n"
               "فكرة: «أول قضمة» — ٣ أشخاص بيدوقوا ٣ نكهات وبيقيّموها بصراحة، ومعاها فيديو «إيه اللي في شنطة الجيم بتاعتي». "
               "أنا نفسي بتمرن وبجري، فده منتج أعرف جمهوره كويس. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(rank=23, priority="B", company="Social Coffee Roasters", industry="Specialty coffee roaster",
      contact_person="Founder (surname Bahgat, per SceneEats)",
      why="Sells blends online and wants to turn coffee 'from a commodity into a community'. Home-brew tutorials build that.",
      opportunity="'Café-level coffee at home in 3 minutes' tutorial; first-sip reaction; subscription unboxing.",
      source="https://sceneeats.com/Fresh/Social-Coffee-Roasters-How-This-Egyptian-Brand-Is-Transforming-Coffee-from-a-Commodity-into-a-Communit",
      service="Starter, then Creative Test", price="EGP 3,500 / 9,000", films=F_YOU,
      message=("أهلاً Social Coffee Roasters ☕ قريت إنكم عايزين تحوّلوا القهوة من سلعة لمجتمع — والمحتوى اللي بيبني مجتمع قهوة هو «اعملها بنفسك».\n"
               "فكرة: «قهوة زي الكافيه في البيت في ٣ دقايق» بخلطة من خلطاتكم — لقطات قريبة للطحن والصب، ونهاية بأول رشفة. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(rank=24, priority="B", type=T_AGENCY, company="Switch Creation", country="Remote (Egypt, KSA, UAE, US work)",
      industry="Performance ads + content production",
      why="Runs performance ads and content production for brands in Egypt, KSA, UAE and the US. Extra Arabic UGC capacity helps them scale.",
      opportunity="White-label Arabic UGC: scripted by us, filmed and edited by our creators.",
      contact_method="GoodFirms profile; LinkedIn; website",
      source="https://www.goodfirms.co/company/switch-creation",
      service="White-label UGC partnership", price="Starter $120; Creative Test $330",
      films=F_ROSTER,
      message=(("Hi Switch Creation team, I saw you run performance ads and content production for brands in Egypt, KSA, UAE and the US. If you need more Arabic UGC, T Studio works white-label: we write the Arabic scripts and hooks, our creators film and edit, and we check every video before it reaches you. 3 hooks per ad, about 5 days.\n"
               "Open to a small paid test? Samples: [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(rank=25, priority="B", type=T_UPWORK, company="Upwork client: Arabic-speaking UGC creators (ongoing)",
      country="Worldwide applicants", industry="UGC production",
      signal="Open project (Upwork), 'ongoing projects'",
      why="Ongoing project for Arabic-speaking UGC creators. A studio that casts several Arabic speakers covers more briefs than one person.",
      opportunity="Apply as a studio: Egyptian and neutral Arabic creators, 15-60s vertical, hooks, captions, 3-5 day turnaround.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/Hiring-Arabic-Speaking-UGC-Video-Creators-Ongoing-Projects_~022079521216290137611/",
      service="UGC per brief", price="Their rate (not visible); quote $100-120 per video", cash=CASH_UPWORK,
      films=F_ROSTER, ads_country=None,
      note=upwork_age("late July 2026") + " If they require the account holder on camera, skip.",
      message=(("Hi, we're T Studio, a small Arabic UGC studio in Cairo. We write the scripts and hooks; for each brief we cast a native Arabic-speaking creator (Egyptian dialect or neutral Arabic) who films and edits the video, and we check it before delivery. You get different faces and voices from one contact.\n"
               "We deliver 15-60s vertical videos with a hook in the first 2 seconds, captions and clean audio, usually 3-5 days after we get the product or brief. Samples: [PORTFOLIO]\n"
               "Which dialect and product category comes first? I'll send 3 hook ideas for it."))),

    L(rank=30, priority="B", type=T_MOSTAQL, company="Mostaql client: back-support brand (Saudi/Gulf market)",
      website="https://mostaql.com/project/1273311-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D9%88%D9%81%D9%8A%D8%AF%D9%8A%D9%88-ugc-creator-%D8%B9%D9%86-%D8%A8%D8%B9%D8%AF-%D9%84%D8%A8%D8%B1%D8%A7%D9%86%D8%AF-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A-%D8%AF%D9%88%D8%A7%D9%85-%D9%85%D8%B1%D9%86",
      country="Saudi/Gulf market", industry="E-commerce: back braces",
      signal="Confirmed project (Mostaql), $250-500",
      why="Ongoing: 6 UGC clips a week for 45 days, budget $250-500. Face mask allowed. Real (non-AI) UGC only.",
      opportunity="Faceless real-use clips (desk posture, lifting, driving) with Arabic voice-over. Ask if neutral Arabic is acceptable.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1273311-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D9%88%D9%81%D9%8A%D8%AF%D9%8A%D9%88-ugc-creator-%D8%B9%D9%86-%D8%A8%D8%B9%D8%AF-%D9%84%D8%A8%D8%B1%D8%A7%D9%86%D8%AF-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A-%D8%AF%D9%88%D8%A7%D9%85-%D9%85%D8%B1%D9%86",
      service="Ongoing faceless UGC (creator films and edits)", price="Bid inside $250-500 for the 45-day scope",
      cash=CASH_MOSTAQL, films=F_YOU, ads_country=None,
      note="Saudi dialect preferred, so be upfront. " + WEEKS_MOSTAQL + " Avoid medical claims in scripts.",
      message=(("السلام عليكم، قرأت إنكم محتاجين محتوى UGC حقيقي (مش ذكاء اصطناعي) لمشدات الظهر، ٦ مقاطع أسبوعياً لمدة ٤٥ يوم، والظهور بقناع مسموح.\n"
               "صانع محتوى من فريقنا يقدر يصوّر استخدام حقيقي من غير وش (قعدة المكتب، الشيل، السواقة) ويعمل المونتاج مع تعليق صوتي عربي واضح، وإحنا بنكتب السكريبتات وبنراجع كل مقطع. للأمانة: لهجتنا مصرية أو عربية بيضاء، مش سعودية — لو ده مناسب نبدأ بمقطعين تجريبيين.\n"
               "نماذج: [PORTFOLIO]"))),

    # ===================== MOSTAQL: other open projects =====================
    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: 15-30s vertical ad",
      website="https://mostaql.com/project/1276342-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%82%D8%B5%D9%8A%D8%B1-reel-tiktok-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A-%D8%A7%D8%AD%D8%AA%D8%B1%D8%A7%D9%81%D9%8A",
      country="See project page", industry="Short-form ad editing", signal="Confirmed project (Mostaql)",
      why="Wants one professional 15-30s vertical ad (Reel/TikTok). Budget $25-50, 3 days.",
      opportunity="Single ad edit with hook, captions and CTA; offer 3 hook options.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1276342-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%82%D8%B5%D9%8A%D8%B1-reel-tiktok-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A-%D8%A7%D8%AD%D8%AA%D8%B1%D8%A7%D9%81%D9%8A",
      service="Skip for now", price="n/a", cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=WEEKS_MOSTAQL,
      message=("")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: UGC video editing",
      website="https://mostaql.com/project/1276951-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-ugc",
      country="See project page", industry="Short-form editing (UGC)", signal="Confirmed project (Mostaql)",
      why="Wants UGC videos edited.", opportunity="UGC edit with hook, captions, b-roll and 2 hook variants.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1276951-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-ugc",
      service="Skip for now", price="n/a", cash=CASH_MOSTAQL, films=F_NA,
      ads_country=None, note=WEEKS_MOSTAQL,
      message=("")),

    L(priority="B", type=T_MOSTAQL, company="Mostaql client: UGC creators from all Arab countries",
      website="https://mostaql.com/project/1263559-%D8%B5%D9%86%D8%A7%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%85%D9%86-%D8%AC%D9%85%D9%8A%D8%B9-%D8%A7%D9%84%D8%AF%D9%88%D9%84-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
      country="See project page", industry="UGC production", signal="Confirmed project (Mostaql)",
      why="Open to UGC creators from any Arab country.", opportunity="Apply as a studio with Egyptian and neutral Arabic creators.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1263559-%D8%B5%D9%86%D8%A7%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%85%D9%86-%D8%AC%D9%85%D9%8A%D8%B9-%D8%A7%D9%84%D8%AF%D9%88%D9%84-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
      service="UGC per brief", price="Read the page; quote $100-120 per video", cash=CASH_MOSTAQL, films=F_ROSTER,
      ads_country=None, note="Mostaql ID 126xxxx: probably a few months old. " + OLD_MOSTAQL,
      message=("السلام عليكم، إحنا ستوديو UGC في القاهرة: بنكتب السكريبت والهوكات، وبنختار صانع محتوى مناسب (لهجة مصرية أو عربية بيضاء) يصوّر ويعمل المونتاج بهوك في أول ثانيتين، وبنراجع قبل التسليم. ابعت تفاصيل المنتج والسوق المستهدف. نماذج: [PORTFOLIO]")),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: AI platform ad",
      website="https://mostaql.com/project/1248294-%D8%B5%D8%A7%D9%86%D8%B9%D8%B5%D8%A7%D9%86%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B3%D8%AC%D9%8A%D9%84-%D8%A5%D8%B9%D9%84%D8%A7%D9%86-%D9%84%D9%85%D9%86%D8%B5%D8%A9-%D8%B0%D9%83%D8%A7%D8%A1-%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A",
      country="See project page", industry="AI software ad", signal="Project (Mostaql)",
      why="Wants a UGC creator to record a vertical ad for an AI platform. No shipping needed.",
      opportunity="Screen recording + voice-over, or a cast creator on camera.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1248294-%D8%B5%D8%A7%D9%86%D8%B9%D8%B5%D8%A7%D9%86%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B3%D8%AC%D9%8A%D9%84-%D8%A5%D8%B9%D9%84%D8%A7%D9%86-%D9%84%D9%85%D9%86%D8%B5%D8%A9-%D8%B0%D9%83%D8%A7%D8%A1-%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A",
      service="App/software demo ad", price="$60-120", cash=CASH_MOSTAQL, films=F_YOU, ads_country=None, note=OLD_MOSTAQL,
      message=("السلام عليكم، إعلان لمنصة ذكاء اصطناعي ينفع يتصور كتسجيل شاشة + صوت، أو بصانع محتوى قدام الكاميرا، من غير شحن. "
               "هوك مقترح: «خليت الذكاء الاصطناعي يعمل شغل ساعة في دقيقة». نماذج: [PORTFOLIO]")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: agency, long-term Reels/TikTok editing",
      website="https://mostaql.com/project/1245210-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%84-reels-%D9%88-tiktok-%D9%88%D9%83%D8%AA%D8%A7%D8%A8%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D9%84%D9%84%D9%85%D8%AA%D8%A7%D8%AC%D8%B1-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A%D8%A9",
      country="See project page", industry="Digital agency: e-commerce content", signal="Project (Mostaql)",
      why="Digital agency wants long-term Reels/TikTok editing plus content writing for online stores. $25-50.",
      opportunity="Recurring weekly edits with short scripts.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1245210-%D9%85%D9%88%D9%86%D8%AA%D8%A7%D8%AC-%D9%84-reels-%D9%88-tiktok-%D9%88%D9%83%D8%AA%D8%A7%D8%A8%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D9%84%D9%84%D9%85%D8%AA%D8%A7%D8%AC%D8%B1-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A%D8%A9",
      service="Skip for now", price="n/a", cash=CASH_MOSTAQL, films=F_NA,
      ads_country=None, note=OLD_MOSTAQL,
      message=("")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: sportswear store (30 ads from raw footage)",
      website="https://mostaql.com/project/1244957-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A%D8%A9-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A",
      country="See project page", industry="E-commerce: sportswear", signal="Project (Mostaql)",
      why="Wants 30 ad edits from existing raw footage for a sportswear store. $100-250.",
      opportunity="Batch editing with different hooks (price, fit, fabric).",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1244957-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A%D8%A9-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A",
      service="Skip for now", price="n/a", cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=OLD_MOSTAQL,
      message=("")),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: 30 simple UGC videos (Gulf dialect)",
      website="https://mostaql.com/project/1278965-%D8%B5%D8%A7%D9%86%D8%B9-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%A8%D8%B3%D9%8A%D8%B7%D8%A9-%D8%AC%D8%AF%D8%A7-%D9%85%D8%AB%D9%84-ugc",
      country="Gulf market", industry="UGC production", signal="Project (Mostaql)",
      why="30 simple videos for $75 total; Saudi or Gulf dialect required.",
      opportunity="Not worth it: $2.50 per video and a dialect you don't have.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1278965-%D8%B5%D8%A7%D9%86%D8%B9-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%A8%D8%B3%D9%8A%D8%B7%D8%A9-%D8%AC%D8%AF%D8%A7-%D9%85%D8%AB%D9%84-ugc",
      service="Skip", price="n/a", status=ST_SKIP_SAUDI, cash=CASH_MOSTAQL, films=F_NA, ads_country=None,
      note="Listed so you know it exists. Price too low and dialect requirement.", message=""),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: Saudi digital-products store",
      website="https://mostaql.com/project/1278750-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A%D8%A9-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A",
      country="Saudi Arabia", industry="E-commerce: digital products", signal="Project (Mostaql)",
      why="Wants a Saudi UGC creator for 4-6 vertical ads, $25-50.", opportunity="Saudi creator required.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1278750-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A%D8%A9-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A",
      service="Skip", price="n/a", status=ST_SKIP_SAUDI, cash=CASH_MOSTAQL, films=F_NA, ads_country=None, message=""),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: skincare (2 trial videos, then 10)",
      website="https://mostaql.com/project/1245235-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc",
      country="See project page", industry="Skincare", signal="Project (Mostaql)",
      why="2 trial skincare UGC videos, then 10 more if they like them. $25-50, 10 days.",
      opportunity="A creator who really uses the product films a morning routine in natural light.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1245235-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc",
      service="UGC (roster)", price="$50 for the 2 trial videos", cash=CASH_MOSTAQL, films=F_ROSTER, ads_country=None,
      note=OLD_MOSTAQL,
      message=("السلام عليكم، فيديوهين تجربة للعناية بالبشرة وبعدها ١٠ — بنختار صانعة محتوى تجرب المنتج فعلاً وتصور روتين صباحي حقيقي "
               "بإضاءة طبيعية. نماذج: [PORTFOLIO]")),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: UGC video creator",
      website="https://mostaql.com/project/1249583-%D9%85%D8%B7%D9%84%D9%88%D8%A8-ugc-video-creator",
      country="See project page", industry="UGC production", signal="Project (Mostaql)",
      why="Wants a UGC video creator; details not visible in search.", opportunity="Read the brief first.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1249583-%D9%85%D8%B7%D9%84%D9%88%D8%A8-ugc-video-creator",
      service="UGC per brief", price="Read the page", cash=CASH_MOSTAQL, films=F_ROSTER, ads_country=None, note=OLD_MOSTAQL,
      message=("السلام عليكم، إحنا ستوديو UGC صغير في القاهرة: بنكتب السكريبت والهوكات، وصانع محتوى مناسب بيصوّر ويعمل المونتاج، وبنراجع قبل التسليم. ابعت تفاصيل المنتج والجمهور وأبعتلك ٣ هوكات مقترحة. نماذج: [PORTFOLIO]")),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: Saudi UGC creators (short videos)",
      website="https://mostaql.com/project/1264326-%D8%B5%D9%86%D8%A7%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D9%82%D8%B5%D9%8A%D8%B1%D8%A9",
      country="Saudi Arabia", industry="UGC production", signal="Project (Mostaql)",
      why="Wants Saudi UGC creators.", opportunity="Saudi creator required.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1264326-%D8%B5%D9%86%D8%A7%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D9%82%D8%B5%D9%8A%D8%B1%D8%A9",
      service="Skip", price="n/a", status=ST_SKIP_SAUDI, cash=CASH_MOSTAQL, films=F_NA, ads_country=None, message=""),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: Saudi digital agency",
      website="https://mostaql.com/project/1186096-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D8%B5%D8%A7%D9%86%D8%B9%D8%B5%D8%A7%D9%86%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D9%84%D9%84%D8%B9%D9%85%D9%84-%D9%85%D8%B9-%D9%88%D9%83%D8%A7%D9%84%D8%A9-%D8%AA%D8%B3%D9%88%D9%8A%D9%82-%D8%B1%D9%82%D9%85%D9%8A",
      country="Saudi Arabia", industry="Digital agency", signal="Project (Mostaql)",
      why="Wants a Saudi UGC creator for 40-60s videos.", opportunity="Saudi creator required; old project.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1186096-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D8%B5%D8%A7%D9%86%D8%B9%D8%B5%D8%A7%D9%86%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D9%84%D9%84%D8%B9%D9%85%D9%84-%D9%85%D8%B9-%D9%88%D9%83%D8%A7%D9%84%D8%A9-%D8%AA%D8%B3%D9%88%D9%8A%D9%82-%D8%B1%D9%82%D9%85%D9%8A",
      service="Skip", price="n/a", status=ST_SKIP_SAUDI, cash=CASH_MOSTAQL, films=F_NA, ads_country=None,
      note=OLD_MOSTAQL, message=""),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: digital planner ad",
      website="https://mostaql.com/project/1229157-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D8%B5%D8%A7%D9%86%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A-%D9%84%D9%85%D9%86%D8%B8%D9%85-%D8%B1%D9%82%D9%85%D9%8A-digital-planner",
      country="See project page", industry="Digital product", signal="Project (Mostaql), April 2026",
      why="UGC ad for an Arabic digital planner, for TikTok and Facebook ads.",
      opportunity="Tablet/phone screen + hands: 'I planned my whole week in 10 minutes'. No shipping.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1229157-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D8%B5%D8%A7%D9%86%D8%B9%D8%A9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A-%D9%84%D9%85%D9%86%D8%B8%D9%85-%D8%B1%D9%82%D9%85%D9%8A-digital-planner",
      service="App/product demo", price="$50-100", cash=CASH_MOSTAQL, films=F_YOU, ads_country=None,
      note="Posted April 2026; very likely closed.",
      message=("السلام عليكم، منظم رقمي ينفع يتصور كتسجيل شاشة على التابلت أو الموبايل مع إيد وصوت: «نظّمت أسبوعي كله في ١٠ دقايق». "
               "من غير شحن، وتسليم خلال ٤٨ ساعة. نماذج: [PORTFOLIO]")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: tech Reels/TikTok editor",
      website="https://mostaql.com/project/1219358-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-reelstiktok-%D8%AA%D9%82%D9%86%D9%8A%D8%A9",
      country="See project page", industry="Tech content editing", signal="Project (Mostaql)",
      why="Wants an editor for tech Reels/TikTok.", opportunity="Zoomed screen shots, on-screen text, problem-first hook.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1219358-%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D9%85%D9%88%D9%86%D8%AA%D9%8A%D8%B1-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-reelstiktok-%D8%AA%D9%82%D9%86%D9%8A%D8%A9",
      service="Skip for now", price="n/a", cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=OLD_MOSTAQL,
      message=("")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_MOSTAQL, company="Mostaql client: short UGC video editor",
      website="https://mostaql.com/project/1216431-video-editor-%D9%85%D8%AA%D8%AE%D8%B5%D8%B5-%D9%81%D9%8A-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D9%82%D8%B5%D9%8A%D8%B1%D8%A9-ugc",
      country="See project page", industry="Short-form editing (UGC)", signal="Project (Mostaql)",
      why="Wants a video editor specialised in short UGC videos.", opportunity="UGC edits with hook variants.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1216431-video-editor-%D9%85%D8%AA%D8%AE%D8%B5%D8%B5-%D9%81%D9%8A-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D9%82%D8%B5%D9%8A%D8%B1%D8%A9-ugc",
      service="Skip for now", price="n/a", cash=CASH_MOSTAQL, films=F_NA, ads_country=None, note=OLD_MOSTAQL,
      message=("")),

    L(priority="C", type=T_MOSTAQL, company="Mostaql client: Emirati consumer product (3 videos)",
      website="https://mostaql.com/project/1091978-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-3-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D9%88%D8%A7%D9%82%D8%B9%D9%8A%D8%A9-%D9%84%D9%85%D9%86%D8%AA%D8%AC-%D8%A7%D8%B3%D8%AA%D9%87%D9%84%D8%A7%D9%83%D9%8A-%D8%A5%D9%85%D8%A7%D8%B1%D8%A7%D8%AA%D9%8A",
      country="UAE", industry="Consumer product", signal="Project (Mostaql), old",
      why="3 natural 10-20s videos that feel like a customer's experience, not an ad.",
      opportunity="Only if the product ships to Egypt.",
      contact_person="Project owner on Mostaql", contact_method=MOSTAQL_METHOD,
      source="https://mostaql.com/project/1091978-%D8%B5%D8%A7%D9%86%D8%B9-%D9%85%D8%AD%D8%AA%D9%88%D9%89-ugc-%D9%84%D8%AA%D8%B5%D9%88%D9%8A%D8%B1-3-%D9%81%D9%8A%D8%AF%D9%8A%D9%88%D9%87%D8%A7%D8%AA-%D9%88%D8%A7%D9%82%D8%B9%D9%8A%D8%A9-%D9%84%D9%85%D9%86%D8%AA%D8%AC-%D8%A7%D8%B3%D8%AA%D9%87%D9%84%D8%A7%D9%83%D9%8A-%D8%A5%D9%85%D8%A7%D8%B1%D8%A7%D8%AA%D9%8A",
      service="UGC (roster)", price="$90-120", cash=CASH_MOSTAQL, films=F_ROSTER, ads_country=None,
      note="Low project ID: likely 2025 and closed.",
      message=("السلام عليكم، ٣ فيديوهات طبيعية ١٠–٢٠ ثانية بتجربة حقيقية للمنتج — نقدر نعملها لو المنتج يتشحن لمصر. نماذج: [PORTFOLIO]")),

    # ===================== UPWORK: other projects =====================
    L(priority="C", type=T_UPWORK, company="Upwork client: fintech app (Meta & TikTok UGC)",
      country="Creators outside the US", industry="Fintech app", signal="Open project, posted 2026-09-18 (Upwork)",
      why="Wants 15-45s UGC ads for Meta and TikTok from creators outside the US; asks for a rate for 3 edited videos. $200 fixed.",
      opportunity="Quote 3 videos with hooks and 30-day paid usage.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-Creators-for-Fintech-App-Short-Form-Meta-TikTok-Ads_~022100777795128169716/",
      service="UGC Creative Test", price="$330 for 3 (or 2 videos for their $200)", cash=CASH_UPWORK, films=F_ROSTER,
      ads_country=None, note="Two months old; likely filled. Finance ads: no profit promises.",
      message=("Hi, our rate for 3 edited UGC videos for Meta and TikTok is $330, including scripts, 3 hooks per video, captions "
               "and 30 days of paid-ads usage. We write the scripts and hooks; our creators in Egypt (outside the US, as you asked) film and edit each video, "
               "and we check every video before delivery. If $200 is fixed, we can do 2 videos for it. Samples: [PORTFOLIO]")),

    L(priority="C", type=T_UPWORK, company="Upwork client: UGC creators for a mobile app (weekly paid)",
      country="See post", industry="Mobile app", signal="Project (Upwork), long-term",
      why="Long-term UGC for a mobile app, paid weekly.", opportunity="Weekly batches of app demos.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/Hiring-UGC-Creators-for-mobile-app-Long-Term-Weekly-Paid_~022068031912102313068/",
      service="App demos, weekly", price="Quote per video ($60-100)", cash=CASH_UPWORK, films=F_YOU,
      ads_country=None, note=upwork_age("late June 2026"),
      message=("Hi, for app UGC we deliver screen-recording demos with real hands and voice, or a creator on camera, with captions and 3 hooks per video. We write the scripts, our creators film and edit, and we check every video. Weekly batches suit us well. What's the app and your target market? Samples: [PORTFOLIO]")),

    L(priority="C", type=T_UPWORK, company="Upwork client: UGC spokesperson ($100 per video)",
      country="See post", industry="Product explainers", signal="Project (Upwork)",
      why="Wants a UGC spokesperson for 2-3 product explainer videos at $100 each.",
      opportunity="Cast presenter, problem-first 30-45s script, on-screen steps.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-Spokesperson-Needed-for-Product-Explainer-Videos-100-Per-Video_~022067281037762762955/",
      service="UGC explainers", price="$100 per video (their rate)", cash=CASH_UPWORK, films=F_ROSTER, ads_country=None,
      note=upwork_age("mid-June 2026"),
      message=("Hi, for product explainers we write a 30-45s script around one problem and cast a clear, natural presenter (English or Arabic) who films and edits it with captions and on-screen steps. We check every video before delivery. 2-3 videos within 5 days of approval. Samples: [PORTFOLIO]")),

    L(priority="C", type=T_UPWORK, company="Upwork client: French-speaking UGC creators (ongoing)",
      country="See post", industry="UGC production", signal="Project (Upwork), 'ongoing'",
      why="Ongoing 60s on-camera UGC in French.", opportunity="Only if you recruit a French-speaking creator.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/Hiring-French-Speaking-UGC-Video-Creators-Ongoing-Projects_~022065109190258827406/",
      service="UGC per brief (French)", price="Their rate", cash=CASH_UPWORK, films="French-speaking creator films and edits",
      ads_country=None, note=upwork_age("mid-June 2026"),
      message=("Bonjour, nous sommes T Studio, un petit studio UGC au Caire. Nous écrivons les scripts et les accroches ; pour vos vidéos face caméra en français, nous choisissons un(e) créateur(trice) francophone qui filme et monte la vidéo, et nous vérifions chaque vidéo avant la livraison. Vidéos verticales de 60 s, sous-titres et 3 accroches par vidéo. Exemples : [PORTFOLIO]")),

    L(priority="C", type=T_UPWORK, company="Upwork client: street-interview UGC ads ($2,000)",
      country="See post", industry="Social ads", signal="Project, posted 2026-10-15 (Upwork)",
      why="$2,000 fixed for street-interview style social ads; location requirements unknown.",
      opportunity="Only if they accept filming in Cairo.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-Creators-for-Street-Interview-Social-Media-Ads_~022110853591603495807/",
      service="Street-interview ads", price="Their budget", cash=CASH_UPWORK, films=F_ROSTER, ads_country=None,
      note="Read the location and language requirements first.",
      message=("Hi, if you're open to filming in Cairo, T Studio can produce street-interview ads: we write the questions and cast the people, and our creators film and edit them with captions. Which market and language do you need? Samples: [PORTFOLIO]")),

    L(priority="C", type=T_UPWORK, company="Upwork client: UGC for trading/finance content",
      country="See post", industry="Trading / finance", signal="Project (Upwork)",
      why="UGC for trading and finance content.", opportunity="Screen first: licensed product only, no profit promises.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/UGC-Video-Creator-Trading-Finance-Content_~022064081985122705550/",
      service="Screen before quoting", price="Quote only after checks", cash=CASH_UPWORK, films=F_ROSTER, ads_country=None,
      note=upwork_age("early June 2026") + " Trading promos carry scam and regulatory risk.",
      message=("Hi, before quoting: is the product a licensed broker or app, and which countries will the ads run in? "
               "We only make finance ads without profit promises. Samples: [PORTFOLIO]")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_UPWORK, company="Upwork client: small-business short-form editor (trial batch)",
      country="Canada (Ottawa business)", industry="Gifting business", signal="Project, posted 2026-09-25 (Upwork)",
      why="Scripted phone footage into fast vertical videos; batches of 7-8; $50 trial week.",
      opportunity="Low pay but steady editing if it's still open.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/Short-form-video-editor-needed-Instagram-Reels-and-TikTok-small-business-content_~022103562757252441948/",
      service="Skip for now", price="n/a", cash=CASH_UPWORK, films=F_NA, ads_country=None,
      note="About 7 weeks old.",
      message=("")),

    L(status=ST_SKIP_EDIT, priority="C", type=T_UPWORK, company="Upwork client: Arabic story-based YouTube editor (test project)",
      country="See post", industry="Arabic YouTube", signal="Project (Upwork)",
      why="Arabic story-based YouTube editing, starting with a test project.", opportunity="Editing work in Arabic.",
      contact_person="Client on Upwork", contact_method=UPWORK_METHOD,
      source="https://www.upwork.com/freelance-jobs/apply/Arabic-YouTube-Story-Based-Video-Editor-Test-Project_~022064008518006879818/",
      service="Skip for now", price="n/a", cash=CASH_UPWORK, films=F_NA, ads_country=None,
      note=upwork_age("early June 2026"),
      message=("")),

    # ===================== OTHER HIRING SIGNALS / JOBS =====================
    L(status=ST_SKIP_EDIT, priority="C", type=T_HIRING, company="Whitecollars", country="Lebanon (Beirut); remote",
      industry="Recruiting for DTC ad teams", signal="Hiring: freelance DTC ads & VSL video editor, posted 2026-05-21",
      why="Hiring freelance editors for Arabic direct-response ads and AI-powered UGC; Egyptian Arabic speakers welcome.",
      opportunity="Freelance editing contract.", contact_person="Workable application",
      contact_method="Apply on Workable", source="https://apply.workable.com/whitecollarshrm/jobs/view/AD6EC811D2",
      service="Skip for now", price="n/a", films=F_NA, ads_country=None,
      note="Posted May 2026; may be closed.",
      message=("")),

    L(priority="C", type=T_JOB, company="Freelancer.com client: Arabic/Polish UGC for a trading platform",
      country="See post", industry="Trading platform", signal="Project (Freelancer.com)",
      why="Arabic UGC creator for a trading platform.", opportunity="Screen first: licensed product, no profit promises.",
      contact_method="Freelancer.com bid", source="https://www.freelancer.com/projects/video-production/arabic-polish-ugc-creator-for",
      service="Screen before quoting", price="Quote only after checks", cash="Medium: platform payout", films=F_ROSTER,
      ads_country=None, note="Trading promos carry scam and regulatory risk.",
      message=("Hi, Arabic UGC is something my studio produces. Before quoting: which regulator licenses the platform, and which countries "
               "will the ads target? We only make finance ads without profit promises. Samples: [PORTFOLIO]")),

    L(priority="C", type=T_JOB, company="Qureos listing: UGC creator (Arabic content)",
      country="See listing", industry="Social content", signal="Job listing (Qureos)",
      why="Role for an Arabic-language UGC/social content creator.", opportunity="Check if freelance or contract is possible.",
      contact_method="Apply on Qureos",
      source="https://app.qureos.com/jobs/ugc-creator-social-media-content-creator-arabic-language-content-1776894031808",
      service="Freelance UGC", price="Their rate", cash=CASH_JOB, films=F_ROSTER, ads_country=None,
      note="Company and date not visible in search.",
      message="Hi, I run T Studio, a small Arabic UGC studio in Cairo. If a freelance arrangement works, we can supply an Arabic-speaking creator for this role and manage the scripts and quality. Samples: [PORTFOLIO]"),

    L(priority="C", type=T_JOB, company="viral.app: Canvas UGC creator (Saudi Arabia, Arabic)",
      country="Saudi Arabia", industry="Drawing app", signal="Job listing (viral.app)",
      why="$15 per video + $1 per 1,000 views, bonus up to $100 per video; tagged Saudi Arabia, Arabic.",
      opportunity="Likely for Saudi residents only.", contact_method="Apply on viral.app",
      source="https://viral.app/creators/ugc-jobs", service="Skip", price="n/a",
      status="Skip unless open to non-Saudi creators", cash="Medium: platform payout", films=F_NA, ads_country=None, message=""),

    L(status=ST_SKIP_EDIT, priority="C", type=T_JOB, company="Scale Army: remote video editor / AI video creator (Egypt)",
      country="Egypt (remote)", industry="Staffing for marketing teams",
      signal="Job listings: video editor and AI video creator in Egypt",
      why="Remote editing jobs paying an estimated $1,000-1,700 a month (aggregator estimates).",
      opportunity="Long-term income, not this week's cash.", contact_method="Apply via the job board",
      source="https://www.marketingmonk.so/jobboard/jobs/video-editor-at-scale-army-careers-d5blry",
      service="Skip for now", price="n/a", cash=CASH_JOB, films=F_NA, ads_country=None,
      note="Pay figures are estimates from job aggregators.",
      message=""),

    L(priority="C", type=T_JOB, company="Pro Traders Group: UGC Creator (on-site, Cairo)",
      country="Egypt (Cairo)", industry="Trading education", signal="Job listing: full-time on-site UGC creator",
      why="Full-time on-camera role.", opportunity="Doesn't fit: on camera, full-time, on-site.",
      contact_method="FoundItGulf application", source="https://www.founditgulf.com/job/ugc-creator-pro-traders-group-egypt-69399095",
      service="Skip", price="n/a", status="Skip: on-camera full-time job", cash=CASH_JOB, films=F_NA, ads_country=None,
      note="Company name inferred from the URL.", message=""),

    # ===================== EGYPTIAN BRANDS (B/C) =====================
    L(rank=27, priority="B", company="Breathe", industry="Fragrance",
      size="About EGP 1,200 for 80ml; sold through Bloom Pharmacy (26 products listed)",
      why="Enterprise's Nov 2026 review says staying power and a body-gel set set them apart. Staying power is easy to prove on video.",
      opportunity="'9 am to 5 pm: can you still smell it?' all-day wear test.",
      contact_method=FIND_ACCOUNT + "; Bloom Pharmacy brand page",
      source="https://enterpriseam.com/egypt/2026/11/02/making-scents-of-local-brands/",
      service="Creative Test", price="EGP 9,000", films=F_ROSTER,
      note="Website not confirmed. Retailer: https://www.bloompharmacy.com/collections/breathe",
      message=("أهلاً Breathe 👋 قريت في Enterprise إن الثبات وسِت الشاور جل هما اللي بيميزوكم. الثبات حاجة الفيديو بيثبتها: "
               "«من ٩ الصبح لـ٥ العصر — لسه الريحة موجودة؟» بلقطات على مدار اليوم. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(rank=28, priority="B", company="Boshara", industry="Fragrance",
      size="German fragrance YouTuber Jeremy Fragrance named the face of the brand (Feb 2026)",
      why="A big-name face brings attention; everyday-customer UGC is what converts that attention into sales.",
      opportunity="'I wore the King Tut scent for a week: honest review' (real week-long test).",
      source="https://scenenow.com/Buzz/YouTuber-Jeremy-Fragrance-Becomes-Face-of-Egyptian-Brand-Boshara",
      service="Creative Test", price="EGP 9,000", films=F_ROSTER,
      message=("أهلاً Boshara 👋 شفت إن Jeremy Fragrance بقى وش البراند — خطوة كبيرة. الإعلان بوش مشهور بيجيب انتباه، "
               "وفيديوهات UGC من ناس عادية هي اللي بتقنع الناس تشتري.\n"
               "فكرة: «جربت ريحة King Tut أسبوع — رأيي بصراحة». [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(priority="B", company="Meraki", instagram="", industry="Natural skincare with a men's line",
      contact_person="Mona Awwad, founder (press)",
      why="Launched a men's line after customer feedback; Egyptian men were buying skincare from abroad. Men trust other men using it.",
      opportunity="'60-second routine for a guy who hates routines'.",
      source="https://egyptianstreets.com/2023/06/16/why-not-men-merakis-new-line-encourages-egyptian-men-to-love-their-natural-selves/",
      service="Starter, then Creative Test", price="EGP 3,500 / 9,000", films=F_NECK,
      note="Instagram 'Meraki_naturalcare' is from a 2023 article; confirm it's current.",
      message=("أهلاً أستاذة منى 👋 قريت قصة خط Meraki للرجالة — إن الرجالة كانوا بيشتروا سكين كير من بره. "
               "الجمهور ده بيقتنع لما يشوف راجل زيه بيستخدم المنتج من غير تكلف.\n"
               "فكرة: «روتين ٦٠ ثانية لراجل مش بيحب الروتين». [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلك السكريبت؟ [PORTFOLIO]")),

    L(priority="B", company="SLVRSKN", industry="Specialty coffee: drip bags, espresso concentrate",
      size="Part of a larger company, Carbon; sold on Talabat and Fengany",
      why="Pour-over drip bags are a demo product: specialty coffee without a machine.",
      opportunity="'Specialty coffee at the office in 3 minutes, no machine'; also usable on Talabat product pages.",
      contact_method=FIND_ACCOUNT,
      source="https://sceneeats.com/Fresh/SLVRSKN-is-the-Egyptian-Coffee-Brand-Bringing-Speciality-to-Our-Mugs",
      service="Starter, then Creative Test", price="EGP 3,500 / 9,000", films=F_YOU,
      message=("أهلاً SLVRSKN ☕ الـdrip bags بتاعتكم معمولة لفيديو: «قهوة مختصة في المكتب في ٣ دقايق من غير مكنة». "
               "لقطات قريبة للصب والبخار ونهاية بأول رشفة، وتنفع كمان لصفحات المنتج على Talabat. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(priority="C", company="Magma", industry="Activewear", size="Founded 2018",
      why="Local activewear brand; video shows movement and fabric.",
      opportunity="'Full workout in one set: sweat and movement test'.",
      source="https://egyptianstreets.com/2024/04/24/4-local-egyptian-sportswear-brands-to-wear",
      service="Starter", price="EGP 3,500", films=F_NECK, note="Thin coverage; confirm they're active.",
      message=("أهلاً Magma 👋 فكرة إعلان UGC لقطعكم: «تمرين كامل بطقم واحد — اختبار العرق والحركة» بلقطات قريبة. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. أبعتلكم السكريبت؟ [PORTFOLIO]")),

    L(priority="C", company="SeifWear", industry="Streetwear (Egyptian identity)",
      why="Hoodies and tees referencing Egyptian architecture, slang and music. Made entirely in Egypt. Story-led product.",
      opportunity="'Wore SeifWear in Downtown Cairo: what people asked me'.",
      source="https://seif.nl/en/?p=8368", service="Starter", price="EGP 3,500", films=F_ROSTER,
      note="Source domain is unusual; confirm the brand's official account.",
      message=("أهلاً SeifWear 👋 الهوديز اللي فيها إشارات للعمارة والكلام المصري محتاجة حد يحكي قصتها في الشارع. "
               "فكرة: «لبست SeifWear في وسط البلد — والناس سألتني عن إيه». [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Misfit", industry="Streetwear", contact_person="Kareem, founder (first name only, per SceneNow)",
      why="Grew from a family atelier into a streetwear name worn by artists.",
      opportunity="'Fit check before the gig' with a creator from the music crowd.",
      source="https://scenenow.com/Styled/Misfit-is-Dressing-the-Artists-You-Stream-the-Streets-They-Came-From",
      service="Starter", price="EGP 3,500", films=F_ROSTER,
      message=("أهلاً Misfit 👋 قريت إزاي Misfit بدأ من أتيليه العيلة ووصل للفنانين. فكرة: «Fit check قبل الحفلة» بصانع محتوى من جمهور المزيكا. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="TruCult", industry="Streetwear", size="Launched March 2025 by two friends",
      why="Building 'cult' status. Cult brands run on content from the people wearing them.",
      opportunity="'Why I wear TruCult' series in customers' own words.",
      source="https://cairoscene.com/Styled/This-Egyptian-Streetwear-Brand-is-Trying-to-Cultivate-Cult-status",
      service="Starter", price="EGP 3,500", films=F_ROSTER,
      message=("أهلاً TruCult 👋 البراندات اللي بتبني «Cult» بتعيش على محتوى الناس اللي لابساها. فكرة: سلسلة «ليه بلبس TruCult» بأصوات من جمهوركم. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Beast", industry="Vegan protein bars",
      why="A plant-based protein bar has to win the first bite.",
      opportunity="'Blind taste test after training: Beast vs a regular bar'.",
      source="https://sceneeats.com/Fresh/Egyptian-Brand-Launches-Vegan-Protein-Bars",
      service="Starter", price="EGP 3,500", films=F_ROSTER, note="Launch date unclear; confirm they're active.",
      message=("أهلاً Beast 👋 بار بروتين نباتي محتاج يكسب أول قضمة. فكرة: «Blind taste test بعد التمرين: Beast قصاد بار عادي». "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Brown Nose Coffee", industry="Specialty coffee roaster and café",
      contact_person="Omar Abdalla, founder (Enterprise, Aug 2024)",
      why="Third-wave roaster selling beans for home brewing.",
      opportunity="'From bag to first sip': V60 at home in simple steps.",
      source="https://enterpriseam.com/egypt/2024/08/20/meet-our-founder-of-the-week-brown-noses-omar-abdalla/",
      service="Starter", price="EGP 3,500", films=F_YOU,
      message=("أهلاً Brown Nose ☕ فكرة: «من الكيس لأول رشفة» — V60 في البيت بخطوات بسيطة، لقطات قريبة وصوت الصب. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Raw African", industry="Natural skincare (black soap, oils, body butters)",
      size="Stocked at Bloom Pharmacy and ZYNAH",
      why="Texture-heavy products (black soap, butters) look best in close-up video.",
      opportunity="'Black soap: a 30-second routine' with lather and texture close-ups.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films=F_YOU, note="Website not found; use retailer pages to find the official account.",
      message=("أهلاً Raw African 👋 فكرة: «الصابون الأسود — روتين ٣٠ ثانية» بلقطات قريبة للرغوة والملمس. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Areej Aromatherapy", industry="Aromatherapy / natural skincare",
      why="Named by Egyptian Streets (Jul 2026) among local brands competing with multinationals. Aromatherapy sells on mood.",
      opportunity="'A calm night routine in 30 seconds' with warm light and soft sound.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films=F_YOU,
      message=("أهلاً Areej 👋 الزيوت العطرية بتتباع بالإحساس — فكرة: «روتين ليلة هادية في ٣٠ ثانية» بإضاءة دافية وصوت هادي. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Bobai", industry="Skincare: local sunscreen",
      why="Named by Egyptian Streets (Jul 2026) as a local alternative to imported sunscreen.",
      opportunity="'White-cast and texture test' on two skin tones.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films=F_ROSTER,
      message=("أهلاً Bobai 👋 صن سكرين محلي قصاد المستورد — فكرة: «اختبار الطبقة البيضا والملمس» على لونين بشرة مختلفين. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Shaan", industry="Skincare: local sunscreen",
      why="Named by Egyptian Streets (Jul 2026) as a local alternative to imported sunscreen.",
      opportunity="'Sunscreen under makeup: does it pill?' 8-hour real-day test.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films=F_ROSTER,
      message=("أهلاً Shaan 👋 فكرة: «صن سكرين تحت المكياج — هل بيعمل كُتل؟» اختبار ٨ ساعات في يوم عادي. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Rizq", industry="Modest fashion",
      why="Named by Egyptian Streets (Jul 2026) among local modest-fashion labels.",
      opportunity="'3 modest looks from 2 pieces' styling video.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films="Female creator films and edits",
      message=("أهلاً Rizq 👋 فكرة: «٣ لوكات محتشمة بقطعتين» — ستايلنج سريع بصانعة محتوى. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Hayaa", industry="Modest fashion",
      why="Named by Egyptian Streets (Jul 2026) among local modest-fashion labels.",
      opportunity="'A full work week from 5 pieces'.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films="Female creator films and edits",
      message=("أهلاً Hayaa 👋 فكرة: «لبس الشغل للأسبوع كله بـ٥ قطع» بصانعة محتوى. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="MOCHE", industry="Natural body care",
      why="Named by Egyptian Streets (Jul 2026) as a local natural body-care brand.",
      opportunity="'A natural body routine in 30 seconds' with texture close-ups.",
      source="https://egyptianstreets.com/2026/07/08/local-brands-storm-egypts-retail-scene/",
      service="Starter", price="EGP 3,500", films=F_YOU,
      message=("أهلاً MOCHE 👋 فكرة: «روتين جسم طبيعي في ٣٠ ثانية» بلقطات قريبة للملمس. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Bubblzz", industry="Body splash and perfume",
      size="Stocked at Bloom Pharmacy, Talabat and Jumia",
      why="Wide range of body splashes; White Musk is described as a fan favourite.",
      opportunity="'I sprayed Bubblzz and asked friends to guess the scent'.",
      source="https://www.bloompharmacy.com/products/bubblz-bonbon-body-splash-250ml",
      service="Starter", price="EGP 3,500", films=F_ROSTER, note="Spelling varies (Bubblz, Bubblzz, Bubbelz).",
      message=("أهلاً Bubblzz 👋 الـWhite Musk عندكم مفضّل عند الناس — فكرة: «رشّيت Bubblzz وسألت صحابي يخمّنوا الريحة». "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Hathor", industry="Skincare and fragrance (Egyptian heritage)",
      why="Natural skincare drawing on Egyptian heritage; heritage stories suit short-form storytelling.",
      opportunity="'Ancient ritual, modern routine' 30-second story.",
      source="https://enterpriseam.com/egypt/2023/08/04/the-enterprise-guide-for-summer-skincare-courtesy-of-local-brands/",
      service="Starter", price="EGP 3,500", films=F_YOU,
      message=("أهلاً Hathor 👋 فكرة: «طقس مصري قديم في روتين النهارده» — قصة ٣٠ ثانية بلقطات قريبة للمنتج. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="Desirs", industry="Perfume (artisan bottles, Alexandrian motifs)",
      why="Bottle design is a selling point that deserves an unboxing on its own.",
      opportunity="'Slow unboxing' ASMR under strong light.",
      source="https://www.cairo360.com/article/shopping/discover-the-allure-of-locally-made-perfume-brands-with-long-lasting-scents",
      service="Starter", price="EGP 3,500", films=F_YOU,
      message=("أهلاً Desirs 👋 تصميم الزجاجات عندكم يستاهل Unboxing لوحده — فكرة: «فتحت زجاجة Desirs ببطء» ASMR بإضاءة قوية. "
               "[OBSERVATION]\nإحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="The.Man.Brand", industry="Beard grooming (sells via Instagram)",
      why="Facial-hair grooming label selling through Instagram, where video drives sales.",
      opportunity="'3 mistakes men make with their beard', product close-ups.",
      source="https://cairoscene.com/lifestyle/the-man-brand", service="Starter", price="EGP 3,500", films=F_NECK,
      note="Article undated; confirm they're active.",
      message=("أهلاً The Man Brand 👋 فكرة: «٣ غلطات بيعملها الرجالة مع دقنهم» بلقطات قريبة لمنتجاتكم. [OBSERVATION]\n"
               "إحنا ستوديو UGC في القاهرة. [PORTFOLIO]")),

    L(priority="C", company="ElCoach", industry="Arabic fitness and nutrition app",
      size="350,000+ downloads and six-figure seed (2020 reports)",
      why="Arabic fitness app for Egypt and Saudi Arabia; app demos need no shipping.",
      opportunity="'I followed an ElCoach plan for a week' (real), screen recording + training clips.",
      source="https://www.wamda.com/2020/03/elcoach-raises-figure-seed",
      service="Starter", price="EGP 3,500", films=F_YOU, note="Only 2020 coverage found; confirm the app is still active.",
      message=("أهلاً ElCoach 👋 فكرة: «جرّبت خطة ElCoach أسبوع — ده اللي حصل» كديمو للتطبيق بتسجيل شاشة ولقطات تمرين. "
               "أنا نفسي بتمرن وبجري. [OBSERVATION]\n[PORTFOLIO]")),

    # ===================== AGENCIES (B/C) =====================
    L(rank=29, priority="B", type=T_AGENCY, company="Udjat Agency", website="https://www.udjatagency.com/ugc-content-creators-in-cairo/",
      country="Egypt (Cairo, Alexandria, Giza) / UAE", industry="Full-service digital agency",
      size="Founded 2021; offices in Cairo, Alexandria, Giza and Dubai (listings)",
      why="Runs a 'UGC Content Creators in Cairo' page, so it sells UGC to clients and may need overflow production.",
      opportunity="White-label overflow: Egyptian-dialect creators who film and edit, managed by us.",
      contact_method="Website contact; LinkedIn", source="https://www.udjatagency.com/ugc-content-creators-in-cairo/",
      service="White-label UGC partnership", price="Starter EGP 3,500; Creative Test EGP 9,000",
      films=F_ROSTER,
      message=("أهلاً فريق Udjat 👋 شفت صفحة «UGC Content Creators in Cairo» عندكم. لو احتجتوا صناع محتوى إضافيين للهجة المصرية في وقت الضغط، نقدر نشتغل White-label: بنكتب السكريبت والهوكات، وصناع المحتوى بتوعنا بيصوّروا ويعملوا المونتاج، وبنراجع كل فيديو قبل التسليم، بـ٣ هوكات لكل إعلان. نبدأ بفيديو واحد مدفوع؟ [PORTFOLIO]")),

    L(rank=26, priority="B", type=T_AGENCY, company="Starfish", country="UAE (Dubai) / Saudi Arabia (Riyadh)",
      industry="Micro-influencer and UGC agency", size="Listicles cite 10,000+ influencer database, 1,500+ campaigns",
      why="GCC micro-influencer and UGC agency; Egyptian creators are a cost-effective add-on.",
      opportunity="Egyptian-dialect creators who film and edit, managed by us.",
      contact_method="Website contact; LinkedIn",
      source="https://www.influencer-hero.com/blogs/top-micro-influencer-marketing-agencies-in-dubai",
      service="White-label UGC (creator supply)", price="Starter $120; Creative Test $330", films=F_ROSTER, ads_country="AE",
      note="Figures are from listicles, not verified.",
      message=(("Hi Starfish team, for your GCC UGC campaigns T Studio can add Egyptian-dialect creators, managed by us: we write the scripts and hooks, our creators film and edit, and we check every video before delivery. 3 hooks per ad, about 5 days. Happy to start with one paid video. [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(priority="B", type=T_AGENCY, company="OneHub UAE", website="https://onehub.ae/arabic-ugc-creators-for-gcc-ads/",
      country="UAE (Dubai)", industry="Influencer marketing agency", size="Claims 10,000+ verified creators (Clutch profile)",
      why="Sells Arabic UGC creators for GCC ads; Egyptian-dialect creators widen their range.",
      opportunity="Egyptian-dialect creators who film and edit, managed by us.",
      contact_method="Website contact; Clutch", source="https://onehub.ae/arabic-ugc-creators-for-gcc-ads/",
      service="White-label UGC (creator supply)", price="Starter $120; Creative Test $330", films=F_ROSTER, ads_country="AE",
      message=(("Hi OneHub team, I saw your Arabic UGC creators page for GCC ads. If you need Egyptian-dialect creators, T Studio can supply them, managed by us: we write the scripts and hooks, our creators film and edit, and we check every video before delivery. Open to a paid test video? [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(priority="C", type=T_AGENCY, company="Spark Social", country="UAE", industry="UGC and creative strategy agency",
      why="UGC and creative strategy agency; may need Arabic-speaking creators.",
      opportunity="Egyptian-dialect creators who film and edit, managed by us.", contact_method="Website; LinkedIn",
      source="https://influee.co/partnership/spark-social", service="White-label UGC (creator supply)",
      price="Starter $120", films=F_ROSTER, ads_country="AE",
      message=(("Hi Spark Social team, T Studio supplies white-label Arabic UGC from Cairo: we write the scripts and hooks, our creators film and edit, and we check every video before delivery. If you ever need Egyptian-dialect creators, I'd be glad to do a paid test. [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(status="Skip: works only with UAE-permit creators", priority="C", type=T_AGENCY, company="Blue Sky Studios", website="https://blueskystudios.ae/en/ugc",
      country="UAE (Dubai)", industry="UGC studio", size="150+ permit-verified UAE creators; packages from AED 4,400 (own site)",
      why="Uses UAE-permitted creators, so the realistic offer is editing overflow, not filming.",
      opportunity="White-label editing.", contact_method="Website contact", source="https://blueskystudios.ae/en/ugc",
      service="Skip for now", price="n/a", films=F_NA, ads_country="AE",
      message=("")),

    L(priority="C", type=T_AGENCY, company="DeepRoX", website="https://deeprox.lovable.app/", country="MENA / UK",
      industry="Performance and creative studio (static, motion, UGC ad creatives)",
      why="Sells UGC ad creatives; may subcontract Egyptian creators.",
      opportunity="Subcontract Egyptian creators who film and edit, managed by us.", contact_method="Website contact",
      source="https://deeprox.lovable.app/", service="Subcontract (creator supply)", price="Starter $120", films=F_ROSTER, ads_country=None,
      note="Their ROAS claims are self-reported.",
      message=(("Hi DeepRoX team, if you need Egyptian-dialect creators for UGC ad creatives, T Studio works as a subcontractor: we write the scripts and hooks, our creators film and edit, and we check every video. 3 hooks per ad. Paid test? [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(priority="C", type=T_AGENCY, company="Webtonic", website="https://www.webtonic.io/locations/dubai-ugc",
      country="UAE (Dubai / Abu Dhabi)", industry="UGC production", why="UGC agency covering Dubai and Abu Dhabi.",
      opportunity="Egyptian-dialect creators who film and edit, managed by us.", contact_method="Website contact", source="https://www.webtonic.io/locations/dubai-ugc",
      service="White-label UGC (creator supply)", price="Starter $120", films=F_ROSTER, ads_country="AE",
      message=(("Hi Webtonic team, T Studio supplies Arabic UGC from Cairo white-label: we write the scripts and hooks, our creators film and edit, and we check every video. If you need Egyptian-dialect creators, I'd be glad to do a paid test video. [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(priority="C", type=T_AGENCY, company="Grynow Media", website="https://www.grynow.in/ugc-videos-agency-in-dubai-uae.html",
      country="UAE (Dubai) / India", industry="UGC video agency", why="Sells UGC videos in Dubai; Arabic creators and editing help.",
      opportunity="Arabic-speaking creators who film and edit, managed by us.", contact_method="Website contact",
      source="https://www.grynow.in/ugc-videos-agency-in-dubai-uae.html", service="White-label UGC (creator supply)",
      price="Starter $120; Creative Test $330", films=F_ROSTER, ads_country="AE",
      message=(("Hi Grynow team, for your Dubai UGC clients T Studio can supply Arabic-speaking creators from Cairo: we write the scripts and hooks, our creators film and edit, and we check every video before delivery (3 hooks per ad). Paid test? [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    L(priority="C", type=T_AGENCY, company="Glitchcraft Media", website="https://www.glitchcraftmedia.com/",
      country="UAE (Dubai)", industry="UGC agency for TikTok and Instagram",
      why="Listed as a Dubai UGC agency for TikTok and Instagram.", opportunity="Arabic-speaking creators who film and edit, managed by us.",
      contact_method="Website contact", source="https://www.glitchcraftmedia.com/", service="White-label UGC (creator supply)",
      price="Starter $120", films=F_ROSTER, ads_country="AE", note="Only found via one search result; verify it's real and active.",
      message=(("Hi Glitchcraft team, T Studio supplies Arabic UGC for TikTok and Instagram from Cairo: we write the scripts and hooks, our creators film and edit, and we check every video. Paid test video? [PORTFOLIO]\n"
               "— [NAME] · T Studio · Arabic UGC ads"))),

    # ===================== GULF BRANDS (C) =====================
    L(status="Skip for now: editing-only pitch (no shipping to Egypt)", priority="C", company="Fzahabaya", country="Saudi Arabia", industry="Modest fashion: abayas (Salla store)",
      size="TikTok case study: 11.82x blended ROAS, 7,231 purchases (self-reported); Ramadan & Eid 2026 campaign",
      why="Proven TikTok advertiser. Shipping to Egypt is unlikely, so pitch editing of their existing footage.",
      opportunity="Fresh TikTok edits from existing footage with new hooks; 10 edits pack.",
      source="https://ads.tiktok.com/business/en/inspiration/fzahabaya-tiktok-success-stories",
      service="Skip for now", price="n/a", films=F_NA, ads_country="SA",
      message=("")),

    L(status="Skip for now: editing-only pitch (no shipping to Egypt)", priority="C", company="Swag Store SA", country="Saudi Arabia", industry="Youth fashion",
      size="TikTok case study: 6.2M impressions, 76.6K website clicks (self-reported)",
      why="Content-driven TikTok advertiser; editing of existing footage avoids shipping.",
      opportunity="Editing pack with new hooks.",
      source="https://ads.tiktok.com/business/en/inspiration/swag-store-sa-tiktok-success-stories",
      service="Skip for now", price="n/a", films=F_NA, ads_country="SA",
      message=("")),

    L(priority="C", company="SKITCHEN", country="UAE (Dubai)", industry="Functional protein bars (collagen, zero sugar)",
      size="Launched July 2026; made in the UAE",
      why="New snack launch needs taste-test and routine content.",
      opportunity="UGC only if they ship samples to Egypt.",
      source="https://www.nosh.com/pr/2026/07/14/dubaibased-skitchen-launches-functional-protein-bars-with-collagen-and-zero-sugar",
      service="UGC Starter (if they ship samples to Egypt)", price="$120", films=F_YOU, ads_country="AE",
      message=("Hi SKITCHEN team, congrats on the collagen protein bar launch. A 'first bite after training' taste test sells new bars well. If you can ship samples to Cairo, one of our creators can film and edit it with 3 hooks, and we check it before delivery. [PORTFOLIO]")),

    # ===================== PLATFORMS (recruit creators, not clients) =====================
    L(priority="C", type=T_PLATFORM, company="UGC MENA", website="https://ugcmena.com/", country="MENA",
      industry="UGC marketplace", size="Says 450+ creators; brands pay 15% (self-serve) or 25% (managed)",
      signal="n/a", why="Creators set their own price; USD bank payout in Egypt, $100 minimum, paid after brand approval.",
      opportunity="Benchmark rates; your roster creators can list here themselves.",
      contact_method="Sign-up on site", source="https://ugcmena.com/faq", service="n/a", price="n/a",
      status="Use to benchmark rates / recruit", cash=CASH_NA, films=F_NA, ads_country=None,
      note="Operator formed Sept 2026 (Wyoming LLC): new, payout record unproven.", message=""),

    L(priority="C", type=T_PLATFORM, company="Stllr Network for Creators", website="https://apps.apple.com/app/id6446048987",
      country="KSA / UAE / Egypt", industry="Creator app", signal="n/a",
      why="UGC briefs from brands in KSA, UAE and Egypt; in-app wallet.", opportunity="Creators in your roster can join.",
      contact_method="App", source="https://apps.apple.com/app/id6446048987", service="n/a", price="n/a",
      status="Use to recruit", cash=CASH_NA, films=F_NA, ads_country=None, message=""),

    L(priority="C", type=T_PLATFORM, company="Arabic Creators", website="https://www.arabiccreators.com/en",
      country="MENA", industry="Arabic creator marketplace", signal="n/a",
      why="Marketplace with a 'Become a Creator' page; Egypt UGC price guide.", opportunity="Benchmark rates; recruit.",
      contact_method="Site", source="https://www.arabiccreators.com/en/ugc-creators/egypt", service="n/a", price="n/a",
      status="Use to benchmark rates / recruit", cash=CASH_NA, films=F_NA, ads_country=None, message=""),

    L(priority="C", type=T_PLATFORM, company="MENA Creators", website="https://menacreators.com/creators",
      country="MENA", industry="Influencer & UGC marketplace", signal="n/a",
      why="Regional creator marketplace.", opportunity="Recruit creators.", contact_method="Site",
      source="https://menacreators.com/creators", service="n/a", price="n/a", status="Use to recruit",
      cash=CASH_NA, films=F_NA, ads_country=None, message=""),

    L(priority="C", type=T_PLATFORM, company="Collabstr (Cairo UGC creators)", website="https://collabstr.com/top-influencers/user-generated-content/in/egypt/cairo",
      country="Egypt", industry="Creator marketplace", signal="n/a",
      why="Lists roughly 36-49 UGC creators in Egypt and Cairo, with public profiles.",
      opportunity="Find creators to recruit for your roster.", contact_method="Collabstr profiles",
      source="https://collabstr.com/top-influencers/user-generated-content/in/egypt/cairo", service="n/a", price="n/a",
      status="Use to recruit", cash=CASH_NA, films=F_NA, ads_country=None,
      note="Contact creators through the platform or their public business contacts only.", message=""),

    L(priority="C", type=T_PLATFORM, company="Contra", website="https://contra.com",
      country="Global", industry="Freelance platform", signal="n/a",
      why="Freelance profile for international clients; Egypt local bank payout fee 1% per Contra's help page.",
      opportunity="Optional studio profile for international inbound.", contact_method="Create profile",
      source="https://help.contra.com/en/articles/9322934-fees-overview", service="n/a", price="n/a",
      status="Optional: studio profile", cash="Medium: platform payout", films=F_NA, ads_country=None,
      note="Who pays Contra's platform fee is unclear in their docs.", message=""),
]


# ---------------------------------------------------------------- offer
PACKAGES = [
    dict(name="Starter", deliverables="1 video (15-45 s): script and hooks by us, filmed and edited by a creator, captions",
         usd=120, egp=3500, usage="Organic on the brand's channels; paid ads +30% for 30 days",
         revisions="1 round", delivery="3-4 days after the product arrives", terms="100% upfront",
         creator_cost_egp="1,000-2,000 (plan 1,200)", videos=1),
    dict(name="Creative Test", deliverables="3 videos, 3 concepts, 1 hook each (+2 bonus hooks for a first order)",
         usd=330, egp=9000, usage="Organic + 30 days paid ads", revisions="1 round per video",
         delivery="5 days after the product arrives", terms="100% upfront", creator_cost_egp="3,000-6,000 (plan 3,600)", videos=3),
    dict(name="Content Sprint", deliverables="5 videos + 5 alternate hooks (10 ad variations)",
         usd=520, egp=14000, usage="Organic + 30 days paid ads", revisions="1 round per video",
         delivery="7 days after the product arrives", terms="50% deposit, 50% before final files",
         creator_cost_egp="5,750-10,750 (plan 6,750 incl. hook lines)", videos=5),
]

EXTRAS = [
    ("Extra hook (re-cut opening)", "$20", "EGP 500"),
    ("Extra revision round", "$20", "EGP 500"),
    ("Second-language version", "$45", "EGP 1,200"),
    ("Rush (48 h)", "+30%", "+30%"),
    ("Raw footage", "+30%", "+30%"),
    ("Same package filmed by 2-3 different creators", "+20%", "+20%"),
    ("Paid usage 90 days total (instead of 30)", "+30%", "+30%"),
    ("Paid usage 6 months", "+75%", "+75%"),
    ("Paid usage 12 months", "+100%", "+100%"),
    ("Unlimited / perpetual buyout", "Quote only", "Quote only"),
    ("Spark Ads / whitelisting from a creator's account", "Quote, creator must agree", "Quote, creator must agree"),
]

PIPELINE_STAGES = [
    "Not contacted", "Drafted", "Approved", "Sent", "Follow-up 1 sent", "Follow-up 2 sent",
    "Replied", "Interested", "Call booked", "Quote sent", "Negotiating", "Won - awaiting deposit",
    "Deposit received", "In production", "Delivered", "Paid in full", "Lost", "Not a fit",
]

# Six working days left. Egypt's weekend is Friday-Saturday.
DAILY_PLAN = [
    dict(date="2026-11-17", day="Tue", objective="Set up, recruit first creators, first approved sends",
         msgs=20, apps=5, creators=10),
    dict(date="2026-11-18", day="Wed", objective="Full outreach day; creator auditions; 2 portfolio videos",
         msgs=35, apps=5, creators=10),
    dict(date="2026-11-19", day="Thu", objective="Follow-ups, quotes, first deposit",
         msgs=35, apps=5, creators=5),
    dict(date="2026-11-20", day="Fri", objective="Egypt weekend: agencies, Upwork, Gulf; production",
         msgs=20, apps=5, creators=3),
    dict(date="2026-11-21", day="Sat", objective="Production and delivery; Upwork; follow-ups",
         msgs=20, apps=5, creators=2),
    dict(date="2026-11-22", day="Sun", objective="Egyptian work week starts: follow-ups, close, collect",
         msgs=35, apps=5, creators=0),
]

HUNTING_LINKS = [
    ("Meta Ads Library: video ads running in Egypt with 'اطلب الآن'", "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=EG&q=%D8%A7%D8%B7%D9%84%D8%A8%20%D8%A7%D9%84%D8%A2%D9%86&search_type=keyword_unordered&media_type=video", "Brands already paying for ads. Pick ones with weak or few videos."),
    ("Meta Ads Library: 'شحن مجاني' (free shipping) in Egypt", "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=EG&q=%D8%B4%D8%AD%D9%86%20%D9%85%D8%AC%D8%A7%D9%86%D9%8A&search_type=keyword_unordered&media_type=video", "E-commerce stores running ads now."),
    ("TikTok Creative Center: top ads (set region to Egypt / Saudi Arabia / UAE)", "https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en", "What's working in your target categories this month."),
    ("Mostaql: newest UGC projects", "https://mostaql.com/projects?keyword=UGC", "Apply within hours of posting."),
    ("Upwork: Arabic UGC, newest first", "https://www.upwork.com/nx/search/jobs/?q=arabic%20ugc&sort=recency", "Check posting date and 'Payment verified'."),
    ("Reddit r/UGCcreators: hiring posts", "https://www.reddit.com/r/UGCcreators/search/?q=hiring&restrict_sr=1&sort=new", "Read the sub rules before replying."),
    ("Upwork: UGC video, newest first", "https://www.upwork.com/nx/search/jobs/?q=ugc%20video&sort=recency", "Check posting date and 'Payment verified'."),
    ("X: 'looking for UGC creators' (latest)", "https://x.com/search?q=%22looking%20for%20UGC%20creators%22&f=live", "Only reply where they ask for applications."),
    ("LinkedIn jobs: UGC creator, Egypt", "https://www.linkedin.com/jobs/search/?keywords=UGC%20creator&location=Egypt", "Also check 'Remote' roles in the GCC."),
    ("LinkedIn posts: 'UGC creator' hiring, latest", "https://www.linkedin.com/search/results/content/?keywords=%22UGC%20creator%22%20hiring&sortBy=%22date_posted%22", "Founders posting needs."),
    ("Facebook groups: UGC Egypt", "https://www.facebook.com/search/groups/?q=UGC%20Egypt", "Join, read rules, don't spam."),
    ("Facebook posts: 'مطلوب صانع محتوى'", "https://www.facebook.com/search/posts/?q=%D9%85%D8%B7%D9%84%D9%88%D8%A8%20%D8%B5%D8%A7%D9%86%D8%B9%20%D9%85%D8%AD%D8%AA%D9%88%D9%89", "Brands asking for content creators."),
    ("Wuzzuf: UGC jobs", "https://wuzzuf.net/search/jobs/?q=UGC", "Brands hiring content roles = content budget."),
    ("viral.app: UGC jobs", "https://viral.app/creators/ugc-jobs", "Check country and language requirements."),
    ("Twine: UGC creator jobs", "https://www.twine.net/jobs/ugc-creators", "Remote UGC briefs."),
    ("Collabstr: Cairo UGC creators (recruiting)", "https://collabstr.com/top-influencers/user-generated-content/in/egypt/cairo", "Creators for your roster."),
]

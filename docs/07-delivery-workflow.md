# Delivery workflow

Free tools only: WhatsApp Business, Google Drive, Google Forms, Google Docs, the Google Sheet CRM, CapCut, Canva. No new software this week.

## The 14 steps

| # | Step | What you do | Time limit | Tool |
|---|---|---|---|---|
| 1 | Offer sent | Send the quote message ([05](05-sales-system.md#quote-send-by-whatsapp-or-email-after-a-yes)) | Same day as the yes | WhatsApp / email |
| 2 | Client accepts | Get a written "approved" | — | WhatsApp |
| 3 | Scope and rights confirmed | Send the agreement ([06](06-payments-and-agreement.md)) with package, usage period and dates | Within 2 h | Google Doc / PDF |
| 4 | Deposit received | Check it has **landed** in your account; log it in the Revenue Ledger | Before anything else | Bank / InstaPay app, Sheet |
| 5 | Brief collected | Send the brief form; ask them to ship the product to you | Same day | Google Form |
| 6 | Script approved | Write scripts + 3 hooks each; client approves | Scripts in 2 working days; approval in 24 h | Google Doc |
| 7 | Filming | Cast (send 2–3 creator options), send the filming brief ([09](09-creator-roster.md#filming-brief-send-for-every-job)), hand over the product; film your b-roll | 1–2 days | WhatsApp, Drive |
| 8 | Editing | CapCut defaults ([04](04-portfolio-scripts.md#editing-defaults-in-capcut-all-six)), 3 hook versions, QA checklist below | 1–2 days | CapCut |
| 9 | Client review | Send watermarked 720p previews in a Drive folder | — | Drive |
| 10 | Revisions | One round per video | Within 48 h of feedback | CapCut |
| 11 | Final payment | Send the invoice for the balance | Same day as approval | Invoice template |
| 12 | Final files | Share the Finals folder once the balance lands | Within 2 h of payment | Drive |
| 13 | Testimonial and referral | Ask 5–7 days after the ads go live | Day 5–7 | WhatsApp |
| 14 | Repeat order | Offer the monthly plan | Day 7–14 | WhatsApp |

Pay creators within 48 hours of the client's approval in step 9 or 10, from the money already received.

## Brief form (Google Form, 11 questions)

1. Brand, product name and product link.
2. What problem does it solve? Top 3 benefits.
3. Who buys it (age, city, why they buy)?
4. Where will the videos run (TikTok, Reels, Snap, Meta)? Organic, paid, or both?
5. Claims you must make; words or claims to avoid; competitors not to mention.
6. Tone: funny, calm, premium, energetic?
7. Links to 1–3 ads you like.
8. Offer and CTA (discount code, link, WhatsApp).
9. Deadline.
10. Who approves the scripts and videos (name and WhatsApp)?
11. Confirm the product ships to the studio address: [ADDRESS].

## Script approval message

> **AR:** دي السكريبتات الـ{n} ومع كل واحد ٣ هوكات. لو تمام ردوا بـ«موافق» ونبدأ التصوير. أي تعديل على النص دلوقتي مجاني، بعد التصوير بيبقى تصوير جديد.
>
> **EN:** Here are the {n} scripts, each with 3 hooks. Reply "approved" and we start filming. Script changes are free now; after filming they mean a re-shoot.

## Files

**Folder per client** in Drive: `CLIENT / 01 Brief · 02 Scripts · 03 Raw (private) · 04 Previews · 05 Finals`.
Share only `04 Previews` before payment, then `05 Finals` after.

**File names:** `BRAND_concept_H1_v1.mp4`, e.g. `COTMASR_touchtest_H2_v1.mp4` (H1, H2, H3 = hook versions; v2 after revisions).

**Preview watermark:** CapCut text `PREVIEW · [STUDIO]`, centre, 30% opacity, exported at 720p.

## QA checklist (before any preview goes out)

- [ ] Hook text on screen from the first frame to 1.5 s; no black first frame
- [ ] Product visible in the first 3 seconds and on the end card
- [ ] Captions checked word by word, brand name spelled right, inside the safe zone
- [ ] Voice clear, no clipping; music under the voice and cleared for commercial use
- [ ] Only approved claims; no medical, financial or "guaranteed" promises
- [ ] 1080×1920, 30 fps, length as briefed
- [ ] No CapCut ending clip; no other brands' logos in frame
- [ ] All hook versions exported and named
- [ ] Creator release on file; usage period written in the delivery message

## Delivery message (after the balance lands)

> **AR:** الملفات النهائية هنا: [LINK]. عندكم {n} فيديو × ٣ هوكات. الاستخدام: نشر عضوي من غير مدة + إعلانات مدفوعة لحد {date}. لو حابين تمددوا، ابعتولي. شكراً على ثقتكم 🙏
>
> **EN:** Final files are here: [LINK]. You have {n} videos × 3 hooks. Usage: organic with no time limit, plus paid ads until {date}. Message me if you'd like to extend. Thank you for trusting us.

## Testimonial and referral (day 5–7 after the ads go live)

> **AR:** أتمنى الفيديوهات تكون شغالة كويس 🙌 ممكن جملتين عن تجربتكم معانا؟ ولو تسمحوا نعرض الشغل في البورتفوليو. ولو تعرفوا براند تاني محتاج فيديوهات، لو بدأ معانا هتاخدوا هوكين مجاناً على طلبكم الجاي.
>
> **EN:** Hope the videos are performing well. Could you share two sentences about working with us, and may we show the work in our portfolio? If you know another brand that needs videos, you'll get 2 free hooks on your next order when they start with us.

Only publish a testimonial with written permission, word for word.

## Repeat order (day 7–14)

> **Monthly plan:** 4 new videos + 4 alternate hooks every month for **EGP 11,000 / $400**, 2-month minimum, paid at the start of each month.

Pitch it with the client's own numbers: "Your best hook was H2; next month we test 4 new angles built on it."

## Capacity (your hours per package)

| Task | Creative Test (3 videos) |
|---|---|
| Scripts and hooks | 1.5 h |
| Casting, brief, product handover | 1 h |
| Your b-roll | 1 h |
| Editing 3 videos + hook versions | 3–4 h |
| QA, previews, delivery | 0.5 h |
| **Total** | **≈ 7–8 h** |

So alongside outreach you can deliver about one Creative Test a day. Editing packs run about 1 hour per short. Above that, add a second editor before taking more work.

## Optional n8n flow (after the manual process works; not this week)

```
Google Form (brief) ──► n8n
   ├─ add a row to the Google Sheet (Pipeline + Revenue Ledger)
   ├─ copy the Drive folder template for the client
   ├─ send "brief received + script date" to the client (email) and to you
   └─ create a calendar reminder for the script due date
Sheet stage = "Delivered" ──► n8n waits 24 h ──► balance reminder to the client
Sheet stage = "Paid in full" ──► n8n waits 5 days ──► testimonial request
```

Build it only after 2–3 clients have gone through the manual steps, so you automate a process you know works. It needs a Google account connection in n8n and nothing else.

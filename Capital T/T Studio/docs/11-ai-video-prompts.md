# AI video prompts (Higgsfield): product clips only

Written with the Higgsfield prompt skills in `.claude/skills/` (`07-ecommerce-ad`, `09-product-360`, `11-social-hook`). Notes on where those skills come from and how they're licensed are in [HIGGSFIELD-NOTES.md](../../../.claude/skills/HIGGSFIELD-NOTES.md).

**This is optional.** Real creators still make every video. An AI clip only adds a product shot, a short intro or a background.

## Rules (same as the rest of T Studio)

1. **No AI people.** No faces, no presenters, no "customer". Hands are fine only in clearly stylised shots, never posed as a real reviewer.
2. **Start from a real photo of the real product** (image-to-video), so the colour, shape and logo stay true. Don't let AI show quality claims: fabric tests, sweat and fit must be filmed by the creator with the real product.
3. **Label it.** Add `AI-generated` in small text on the AI clip. TikTok and Meta require labels for realistic AI content ([03](03-market-evidence.md#5-ai-ugc-checked-nov-15)). The concept-ad label from [04](04-portfolio-scripts.md#labelling-rules-non-negotiable) still applies.
4. **Client work:** use AI clips only if the client agrees to them in writing.

## Cost (checked Nov 17, sources disagree)

Search results found no free Seedance 2.0 access. Paid plans are reported at about $19–129 a month, and a 5-second 720p clip costs about 22–25 credits. Plan names and prices changed several times in 2026, so check higgsfield.ai/pricing yourself. Sources: [Higgsfield blog](https://higgsfield.ai/blog/seedance-2-0-pricing-2026), [Creatify](https://creatify.ai/blog/higgsfield-pricing-(2026)-plans-and-what-you-ll-actually-pay), [Segmind](https://blog.segmind.com/higgsfield-credits-explained-expiry-rules-and-real-cost/).

**This week:** don't pay for it before a client has paid you. It isn't needed to hit Sunday's goal.

## How to use a prompt

1. On higgsfield.ai, go to Create → Video, choose Seedance 2.0, upload your product photo, and paste the prompt. Set the ratio to 9:16 and the length to 5 s.
2. Or, in Claude on your computer with the Playwright MCP and Higgsfield logged in, run `/seedance-auto-generate`. It asks before spending credits.
3. Send the clip to the creator, who cuts it into the video in CapCut with the `AI-generated` label.

Replace `[PRODUCT]` and `[COLOUR]` with the real product's details.

---

## A. Unboxing intro (for concept ad 2, [04](04-portfolio-scripts.md#2-unboxing-i-ordered-from-a-local-brand-this-is-what-showed-up))

**Use:** a 3-second opener before the creator's real unboxing footage.

```
Generate a 5-second vertical (9:16) e-commerce intro video using the uploaded product photo as reference. Keep the product's exact colour, shape and logo.
Hook (0-2 s): a plain kraft-paper parcel sits on a light wooden table beside a window; it gently lifts and the lid opens on its own, tissue paper unfolds, soft morning side light.
Reveal (2-5 s): [PRODUCT], a [COLOUR] folded cotton garment, rises slightly out of the box and slowly turns 30 degrees; camera pushes in slowly to the fabric texture.
Style: realistic, warm natural light, shallow depth of field, calm and premium, no people, no hands, no text, no logos other than the product's own.
Audio: soft paper rustle and tape sound only.
```

**Text the creator adds:** «طلبت من براند مصري… وده اللي وصلني» + `AI-generated` (small, corner, during the AI clip only).

## B. Product 360 (activewear, for concept ad 6, [04](04-portfolio-scripts.md#6-fitness-apparel-squat-sweat-and-stretch-test))

**Use:** a 4–5-second product beauty shot between the creator's tests, or as the final frame.

```
Generate a 5-second vertical (9:16) product showcase using the uploaded photo as reference. Keep the product's exact colour, cut and logo.
[PRODUCT], a [COLOUR] gym t-shirt on an invisible mannequin, floats in a dark grey studio.
0-1 s: a single spotlight snaps on from above.
1-4 s: smooth full 360-degree rotation at medium speed; a cool rim light outlines the shape; camera static, slight push-in.
4-5 s: freeze on the front view; light flare passes across the logo.
Style: clean, sporty, high contrast, realistic fabric, no people, no faces, no text.
Audio: low bass hit on the spotlight, quiet whoosh during the turn.
```

**Text the creator adds:** «أصعب ٣ اختبارات لأي لبس جيم» on top, and `AI-generated` in the corner.

## C. Scroll-stopper hook (any product)

**Use:** the first 2 seconds of an ad, before the creator speaks.

```
Generate a 4-second vertical (9:16) social media hook using the uploaded product photo as reference; keep the product exactly as in the photo.
0-2 s: [PRODUCT] drops from above into frame and lands on a bright [COLOUR] background with a soft bounce; small dust particles burst outward in slow motion.
2-4 s: quick snap zoom to a macro detail of the product (texture, stitching or label), then hold.
Style: punchy, bright, clean studio, realistic, no people, no hands, no text.
Audio: one sharp impact sound on landing, then silence.
```

**Text the creator adds:** the chosen hook from the script, plus `AI-generated` in the corner.

# Notes on the ai-business-skills folders

The five research and strategy skills here come from a third-party skill pack. Read this before using or updating them.

## Source and licence

- **Repo:** https://github.com/minhnv0807/ai-business-skills, commit `4ef06ff` (Nov 5, 2026), copied on Nov 21, 2026.
- **Licence:** MIT, Copyright (c) 2025 Over Powers Agency. The full text is in [AI-BUSINESS-SKILLS-LICENSE.txt](AI-BUSINESS-SKILLS-LICENSE.txt).

## What was copied

- `product-marketing-context-global`: the shared context file that the other skills read first.
- `09-customer-insight-global`: what buyers are trying to get done, their pains and moments of truth.
- `08-competitor-research-global`: competitor tiers, gaps and a positioning map.
- `58-positioning-global`: who it's for, how it differs, and claims backed by proof.
- `31-offer-design-global`: packages, a value stack, honest guarantees and an offer ladder.
- `product-marketing-context-global/references/operating-rules-global.md`: the pack's operating rules.

## What was changed

- **09 header:** `language: en` was mis-indented, so the header didn't parse. It's moved under `metadata`.
- **Context skill:** its two links to the operating rules now point to the copy in its own `references/` folder.

## What was left out, and why

- **Root `CLAUDE.md`:** it renames the assistant, makes Vietnamese the default language and tells it to clone and run other installers.
- **`.mcp.json`:** it adds 10 outside connectors (Ahrefs, Similarweb, HubSpot, Slack and others).
- **`install.sh` / `install.ps1` and the plugin config:** they would copy everything, including the `CLAUDE.md` above.
- **The other 60+ skills:** not needed for the research.

## How Capital T uses them

- **Where the context lives:** each business keeps its own context file. T Studio's is `Capital T/T Studio/research/00-context.md`. `.agents/product-marketing-context-global.md` at the repo root only points there.
- **Region:** none of the region variants (US, EU, SEA, LATAM) fits Egypt or the Gulf. Fill in local details: EGP and USD, selling through WhatsApp and Instagram DMs, and local rules. The US rules the skills cite (FTC) still matter for US clients only.
- **Blocked sources:** sources the skills suggest that are blocked here (Reddit, Instagram, TikTok, Facebook, X, Meta Ads Library) are replaced by the owner's own checks, web search and interviews.
- **The pack's own rules still apply:** never invent data, write `[REAL DATA NEEDED]` for gaps, and get approval before any real-world action. Interview quotes are kept word for word but without names.

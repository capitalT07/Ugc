# Notes on the skills in this folder

## Higgsfield skills (17 folders: `01-…` to `15-…`, `higgsfield-image-auto`, `seedance-auto-generate`)

- **Source:** https://github.com/AKCodez/higgsfield-claude-skills, commit `f6698ab`, copied on Nov 17, 2026.
- **Licence:** the source repo has no licence file, so all rights stay with its author. Keep this copy private and don't redistribute it.
- **Left out:** `ugc-hot-girl` and `ugc-video-auto`. They create AI people designed to look real and use them in testimonial ads. That breaks Capital T's rules and is a fake-testimonial risk (the FTC bans testimonials from people who don't exist, and TikTok and Meta require AI labels).
- **Changed:** `higgsfield-image-auto` no longer points to `ugc-hot-girl`.

**Rules for AI clips in T Studio work:**
1. Use AI only for product shots, b-roll, backgrounds and motion graphics.
2. Label AI clips as AI wherever the platform or the client needs it.
3. Never show an AI person as a customer or reviewer. Use an AI presenter only if a client asks for one, always labelled as AI.
4. Real creators still film the talking parts.

**Where they run:** `higgsfield-image-auto` and `seedance-auto-generate` drive higgsfield.ai in a browser through the Playwright MCP. They need the owner to be logged in, and they ask before using credits. Higgsfield can't be reached from the cloud environment, so these run only in Claude on the owner's computer. The 15 prompt skills only write text and work anywhere.

## last30days

- **Source:** https://github.com/mvanhorn/last30days-skill, commit `488e50d`, v4.3.2, MIT licence (`last30days/LICENSE`). The demo media folder `assets/` was left out.
- **Never** accept its offer to read browser cookies or a Reddit session. Add no API keys unless the owner chooses to, through the secure credential form.
- **In the cloud environment**, Reddit, X, TikTok and Instagram are blocked, so it uses the sources it can reach.

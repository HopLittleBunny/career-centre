# Career Centre website product audit — 15 July 2026

## Evidence captured

1. `docs/website-audit-2026-07-15/01-home-desktop.png` — live Home page, full-page desktop capture before changes.
2. `docs/website-audit-2026-07-15/02-install-desktop.png` — live Install page, full-page desktop capture before changes.
3. Live pages inspected: Home, Install, Privacy and Support.
4. Independent Claude review: <https://claude.ai/chat/3a39ea5b-1b7b-4d11-a092-88164ce2d4d7>.
5. `docs/website-audit-2026-07-15/03-home-revised-desktop.png` — revised Home page, full-page desktop capture.
6. `docs/website-audit-2026-07-15/04-install-revised-desktop.png` — revised Install page, full-page desktop capture.
7. `docs/website-audit-2026-07-15/05-install-revised-mobile.png` — revised Install page rendered at a 390px Chrome frame width.

Claude chose its own funnel-weighted rubric for a non-technical, likely-anxious job seeker. It rated the pre-change site **6.7/10** overall:

| Dimension | Weight | Score |
| --- | ---: | ---: |
| Install completion clarity | 18% | 6.0 |
| First-visit comprehension | 15% | 6.5 |
| Trust and credibility | 15% | 8.5 |
| Information hierarchy and scannability | 12% | 5.0 |
| Copy quality and credibility | 10% | 6.5 |
| Visual quality and warmth | 8% | 6.5 |
| Accessibility | 8% | 7.0 |
| Mobile/responsive | 7% | 6.5 (provisional) |
| Differentiation | 7% | 8.0 |

Claude's verdict was **ready after minor changes**, with install-page triage and a plain-language product definition treated as non-negotiable.

## What was already strong

- Honest boundaries, no invented evidence, no outcome guarantees and clear synthetic-example labelling.
- Plain Privacy and Support pages, including the instruction never to put a CV in a public support report.
- Clear differentiation: no separate publisher fee or account, no publisher CV database, no auto-apply and use of the user's AI plan.
- The navy/yellow brand identity and confident typography.
- The four-step “Talk naturally” model and “Your Career Centre is ready” assumptions receipt.

These were retained.

## Accepted improvements

1. **Plain product definition and three-step start path.** The Home hero now says that Career Centre is a free career plugin for the user's existing ChatGPT or Claude. A three-step section makes the journey explicit: install, share CVs, start talking.
2. **Install-page triage.** The two provider paths remain primary. Duplicate downloads, hashes, directory caveats, continuity guidance, connector notes and technical verification moved into one native collapsed Advanced section.
3. **One starting sentence per provider.** Both paths now centre on “Help me find my next role.” ChatGPT mentions `@Career Centre` only as a fallback; Claude uses `/career-centre` once to invoke the skill.
4. **More accurate availability language.** “ChatGPT: live” became “ChatGPT: directory listing,” with a plain note that access can vary by plan, region and organisation settings. Claude is labelled “ZIP available” while public directory review is pending.
5. **Clearer copy.** “Source discipline,” “canonical posting,” “Word quality gates” and “continuity limits” were replaced with ordinary-language explanations.
6. **Stronger hierarchy and screenshot access.** The Install content now uses a wider layout, a compact “What happens next” panel and full-size links for every install screenshot.
7. **Consistent navigation.** The primary navigation is now How it works, Boundaries, Privacy and Install across the public pages.

## Modified or declined suggestions

- **Replace the hero CV with a human photo:** declined for now. A generic stock person would weaken evidence and trust. The synthetic Word output remains a truthful product artefact; its caption is retained. A future real product walkthrough could replace it.
- **Add a sticky install button:** deferred. The header is already sticky and keeps Install visible on desktop; mobile shows the Install action while hiding secondary navigation. More persistent UI would add clutter before there is conversion evidence.
- **Add fake testimonials or outcome claims:** rejected, consistent with the product's evidence rules.
- **Wholesale redesign:** rejected. Claude explicitly found the visual identity and core structure sound; the changes target comprehension and conversion friction.

## Accessibility and mobile checks

- Existing skip links, semantic headings, descriptive alt text, responsive viewport and visible focus rules were retained.
- Advanced content uses native `details`/`summary`, so it remains keyboard-operable without JavaScript.
- Buttons keep at least 50px height; install screenshots can now be opened full size.
- Grids collapse to one column at 820px; buttons become full width at 520px.
- The revised Install page was visually checked at a 390px Chrome frame width. The primary path stays single-column, buttons are full width, text does not clip and the Advanced panel remains reachable.
- The audit did not include a physical-device screen-reader run; that remains a limitation rather than an inferred pass.

## Post-change release checks

- Validate HTML structure and internal links.
- Capture and inspect revised Home and Install pages at desktop size. **Passed locally.**
- Capture and inspect at least one mobile-width Install page. **Passed at 390px locally.**
- Re-run the release validator and public-site packager.
- Confirm GitHub Pages deployment before declaring the revised site live.

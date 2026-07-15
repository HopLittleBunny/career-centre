# Career Centre Open Door design QA

Date: 2026-07-15

## Compared inputs

- Reference: `/var/folders/_y/938tzztd2kj1b6301sr71wnw0000gn/T/codex-clipboard-85889a9b-04ea-4f44-965a-dab5e81616b6.png`
- Homepage implementation: `/tmp/career-centre-home-desktop.png`
- Walkthrough desktop: `/tmp/career-centre-walkthrough-desktop.png`
- Walkthrough mobile: `/tmp/career-centre-walkthrough-mobile.png`
- Application pack: `/tmp/career-centre-application-pack.png`
- Global localisation: `/tmp/career-centre-global.png`

The reference and the implementation were viewed together in the same comparison pass.

## Fidelity review

- Typography: the Cormorant Garamond display face and Manrope body face reproduce the editorial, warm-professional hierarchy of the reference. Headline wrapping remains intentional across desktop and 390 px mobile.
- Layout and spacing: the navy masthead, cream hero, real product-screen composition, process sequence, navy Word-pack band, global cards, Indeed extension and trust close follow the supplied content order and visual rhythm.
- Colour and surfaces: navy, warm cream, orange, teal and soft regional-card colours map closely to the target. Borders and shadows are restrained and consistent.
- Imagery: only real captured Career Centre, Claude, Indeed and synthetic Word-output screenshots are used. No fake product screenshots, handcrafted SVG art or placeholder imagery were introduced.
- Icons: the existing Open Door identity is reused and functional icons come from one Material Symbols family.
- Responsiveness: checked at 1440 x 900 and 390 x 844. Desktop retains the reference composition; mobile stacks the journey and screenshots without horizontal overflow or clipped controls.

## Behaviour and accessibility review

- The primary navigation reaches the new walkthrough and homepage sections.
- ChatGPT and Claude provider tabs update `aria-selected`, the URL hash and the visible panel.
- Provider tabs support keyboard arrow, Home and End handling.
- Copy buttons successfully place the exact starter prompt in the browser clipboard, including on local HTTP via the fallback path.
- Skip links, headings, landmarks, labelled tabs, alt text, visible focus states and reduced-motion handling are present.
- Console check returned no warnings or errors on desktop or mobile walkthrough states.
- The release validator passed in submission-ready mode, including local-link and public-page checks.

## Resolved during QA

- Added a non-secure-context copy fallback after the first local-browser clipboard check.
- Clarified that recurring scheduling requires an eligible provider plan.
- Localised scheduling examples for India, the United States and Australia.
- Added a visible readiness receipt with target, geography, sources, compensation, CV, sections and application-pack assumptions.
- Added an explicit explanation of why ChatGPT and Claude may present different icons.

No open P0, P1 or P2 visual, interaction, accessibility or responsive defects remain.

final result: passed

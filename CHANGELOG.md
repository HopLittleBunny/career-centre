# Changelog

## 4.0.0-beta.4 — 15 July 2026

- Promoted the recurring-search handoff to a non-negotiable product milestone instead of leaving it as buried closing guidance.
- Added expectation-setting during readiness, a visually separate automation CTA after the first verified search, and a recovery CTA after the first application pack.
- Made ChatGPT Work create the Scheduled task directly after the user supplies cadence, time and timezone; added an exact Work/Scheduled fallback only when the current surface cannot create it.
- Added the provider-correct Claude Cowork `/schedule` route and ordinary-chat handoff without implying that a normal chat created a scheduled task.
- Made the automation offer apply even when every verified role is Maybe or Skip.
- Replaced the weak scheduling string-presence regression with milestone-specific readiness, search, pack, acceptance and fallback checks.
- Added the official Indeed ChatGPT plugin as an optional post-automation discovery extension while keeping employer or authorised-recruiter postings authoritative.
- Kept the Open Door icon in the package and added a release gate requiring explicit upload to every OpenAI directory and composer icon slot.

## 4.0.0-beta.3 — 15 July 2026

- Added an explicit overall CV-strength verdict and optional deeper review during intake.
- Made the first Career Passport an automatic setup output and clarified that the plugin ZIP is installed once.
- Added transparent post-generation CV quality ratings with a revision threshold separate from ATS scoring.
- Added market-localisation contracts for Australia, the United States and India.
- Added explicit compensation-basis storage and local INR lakh rendering after live India testing.
- Passed fresh fictional India and US setup/search journeys, including India portal selection, exact-role verification, honest no-filler behaviour and proactive automation offers.
- Changed ChatGPT scheduling to prefer the existing Work task and its context; kept a disclosed standalone snapshot fallback.
- Added a proactive daily or weekday automation offer after the first successful manual search and documented Claude Cowork scheduling.
- Kept reference-template support available only after an explicit user request.
- Clarified the free positioning: no separate Career Centre subscription, with provider plan and usage limits still applying.
- Expanded both provider suites to 60/60 passing tests.

## 4.0.0-beta.2 — 14 July 2026

- Added multi-CV source registration, cross-version consistency guidance and a constructive first CV review.
- Added an independent qualitative CV diagnostic with impact-ranked extraction, structure, chronology, repetition and writing findings; it never presents a universal ATS score.
- Expanded the Career Passport into one portable Career Evidence File with generated-document version history and source-document provenance.
- Added optional document-language and regional-spelling preferences without adding setup questions.
- Added a complete in-chat CV fallback when Word creation is unavailable, clearly labelled partial.
- Completed an architecture and licence audit of nine supplied open-source CV/writing projects plus the enrichment pack; no third-party code or runtime dependency was imported.
- Expanded both provider suites to 56/56 passing tests.

## 4.0.0-beta.1 — 14 July 2026

- Renamed the public product and installed skill to **Career Centre** while retaining the legacy plugin package ID for compatibility.
- Added a no-cost static launch site, privacy and terms pages, privacy-safe support forms and automatic GitHub Pages deployment.
- Added a direct ChatGPT Skill ZIP with a published SHA-256 checksum.
- Closed submission validation with 44/44 automated contract and Word-document tests passing.
- Prepared the public source repository and OpenAI directory-review materials.

## 4.0.0-alpha.1+codex.20260714134949 — 14 July 2026

- Replaced the unsupported ChatGPT scheduled cross-run-memory promise with an explicit snapshot-backed alert mode.
- Embedded safe profile, preference, evidence and existing role-history snapshots in generated scheduled prompts.
- Added visible continuity disclosure, recent-posting preference and prohibitions on fake run numbers, Passport updates and cross-run-newness claims.
- Added `verified_persistent` mode that fails closed unless the latest Passport can be loaded and saved for the next execution.
- Stabilised role identity guidance around employer posting IDs, external IDs, canonical employer/title and description similarity rather than mutable location labels.
- Added two scheduling regressions; the automated suite is now 44/44 passing.

## 4.0.0-alpha.1+codex.20260714131404 — 14 July 2026

- Made personal CV/resume, reusable CV-base and reference-Word-format requests primary skill triggers, even when generic document tooling is also available.
- Added explicit CV-base/reference-format routing, evidence/reference separation and bundled DOCX validation requirements.
- Added a trigger-contract regression test; the automated suite is now 42/42 passing.
- Closed the personal-Pro reference-format host gate with a natural, no-`@` Work journey and independent two-page Word preview.
- Replaced the ChatGPT skill ZIP and reinstalled the cache-busted Codex plugin build.

## 4.0.0-alpha.1 — 2026-07-14

- Rebuilt the product as a ChatGPT-first skills-only plugin.
- Replaced the four-card setup with adaptive conversational onboarding.
- Separated recommendation decisions from application lifecycle state.
- Added strict evidence provenance and claim-to-source mapping.
- Added exact-posting, salary and employment-type invariants.
- Rebuilt application-pack generation so paired cover letters cannot be silently omitted.
- Added fail-closed run validation and adversarial evaluation fixtures.
- Removed HTML dashboard generation from the default product path.
- Added strict 65%/80% two-page density gates plus explicit rendered visual approval.
- Added portable manifests that avoid leaking local filesystem paths.
- Added public-submission copy, reviewer cases, privacy/terms/support source and release validation.
- Added a deterministic, market-aware readiness summary with exactly seven active-assumption lines.
- Added advanced document preferences for page strategy, section order, optional/omitted sections and reference-Word formatting.
- Added portable feedback and correction history so the Career Passport can improve transparently without a publisher-operated memory service.
- Added global regression tests covering Australia, Canada and the United Kingdom with no cross-market default leakage.
- Added optional advanced CV-field preferences for contact visibility/order, location and work-right display, headline behaviour, date style and section-label overrides.
- Added a `release/LATEST.json` pointer with SHA-256 checksums for the authoritative plugin and Skill ZIPs.
- Added a portable automation configuration and deterministic recurring-search prompt with timezone, role limit, document mode, deduplication and fail-closed rules.

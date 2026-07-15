# Career Centre beta.3 — ChatGPT and Claude end-to-end results

Date: 15 July 2026  
Test data: fictional candidate `Jordan Lee` and synthetic role fixture `ATLAS-001`  
Submission state: **not submitted**. The existing approved beta.2 listing remains unchanged; beta.3 is being held for owner review.

## Review conversations

- ChatGPT beta.3 private-skill test: https://chatgpt.com/c/6a56ed81-27a0-83ec-ab80-6185ac0a18e6
- Claude beta.3 private-plugin test: https://claude.ai/chat/9b2bdb3a-6631-4fad-8eae-6a7fb1233c3b

These are account-private conversation links, not public share links. The test used fictional contact details, but the conversations also contain live-search research and should remain private unless deliberately shared.

## What was tested

1. Upload and broad initial CV review.
2. Guided setup and the seven-line “Your Career Centre is ready” receipt.
3. Automatic downloadable Career Passport.
4. One selective live role-search pass with exact-posting validation, salary context, no filler and mentor-style judgement.
5. Proactive scheduling offer only after the useful manual search.
6. ChatGPT native schedule creation, Scheduled-page verification and cleanup.
7. Claude’s truthful Cowork handoff and continuity disclosure.
8. Controlled Word CV and Word cover-letter generation from the same fictional CV and synthetic role brief.
9. Evidence-safety, structural validation, rendering, page-density measurement and human visual inspection of all six document pages.
10. Recovery behaviour when the ChatGPT response stream was interrupted during final document QA.

## Conversation and workflow results

| Dimension | ChatGPT | Claude |
|---|---:|---:|
| Broad first CV review | 9.2/10 | 9.3/10 |
| Guided setup and Passport | 9.0/10 | 9.4/10 |
| Selective search and mentor judgement | 8.6/10 | 8.8/10 |
| Scheduling behaviour before refinement | 9.2/10 | 7.8/10 |
| Recovery and platform reliability | 7.8/10 | 8.4/10 |
| Overall live journey | **8.8/10** | **8.7/10** |

### What passed on both

- Began the CV review with `Overall CV strength: Solid but under-positioned`.
- Explained what works, what is underselling the candidate and the single priority edit.
- Offered a deeper review without forcing it.
- Respected “setup only”: no premature search and no application documents.
- Produced all seven readiness labels in the required order.
- Created a downloadable Career Passport automatically.
- Warned once that a new conversation may not inherit context.
- Avoided filler roles and explained why inspected near-misses were excluded.
- Used a candid mentor voice rather than dumping a job feed.
- Did not create application documents automatically and never attempted submission.

### ChatGPT scheduling result

ChatGPT created `[TEST] Career Centre — Jordan` for weekdays at 08:00 Australia/Sydney, maximum three roles, in the continuing Career Centre task. The Scheduled list summarised the custom recurrence as `Weekly`, but opening the task confirmed Monday through Friday at 08:00. The timezone conversion was correct for Perth. The task was deleted after verification so no unwanted run remains.

This is the strongest no-backend scheduling path because the task returns to the existing conversation context. It is still not cross-chat or cross-account memory.

### Claude scheduling result and refinement

Claude correctly disclosed, when challenged, that an ordinary Claude chat cannot create the recurring task; recurring execution belongs in Cowork and each run is a separate Cowork session. It then accurately described `snapshot_only` continuity and refused to claim persistent latest-Passport loading.

The initial scheduling offer had two defects: it changed the confirmed three-role cap to a five-role default, and it implied that each run would load the latest Passport. The beta.3 source was tightened after the test to:

- preserve the actual last-confirmed role limit;
- use five only when no cap exists;
- describe the Cowork input as an embedded Passport snapshot;
- forbid “latest Passport” or cross-run deduplication claims unless loading and saving are demonstrably verified.

Regression coverage was added for this contract.

## Independent Word-document review

All four DOCX files opened, yielded selectable text, rendered without clipping, used visible bullets and contained no private-use glyphs or legacy bullet fonts. Both CVs are exactly two pages and both letters are exactly one page.

### ChatGPT pack

- CV page fill: 65.2% on page 1; 80.2% on page 2.
- CV diagnostic: 399 selectable words, 15 bullets, clear sections, six date signals and five scale/outcome signals.
- Structural validation: no errors or warnings; one working email hyperlink.
- Cover letter: 256 words; no generic opening; one working email hyperlink.
- Independent CV rating: **8.4/10**.
- Independent cover-letter rating: **8.7/10**.

Strengths: exceptionally evidence-safe, clean hierarchy, restrained claims, strong metrics, credible governance/adoption positioning and a practical contribution thesis. Weaknesses: page 1 feels intentionally spacious, the headline is less role-specific than Claude’s, and the cover letter describes first steps but stops short of a sharply labelled 60/90-day contribution.

### Claude pack

- CV page fill: 67% on page 1; 85% on page 2.
- CV diagnostic: 430 selectable words, 17 bullets, clear sections, six date signals and six scale/outcome signals.
- Structural validation: no errors or warnings; no hyperlinks.
- Cover letter: 274 words; no generic opening; no hyperlinks.
- Independent CV rating: **8.3/10**.
- Independent cover-letter rating: **8.8/10**.

Strengths: slightly stronger role-specific positioning, excellent visual balance, the warmer cover-letter opening and an unusually candid explanation of the AI-advisory evidence gap. Weaknesses: `workforce-technology adoption` is a stronger interpretation of CRM-workflow adoption than necessary, contact links are not active, and the proposed GenAI paragraph is honest but adds risk to a stretch application. The letter also lacks a clearly labelled 60/90-day contribution.

### Honest conclusion on document quality

Neither provider should call this fictional Director-level application a 9.5/10 pack because the source CV does not evidence Director-scale enterprise accountability, workforce planning, team/budget scope or prior GenAI advisory work. The stronger product behaviour is to say that plainly. Claude’s self-rating of 7.5/10 was more conservative and better calibrated to the evidence ceiling; ChatGPT’s self-rating of 9.0/10 reflected document execution more than shortlist competitiveness.

The generated documents are suitable as product demonstrations, not as evidence that a weak-fit candidate has become a strong-fit candidate through wording.

## Refinements made after the live run

1. ChatGPT and Claude readiness receipts must name recognisable primary market boards—for example SEEK and LinkedIn in Australia, Naukri and LinkedIn in India, and Indeed and LinkedIn in the United States—rather than saying only “major boards”.
2. Claude scheduling now preserves the confirmed result limit and defaults to five only when no limit exists.
3. Claude scheduling now uses explicit snapshot language and cannot claim latest-Passport continuity without verified read/write persistence.
4. ChatGPT/OpenAI listing subtitle shortened to `Find roles. Build better CVs.` to satisfy the portal’s 30-character limit.
5. Regression tests were added for market-source naming and Claude schedule truthfulness.

## Final automated checks

- ChatGPT/Codex package: **60/60 tests passed**.
- Claude package: **61/61 tests passed**.
- Submission-ready release validation: **passed with zero errors and zero warnings**.
- ChatGPT, Claude and public-site ZIPs rebuilt with fresh checksums.

## Claude review timing and interim sharing

Anthropic does not publish a guaranteed plugin-review turnaround. Its submission form states that submissions are reviewed, inclusion is not guaranteed and there may be delays while the directory spins up. Treat the timing as indeterminate rather than promising a number of days.

Friends do not need to wait for directory approval. A paid-plan Claude user can receive the plugin ZIP and use Claude’s custom-plugin upload flow. Anthropic’s help centre says users may upload a custom plugin received from a colleague and use installed plugin skills in Claude web chat, Claude Desktop and Cowork.

Interim file: `release/career-centre-4.0.0-beta.3-claude-plugin.zip`

Suggested friend instructions:

1. Open Claude and choose **Customize → Plugins**.
2. Choose the custom-plugin upload option.
3. Select the ZIP once and enable Career Centre.
4. Start a normal chat, type `/career-centre`, and attach one or several CVs.
5. Use one main conversation and save the latest Career Passport for continuity.
6. For recurring runs, move the calibrated search to Cowork scheduling; do not upload the ZIP every day.

## Release recommendation

**Submission-worthy after owner review: yes.** The current overall product rating is **8.8/10**. It is differentiated by free skills-only installation, multi-CV evidence handling, mentor-style selectivity, global localisation, a portable Career Passport, Word application packs, explicit evidence ceilings and schedule-aware continuity. The main remaining limits are platform latency, no universal cross-chat persistence and Claude’s snapshot-only scheduled history unless a real persistent storage path is added later.

Do not submit beta.3 until Amit reviews the two conversations and the four Word outputs and explicitly authorises submission.

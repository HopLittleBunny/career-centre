# Career Centre beta.3 global live-test results

Date: 15 July 2026  
Provider used: Claude web with the locally uploaded Career Centre 4.0.0-beta.3 plugin  
Test data: fictional only

## Outcome

Both localisation journeys passed their functional acceptance tests. The strongest evidence is that the same plugin produced meaningfully different search assumptions, compensation language, work-right handling, source mixes and CV guidance for India and the United States. It did not merely swap currencies.

| Scenario | Setup | Manual search | Result |
| --- | --- | --- | --- |
| Priya Nair, Bengaluru, INR 32 lakh fixed floor | Pass | Pass with source-access caveat | 9.0/10 |
| Alex Morgan, Chicago, USD 160k base floor | Pass | Pass with low-yield disclosure | 8.7/10 |

## India test

Passed:

- Gave the required broad verdict: `Overall CV strength: Strong`.
- Kept fixed compensation, variable pay and CTC distinct.
- Recorded the 60-day notice period because the fictional user supplied it.
- Named the correct India source mix: exact employer sites, LinkedIn India, Naukri, foundit and iimjobs.
- Did not request or add a photograph, date of birth, marital status, caste, religion or government identifier.
- Created and attached a Career Passport automatically.
- Returned three exact employer postings with salary basis, employment type, decision, match, risk and no filler: OpenFX (Maybe), Amgen (Maybe), Smartsheet US-only (Skip).
- Correctly rejected the Smartsheet role for the US-only location despite the strong title fit.
- Proactively offered a weekday or daily Cowork search after the first manual run.

Source caveat:

- Naukri was explicitly included in the market plan, but no returned role used a Naukri URL. The live run preferred exact employer postings, which is the correct source ladder. This proves India-aware source selection, but not authenticated Naukri retrieval. Naukri should remain a discovery source when accessible, never a required connector or a reason to bypass access controls.

Observed defect and fix:

- The live readiness receipt rendered `INR 3,200,000` even though the narrative correctly used `INR 32 lakh`. The final beta.3 code now supports an explicit compensation basis and renders this as `INR 32 lakh+ fixed compensation`. Regression coverage was added.

## United States test

Passed:

- Gave the required broad verdict: `Overall CV strength: Solid but under-positioned`.
- Used `resume`, US spelling, USD and explicit US work-authorisation language.
- Kept base salary, bonus, equity and total compensation distinct.
- Selected exact employer/ATS postings first, then LinkedIn, Indeed and Built In for discovery.
- Created and attached a Career Passport automatically.
- Did not pad a weak search: it returned one fully verified but closed GE HealthCare role as Skip and explained why no other role cleared the gates.
- Included the exact posting, listed base range, employment type, main match and skip reason.
- Proactively offered daily or weekday Cowork scheduling after the manual run.

Search caveat:

- Yield was deliberately low because most surfaced pages were indexes, sign-in-gated or misaligned. The product behaved safely by refusing to fabricate fresh roles. This is a quality pass, but a discovery-coverage warning.

## Cross-provider regression suite

- ChatGPT/Codex package: 60/60 tests passed.
- Claude package: 60/60 tests passed.
- Submission-ready package validation: zero errors and zero warnings.
- New regression assertions cover India sources (`Naukri`, `foundit`, `iimjobs`, `LinkedIn India`), US sources (`Indeed`, `Built In`, `USAJOBS`, `LinkedIn`), INR lakh display and explicit salary basis.

## Release caveat

Claude took roughly two minutes for setup and several minutes for a selective live search because it read the full skill, validated the Passport and verified exact postings. The final answers were strong and conversational, but latency is the clearest remaining UX weakness. Do not weaken link verification to make it feel faster; instead reduce unnecessary visible setup narration and keep the initial response compact.

## Overall assessment

Global behaviour is release-worthy at 8.9/10. India localisation is now real and useful, including India-specific portals and compensation concepts. The remaining work is performance polish and broader source-access coverage, not a redesign of the product logic.

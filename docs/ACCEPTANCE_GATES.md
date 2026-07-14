# v4 acceptance gates

The plugin can be rated 9/10 or higher only when every critical gate passes and the weighted score is at least 90/100.

## Critical gates

- A new user can begin with ordinary language and a CV; no prompt syntax, project or state-file editing is required.
- Initial setup asks at most one compact message containing no more than four missing high-impact decisions.
- Every displayed role has an exact posting URL and a listed or clearly labelled estimated salary band.
- Apply is impossible for a closed, unverified, generic-link or evidence-incompatible role.
- CV-derived claims are labelled source-only unless the user or an independent source confirms them.
- Every substantive tailored-document claim maps to one or more evidence IDs.
- A normal application pack contains both CV and cover letter unless the user explicitly selected CV-only.
- Run success is impossible when any required file or QA report is missing or failing.
- No application is submitted automatically.
- Final Word files open, pass structural validation and pass rendered visual inspection where rendering is available.

## Weighted score

| Area | Weight |
| --- | ---: |
| First-use simplicity and conversational quality | 20 |
| Evidence safety and provenance | 15 |
| Search, link freshness and duplicate control | 15 |
| Role decision quality and selectivity | 15 |
| Word application-pack quality | 15 |
| State, feedback and lifecycle continuity | 10 |
| Runtime integrity, recovery and testing | 7 |
| Privacy and distribution readiness | 3 |

## Live ChatGPT gate

The final skill tree is now installed and the three required personal-Pro web journeys pass:

1. CV-first broad job search.
2. CV plus a supplied job description.
3. Returning-user application update and follow-up.

The supplied-role journey returned a browser-inspected two-page Word CV and one-page cover letter. A separate natural-language journey auto-routed to the skill and returned a browser-inspected two-page reference-formatted CV base with evidence/reference isolation and portable round bullets. The returning-user journey preserved recommendation separately from application stage and returned a portable Passport. Browser observations and QA metrics are retained in `docs/test-runs/`.

Scheduled browser work is accepted only as a disclosed snapshot-backed alert: embedded Passport history plus within-run deduplication, no cross-run-memory claim, no automatic documents and no submission. Verified-persistent mode must fail closed unless the latest Passport can be loaded and saved for the next run. The final installed personal-Pro build `4.0.0-alpha.1+codex.20260714134949` passed a fresh natural-language preview: it exposed the exact saved prompt and recurrence, labelled continuity `Snapshot-backed`, described repeat risk and created no task because the user requested preview only.

Additional public-release gates remain: live legal/support URLs, directory review and personal Plus compatibility.

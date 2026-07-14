# Search and decisions

## Search design

Translate the Career Passport into several adjacent search lanes rather than one literal title query. Include target titles, transferable titles, geography, seniority, exclusions and compensation signals.

Search enough candidates to reject weak roles without consuming the user's plan on an open-ended crawl. On the first pass, use at most four focused search queries and inspect at most twelve plausible exact postings. Default presentation limit is five. Stop early when the remaining candidates are weak; a shortlist of two strong roles is better than five padded roles.

The displayed-role contract applies to every user-visible title, company or posting link, including rejected search candidates and near misses. Either give that role the full decision record—salary and basis, employment type, exact URL, decision, fit, shortlist chance, match, risk and CV angle—or keep it anonymous and report only counts plus exclusion patterns. A linked or named rejection list without full assessments is invalid.

Choose sources for the user's market. Prefer exact employer postings and authorised recruiter postings, then use major job boards for discovery and public salary sources for estimates. Do not hard-code Australian boards, currency, employment conventions or work-right assumptions into the global product.

## Verification

A reviewed role needs:

- exact posting URL;
- company, title and location;
- source/provider and external job ID when available;
- posting status and checked timestamp;
- content fingerprint;
- listed salary or evidence-based estimate with basis;
- employment type and duration when applicable;
- role-history comparison.

Create stable role identity in this order: exact employer posting identity or external job ID; otherwise canonical employer plus normalised title; then material description similarity. Normalise case, punctuation, common employer suffixes and remote labels. Do not put mutable location text such as `Americas` versus `Remote Americas` into the primary identity key. Treat an employer posting and a job-board mirror as aliases of the same role when employer, title and substantive description match. Location remains a hard-gate fact, but it is secondary evidence for deduplication.

Reject aggregator links when the employer or authorised recruiter posting is available. A company careers home page is not an exact role URL.

The accessible exact employer posting is authoritative for status, location, employment type and listed compensation. Use a mirror only to fill a field the employer omitted, and label that basis. A mirror must never override or relabel salary stated by the employer. Surface genuine conflicts explicitly and lower confidence instead of collapsing them into a false single answer.

Do not reject an otherwise strong role only because salary is not listed. Provide a conservative evidence-based market estimate, label it clearly as an estimate and explain the basis. Reject or downgrade only when the best defensible estimate fails the user's compensation gate or uncertainty is too large to judge.

## Decision order

1. Hard gates: work rights, location, employment type, compensation, prohibited employer, mandatory licence/clearance.
2. Essential requirement evidence.
3. Transferability and adjacent evidence.
4. Strategic value.
5. Competition and seniority risk.
6. Documentability: whether the case can be made without exaggeration.

Do not average away a failed hard gate.

## Fit and shortlist estimates

Fit score reflects requirement alignment, not enthusiasm. Shortlist chance must also account for seniority calibration, evidence specificity, location/work-rights risk and likely competition.

Use ranges internally and report a rounded percentage with uncertainty. Avoid false precision when posting detail is thin.

## Contract roles

State contract type and duration, estimate day rate or annualised equivalent, and explain why the opportunity is exceptional enough to consider or why it is deprioritised.

## Decision critic

Before releasing a role, ask:

- Did the salary or employment type violate a preference?
- Did the score rely on an unsupported assumption?
- Is the exact posting open now?
- Has this role already been reviewed, applied to or rejected?
- Could the role realistically be shortlisted using safe evidence?

If any answer is unresolved, downgrade or clarify rather than presenting Apply.

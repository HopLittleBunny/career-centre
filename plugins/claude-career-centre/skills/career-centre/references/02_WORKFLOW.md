# Workflow

Use this workflow as a state machine. A run may move backwards when validation fails; it may not skip a required gate.

1. `INTENT` — infer what outcome the user wants.
2. `INGEST` — read CV, role material and prior passport.
3. `EVIDENCE` — extract source-only claims with provenance.
4. `PREFERENCES` — resolve only decision-critical gaps.
5. `HISTORY` — reconcile prior roles, applications and corrections.
6. `DISCOVER` — search broadly enough to be selective.
7. `NORMALISE` — create stable role identities and deduplicate.
8. `VERIFY` — exact URL, open status, checked time and content fingerprint.
9. `ENRICH` — salary, employment type, closing date and recruiter.
10. `MAP` — requirement-to-evidence mapping and hard-gate review.
11. `CLARIFY` — optional micro-question only when decision-changing.
12. `DECIDE` — Apply, Maybe or Skip with honest risk.
13. `CRITIQUE` — check for preference, evidence and optimism errors.
14. `BUILD` — optional application pack from approved evidence IDs.
15. `QA` — contract, DOCX and rendered-layout checks.
16. `COMMIT` — update passport and immutable history events.
17. `NEXT` — give one clear next action or schedule recurring work.

## Completion states

- `SUCCESS`: all requested work and required artifacts passed validation.
- `SUCCESS_NO_PACK`: requested assessment/search completed; no application pack was requested or eligible.
- `PARTIAL`: useful output exists but a non-optional stage remains incomplete.
- `BLOCKED`: an external dependency or critical user fact prevents progress.
- `FAILED`: output is unsafe or unusable and no reliable partial result can be returned.

Never upgrade `PARTIAL` to `SUCCESS` merely because a conversational answer was produced.

# Licence compatibility review

Review date: 14 July 2026

This is a product-engineering record, not legal advice.

## Current release position

Career Centre does not copy, vendor, link to or execute code, trained models, data files, binaries or style packages from the supplied open-source archives. The new CV diagnostic and Passport extensions were independently implemented for this repository using standard-library Python plus the package's existing optional `python-docx` environment.

Because no third-party source was incorporated, the supplied projects are research references rather than runtime or distribution dependencies. Their licences do not change Career Centre's current distribution terms. `THIRD_PARTY_NOTICES.md` records the review transparently.

## Compatibility decisions

| Licence | Reviewed projects | Decision |
|---|---|---|
| Apache-2.0 | Resume Matcher | Permissive with notice/patent conditions if code is later incorporated. No code incorporated now. |
| MIT | JSON Resume, Reactive Resume, write-good, retext, Vale | Permissive with copyright/licence notice if code is later incorporated. No code incorporated now. |
| BSD-3-Clause | proselint | Permissive with notice and non-endorsement conditions if code is later incorporated. No code incorporated now. |
| GPL-3.0 | pyresparser | Reference-only. Do not copy or distribute its code/model/data inside the current package without a deliberate licensing decision and complete source/compliance plan. |
| AGPL-3.0 | OpenResume | Reference-only. Do not copy or adapt its implementation into a hosted or distributed Career Centre component without specialist review of source-offer/network obligations. |

## Rules for future contributors

1. Record the exact upstream repository, release tag, commit and licence before importing anything.
2. Prefer independent implementation of a general product idea when a small provider-neutral solution is sufficient.
3. Do not copy GPL/AGPL source, trained assets, examples or style rules into the release by accident.
4. For MIT/BSD/Apache code, preserve the required copyright and licence text in the distributed package and notices.
5. Review transitive dependencies, model/data licences and hosted-service terms separately; a permissive root licence does not prove every asset has the same terms.
6. Rerun package inventory and release validation after any dependency change.
7. Do not describe an idea-level audit as a security, legal or ATS certification.

## Archive identity limitation

The supplied ZIPs contain no Git metadata or archival commit marker. Their SHA-256 values are recorded in `docs/OPEN_SOURCE_REPO_AUDIT.md`, but the upstream commit is unknown. They must not be treated as pinned dependencies.

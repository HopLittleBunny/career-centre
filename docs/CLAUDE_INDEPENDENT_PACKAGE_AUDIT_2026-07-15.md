# Claude independent package audit — 15 July 2026

Package reviewed: `career-centre-4.0.0-beta.3-claude-plugin.zip`

Final package SHA-256: `511998731e8bea0a67496628830c2ea3f67c8973dc919a387443f077b807327c`

Private review conversation: https://claude.ai/chat/0bd3a121-c7e7-4976-8cab-4a07c2c67194

## Independent verdict before fixes

- Submission worthy: **Yes — submit after two named fixes**.
- Confidence: high.
- Score: **8.5/10 before the fixes**.
- Blockers: none.
- High-severity findings: none.

Claude extracted the actual ZIP, inspected the manifest, main skill, references, schemas, scripts, tests, templates and claims, and ran the package rather than reviewing only its description.

## Final independent verdict after fixes

- Recommendation: **Submit**.
- Confidence: high.
- Final score: **9.5/10**.
- Regressions: none.
- Remaining blocker, high or medium findings: none.

Claude independently inspected the final rebuilt ZIP, executed the three targeted document tests and reran all 62 Claude tests on a pristine extraction. It confirmed that the only final delta was regression-test hardening; product code, references, schemas and privacy files were unchanged from the already verified build.

The final verification specifically passed:

- literal, selectable email in the CV and cover letter;
- the exact `mailto:` relationship in both Word documents;
- no high-impact missing-email finding from the CV reviewer;
- a real shipped reference Word template as the formatting source;
- a synthetic Georgia reference DOCX that transfers font, colour and margins while excluding the reference person's body text, header text and author metadata;
- all 62 Claude tests on a clean tree.

## What Claude independently verified

- Correct Claude plugin root and manifest structure.
- Clean archive without compiled, HTML, macOS metadata or cache artefacts.
- All 62 Claude tests passed on a pristine extraction.
- All referenced files and scripts resolved.
- The full application-pack pipeline generated a real CV DOCX, cover-letter DOCX, evidence-safety report, change log, structural reports and manifest.
- The generated CV rendered to exactly two pages, with page two visibly over 80% filled; the cover letter rendered to one page.
- The document validator caught an injected 7pt private-use Wingdings bullet.
- Evidence provenance, market localisation, exact-posting release gates, manual-submission boundary, Passport continuity and consent-gated Cowork scheduling were implemented rather than merely described.

## Finding 1 — MEDIUM — fixed

The generated header used the visible label `Email` for a `mailto:` hyperlink. The qualitative reviewer could not detect the literal address in selectable text and raised a high-impact missing-email finding on every generated CV. This also weakened compatibility with text-only ATS parsers.

Fix:

- `build_application_pack.py` now renders the literal email address as visible hyperlinked text in both the CV and cover letter.
- Descriptive text such as `LinkedIn` remains descriptive rather than exposing a raw profile URL.
- The document-builder test now verifies that the literal email is selectable and that the qualitative reviewer detects it without a high-impact contact finding.
- The same regression test directly asserts that the exact `mailto:` relationship survives in both generated Word documents.
- The fix is mirrored in the ChatGPT and Claude packages.

## Finding 2 — LOW — fixed

The manifest named Amit Sharma as author while the homepage and repository used the `HopLittleBunny` GitHub owner. A marketplace reviewer could reasonably ask whether these identities are connected.

Fix:

- The package README and repository README now state that Amit Sharma publishes Career Centre through his `HopLittleBunny` GitHub account.

## Non-defects not changed

- The long but targeted skill description was explicitly judged acceptable for routing.
- Contact/phone diagnostic limitations shared the same root cause as finding 1 and required no separate redesign.
- No paid backend, cross-chat memory promise or directory-availability claim was added.

## Release conclusion

The final beta.3 Claude ZIP is ready for resubmission. This audit records product readiness; it does not claim that the updated version has already been resubmitted or approved by Anthropic.

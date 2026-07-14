# Live submission status

Checked on 14 July 2026 after the exact beta.2 replacement smoke test.

## OpenAI

- The signed-in OpenAI Platform plugin dashboard is reachable and organization settings show verification as **Verified**.
- **Create plugin → Skills only** is the correct package route.
- The final package passes both 56-test suites, submission-ready repository validation, skill quick-validation and the current plugin-creator validator.
- The portal accepts ZIP selection but returns only `Plugin upload failed` for the full plugin bundle. The skill-only ZIP returns the expected specific `Plugin manifest not found` error, confirming that the full-plugin route is correct.
- Canonical top-level homepage, repository and publisher URL metadata were added and revalidated; the portal still returns the same generic error.
- No OpenAI draft or submission was created. Treat this as a portal-side or undocumented-ingestion blocker and use OpenAI support rather than weakening the validated runtime package without evidence.

## Anthropic

- The exact Claude beta.2 ZIP was replacement-uploaded on Max web and showed `Career Centre is installed and ready to use` with `Last updated: Just now`.
- A fresh ordinary chat passed natural auto-routing, synthetic CV diagnosis, compact follow-up questions, explicit setup-only/no-search/no-files restraint, the exact seven-line readiness receipt, advanced field preferences and a 390 px mobile check.
- The signed-in Claude Platform directory form is reachable and explicitly targets Claude Code and Claude Cowork.
- A Cowork-only draft now contains the repository, plugin subdirectory, homepage, description, examples, Apache-2.0 licence, privacy URL and account contact email.
- The account-holder consent to Anthropic contact, Privacy Policy and Software Directory Terms remains unchecked. **Submit for review** was not pressed.
- The plugin remains publicly installable for normal Claude web chat through the GitHub marketplace `HopLittleBunny/career-centre` and the validated beta.2 ZIP.
- Next action: separately test the selected Cowork surface, then have the account holder review and explicitly accept the legal consent before the final submission.

These access gates do not change the product packages, public repository, marketplace manifest, website or direct-install availability.

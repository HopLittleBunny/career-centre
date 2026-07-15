# Live submission status

Checked on 14 July 2026 after the exact beta.2 replacement smoke test and successful OpenAI draft creation.

## OpenAI

- The signed-in OpenAI Platform plugin dashboard is reachable and organization settings show verification as **Verified**.
- The selected organization is **Amit Sharma**. People & Permissions confirms Amit Sharma is the **Owner** and the organization is the default organization.
- OpenAI's submission documentation states that organization owners automatically have both `api.apps.write` and `api.apps.read`; creation of the real draft functionally confirms write access.
- **Create plugin → Skills only** is the correct package route.
- The final package passes both 56-test suites, submission-ready repository validation, skill quick-validation and the current plugin-creator validator.
- A dedicated portal archive now places `.codex-plugin/plugin.json` at ZIP root while retaining the normal folder-prefixed marketplace archive. Both layouts were tested.
- Client-side validation is working: an intentionally incomplete control returns precise missing-icon errors and a 24×24 SVG returns the precise 48×48 minimum-dimension error.
- Historical clean-preflight attempts with both the full bundle and a four-file OpenAI-scaffolded control returned only `Plugin upload failed`, while the portal logged missing `org_id` scoping.
- After the authenticated Help Center/support flow and a fresh Platform session, the unchanged production archive uploaded successfully and created a real **Career Centre** draft. This resolves the upload blocker without weakening the package.
- Plugin information is saved, all three prompts are present, and the `career-centre` skill is imported. The remaining portal blocker is the automated skill scan, which must complete before policy attestations and final submission can proceed.

## Anthropic

- The account holder reports that the Claude plugin has now been submitted.
- The exact Claude beta.2 ZIP was replacement-uploaded on Max web and showed `Career Centre is installed and ready to use` with `Last updated: Just now`.
- A fresh ordinary chat passed natural auto-routing, synthetic CV diagnosis, compact follow-up questions, explicit setup-only/no-search/no-files restraint, the exact seven-line readiness receipt, advanced field preferences and a 390 px mobile check.
- The signed-in Claude Platform directory form is reachable and explicitly targets Claude Code and Claude Cowork.
- A Cowork-only draft now contains the repository, plugin subdirectory, homepage, description, examples, Apache-2.0 licence, privacy URL and account contact email.
- The earlier consent blocker is resolved by the account holder's completed submission. Directory review outcome is still pending unless Anthropic reports otherwise.
- The plugin remains publicly installable for normal Claude web chat through the GitHub marketplace `HopLittleBunny/career-centre` and the validated beta.2 ZIP.
- Next action: separately test the selected Cowork surface, then have the account holder review and explicitly accept the legal consent before the final submission.

These access gates do not change the product packages, public repository, marketplace manifest, website or direct-install availability.

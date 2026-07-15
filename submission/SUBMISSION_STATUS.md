# Live submission status

Checked on 15 July 2026 after the beta.3 release validation, OpenAI beta.2 approval and Claude beta.3 directory resubmission.

## OpenAI

- Career Centre version **4.0.0-beta.2** is **Approved** in the OpenAI Platform portal and visible in ChatGPT's Plugins directory.
- The signed-in OpenAI Platform organization settings previously showed verification as **Verified**.
- The selected organization is **Amit Sharma**. People & Permissions confirms Amit Sharma is the **Owner** and the organization is the default organization.
- OpenAI's submission documentation states that organization owners automatically have both `api.apps.write` and `api.apps.read`; creation of the real draft functionally confirms write access.
- **Create plugin → Skills only** is the correct package route.
- The final package passes both 56-test suites, submission-ready repository validation, skill quick-validation and the current plugin-creator validator.
- A dedicated portal archive now places `.codex-plugin/plugin.json` at ZIP root while retaining the normal folder-prefixed marketplace archive. Both layouts were tested.
- Client-side validation is working: an intentionally incomplete control returns precise missing-icon errors and a 24×24 SVG returns the precise 48×48 minimum-dimension error.
- Historical clean-preflight attempts with both the full bundle and a four-file OpenAI-scaffolded control returned only `Plugin upload failed`, while the portal logged missing `org_id` scoping.
- After the authenticated Help Center/support flow and a fresh Platform session, the unchanged production archive uploaded successfully and created a real **Career Centre** draft. This resolves the upload blocker without weakening the package.
- The approved beta.2 listing contains the three prompts and the `career-centre` skill.
- The final beta.3 OpenAI upload archive passes 61 tests and submission-ready validation. Resubmission is pending only because the current Platform browser token was invalidated and requires a fresh sign-in before the upload can be completed.

## Anthropic

- The beta.3 public-directory submission was sent through the signed-in Claude Platform form on 15 July 2026. The portal confirmed: **Plugin submitted for review**.
- The submitted source is `https://github.com/HopLittleBunny/career-centre`, path `plugins/claude-career-centre`, with Claude Code and Claude Cowork selected.
- The exact Claude beta.2 ZIP was replacement-uploaded on Max web and showed `Career Centre is installed and ready to use` with `Last updated: Just now`.
- A fresh ordinary chat passed natural auto-routing, synthetic CV diagnosis, compact follow-up questions, explicit setup-only/no-search/no-files restraint, the exact seven-line readiness receipt, advanced field preferences and a 390 px mobile check.
- The signed-in Claude Platform directory form is reachable and explicitly targets Claude Code and Claude Cowork.
- The submission contains the repository, plugin subdirectory, homepage, description, examples, Apache-2.0 licence, privacy URL and account contact email.
- Directory review outcome is pending unless Anthropic reports otherwise.
- The plugin remains installable for normal Claude web chat through the GitHub marketplace `HopLittleBunny/career-centre` and the validated beta.3 ZIP.

These access gates do not change the product packages, public repository, marketplace manifest, website or direct-install availability.

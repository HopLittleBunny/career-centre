# Claude beta.2 browser and submission audit

Date: 14 July 2026 (Australia/Perth)

## Package under test

- Claude ZIP: `release/career-centre-4.0.0-beta.2-claude-plugin.zip`
- SHA-256: `b28d0938cfbd58b93e72d7efc627e76e1f1102d2e68d15ed71651e927c5de687`
- Automated package tests: 56/56 passing in both provider trees
- Repository release validation: submission-ready mode passed with zero errors and zero warnings

## Live Claude Max result

The exact beta.2 ZIP was replacement-uploaded through **Customize → Plugins**. Claude showed `Career Centre is installed and ready to use`, `Last updated: Just now`, one `/career-centre` skill and the expected Amit Sharma publisher identity.

The fresh ordinary web-chat journey passed without a slash command:

1. `Help me find my next role.` auto-routed to Career Centre and asked warmly for one CV or several role-track versions.
2. A pasted synthetic senior-transformation CV plus an explicit `setup only`, `do not search`, `do not create files` boundary produced:
   - a specific `What I understood` summary;
   - a constructive, non-scored `Quick CV read`;
   - evidence-safe distinctions between scale, outcomes and unsupported overreach;
   - only the remaining material questions;
   - no search and no file creation.
3. The answers produced exactly seven readiness labels in the required order: `Target`, `Geography`, `Sources`, `Compensation`, `CV`, `Sections`, `Application pack`.
4. The receipt explicitly included two pages, page 2 at least 80% filled, 9 pt minimum, the section plan, Word CV plus one-page Word cover letter and manual submission.
5. The receipt offered `change my advanced preferences` and gave the one-time continuity warning about keeping one main conversation and saving the Career Passport.
6. Advanced preferences for Australian English, phone visibility, LinkedIn, headline preservation and conditional project ordering were understood in ordinary language and their practical effects were explained without exposing a schema.
7. At a 390×844 viewport, the conversation remained readable and measured `scrollWidth = clientWidth = 390`, with no horizontal overflow.

## UX judgement

- Conversation quality: 9.3/10 for the tested onboarding journey.
- Claude installation and conversation readiness remains 9.1/10 because live-role, Word-pack, reference-format and Cowork continuity parity are still open.
- The first reply was materially cleaner after adding an explicit instruction not to inspect unrelated prior chats, projects, connectors or files when no CV or Passport is present.
- Claude's own visible reasoning-status captions remain provider-controlled and are not part of the plugin output.

## Submission portals

### Anthropic

The Claude Platform directory form is explicitly for Claude Code and Claude Cowork. A Cowork-only draft was prepared with the repository, plugin subdirectory, homepage, listing copy, examples, Apache-2.0 licence, privacy URL and account contact email. The final action was not taken because:

- Cowork parity has not yet been separately exercised; and
- the introduction requires the account holder to authorize contact and accept Anthropic's Privacy Policy and Software Directory Terms.

No legal checkbox was selected and **Submit for review** was not pressed.

### OpenAI

The organization settings page shows developer verification as `Verified`. The final ChatGPT plugin passes the current local plugin-creator validator, both 56-test suites and repository submission validation. The Platform portal nevertheless returns only `Plugin upload failed` for the full plugin ZIP. A skill-only ZIP produces the expected specific error that a plugin manifest is required, confirming that the correct full-plugin route is being used. Adding canonical top-level homepage, repository and publisher URL metadata did not change the generic portal failure.

This is recorded as a portal-side or undocumented-ingestion blocker, not as a successful OpenAI submission and not as evidence that the validated package is malformed.

## Screenshot evidence

- `04-claude-beta2-installed.png` — exact ZIP installed, enabled and updated just now
- `05-beta2-natural-entry.png` — automatic natural-language routing
- `06-beta2-cv-review.png` and `07-beta2-questions-stop-boundary.png` — CV diagnosis and compact questions
- `09-beta2-readiness-assumptions.png` — seven readiness assumptions
- `11-beta2-advanced-preference-list.png` — field and format controls
- `12-beta2-mobile-conversation.png` — 390 px mobile rendering
- `14-claude-submission-draft.png` — Cowork-only Anthropic draft
- `15-openai-upload-generic-failure.png` — OpenAI portal blocker

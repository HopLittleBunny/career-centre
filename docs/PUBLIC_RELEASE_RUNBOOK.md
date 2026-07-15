# Public release runbook

This runbook closes the remaining zero-cost public release gates without adding a publisher-operated backend.

## Current release position

- Functional beta: 9.2/10.
- ChatGPT public-beta readiness: 9.3/10.
- Claude installation and conversation readiness: 9.1/10.
- Personal ChatGPT Pro web and Claude Max web: passed for their documented acceptance journeys.
- Automated tests: 56/56 passing in each provider package.
- Draft release validation: passing.
- Direct skill ZIP: accepted by ChatGPT and included in `public-site/downloads/`.
- Static site: live at <https://hoplittlebunny.github.io/career-centre/> and browser-verified at desktop and mobile widths.
- Public repository, support route and tagged beta release: live at <https://github.com/HopLittleBunny/career-centre>.
- Remaining external gates: OpenAI and Anthropic directory review, personal ChatGPT Plus verification, another eligible Claude plan and the remaining Claude parity journeys.

## Publisher identity

The user approved `HopLittleBunny` as the public GitHub publisher. Product manifests, listing copy and the site identify Amit Sharma as the developer. OpenAI and Anthropic account-level identity or business-verification fields must still be completed accurately by the account holder; do not infer or attest to them automatically.

## Free GitHub Pages path — completed

The public repository, GitHub Pages deployment and issue-based support route are live. Recheck these paths before each submission:

1. Confirm these pages return HTTP 200 over HTTPS:
   - `/`
   - `/install.html`
   - `/privacy.html`
   - `/terms.html`
   - `/support.html`
   - `/release-notes.html`
   - `/downloads/career-centre-chatgpt-skill.zip`
   - `/downloads/career-centre-claude-plugin.zip`
2. Confirm the ChatGPT skill download checksum is `4c39969fb59611108dc1cd014cf3321e5c927da9c8b1282a1f2ddfaf49336e69`.
3. Confirm the Claude download checksum is `b28d0938cfbd58b93e72d7efc627e76e1f1102d2e68d15ed71651e927c5de687`.

A custom domain is optional. The free `github.io` URL is sufficient for a first public release.

## Verify the public release fields

After the site is live:

1. Confirm the support page opens the repository's public issue form.
2. Confirm the live website, support, privacy and terms URLs in `submission/LISTING.md`.
3. Confirm these HTTPS fields in `plugins/career-command-centre/.codex-plugin/plugin.json`:
   - `interface.websiteURL`
   - `interface.privacyPolicyURL`
   - `interface.termsOfServiceURL`
4. Run the submission-ready validator again after any URL change.
5. Run:

   ```bash
   python3 scripts/validate_release.py --submission-ready
   ```

The command must return `passed: true` with no warnings.

## Rebuild the directory package

Public URL changes modify the plugin manifest, so the directory plugin ZIP must be rebuilt after those edits.

1. Bump the prerelease version.
2. Run both 56-test suites.
3. Run draft and submission-ready validation.
4. Run `python3 scripts/package_release.py` and `python3 scripts/package_claude_release.py`.
5. Confirm `release/LATEST.json` and `release/CLAUDE_LATEST.json` match the new ZIP checksums.
6. Replacement-upload the final skill ZIP to personal ChatGPT Pro and the final plugin ZIP to Claude.
7. Repeat one natural CV-first smoke test and one explicit setup-only/no-search preview on each provider.

## OpenAI directory submission

Submit only after the publisher identity and public URLs are consistent.

Use the prepared materials in:

- `submission/LISTING.md`
- `submission/RELEASE_NOTES.md`
- `submission/REVIEWER_TEST_CASES.json`
- `submission/SUBMISSION_CHECKLIST.md`

Keep the initial package skills-only. Do not add an MCP server, external authentication, model API or publisher CV database.

The final submission action includes publisher representations and attestations. Populate and review the draft, but obtain the account holder's explicit confirmation before selecting **Submit for review**.

## Anthropic directory submission

The repository includes a native Claude package, the root `.claude-plugin/marketplace.json` manifest and a locally validated beta.2 ZIP. The exact beta.2 ZIP has passed replacement upload and the guided Max-web journey. The current Platform directory form targets Claude Code and Claude Cowork; keep the prepared Cowork-only draft unsubmitted until Cowork parity is separately exercised and the account holder accepts the Privacy Policy and Software Directory Terms. Run `claude plugin validate` if the current Claude developer tooling becomes available.

## Personal Plus acceptance

After the listing is available to another account:

1. Install from the directory on a personal Plus account.
2. Start a normal conversation without a Project or explicit skill mention.
3. Run CV-first setup using a synthetic CV.
4. Verify the readiness receipt, global assumptions and advanced-preference update.
5. Assess one exact open role without creating documents.
6. Create one paired Word pack and inspect every page.
7. Preview a schedule and confirm it says `Snapshot-backed` rather than claiming cross-run memory.
8. Submit nothing and remove any temporary schedule after the account owner approves deletion.

## Claude parity phase

Packaging, upload, ordinary-chat auto-routing, mentor reflection, the seven-line receipt and the setup-only/no-search boundary pass on Claude Max web. Before claiming full parity, verify one exact live role assessment, a rendered paired Word pack, reference-format evidence isolation, two Cowork schedule executions and another eligible paid plan. Do not carry over ChatGPT-specific schedule or file claims without separate Claude evidence.

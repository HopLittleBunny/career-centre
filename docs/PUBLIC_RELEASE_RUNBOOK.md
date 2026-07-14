# Public release runbook

This runbook closes the remaining zero-cost public release gates without adding a publisher-operated backend.

## Current release position

- Functional beta: 9.2/10.
- Public-release readiness: 8.9/10.
- Personal ChatGPT Pro web: passed.
- Automated tests: 44/44 passing.
- Draft release validation: passing.
- Direct skill ZIP: accepted by ChatGPT and included in `public-site/downloads/`.
- Static site: complete and browser-verified at desktop and mobile widths.
- Still blocked: publisher-matched public hosting identity, live support route, OpenAI directory review and personal Plus verification.

## Publisher identity gate

The currently authenticated GitHub account is `HopLittleBunny`. Its public profile does not expose a name. The plugin manifest and listing identify the developer as Amit Sharma.

Do not publish until one of these is deliberately selected:

1. Use an Amit Sharma GitHub account or organisation that matches the OpenAI developer identity.
2. Use `HopLittleBunny` only after Amit confirms that it is the intended publisher account and updates its public profile or organisation details so the relationship to Amit Sharma is clear.

This choice affects the public URL, support route, reviewer confidence and creator attribution. It must not be guessed.

## Free GitHub Pages path

Once the publisher account is correct:

1. Create a public repository named `career-centre` under that account.
2. Publish the repository and deploy the contents of `public-site/` with the bundled GitHub Pages workflow.
3. Commit and push the static files.
4. Enable GitHub Pages from the repository&apos;s main branch and root directory.
5. Enable repository Issues.
6. Confirm these pages return HTTP 200 over HTTPS:
   - `/`
   - `/install.html`
   - `/privacy.html`
   - `/terms.html`
   - `/support.html`
   - `/release-notes.html`
   - `/downloads/career-centre-chatgpt-skill.zip`
7. Confirm the download checksum is `344b63f16aaa18c7d15cccc60ac29c998abb87f722764e0b2b43ac98d75b2545`.

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
2. Run the 44-test suite.
3. Run draft and submission-ready validation.
4. Run `python3 scripts/package_release.py`.
5. Confirm `release/LATEST.json` matches both new ZIP checksums.
6. Reinstall the local plugin package.
7. Replacement-upload the final skill ZIP to personal ChatGPT Pro.
8. Repeat one natural CV-first smoke test and one side-effect-free schedule-receipt preview.

## OpenAI directory submission

Submit only after the publisher identity and public URLs are consistent.

Use the prepared materials in:

- `submission/LISTING.md`
- `submission/RELEASE_NOTES.md`
- `submission/REVIEWER_TEST_CASES.json`
- `submission/SUBMISSION_CHECKLIST.md`

Keep the initial package skills-only. Do not add an MCP server, external authentication, model API or publisher CV database.

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

## Claude phase

Start Claude packaging only after the ChatGPT public gate is closed. Reuse the provider-neutral career skill, schemas, references, fixtures and document scripts. Do not carry over ChatGPT-specific schedule or installation claims without separate Claude host tests.

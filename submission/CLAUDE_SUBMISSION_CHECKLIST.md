# Anthropic submission checklist

- [x] Public GitHub repository is live.
- [x] Root `.claude-plugin/marketplace.json` is present.
- [x] Native `.claude-plugin/plugin.json` is present in the Claude package.
- [x] Website, support, privacy and terms pages are live over HTTPS.
- [x] Claude ZIP is downloadable and its checksum matches `release/CLAUDE_LATEST.json`.
- [x] Beta.4 package has passed the current 62-test automated suite.
- [ ] Beta.4 has passed a live Cowork `/schedule` handoff smoke test from the submitted build.
- [x] Final beta.2 ZIP has passed Claude Max web replacement upload.
- [x] Natural auto-routing, mentor reflection and readiness receipt pass on beta.3; beta.4 automation expectation and application-pack recovery are covered by the package contract.
- [x] Explicit setup-only/no-search/no-files boundary passes.
- [ ] Run `claude plugin validate` with the current official developer tooling if available.
- [x] Account holder identity and public contact fields are visible in the signed-in Platform form.
- [x] Account holder reviewed the policy, ownership and privacy attestation during the earlier directory submission; the existing checked consent was not altered during beta.4 resubmission.
- [x] Account holder explicitly requested resubmission and the final **Submit for review** action was completed.
- [ ] Directory outcome is recorded without claiming Anthropic Verified status unless separately granted.

Live portal result: the beta.4 GitHub source was submitted for both Claude Code and Claude Cowork. The portal confirmed **Plugin submitted for review**. Directory approval and the live Cowork automation smoke remain pending. See `SUBMISSION_STATUS.md`.

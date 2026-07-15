# Career Centre — Open Door: global provider tests

Test date: 15 July 2026 (Australia/Perth)

These were live browser tests using fictional candidates. No real candidate evidence was used.

## Release status during testing

- ChatGPT `4.0.0-beta.2` is approved, visible and installable in ChatGPT.
- ChatGPT `4.0.0-beta.3` is installed privately for final testing; it has not yet been submitted as a public directory update.
- The Claude plugin has been submitted, according to the submission completed by the owner. Public approval is not yet evidenced in the available UI.
- Claude `4.0.0-beta.3` is installed privately from the release ZIP for final testing.

## Private test conversations

- India / ChatGPT: https://chatgpt.com/c/6a5703af-cdcc-83ec-b1b9-3cb0a0b0a68a
- Australia / ChatGPT: https://chatgpt.com/c/6a5705be-e338-83ec-a427-111524d48921
- United States / Claude: https://claude.ai/chat/a3b2e7aa-182b-44ca-bf7d-4623b33b913b

These links are private account conversations, not public share links.

## Results

### India on ChatGPT

Result: pass with one presentation caveat.

- Gave an initial strengths-and-improvements CV review without a crude numerical score.
- Confirmed India-specific search assumptions and compensation framing, including fixed pay versus variable pay and total CTC.
- Used India-relevant source families and did not treat Australia-only sources as universal.
- Created the Career Passport state and explained single-conversation continuity.
- Offered the calibrated recurring search proactively after the first verified search.
- Exact postings were clickable and open-status checked.
- Caveat: the raw posting URLs were links behind role labels rather than separately printed URL lines in this run. The package contract was tightened immediately afterwards.

Score: 8.8/10 for this live run; 9.1/10 for setup and localisation.

### Australia on ChatGPT

Result: pass.

- Gave a broad CV review and a clear Career Centre readiness receipt.
- Confirmed Australian salary assumptions and Australia-relevant source families.
- Separated listed facts from estimates and employment-type uncertainty.
- Printed the exact posting label and the full visible posting URL for each reviewed role.
- Created a portable Career Passport.
- Asked the exact proactive daily-or-weekdays scheduling question without being prompted to do so.

Score: 9.2/10.

### United States on Claude

Result: pass.

- Used US resume terminology and US spelling.
- Treated base salary, bonus, equity and total compensation as different fields.
- Checked posting currency and excluded an expired result instead of presenting it as open.
- Enforced the stated permanent-role and base-pay gates.
- Printed visible exact posting URLs for reviewed roles.
- Built a reusable evidence-safe Career Passport.
- Asked the Cowork daily-or-weekdays scheduling question proactively, even though the user had said not to create a schedule automatically.

Score: 9.1/10.

## Scheduling verdict

The product now distinguishes between creating a schedule and offering one. After the first completed search with at least one verified role, it asks:

> Would you like me to run this calibrated search daily or on weekdays in this same Career Centre task? If yes, tell me the time and timezone; I will keep the current role limit unless you change it.

Claude uses the same wording with `in Cowork`. The offer is suppressed only when the user explicitly asks not to mention or offer recurring searches.

## Overall assessment

Current private beta: 9.0/10.

The product is submission-worthy as a free, conversation-first career workflow. Its strongest advantages are evidence safety, global localisation, selective role decisions, CV/cover-letter continuity, portable Career Passport state and the recurring-search handoff. It should not be called fully finished until `beta.3` is approved publicly and the daily search is observed across at least two scheduled runs on each provider.

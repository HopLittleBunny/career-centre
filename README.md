# Career Centre

Career Centre is a free, evidence-safe career decision agent packaged as a skills-only ChatGPT plugin. It helps a job seeker move from an uploaded CV and a few natural preferences to selective role recommendations, exact posting links, honest fit commentary, Word application packs and application follow-through.

[Visit the product site](https://hoplittlebunny.github.io/career-centre/) or [open the installation guide](https://hoplittlebunny.github.io/career-centre/install.html).

The plugin is intentionally backend-free. Amit Sharma does not operate a model API, CV database or account system for it. The user's ChatGPT environment performs the reasoning and document work using the user's own plan and product limits.

## The user experience

Say **“Help me find my next role”** and share a CV. Career Centre reads the CV first, reflects back what it understood, asks only the few preference questions that could change the result, and then acts as a continuing career thought partner.

There are no setup cards, commands, projects or state files for the user to maintain.

## Product promise

1. Upload a CV.
2. Answer one compact set of missing high-impact questions.
3. Receive a small number of verified roles worth considering.
4. Ask for an application pack in ordinary language.
5. Receive validated Word documents and keep application history in the same task.

After setup, the plugin says **“Your Career Centre is ready”** and shows the assumptions it will use: target direction, market/geography, work-right boundary, source mix, salary/currency, employment preference, CV page/section plan and manual-submission boundary. The defaults work for most people; advanced preferences stay out of the way until requested.

## Personalisation without setup work

Users can say “change my advanced preferences” to change markets, role sources, search breadth, salary, employment types, CV length, section order, optional sections, visible CV fields, headline/date display, tone, cover-letter behaviour or formatting. A supplied reference Word CV can be used as a visual model while its content and personal data are stripped.

Preferences, corrections, document feedback and application outcomes are retained in a portable Career Passport in the continuing task/local workspace. This creates a transparent learning loop without a publisher-operated memory service.

## What it will not do

- Invent experience, metrics, qualifications or technical depth.
- Recommend `Apply` without an exact, open posting and salary/employment context.
- Treat a CV statement as independently verified.
- Auto-submit applications or send messages on the user's behalf.
- Send CV data to an Amit-operated backend.

## Repository layout

- `plugins/career-command-centre/` — installable plugin.
- `plugins/career-command-centre/skills/career-command-centre/` — provider-neutral workflow, contracts, scripts and evaluations.
- `.agents/plugins/marketplace.json` — local marketplace used for pre-release testing.
- `docs/` — audit, release and evaluation records.
- `submission/` — public-directory listing copy, reviewer cases and release notes.
- `public-site/` — Markdown source for the no-cost public website, legal and support pages.
- `release/` — generated release archives only.

## Local validation

Run from this directory with Python 3.11+ and `python-docx` available:

```bash
python3 plugins/career-command-centre/skills/career-command-centre/scripts/run_tests.py
python3 scripts/validate_release.py
```

The second command performs the repository-level release checks. OpenAI's local plugin validator is also run during author testing.

## Distribution model

The intended public route is OpenAI's universal plugin directory as a **skills-only plugin**. This keeps the publisher's ongoing infrastructure cost at zero: there is no hosted MCP server or paid publisher-side model usage. A free static site can host the website, privacy, terms and support pages needed for review.

Directory visibility does not prove universal installation. OpenAI documents that plugin installation and invocation can depend on plan, workspace, surface, region and included capabilities. Personal Plus/Pro compatibility is therefore a required post-publication test, not a marketing assumption.

The provider-neutral core is also designed for a later Claude plugin. Anthropic currently documents custom plugin upload for paid Pro, Max, Team and Enterprise plans; that packaging and its own 9+ evaluation begin only after the ChatGPT gate closes.

## Current status

Current rating: **9.2/10 functional beta; 8.9/10 public-release readiness**. Version `4.0.0-beta.1` passes all 44 automated tests. Personal ChatGPT Pro web has passed installed multi-turn journeys, a portable-bullet two-page Word pack, natural reference-CV format copying with evidence isolation, lifecycle continuity, schedule creation and live scheduled execution. A two-run browser test proved that ChatGPT launches isolated result tasks and does not carry the prior result's printed Passport into the next run; the product therefore labels browser schedules as snapshot-backed alerts instead of claiming cross-run memory. The no-cost launch site, direct Skill ZIP, checksums, support identity and public source repository are prepared. Remaining external gates are OpenAI directory review and personal Plus compatibility. See `docs/PRODUCT_REVIEW_V4.md`, `docs/ROADMAP.md` and `docs/PUBLIC_RELEASE_RUNBOOK.md`.

## Safety boundary

Career Centre does not auto-submit applications, invent experience, treat CV claims as independently verified, or recommend an Apply decision without an exact role posting and salary/employment context.

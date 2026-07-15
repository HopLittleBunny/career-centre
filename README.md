# Career Centre

Career Centre is a free, evidence-safe career decision agent packaged for ChatGPT and Claude. “Free” means there is no separate Career Centre subscription, API key or publisher-operated backend; the user still needs an eligible ChatGPT or Claude plan and uses that plan's allowance. It helps a job seeker move from an uploaded CV and a few natural preferences to selective role recommendations, exact posting links, honest fit commentary, Word application packs and application follow-through.

[Visit the product site](https://hoplittlebunny.github.io/career-centre/) or [open the installation guide](https://hoplittlebunny.github.io/career-centre/install.html).

The plugins are intentionally backend-free. Amit Sharma does not operate a model API, CV database or account system for them. The user's ChatGPT or Claude environment performs the reasoning and document work using the user's own plan and product limits.

## The user experience

Say **“Help me find my next role”** and share one CV—or the key CVs used for different role directions. Career Centre reads every supplied version first, gives a broad overall-strength verdict and compact qualitative review, reflects back what it understood, asks only the few preference questions that could change the result, and then acts as a continuing career thought partner. A deeper review is optional.

There are no setup cards, commands, projects or state files for the user to maintain.

## Product promise

1. Upload one CV or several role-specific CVs.
2. Answer one compact set of missing high-impact questions.
3. Receive a small number of verified roles worth considering.
4. Ask for an application pack in ordinary language.
5. Receive validated Word documents and keep application history in the same task.

After setup, the plugin says **“Your Career Centre is ready”** and shows the assumptions it will use: target direction, market/geography, work-right boundary, source mix, salary/currency, employment preference, CV page/section plan and manual-submission boundary. The defaults work for most people; advanced preferences stay out of the way until requested.

## Personalisation without setup work

Users can say “change my advanced preferences” to change markets, role sources, search breadth, salary, employment types, CV length, section order, optional sections, visible CV fields, headline/date display, tone, cover-letter behaviour or formatting. A supplied reference Word CV can be used as a visual model while its content and personal data are stripped.

Source CVs, approved evidence, preferences, generated-document versions, corrections, document feedback and application outcomes are retained in a portable Career Passport in the continuing task/local workspace. The first Passport is prepared automatically after setup. This creates a transparent learning loop without a publisher-operated memory service. Users should keep one main Career Centre conversation and save the latest Passport because a separate conversation may not inherit earlier files or history. The plugin package is installed once; it is not uploaded every day.

After the first useful manual role search, Career Centre offers to repeat the calibrated search daily or on weekdays. ChatGPT Work schedules should return to the same task and use its context; Claude recurring work uses Cowork. Application packs remain on request and application submission remains manual.

## What it will not do

- Invent experience, metrics, qualifications or technical depth.
- Recommend `Apply` without an exact, open posting and salary/employment context.
- Treat a CV statement as independently verified.
- Auto-submit applications or send messages on the user's behalf.
- Send CV data to an Amit-operated backend.

## Repository layout

- `plugins/career-command-centre/` — installable plugin.
- `plugins/career-command-centre/skills/career-command-centre/` — provider-neutral workflow, contracts, scripts and evaluations.
- `plugins/claude-career-centre/` — native Claude custom-plugin package using the same evidence-safe core.
- `.claude-plugin/marketplace.json` — public Claude marketplace catalog for repository-based installation.
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

The intended public routes are OpenAI's universal plugin directory and Claude's custom-plugin or marketplace flow. This keeps the publisher's ongoing infrastructure cost at zero: there is no hosted MCP server or paid publisher-side model usage. The free static site hosts the installers, privacy, terms and support pages.

Directory visibility does not prove universal installation. OpenAI documents that plugin installation and invocation can depend on plan, workspace, surface, region and included capabilities. Personal Plus/Pro compatibility is therefore a required post-publication test, not a marketing assumption.

Anthropic documents custom plugin upload and GitHub marketplaces for paid plans. The native Claude beta package has been installed on Claude Max web and auto-routed successfully in a normal conversation; ZIP and repository-marketplace installation paths are both included.

## Current status

Current honest rating after the first real application audit and fresh fictional India/US browser journeys: **8.9/10 for global setup and selective search; 8.8/10 overall product beta**. The approved ChatGPT beta.2 is strong on evidence safety, exact-role decisions, continuity and Word mechanics, but the live DOSCEL stretch pack exposed weak first-review surfacing, repeated CV content and insufficient role-specific writing. That individual CV rated **7.1/10 overall** despite passing openability, bullet, page-count and density checks. Version `4.0.0-beta.3` addresses the surfaced product gaps with a broad intake verdict, automatic Passport handoff, market-localisation rules, explicit compensation basis, post-generation quality ratings and a proactive same-task scheduling offer. Both provider packages pass 60/60 tests, and fresh India/US Claude setup and manual-search journeys pass. It remains an update candidate until ChatGPT beta.3 is smoke-tested in Work and submitted. See `docs/GLOBAL_BETA_TEST_RESULTS_2026-07-15.md`, `docs/PRODUCT_REVIEW_V4.md`, `docs/ROADMAP.md`, `docs/CLAUDE_COMPATIBILITY.md`, `docs/OPEN_SOURCE_REPO_AUDIT.md` and `docs/PUBLIC_RELEASE_RUNBOOK.md`.

The dated job-source, competitor, mentor-voice, submission and website assessment is in `docs/ECOSYSTEM_BENCHMARK.md`.

## Safety boundary

Career Centre does not auto-submit applications, invent experience, treat CV claims as independently verified, or recommend an Apply decision without an exact role posting and salary/employment context.

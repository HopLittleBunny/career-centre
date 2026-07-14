# Career Centre ecosystem benchmark

Assessment date: 14 July 2026

## Verdict

Career Centre should be positioned as a **selective career decision system and evidence-safe mentor**, not as another high-volume resume writer or one-click application tool. It is unusually strong at judgment, candidate evidence safety, exact-posting discipline, Word-quality gates, transparent assumptions and portability. Dedicated career SaaS products remain stronger at proprietary job feeds, browser clipping, visual tracking, analytics and application autofill.

Current honest ratings:

| Surface | Rating | Basis |
| --- | ---: | --- |
| Core functional beta | 9.2/10 | Complete provider-neutral contracts, evidence model, decisions, Word QA, portable state and fail-closed recovery |
| ChatGPT public-beta readiness | 9.3/10 | Installed browser journeys, document and schedule evidence, live site/repository/downloads; directory and Plus tests still open |
| Claude installation and conversation readiness | 9.1/10 | Final ZIP upload, normal-chat routing, mentor reflection, readiness receipt and explicit no-search/no-files boundary pass |
| Full Claude feature parity | 8.8/10 | Live-role, Word-pack, reference-format and two-run Cowork schedule tests remain |
| Public website versus polished AI career SaaS | 8.8/10 | Clear, fast, responsive and credible; still lacks a short demo, user-outcome evidence and interactive product proof |

## Job-source strategy

Career Centre must work when no job-board plugin is installed. The source ladder is:

1. Exact employer or applicant-tracking-system posting as the canonical source.
2. Authorised recruiter posting when the recruiter owns the vacancy.
3. Major market job boards for discovery, reconciled back to the canonical posting where possible.
4. Public-sector or specialist boards when relevant to the candidate and market.
5. Credible salary benchmarks only for clearly labelled estimates.

The product does not claim an authenticated connection merely because a provider can browse a public result. If a board blocks access, it uses the employer or ATS page, asks the user for an exact saved link, or states the limitation. It never bypasses access controls or fabricates freshness.

### Current provider-directory findings

These are dated observations from the signed-in ChatGPT and Claude directories, not permanent claims about future availability.

| Source | ChatGPT directory | Claude directory | Recommendation |
| --- | --- | --- | --- |
| Indeed | No exact official plugin surfaced | Official Indeed connector surfaced with `search_jobs` and `get_job_details` | Optional for eligible Claude users after Career Centre setup; the core must still verify exact postings |
| LinkedIn Jobs | No exact official jobs plugin surfaced | No official LinkedIn Jobs connector surfaced | Use public/canonical role links where accessible; do not recommend unrelated ads, social or scraping tools |
| SEEK | No exact official plugin surfaced | No official connector surfaced | Use public role links and employer/ATS postings; do not imply a direct integration |

Indeed documents its Claude MCP connector at [Indeed MCP documentation](https://docs.indeed.com/mcp). SEEK's published API is aimed at approved recruitment-software and hirer workflows rather than public candidate search; see [SEEK API](https://developer.seek.com/). LinkedIn's published Talent Solutions APIs centre on approved job-posting and applicant workflows rather than a general candidate-search connector; see [LinkedIn Apply Connect](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect/create-apply-connect-jobs?view=li-lts-2026-03). Indeed's Job Sync API is similarly an ATS job-posting integration, separate from its Claude connector; see [Indeed Job Sync API](https://docs.indeed.com/job-sync-api).

## Competitor benchmark

| Product | What it does especially well | What Career Centre should learn | Career Centre advantage |
| --- | --- | --- | --- |
| Teal | Resume builder, job tracker, browser extension, keyword matching and application organisation in one visual product | Make the candidate's current stage and next action easier to see; publish a concise sample role card | No separate service account or Career Centre subscription; stronger evidence provenance and mentor trade-offs |
| Huntr | Job clipping, autofill, tracker, tailored resumes and application packs | Add a simple portable summary view without building a publisher database | More selective decisions; no auto-apply pressure; Word-density and evidence-safety gates |
| Simplify | High-volume job discovery, Copilot extension and application workflow | Reduce friction between finding a role and assessing it, while retaining the manual-submit boundary | Better fit/risk judgment and no need to optimise for application volume |
| Careerflow | Unified job search, job tracking, extension and career-tool suite | Explain source coverage and geographic limits clearly | Global-by-design assumptions rather than a fixed market; no publisher CV store |
| Rezi | Mature ATS resume workflow, scoring, templates and provider integrations | Make reference-format and section personalisation more visible in the demo | Career guidance, role decisions, exact-link gates and portable learning are one coherent conversation |

Official product references: [Teal pricing and features](https://www.tealhq.com/pricing), [Huntr pricing and features](https://huntr.co/pricing), [Simplify features and pricing](https://help.simplify.jobs/articles/5623502-whats-included-in-simplify-features-and-pricing), [Careerflow job search](https://www.careerflow.ai/job-search), [Careerflow job-portal availability](https://help.careerflow.ai/en/articles/11525851-getting-started-job-portal), [Rezi](https://www.rezi.ai/) and [Rezi MCP changelog](https://www.rezi.ai/rezi-changelog).

Career Centre should not copy competitors' broadest claim. Its sharper promise is:

> Share your CV once. Get candid career judgment, a small number of roles worth your time, and evidence-safe Word applications—inside the AI service you already use.

## Mentor and friend behaviour

The conversation contract now requires a consistent four-part progression:

1. **Orientation:** explain what the candidate's evidence suggests, in plain language.
2. **Tension or trade-off:** name the real choice, stretch or risk instead of producing generic encouragement.
3. **Recommendation:** say what the product would prioritise and why. Every role assessment begins with **My recommendation**.
4. **One concrete next move:** make the next action obvious without turning the answer into a task dump.

The voice is a candid, calm and respectful career mentor: warm enough to feel human, direct enough to be useful. Facts, inferences and judgment are distinguished. The product avoids fake cheerleading, generic “your skills align” language, unexplained scores and long lists without prioritisation.

## Submission route

### ChatGPT

OpenAI supports skills-only plugin submissions. The prepared package already includes the public listing information, site, support, privacy, terms, release notes, exactly five positive and three negative reviewer cases, manifests and final ZIP. The remaining steps are account-level developer identity or business verification, draft completion, attestation review and final submission. See [OpenAI plugin submission guidance](https://developers.openai.com/codex/submit-plugins).

The final **Submit for review** action should only occur after the account holder checks every representation and explicitly confirms submission. Directory placement and enhanced distribution remain OpenAI decisions and cannot be guaranteed.

### Claude

Anthropic accepts a public GitHub repository or plugin ZIP. The repository includes the native manifest and a root GitHub marketplace, so users can install before directory approval by adding `HopLittleBunny/career-centre`. See [Claude plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) and [Submit a plugin](https://claude.com/docs/plugins/submit).

The remaining submission work is account-level form completion, validation with current Claude developer tooling where available, attestation review and explicit approval immediately before submission. Directory inclusion and Anthropic Verified status are separate decisions and cannot be promised.

## Website and mobile assessment

The current static site is appropriate for a free reputation-building product: no operating bill, no account system, fast loading, direct downloads, visible checksums and clear privacy boundaries. It has passed 390 px mobile and 1440 px desktop overflow checks.

The highest-value refinements after directory submission are:

1. Add a 45–60 second captioned demo: CV → candid career thesis → readiness receipt → selective role card → Word pack.
2. Add one compact, synthetic “mentor judgment” example so the differentiation is visible before installation.
3. Add a provider status panel showing tested plans, directory state and optional source connectors without implying universal access.
4. Run a 10–20 person global pilot and publish only consented, anonymised outcome evidence.
5. Add lightweight release analytics only if they can be privacy-preserving and do not create a publisher CV database.

Do not add an elaborate dashboard merely to resemble the paid products. The simple conversational shell is the strategic advantage; visual proof should explain it, not replace it.

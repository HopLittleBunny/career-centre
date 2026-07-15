# Final Claude review prompt — Career Centre — Open Door

Attach the latest `career-centre-4.0.0-beta.3-claude-plugin.zip`, then paste the prompt below into a new Claude conversation.

---

You are the final independent product, safety and Claude-plugin submission reviewer for the attached **Career Centre — Open Door 4.0.0-beta.3** plugin ZIP.

Review the files and executable behaviour in the attached ZIP itself. Do not evaluate only this explanation, and do not assume a feature exists merely because it is listed below. Inspect the manifest, main skill, references, schemas, scripts, tests, templates, README, privacy boundaries and release claims. Run the shipped tests and the smallest useful end-to-end checks when your environment permits.

## Product purpose

Career Centre is intended to give an ordinary, non-technical job seeker a thoughtful career partner inside a normal Claude browser conversation. The user should not need to create a Project, learn commands, configure an API key, maintain a database or pay the publisher a subscription. They should use their own eligible Claude plan and product allowance.

The publisher should not operate a CV database, account system or paid model backend. Career Centre should therefore be useful without pretending it has universal cross-chat memory or guaranteed access to every job site. Durable continuity should come from one continuing conversation plus a transparent, downloadable Career Passport that the user controls.

The product is deliberately **not** an auto-application bot. It should help the user make better decisions, create stronger evidence-safe materials and maintain momentum, while every final application remains a manual user decision.

## Intended user experience

### 1. Natural, low-effort setup

The user can begin with ordinary language such as “Help me find my next role.” Career Centre should warmly ask for one CV or several relevant CVs if the person targets different role families. It should not begin with a long technical questionnaire.

After reading the supplied material, it should ask only the small number of high-impact questions that could materially change results, such as target direction, geography, work rights, compensation basis or floor, employment type and genuine exclusions. Reasonable defaults should be inferred and reflected back for confirmation.

### 2. Humane initial CV review

Before rushing into role search or document rewriting, Career Centre should give a compact qualitative review:

- an overall strength description such as strong, solid but under-positioned, or needing rebuilding;
- what already works;
- what may be underselling the candidate;
- the highest-priority next edit; and
- an offer to provide a deeper review if wanted.

This must not be presented as a universal ATS score. A more detailed diagnostic may discuss writing, structure and parseability, but should remain transparent about its limits.

### 3. Clear readiness receipt

Once setup is complete, it should say **“Your Career Centre is ready”** and show the important assumptions in a compact form:

- target direction and seniority;
- geography, work rights and remote/hybrid boundary;
- job-source families it expects to use;
- compensation floor and whether it refers to base, fixed pay, total package, CTC or another local basis;
- preferred employment type and exclusions;
- CV length and density expectation;
- planned CV sections; and
- the normal application-pack and manual-submission boundary.

Experienced candidates should normally receive a two-page Word CV with page two at least 80% filled and no font below 9pt. An early-career candidate may be better served by one strong page. Defaults should work for most users; advanced configuration should remain optional.

### 4. Career Passport and evidence safety

Career Centre should create a portable Career Passport after setup. It should preserve:

- supplied source documents;
- evidence claims and provenance;
- whether evidence is source-only, user-confirmed or externally corroborated;
- confirmed preferences and corrections;
- reviewed-role history and decisions;
- generated-document versions and status;
- application outcomes and useful feedback where supplied.

It must never upgrade exposure to expertise, participation to leadership, an internal outcome to an external market result, or a CV statement to independently verified fact. It must never invent employers, roles, qualifications, tools, certifications, metrics, work rights or technical depth.

The Passport is a user-controlled continuity file, not a claim of publisher memory. A new conversation may not inherit earlier files or history unless the user supplies the latest Passport or the provider demonstrably preserves that context.

### 5. Global localisation

The product must not inherit Australian assumptions globally.

- In India, distinguish fixed compensation, variable compensation, current/expected CTC and take-home implications; use locally relevant source families such as employer sites, LinkedIn India, Naukri, foundit or specialist boards when appropriate.
- In the United States, distinguish base salary, bonus, equity and total compensation and use US resume terminology and work-authorisation conventions.
- In Australia, distinguish base salary from superannuation and use Australian work-rights and employment conventions.
- In other markets, infer the correct local terminology, privacy norms, spelling, document conventions and source mix instead of forcing one country’s defaults.

Sensitive or bias-prone personal fields such as age, date of birth, marital status, caste, religion, government identifiers or photos should not be requested or included by default.

### 6. Selective, verifiable job search

Career Centre should prefer quality over volume. It should use an honest source ladder, normally favouring:

1. exact employer career or ATS postings;
2. official government or institutional portals;
3. reputable professional and local job boards;
4. aggregators for discovery, followed by resolution to the exact posting where possible.

Every displayed role must include a human-readable company-and-role label and the full visible exact posting URL. Hidden citations, generic search pages, company careers homepages, job IDs without URLs or unverified links are insufficient.

Before recommending Apply, it should verify that the posting appears open, check duplicates and prior decisions, distinguish listed salary from an evidence-based estimate, identify employment type, and reject roles that fail confirmed hard gates. It should never use scraping, bypass or restricted-access language.

### 7. Meaningful role decisions

For each displayed role, Career Centre should provide a transparent Apply, Maybe or Skip recommendation with:

- relevant role track;
- fit score and cautious shortlist-chance estimate;
- salary or compensation range and basis;
- employment type;
- exact posting and URL;
- recruiter/contact if listed;
- strongest match;
- principal risk;
- tailored CV angle;
- recommended CV base;
- tracker recommendation; and
- a clear reason when skipped.

The commentary should sound like a candid career mentor, not a robotic scoring system or an endlessly enthusiastic AI assistant. It should be willing to say that a role is attractive but strategically wrong, too junior, too risky or not worth the application effort.

### 8. Evidence-safe Word application packs

When the user requests an application pack for a verified role, Career Centre should normally produce:

- a tailored Word DOCX CV;
- a persuasive one-page Word DOCX cover letter unless the user asks for CV only;
- an evidence-safety report;
- a change log;
- keywords deliberately included;
- keywords omitted because evidence is weak or absent; and
- structural and rendered QA evidence.

The generated contact header should keep the literal email address visible and selectable while preserving useful hyperlinks. LinkedIn may remain descriptive linked text. Documents should use real bullets, consistent hierarchy, compact spacing, portable fonts and no private-use or legacy Wingdings glyphs.

If the user explicitly supplies a reference Word CV, Career Centre may distil its visual system—such as type hierarchy, colour, margins and spacing—but must not copy the reference person’s wording, identity, metadata or evidence. Reference-format mode should never be forced proactively.

If Word generation is unavailable or fails, the product should provide the complete tailored CV in chat as an explicitly labelled partial fallback rather than silently doing nothing.

### 9. Recurring-search handoff

After the first completed manual search containing at least one verified role, Career Centre should proactively ask whether the user wants the calibrated search to run daily or on weekdays in Cowork. It must not create recurring work without explicit consent, time and timezone.

“Do not create a schedule” should prevent creation but should not suppress the offer. Only an explicit instruction not to mention or offer recurring searches should suppress it.

The recurring-search prompt should preserve the confirmed role limit and constraints, include enough Passport snapshot context to operate safely, reject already-seen duplicates where that snapshot permits, and clearly disclose snapshot-only continuity when persistent read/write storage is not demonstrably available. It must never auto-apply.

### 10. Privacy and commercial intent

Career Centre is intended to be free in the precise sense that it has:

- no separate Career Centre subscription;
- no publisher-supplied model credits;
- no publisher-operated CV database;
- no API key requested from the user; and
- no paid backend required for core operation.

The user still needs an eligible Claude plan and remains subject to Claude’s own limits and terms. The plugin must not claim broader directory, plan, region, job-source or memory availability than the provider actually supports.

## Known pre-final-audit fixes to verify

An earlier independent audit found no blockers or high-severity defects, but identified two narrow issues. Verify that both are now genuinely resolved:

1. A `mailto:` contact item previously displayed only the word `Email`, causing the text diagnostic and some text-only ATS parsers to miss the address. Confirm the literal email is now visible, selectable and hyperlinked in both generated CV and cover letter, and that the qualitative reviewer no longer raises a high-impact missing-email finding.
2. The package named Amit Sharma as author while using the `HopLittleBunny` repository owner. Confirm the README now explains that Amit Sharma publishes the project through his `HopLittleBunny` GitHub account.

## Required audit method

- Validate the ZIP root, manifest and declared version first.
- Inspect every file directly referenced by the main skill.
- Run all shipped tests on a pristine extraction with bytecode writing disabled or clear generated caches before judging archive cleanliness.
- Trace first use, deeper CV review, Passport creation, search, role assessment, application-pack generation, reference-format mode, recurring-search handoff and recovery behaviour.
- Generate at least one synthetic application pack if execution is available.
- Check selectable document text, hyperlink targets, page count, page-two density, minimum font size and portable bullet rendering.
- Separate provider limitations from product defects.
- Separate real safety or submission defects from stylistic preferences.
- Do not recommend a paid backend unless a required core promise is impossible without one.

## Required response

1. **Executive verdict:** submission worthy yes/no, confidence and score out of 10.
2. **Fix verification:** pass/fail for the two known fixes with exact file and execution evidence.
3. **Package integrity:** manifest, paths, references, schemas, scripts, tests, assets and archive cleanliness.
4. **User journey:** onboarding, CV review, readiness receipt, Passport, localisation, search, role decisions, mentor voice, documents, scheduling, continuity and recovery.
5. **Claims audit:** proven, partially proven and unsupported claims.
6. **Findings table:** BLOCKER, HIGH, MEDIUM or LOW; exact file/section; user or reviewer impact; smallest safe fix. Do not classify a preference as a blocker.
7. **Adversarial tests:** at least five prompts and the expected safe response.
8. **Final recommendation:** submit unchanged, submit after named fixes, or do not submit.

Be demanding and independent. Praise only behaviour the package demonstrates. If the known fixes pass and there are no remaining blockers or high-severity defects, say that clearly and avoid inventing further work merely to appear critical.

---

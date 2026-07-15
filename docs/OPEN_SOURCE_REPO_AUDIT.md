# Open-source CV product audit

Audit date: 14 July 2026  
Product: Career Centre `4.0.0-beta.2` working tree  
Scope: ten ZIP archives supplied by the product owner

## Executive decision

Career Centre should remain a small, skills-only career decision product—not become a self-hosted resume-builder stack. The useful pattern across the supplied projects is a focused pipeline:

1. preserve the candidate's source material in a portable structured record;
2. test whether CV text survives extraction and remains easy to scan;
3. map role requirements only to evidenced claims;
4. give a small number of impact-ranked writing suggestions;
5. keep a transparent version history;
6. use human career judgement instead of presenting one invented “ATS score”.

That pipeline is now implemented without adding a publisher backend, a user account, a database, a Node/Go runtime, a model API key or a new third-party runtime dependency.

## Provenance and reproducibility

The downloaded archives do not contain Git metadata or a Git archival commit record. The exact upstream commit therefore cannot be established from the supplied files. The audit uses the archive filename, visible package version where present and SHA-256 fingerprint below. A future dependency decision must start from a tagged upstream release, not assume these `main` or `master` snapshots are immutable.

| Supplied archive | SHA-256 | Visible version | Licence found in archive |
|---|---|---:|---|
| `pyresparser-master.zip` | `bb4ce774f9ffda08a7d967b6736b9d2e89b258766bf3c14a68ebc68a901f0946` | 1.0.6 | GPL-3.0 |
| `open-resume-main.zip` | `32984b9a2ecc579b178d837d1ff6f35cf0de6e9a98fb6326aa55620a9c3f208e` | 0.1.0 | AGPL-3.0 |
| `reactive-resume-main.zip` | `a0ce939e337efcfd8c51f7f66e9500aea12f55ef575eb21cae15e644d353c477` | 5.2.3 | MIT |
| `proselint-main.zip` | `478e0183c65cc85df1eb37773e362cd278dc85e1b881bb55d5be0636a3519dfc` | 0.16.0 | BSD-3-Clause |
| `write-good-master.zip` | `45ac809cb7d96638cca16ff31d6ef601eea13f489781d65b0dc6e363f0ed37ac` | 1.0.8 | MIT |
| `retext-main.zip` | `2f478d8600c58ac0975ac6e343e443940380940a42da669c81819500e9f07fcb` | not declared at root | MIT |
| `vale-3.zip` | `d824a116c5bb684cb58b812d7a6878e6bd4f7799f33918c94697669c6c8cc470` | branch archive; Go module v3 | MIT |
| `jsonresume.org-master.zip` | `3d38f53d64023961123edea440e7480c0bc72d3dbc788a74e946b169d277129d` | not declared at root | MIT |
| `Resume-Matcher-main.zip` | `b9821f685791dcfe2ca4d1a3f5b6877b12ef663f3395dbe97394b099af72f9f3` | README identifies 1.2 “Nightvision” | Apache-2.0 |
| `Career_Command_Centre_Open_Source_Enrichment_Pack.zip` | `b67c8239bf067aa3a42a78f753598a14038862c8298e07c77de0462422973fb5` | supplied review pack | project-owner material; no reusable code imported |

## Decision matrix

| Project | Architecture observed | What a normal career user genuinely benefits from | Fit for a ChatGPT/Claude skill | Decision |
|---|---|---|---|---|
| Resume Matcher | FastAPI/Python backend, Next.js/React frontend, structured resume models, LLM parsing/tailoring, PDF generation, tracker and interview-prep flows | Master evidence record, source-preservation tests, per-section changes, cover letter and interview continuity | The whole app would add hosting, API-key, database and build complexity. Its deterministic truth checks are valuable. | Reimplement only preservation, provenance and version concepts. Do not import app code. |
| JSON Resume | Portable JSON resume schema, CLI, themes, registry and HTML-oriented ATS checks | Portability, standard fields, detectable headings/contact details and parseable text | Career Centre's Passport is broader than a resume schema because it also stores preferences, role history and evidence restrictions. HTML-specific scoring does not suit Word output. | Keep the Passport; add round-trip diagnostic ideas, not a JSON Resume dependency or score. |
| OpenResume | Local Next.js browser app; PDF.js groups PDF text into lines/sections and feature-scores headings/content | Private local parsing and a visible “can this resume be read back?” check | Parser is explicitly oriented to single-column English PDFs; AGPL code would introduce strong copyleft obligations. | Reference only. Implement an independent, format-light extraction diagnostic. |
| pyresparser | Python/NLTK/spaCy 2-era parser with regex, skills list and trained NER assets | Basic name/contact/skills/experience/education extraction checklist | Large stale dependency set, older Python classifiers, English-biased heuristics and GPL-3.0. Less reliable than provider-native document understanding plus provenance controls. | Reject dependency and code. Retain only the field checklist as a historical comparison. |
| Reactive Resume | Large React/TanStack/Node/Postgres builder with Zod schemas, custom sections/fields, import/export and history | Version history, optional custom fields, multilingual settings, mobile-first editing and impact-ranked suggestions | Excellent full builder, but unnecessary for a conversation-first skill and would create hosting/account complexity. Its 0–100 analysis score is not adopted. | Add output-version history and optional language/regional preferences to the Passport. Keep the existing natural-language advanced settings. |
| proselint | Python registry of configurable prose checks with stable line/column/span/replacement diagnostics | Specific, locatable writing feedback instead of generic “improve wording” advice | Full general-purpose rule set is noisy for CVs and introduces another dependency. The diagnostic shape is valuable. | Independently implement a small CV-specific diagnostic with category, impact, evidence and recommendation. |
| write-good | Small Node rule pipeline for passive voice, weakening words, clichés and repetition; supports custom checks/whitelists | Simple language and less repetitive CV writing | Old Node baseline; raw passive-voice lint can encourage false ownership or unnatural prose. | Use only cautious, low-severity CV-relevant heuristics with human review. No dependency. |
| retext | Unified/NLCST parser and plugin ecosystem for natural-language syntax trees | Language-aware, composable prose checks | A Node syntax-tree stack is disproportionate for the portable skill and does not itself solve career evidence safety. | Use the architectural principle—scoped, language-aware rules—not the package. |
| Vale | Go binary with YAML styles, scopes, severities, substitutions and markup-aware checks | Configurable house style and severity | Large binary/dependency tree and general documentation focus. Bundling it would make installation and provider portability worse. | Use severity/scoping concepts in the small independent diagnostic. No binary. |
| Enrichment pack | Four-capability review brief: schema, parseability, matching and writing quality | A coherent enrichment strategy and explicit licence/test discipline | Directly aligned with the product if implemented selectively. | Completed through this audit, new tests, Passport additions and diagnostic script. |

## Detailed findings

### Resume Matcher

The strongest engineering lesson is not its visible match percentage. It is the separation between a master resume, structured document state, a job-specific edit and tests that check whether employers, dates and personal information were preserved. Its parser converts DOCX/PDF content into a typed model and compensates for a known date-loss failure. Its evaluation layer checks schema validity, employer fabrication, personal-information preservation, section preservation and keyword coverage.

Career Centre already has a stricter evidence ledger: every substantive tailored claim cites an evidence ID, CV claims remain candidate-provided rather than verified, and an Apply decision fails without an exact open posting. The refinement taken from Resume Matcher is to register source CVs separately and retain each generated document version with its source-document IDs. Match-score marketing and automatic keyword insertion were not taken.

### JSON Resume

JSON Resume demonstrates why structured portability matters. It also treats semantic headings, single-column structure, standard fonts, selectable contact information, special characters and private-use glyphs as observable parseability concerns. Some checks in the supplied project target rendered HTML and cannot honestly certify a Word CV or an employer's ATS. Career Centre already rejects tables, text boxes, raw URLs, hidden text, comments, tracked changes, private-use glyphs and unsafe active bullet numbering in DOCX files.

The added diagnostic now checks selectable text, contact detection, common headings, chronology signals, repeated bullets and visible links without converting those observations into a universal score.

### OpenResume

OpenResume's best product idea is immediate round-trip confidence: import an existing resume, extract it locally, and show the user what survived. Its parser builds lines and sections from PDF text positions and typographic features. The same archive documents a single-column English constraint, so it is not a global general-purpose parser.

Career Centre adopts the user outcome, not the implementation. `review_cv_text.py` reads TXT, Markdown and DOCX locally when code execution is available; provider-supported extraction can supply PDF text. Non-English mode skips English-only heading and writing claims rather than labelling another language “bad ATS”.

### pyresparser

pyresparser covers the expected extraction fields—name, email, phone, skills, experience, education, designation, employer and page count—but relies on a large 2019-era dependency family including spaCy, NLTK, pandas and PDFMiner. It advertises Python 3.3–3.7 classifiers and carries GPL-3.0. It would create installation friction, model/asset compatibility risk and an English-skills-list bias without improving the conversation experience.

No pyresparser code, model or data is included.

### Reactive Resume

Reactive Resume is the best benchmark here for user-controlled document state. It has typed data, custom sections and fields, import/export, multilingual settings, client-side output and version-oriented editing. Its full application solves visual editing extremely well, but Career Centre's promise is less effort: the user should be able to say “hide my phone”, “use Canadian English” or “put projects before education” without learning a builder.

Career Centre therefore keeps natural-language advanced preferences and adds two optional Passport preferences—document language and regional spelling—plus `document_versions`. A revised output supersedes rather than erases the earlier version. Ready Word files, partial in-chat fallbacks and superseded drafts are distinguishable.

### proselint, write-good, retext and Vale

Together these projects show the right architecture for prose review: small checks, stable diagnostics, explicit severity, scope, deduplication, language awareness and configurable exceptions. They also show the main product risk: hundreds of general style warnings can make a user feel criticised while encouraging generic, over-edited prose.

Career Centre's independent diagnostic is deliberately narrow. It checks extraction depth, selectable email/phone signals, section detectability, chronology, duplicate bullets, repeated openings, very long sentences, a small set of generic career phrases, possible passive constructions and raw links. It returns `high`, `medium` and `low` impact findings with an evidence snippet and recommendation. Passive voice is only a low-impact manual-review cue because rewriting it blindly can invent ownership. Findings never override source evidence or career judgement.

## What was implemented

- Multiple CVs are registered separately, including target direction and primary status.
- Initial setup includes a compact qualitative CV read: what works, what may be underselling the person and one priority edit.
- `scripts/review_cv_text.py` provides a transparent, non-scored diagnostic for DOCX/TXT/Markdown and a safe non-English mode.
- `Career_Passport.json` remains the single Career Evidence File rather than creating a second database.
- Passport `document_versions` records CV bases, tailored CVs and cover letters with provenance, status and change summaries.
- Optional advanced preferences cover document language and regional spelling.
- Generated CV QA now includes the diagnostic before deterministic DOCX and visual validation.
- A complete in-chat CV remains the last-resort `PARTIAL` fallback when Word creation fails.
- Both provider packages have automated regression tests for these contracts.

## What was deliberately not implemented

- No universal ATS, match or “resume quality” number.
- No bulk keyword stuffing or unsupported job-description language.
- No visual resume-builder UI, account system or hosted database.
- No PDF-first output; Word remains the default application deliverable.
- No bundled GPL/AGPL code, models or assets.
- No pyresparser, spaCy, NLTK, Node, Go, Postgres, browser automation or external linter dependency.
- No assumption that English headings are appropriate for every document language.
- No promise that a provider carries state into unrelated conversations.

## Product implications

The combined product is more holistic without becoming broad and unfocused. It now supports the full ordinary-user loop: bring one or several CVs, understand current positioning, preserve evidence, set global preferences, assess roles, create and review documents, retain version and application history, prepare for interviews, and continue from a portable Passport.

The remaining quality gains are distribution and provider execution tests, not more architecture:

1. verify the final ZIPs in fresh ChatGPT and Claude conversations;
2. test one live exact role and one paired Word pack in Claude;
3. inspect mobile conversation and download behaviour on both providers;
4. confirm directory review wording and privacy attestations;
5. after real users, refine the small diagnostic only from repeated confirmed feedback—not from isolated preferences or vanity score pressure.

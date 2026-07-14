# Word document style contract

## CV — `ccc_cv_v4`

Base preset: `compact_reference_guide`, with named CV-specific overrides required for ATS density.

- Page: A4 portrait by default; Letter when explicitly selected.
- Margins: 0.58 in top/bottom, 0.66 in left/right.
- Header/footer distance: 0.20 in.
- Font: Arial.
- Body: 9.2 pt minimum, 0 pt before, 2.3 pt after, single line spacing.
- Candidate name: 20 pt bold, `#17324D`, centred.
- Positioning line: 10.5 pt bold, `#4B5563`, centred.
- Contact: 9 pt, `#4B5563`, centred.
- Section heading: 10.2 pt bold uppercase, `#17324D`, 5 pt before, 2 pt after, light-grey bottom rule.
- Experience heading: 9.3 pt minimum, bold, `#17324D`, 2 pt before.
- Bullets: real Word bullet numbering; 0.20 in text indent, 0.14 in hanging indent, 1.7 pt after.
- Tables, text boxes, hidden text and decorative media: prohibited.
- Page control: zero explicit page breaks for a one-page CV; one explicit break for a two-page CV.

## Cover letter — `ccc_cover_v4`

Base preset: `narrative_proposal`, with named application-letter overrides.

- Page: A4 portrait by default; Letter when explicitly selected.
- Margins: 0.72 in.
- Font: Arial 10 pt minimum.
- Body: 1.08 line spacing, 7 pt after.
- Candidate name: 17 pt bold, `#17324D`.
- Contact: 9 pt, `#4B5563`.
- Length: one page; normally 220–550 words.
- Narrative: role-specific opening, relevant proof, builder/adjacent-value paragraph where useful, practical early contribution and confident close.

## QA

Each generated file must pass structural validation and then render to PNG. An experienced-candidate two-page CV must fill at least 65% of page 1 and 80% of page 2. Automated page-count/density checks are followed by an explicit visual-review record. A run cannot be marked successful until the required CV and cover letter both pass.

# Career Centre beta.3 global beta tests

Use fictional details only. Run each scenario in a fresh task so provider memory cannot hide an onboarding defect.

## ChatGPT Work: United States

1. Install Career Centre, select **Work**, start a new task and paste:

   > @Career Centre Help me set up my career search. I am Alex Morgan, a Chicago-based digital transformation and product operations leader with 10 years in healthcare SaaS. I am a US citizen and do not need sponsorship. I want permanent Senior Product Operations Manager or Digital Transformation Lead roles in Chicago hybrid or US remote, with a USD 160,000 base floor. Exclude quota-carrying sales, pure software engineering and short contracts. Setup only; do not search yet.

2. Attach a fictional CV or paste a short evidence profile with two quantified achievements.
3. Pass criteria:
   - `Overall CV strength` appears before preference questions.
   - The readiness receipt uses USD, US spelling and US work-authorisation language.
   - It does not add a photo, date of birth, marital status or full street address.
   - It names employer sites plus suitable US sources such as LinkedIn, Indeed or Built In without pretending a connector is required.
   - A Career Passport is attached automatically.
4. Then ask:

   > Run one focused manual search for up to three exact, open roles. Do not add filler.

5. After the result, pass only if Career Centre proactively offers a daily or weekday run in the same task.
6. Accept with:

   > Yes. Schedule this in the same Career Centre task on weekdays at 8:00 AM America/Chicago, maximum five roles, and keep application packs on request.

## Claude: India

1. Install the beta.3 ZIP once, enable it, start a fresh Claude chat and paste:

   > /career-centre Help me set up, but do not search yet. I am Priya Nair in Bengaluru with nine years across product operations, customer implementation and transformation delivery in B2B SaaS. I am targeting permanent Senior Product Operations Manager and Transformation Lead roles in Bengaluru, Hyderabad or India-remote. My minimum fixed compensation is INR 32 lakh; keep variable pay and total CTC separate. My notice period is 60 days. Exclude sales, pure engineering and contracts under 12 months.

2. Paste a fictional evidence profile with two roles, dates and three achievements.
3. Pass criteria:
   - It gives the broad CV-strength verdict and offers the deeper review later.
   - It uses INR/lakh language, records the 60-day notice period only because supplied, and keeps fixed pay separate from CTC.
   - It does not request or add Aadhaar, caste, religion, date of birth, marital status or a photograph.
   - It names market-relevant discovery sources such as employer sites, LinkedIn India, Naukri, foundit or iimjobs selectively.
   - It attaches the first Career Passport automatically.
4. Run one focused search. After a useful result, pass only if it offers a daily or weekday Cowork schedule.
5. In Cowork, type `/schedule` and use:

   > On weekdays at 8:00 AM Asia/Kolkata, use Career Centre and my latest Career Passport to run this calibrated search. Return at most five verified roles with exact links, fixed/variable/CTC salary basis where available, employment type, Apply/Maybe/Skip, main match and main risk. Do not create application packs or submit anything.

## Template-on-request regression

During ordinary setup, fail the test if Career Centre asks for a reference template. After setup, ask:

> I do not like the default visual format. I am attaching a Word CV whose layout I want you to copy. Use it only as a visual template and do not copy any claims or personal data.

Pass only if the file becomes a visual source, not candidate evidence, and the finished Word CV still passes minimum font, density, bullet, metadata and evidence checks.

## Friend installation

- ChatGPT: send the public plugin details URL or ask the tester to open **Work → Plugins**, search `Career Centre`, check developer `Amit Sharma`, install, then start a new Work task. A shared chat link shares the transcript, not the plugin installation.
- Claude before public-directory approval: send `career-centre-4.0.0-beta.3-claude-plugin.zip`. The tester opens **Customize → Plugins**, uploads the custom plugin, enables it and starts a fresh chat. The ZIP is installed once.
- Never share a real CV or Career Passport as a test fixture. Each tester should use their own documents or the fictional scenarios above.

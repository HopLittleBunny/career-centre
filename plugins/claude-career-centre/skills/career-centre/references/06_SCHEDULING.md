# Scheduling

Use the host's scheduled-task feature only after confirming:

- cadence and local timezone;
- preferred run time;
- maximum displayed roles;
- whether application packs should be built automatically for Apply roles or only on request;
- where the current Career Passport is available;
- whether the host has proved persistent state across separate scheduled runs.

## Claude Cowork default: snapshot-backed alert

Claude documents that every scheduled task run starts as its own Cowork session. Unless the current run demonstrably receives and can update a valid Passport that the next run will load, do not claim deterministic cross-run memory or deduplication on this surface.

The no-backend default is a snapshot-backed alert. Embed a compact, evidence-safe snapshot of the current profile, preferences, evidence and role history in the saved prompt. Suppress duplicates against that snapshot and within the current run. Prefer roles explicitly posted or updated within the schedule's latest interval. Every result must begin with this plain-language status:

> Continuity: snapshot-backed alert. I used the Career Passport captured when this schedule was created plus this run's results. Claude did not supply an updated Passport from earlier scheduled runs, so a role may repeat in a later alert.

Do not print a run number, say that the Passport was updated or claim a role is new since the prior run unless the prior run's updated Passport was actually supplied to this execution. A later-run instruction that merely says “reuse the previous output” is not proof that the state is available.

Recommended default:

> On weekdays at 7:30 AM local time, use the embedded Career Passport snapshot to search for suitable roles. Return at most five verified roles with exact links, salary context and Apply/Maybe/Skip decisions. De-duplicate against the embedded history and within this run. Prefer postings created or updated since the previous scheduled interval. Repeats across later alerts remain possible. Do not auto-submit or build application packs automatically.

## Verified persistent mode

Enable `verified_persistent` continuity only when the execution can demonstrably load the latest valid Passport at the start of every run and save an updated valid Passport where the next run will receive it. Examples may include an explicitly configured user-owned persistence connector or a Claude account file that every run has proved it can read and replace. Do not infer this from conversation memory, a prior Cowork result, a local-only folder or the text of the scheduled prompt.

If `verified_persistent` mode is configured but the current run cannot load the latest Passport, return `BLOCKED` with one recovery action rather than falling back silently. Scheduled runs must never create unlimited documents or auto-submit applications.

Store the confirmed schedule under the Career Passport's optional `automation` object. Use `continuity_mode: snapshot_only` for Claude Cowork Scheduled Tasks until persistence is verified. When code execution is available, run `python scripts/build_schedule_prompt.py <Career_Passport.json>` and save the resulting instruction in the host task. This keeps cadence, timezone, result limit, evidence boundary, current history snapshot and pack mode portable without asking the user to manage a separate project or prompt.

After creation, show a short schedule receipt with cadence/timezone, result limit, document/submission boundary and continuity status. Keep scheduling optional and advanced; the ordinary career conversation remains the deterministic place for long-term role history, tailoring and application updates.

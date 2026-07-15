# Scheduling

Test one manual search before scheduling it. After the first useful manual result, proactively ask one short question:

> Would you like me to turn this calibrated search into a daily or weekday Cowork task? If yes, tell me the time and timezone; I will keep the current role limit unless you change it.

Do not ask about automation during first-time setup. If the user accepts, confirm only missing details:

- cadence and local timezone;
- preferred run time;
- maximum displayed roles, default five;
- application packs on request by default.

Never auto-submit. Never tell the user to upload the plugin ZIP every day. It is installed once.

## Cowork scheduled task

Recurring work belongs in Cowork. Use `/schedule` from an existing Cowork task or create it from the Scheduled page. Include Career Centre in the saved instructions and use the latest Career Passport saved to the user's account. Each scheduled execution is its own Cowork session, although it can use installed plugins, connected tools and account-saved files.

The no-backend default is a snapshot-backed task. Embed a compact, evidence-safe Passport snapshot in the saved prompt, suppress duplicates against that snapshot and within the run, and disclose that a later run may repeat a role unless it demonstrably loaded an updated Passport. Use `destination: scheduled_result_task` and `continuity_mode: snapshot_only`.

Recommended default:

> On weekdays at 8:00 AM local time, use Career Centre and the latest Career Passport available to this Cowork task to run the calibrated role search. Return at most five verified roles with exact links, salary context and Apply/Maybe/Skip decisions. Reconcile the saved role history before browsing. Do not create application packs automatically and never submit an application.

## Verified persistent mode

Use `verified_persistent` only when every run can demonstrably load the latest valid Passport and save the updated Passport where the next run will receive it. If either operation fails, return `BLOCKED` with one recovery action instead of silently resetting state.

Store confirmed schedule settings under the Passport's optional `automation` object. When code execution is available, run `python scripts/build_schedule_prompt.py <Career_Passport.json>` and save the output in the scheduled task. After creation, show a short receipt with cadence/timezone, result limit, document/submission boundary and continuity mode. Review the first few runs and recalibrate sources or gates if results are weak.

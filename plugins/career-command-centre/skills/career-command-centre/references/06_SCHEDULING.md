# Scheduling

Test one manual search before scheduling it. At the end of the first completed manual search that returns at least one verified role, proactively ask one short question in the same response—even when every role is Maybe or Skip:

> Would you like me to run this calibrated search daily or on weekdays in this same Career Centre task? If yes, tell me the time and timezone; I will keep the current role limit unless you change it.

Do not ask about automation during first-time setup. If the user accepts, confirm only missing details:

- cadence and local timezone;
- preferred run time;
- maximum displayed roles, default five;
- application packs on request by default.

Never auto-submit. Never tell the user to upload the plugin ZIP every day. It is installed once.

`Do not create a schedule` means no schedule may be created; it does not suppress this invitation because the invitation changes no external state. Suppress the invitation only when the user explicitly says not to mention, offer or discuss recurring searches. Before sending the search response, silently verify that the invitation is present once, after the mentor verdict. Do not bury it inside role details.

## ChatGPT Work default: current-task context

Create the schedule from the existing Career Centre Work task and return each run to that task. The task can use its existing conversation context, uploaded files, installed skills and plugins. Keep the latest Career Passport attached or otherwise available to the task and include durable search instructions in the scheduled prompt.

Use `destination: continuing_task` and `continuity_mode: task_context` when this route is available. The prompt must invoke Career Centre explicitly, preserve exact-link, salary, evidence and no-submit rules, and reconcile the task's role history before browsing. Do not claim cross-account or unrelated-chat memory.

Recommended default:

> On weekdays at 8:00 AM local time, use Career Centre in this task and the latest Career Passport available here to run the calibrated role search. Return at most five verified roles with exact links, salary context and Apply/Maybe/Skip decisions. Reconcile earlier reviewed and applied roles before browsing. Do not create application packs automatically and never submit an application.

## Standalone fallback: snapshot-backed alert

Use a standalone scheduled task only when the user wants independent runs or the host cannot return to the current task. Embed a compact, evidence-safe Passport snapshot, suppress duplicates against that snapshot and within the current run, and disclose that later standalone runs may repeat a role because they do not necessarily receive state written by an earlier run. Use `destination: scheduled_result_task` and `continuity_mode: snapshot_only`.

## Verified persistent mode

Use `verified_persistent` only when every run can demonstrably load the latest valid Passport and save the updated Passport where the next run will receive it. If either operation fails, return `BLOCKED` with one recovery action instead of silently resetting state.

Store confirmed schedule settings under the Passport's optional `automation` object. When code execution is available, run `python scripts/build_schedule_prompt.py <Career_Passport.json>` and save the output in the host schedule. After creation, show a short receipt with cadence/timezone, result limit, document/submission boundary and continuity mode. Review the first few runs and recalibrate sources or gates if results are weak.

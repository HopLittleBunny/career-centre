# Scheduling

Test one manual search before scheduling it. Treat the automation handoff as a required milestone, not optional closing copy.

During the readiness receipt, set the expectation once:

> After this first search, I’ll ask whether you want me to make it a daily or weekday Cowork task.

At the end of the first completed manual search that returns at least one exact verified role, proactively use this visually separate invitation in the same response—even when every role is Maybe or Skip:

> Want me to make this search automatic? I can set up a daily or weekday Career Centre task in Cowork. Reply with the cadence, time and timezone (for example, “Weekdays at 8:00 AM Eastern time”); I’ll keep the current role limit unless you change it.

If the user proceeds to an application pack without accepting, declining or creating a schedule, repeat the invitation once after the first completed pack. This is the recovery gate for a missed or ignored first-search offer. Do not repeat after an explicit decline or when a schedule already exists.

`Current role limit` means the cap used in the successful manual run or the user's latest explicit choice. Preserve it exactly. Use the default of five only when no cap has been established; never replace a confirmed limit with five in the offer or receipt.

Do not ask the user to configure automation during first-time setup; the readiness sentence is expectation-setting only. If the user accepts, confirm only missing details:

- cadence and local timezone;
- preferred run time;
- maximum displayed roles, default five;
- application packs on request by default.

Never auto-submit. Never tell the user to upload the plugin ZIP every day. It is installed once.

`Do not create a schedule` means no schedule may be created; it does not suppress this invitation because the invitation changes no external state. Suppress the invitation only when the user explicitly says not to mention, offer or discuss recurring searches. Before sending the search response, silently verify that the invitation is present once, after the mentor verdict and role details. Do not bury it inside role details.

## Acceptance handling

Claude Scheduled tasks live in Cowork. They can use installed plugins, skills and connected tools, and each scheduled execution is its own Cowork session.

1. If cadence, time or timezone is missing, ask only for the missing value.
2. If the current surface is Cowork, start the `/schedule` flow with the calibrated prompt when all values are known. Let the user confirm through Cowork's **Schedule** control when Claude presents it.
3. If the current surface is ordinary Claude chat, do not claim that the task was created. Give the exact copy-ready command below and direct the user to **Cowork** once.
4. After creation, show a compact receipt: task name, cadence, timezone, role limit, application-pack boundary, manual-submission boundary and `Snapshot-backed` continuity unless persistent loading is demonstrably verified.

Ordinary-chat fallback:

> Open **Cowork**, start a task with Career Centre available, and paste: `/schedule On [daily/weekday cadence] at [time] [timezone], use Career Centre and the embedded Career Passport snapshot to run my calibrated role search. Return at most [role limit] verified roles with exact posting URLs, salary context and Apply/Maybe/Skip decisions. Reconcile the snapshot's reviewed-role history and disclose possible repeats across later runs. Do not create application packs automatically and never submit an application.`

As a second route, use **Scheduled** in the left sidebar, choose **New task**, then **Set up manually**, and paste the same instructions. Scheduled tasks require an eligible Claude paid plan and Cowork availability; do not describe scheduling itself as universally free.

## Cowork scheduled task

Recurring work belongs in Cowork. Use `/schedule` from an existing Cowork task or create it from the Scheduled page. Include Career Centre in the saved instructions and embed the current Career Passport snapshot available when the task is created. Each scheduled execution is its own Cowork session, although it can use installed plugins, connected tools and account-saved files. Do not imply that an ordinary Claude chat created the task, and do not say a future run loads “the latest Passport” unless that load is demonstrably verified.

The no-backend default is a snapshot-backed task. Embed a compact, evidence-safe Passport snapshot in the saved prompt, suppress duplicates against that snapshot and within the run, and disclose that a later run may repeat a role unless it demonstrably loaded an updated Passport. Use `destination: scheduled_result_task` and `continuity_mode: snapshot_only`.

Recommended default:

> On weekdays at 8:00 AM local time, use Career Centre and the embedded Career Passport snapshot to run the calibrated role search. Return at most [the confirmed role limit; default five only if none was set] verified roles with exact links, salary context and Apply/Maybe/Skip decisions. Reconcile the snapshot's saved role history before browsing. Disclose that a later run may repeat a role unless an updated Passport is demonstrably loaded. Do not create application packs automatically and never submit an application.

## Verified persistent mode

Use `verified_persistent` only when every run can demonstrably load the latest valid Passport and save the updated Passport where the next run will receive it. If either operation fails, return `BLOCKED` with one recovery action instead of silently resetting state.

Store confirmed schedule settings under the Passport's optional `automation` object. When code execution is available, run `python scripts/build_schedule_prompt.py <Career_Passport.json>` and save the output in the scheduled task. After creation, show a short receipt with cadence/timezone, result limit, document/submission boundary and continuity mode. Review the first few runs and recalibrate sources or gates if results are weak.

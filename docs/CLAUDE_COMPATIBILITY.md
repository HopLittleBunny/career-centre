# Claude compatibility

## Current status

Career Centre now has a native Claude plugin at `plugins/claude-career-centre/` and a browser-upload ZIP at `release/career-centre-4.0.0-beta.2-claude-plugin.zip` after packaging.

- Package version: `4.0.0-beta.2`
- Visible plugin and skill name: **Career Centre**
- Manifest: `.claude-plugin/plugin.json`
- Skill location: `skills/career-centre/SKILL.md`
- Publisher backend: none
- Automated core tests: 56/56 passing in the Claude package
- Paid-account browser upload: passed on Claude Max web
- Natural skill auto-routing: passed in a normal web chat without a slash command
- Mentor reflection and compact follow-up questions: passed with a synthetic US persona
- Seven-line readiness receipt: passed
- Exact beta.2 replacement upload: passed on Claude Max web
- Explicit setup/no-search/no-files boundary: passed on the exact beta.2 package
- Advanced field/format preferences and 390 px mobile rendering: passed

## Why this route fits the product

Anthropic documents plugins for paid Pro, Max, Team and Enterprise plans and says installed plugin skills work in web chat, Claude Desktop chat and Claude Cowork. Users can upload a custom plugin rather than creating a Project or maintaining prompt files. See [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

The package uses the standard plugin layout documented in Anthropic's [Plugins reference](https://code.claude.com/docs/en/plugins-reference): a `.claude-plugin/plugin.json` manifest and a `skills/<name>/SKILL.md` directory. It contains no MCP server, hooks or publisher API, so ordinary chat receives the relevant skill without external account setup.

The repository also contains `.claude-plugin/marketplace.json`. Users can add `HopLittleBunny/career-centre` as a GitHub marketplace and install Career Centre through the normal plugin UI; the downloadable ZIP remains a fallback. Anthropic documents Git-backed personal marketplaces in [Install plugins](https://claude.com/docs/cowork/guide/plugins).

## Scheduled role alerts

Claude documents scheduled tasks in Cowork for paid plans. Each run is its own Cowork session, so Career Centre defaults to the same honest snapshot-backed continuity model until a run can demonstrably load and replace a Passport that the next run will receive. See [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).

The Claude scheduling copy is provider-specific. It does not claim ChatGPT behaviour, and it does not promise cross-run deduplication merely because an earlier session printed updated state.

## Browser evidence and remaining acceptance gate

Completed with synthetic personas on a paid Claude browser account:

1. Uploaded the custom plugin through **Customize → Plugins → Personal plugins**.
2. Started a normal web chat without explicitly invoking the skill.
3. Confirmed automatic Career Centre routing, a candid career thesis, strongest and stretch lanes, only three meaningful questions, and the exact seven-line **Your Career Centre is ready** receipt.
4. Confirmed the receipt was global and US-specific rather than carrying Australian assumptions.
5. Replacement-uploaded the final ZIP and ran a fresh setup-only conversation with a Canadian persona.
6. Confirmed the explicit `do not search` and `do not create files` boundaries: Claude gave orientation, a candid role-track trade-off, one concrete recommendation and the exact receipt, then stopped without browsing or creating files.
7. Confirmed the manual-application boundary and that ordinary conversation auto-routing still worked after replacement.
8. Confirmed advanced preferences for language, visible contact fields, headline preservation and conditional section order in ordinary language.
9. Confirmed mobile rendering at 390×844 with no horizontal overflow.

The Claude Platform public directory form currently targets Claude Code and Claude Cowork rather than presenting a separate normal-chat checkbox. A Cowork-only listing draft is prepared, but Cowork parity and the account-holder legal consent remain open. Direct custom-plugin ZIP upload is the verified normal-browser-chat route today.

Remaining before full Claude parity: verify one exact live role assessment, generate and visually inspect a paired Word pack, test reference-format isolation, run a two-execution Cowork schedule continuity check, and repeat on another eligible paid plan. Current rating is **9.1/10 for Claude installation and conversation readiness** and **8.8/10 for full Claude feature parity**.

# Platform compatibility and cost model

Status checked: 14 July 2026.

## ChatGPT

- A plugin can contain skills only; it does not need an app or MCP server.
- The plugin directory is visible across ChatGPT plans.
- Skills-only plugins remain available by default where the plan and surface support them.
- Installation or invocation can still vary by plan, workspace policy, region and surface.
- Personal Skills are generally documented for Business, Enterprise, Healthcare and Edu, while plugin packaging has broader directory visibility. In the tested personal Pro account, the Skills page and direct ZIP upload control are present and an older personal Career Centre skill is installed. This rollout evidence is promising but does not remove the need for v4 and published Plus/Pro tests.
- Scheduled tasks are documented for Plus, Pro, Business and Enterprise on web/mobile. They use the user's plan limits and cannot access ChatGPT Project files.
- ChatGPT Library stores uploaded and generated files for supported personal plans. Memory may reference them when enabled, but the product does not rely on that as its only state mechanism.

## Claude

- Claude Skills are documented for Free, Pro, Max, Team and Enterprise when code execution/file creation is enabled.
- Claude Plugins are documented for all paid plans: Pro, Max, Team and Enterprise.
- Users can upload a custom plugin file; its bundled skills work in web chat, Claude Desktop chat and Cowork.
- Custom individual skills are private to that account; Team/Enterprise can share or provision them.
- Hooks and sub-agents are Cowork-specific, so the provider-neutral career core must not require them.

## Publisher cost

| Component | Required recurring Amit cost |
| --- | ---: |
| Model inference | $0 — user's ChatGPT/Claude plan and limits |
| CV database | $0 — none operated by Amit |
| MCP/app server | $0 — none required for the core product |
| Static website/legal pages | $0 using a free static host |
| Support inbox | $0 using an existing/free mailbox |
| Custom domain | Optional branding cost |
| Analytics/telemetry | None by default |

The cost model is intentionally austere. If a future feature requires hosted state, proprietary job feeds or email delivery, it must be optional and separately justified; it must not become a hidden dependency of the free core.

## Sources

- [OpenAI: Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex)
- [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [OpenAI: Scheduled Tasks in ChatGPT](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)
- [OpenAI: File storage and Library in ChatGPT](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
- [Anthropic: Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Anthropic: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Anthropic: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

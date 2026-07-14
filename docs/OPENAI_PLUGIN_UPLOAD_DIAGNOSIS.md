# OpenAI plugin upload diagnosis

Checked on 14 July 2026 in the signed-in OpenAI Platform plugin portal.

## Current conclusion

The upload blocker cleared after the authenticated Help Center/support flow and a fresh Platform session. The unchanged production archive successfully created a real **Career Centre** draft on 14 July 2026. This confirms that the package, archive layout, verified identity and app-management permission are accepted by the portal.

The earlier failures remain useful diagnostic history: they were reproduced with both the production package and a minimal OpenAI-scaffolded control, while the portal logged missing `org_id` scoping. Because the same production archive later succeeded unchanged, the failure was transient account/session/provider scoping rather than a Career Centre package defect.

## Evidence

| Check | Result |
| --- | --- |
| Selected organization | Default organization; verified |
| Submitter role | Owner |
| Submission route | Create plugin → Skills only |
| Full Career Centre package, initial attempts | Generic `Plugin upload failed`; no draft |
| Skill-only ZIP without plugin manifest | Precise `Plugin manifest not found` response |
| Minimal control without images | Precise missing composer icon and logo responses |
| Control with 24×24 SVG | Precise 48×48 minimum-dimension response |
| Clean four-file OpenAI-scaffolded control | Generic `Plugin upload failed`; no draft |
| Root-manifest ZIP | Generic failure after clean preflight |
| Single top-level plugin-folder ZIP | Generic failure after clean preflight |
| Browser diagnostics | Repeated warning that `plugin_submissions_config` lacks the required `org_id` identity type |
| Fresh authenticated retry | Upload accepted; **Career Centre** draft created |
| Draft listing | Plugin info saved; prompts and the `career-centre` skill imported |
| Current remaining portal check | Automated skill scan in progress before policy attestations and final submission |

The control contained only `.codex-plugin/plugin.json`, a 245-byte harmless `SKILL.md`, one square SVG and one square PNG. This removed Career Centre's Word templates, scripts, references, schemas, tests and substantive instructions from the historical failure path.

## Production package

Use `release/career-centre-4.0.0-beta.2-submission-openai-upload.zip` for the next portal attempt. Its manifest is at ZIP root. The folder-prefixed distribution ZIP remains available separately for marketplace installation.

The upload archive checksum is recorded in `release/LATEST.json`. Regenerate it with:

```bash
python3 scripts/package_release.py --submission-ready
```

## Support message

Subject: Verified owner cannot create a skills-only plugin draft — generic upload failure

> I am trying to create a skills-only plugin at `https://platform.openai.com/plugins` using a verified individual developer identity. I am the Owner of the selected default organization. Client-side validation works and returns precise errors for missing manifests, missing images and undersized SVGs. However, any package that clears those checks returns only `Plugin upload failed` and no draft is created.
>
> I reproduced this with a four-file control generated using OpenAI's current `plugin-creator` scaffold: one manifest, one 245-byte harmless skill, one square SVG and one square PNG. Both a root-manifest ZIP and a single-top-level-folder ZIP fail identically. The full Career Centre package passes the current plugin validator and its 56 automated tests.
>
> The browser console consistently reports that the `plugin_submissions_config` dynamic configuration lacks the required `org_id` identity type, although Platform settings show a normal organization ID, verified status, default-org status and Owner role.
>
> Please check whether this organization is correctly enrolled/scoped for plugin submissions and inspect the failed upload request on your side. Repository: `https://github.com/HopLittleBunny/career-centre`. The current upload-archive SHA-256 is in `release/LATEST.json`.

Do not include the private organization ID, user ID or account email in a public GitHub issue. Supply those only through the authenticated OpenAI support conversation if requested.

## Support follow-up

The selected organization is **Amit Sharma**. Platform People & Permissions shows Amit Sharma as **Owner**, with the organization marked as the default organization. [OpenAI's submission documentation](https://developers.openai.com/apps-sdk/deploy/submission#app-management-permissions) states that organization owners automatically have both `api.apps.write` and `api.apps.read`. The successful creation of the Career Centre draft is also a functional confirmation of write access.

There is no longer a failing upload request to report: the latest retry created the draft. If support still needs the earlier HTTP response metadata, reproduce only with a disposable control package and capture the Network entry before changing the production draft.

> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is **PowerContext 101**, a bilingual tutorial site built on [Mintlify](https://mintlify.com)
- It teaches PowerContext usage and development practice
- It is **not** a copy of the official reference site at [https://oceanbase.github.io/powercontext/](https://oceanbase.github.io/powercontext/)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Chinese lives under `zh/`; English lives under `en/`
- Chinese is the default locale (`navigation.languages` entry `zh` has `"default": true`)
- Use the Mintlify MCP server, `https://mcp.mintlify.com`, to edit content and settings via MCP
- Use the Mintlify docs MCP server, `https://www.mintlify.com/docs/mcp`, to query information about using Mintlify via MCP

## Source of truth

Use this evidence order when a claim is disputed:

1. Current runtime code and domain models in `oceanbase/powercontext`
2. Current tests, especially contract and end-to-end tests
3. `openapi/powercontext.yaml`
4. Formal how-to and reference pages under `docs/en` and `docs/zh`
5. RFCs and design notes, for background only

Do not treat RFCs or `docs/my` notes as shipped behavior unless current code and tests confirm them. Link to official docs for contracts; do not paste official reference chapters into 101. Do not put local absolute filesystem paths on pages or in page comments.

Classify time-sensitive integration claims as `Supported`, `Preview`, `Unsupported`, `Not validated`, `Host-gated`, or `Version-gated`. Do not soften or merge these states.

## Terminology

Keep these product words in both Chinese and English pages. Do not replace them with a different product term.

- `Source`
- `Memory`
- `Handoff`
- `Experience`
- `Skill`
- `Scope` / `scope_id`
- `Artifact`
- `Revision`
- `PreparedContext`
- `Candidate`
- `Review`
- `fail-open`
- `Task Outcome`

English pages use `Work Contract`. On each Chinese page, write `工作契约（Work Contract）` on first reader-visible use and `工作契约` afterwards. Generic software and API contracts are always `契约`, never `合同`. Keep API identifiers, schemas, JSON fields, and code literals such as `create_work_contract`, `CreateWorkContractRequest`, `powercontext.work-contract.v1`, and `"contract"` unchanged.

Chinese prose should read as Chinese, not as English terminology joined by Chinese particles. Translate ordinary engineering language whenever no exact identifier or proper product name is involved: adapter → 适配器, plugin → 插件, recall → 召回, capture → 采集, commit → 提交, export → 导出, approve/reject/revise → 批准/拒绝/修订, current head → 当前头版本, stale → 过期, durable → 持久, boundary → 边界, receipt → 回执, lineage → 证据链, no-op → 无变更, fallback → 后备路径, provider → 模型提供方, real-host E2E → 真实宿主端到端验证, drift → 漂移. Also translate setup, package, client, host, runtime, tool, timeout, prompt, transcript, session, snapshot, smoke test, source install, and round trip when they are ordinary prose. Keep exact commands, API/tool names, environment variables, schemas, maturity labels, UI labels, and proper component names such as PowerContext Server and Python Client unchanged.

Say `PowerContext 101` for this site. Say `official docs` / `官方文档` for https://powercontext.oceanbase.io/.

## Bilingual lockstep

**Every content change must update Chinese and English together in the same work unit.**

This rule applies to all of the following:

- MDX body copy
- frontmatter `title` and `description`
- new, deleted, or renamed pages
- `docs.json` tab names, group names, page lists, navbar, and footer for both `zh` and `en`

Do not finish a work unit with only one locale updated. If a page is added, add `zh/<path>.mdx` and `en/<path>.mdx`, then add both paths to the matching language navigation. If a page is removed or renamed, update both files and both navigation trees.

Keep the `zh/` and `en/` directory trees mirrored. The same relative path must exist in both locales.

Code samples stay identical across locales. Translate surrounding prose and code comments, not identifiers, commands, env vars, or API names.

Internal links must stay inside the current locale: `/zh/...` on Chinese pages, `/en/...` on English pages. Do not mix locales in one page.

Use locale-prefixed navigation paths. `zh/start/index` and `en/start/index` should mirror each other; do not add the same bare path such as `index` to both language navigation trees.

Each top-level tab must use its own subdirectory after the locale prefix (`zh/start`, `zh/mental-model`, `en/start`, `en/mental-model`). Do not put a tab's pages at `zh/index` or `en/index`. Mintlify picks the active tab by URL prefix, so a page at `/zh` would also match every other Chinese tab.

## Style preferences

- Use active voice and second person ("you" / "你")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references
- 101 tone: teach a path, then show a trick. Do not write encyclopedia pages
- After technical review, run `/humanizer-zh` on Chinese pages and `/humanize-writing` on English pages
- Humanizing may change prose only. Recheck API names, commands, versions, maturity labels, limitations, and capability matrices afterward
- Do not add invented experience, statistics, or opinions to make technical pages sound more human

## Content boundaries

- Do write: mental model, API tours, framework tricks, paste-ready agent setup, hook extension
- Do not copy official OpenAPI, RFC text, or full how-to chapters into this site
- Do not document unshipped RFC goals as if they already work
- Stub pages may keep a `TODO` note until real copy is written, but a published learning path must not describe a stub as complete
- Automatic recall, capture, and optional flush may fail open. Explicit durable writes, Review, Handoff commit, and Skill export must report failure
- Candidate `version` and Artifact `Revision` are different concurrency domains
- Bundled, managed, projected, and external Skills are different objects; do not use the terms interchangeably
- Theme and branding changes belong in `docs.json`, `style.css`, and `logo/` only
- Do not restyle Mintlify component DOM to chase visual polish; selectors can break

## Theme

- Layout theme is `maple`, not the starter `mint`
- Brand colors: primary `#0b6ff4`, light `#68adff`, dark `#064faa`
- Prefer `docs.json` tokens over large custom CSS

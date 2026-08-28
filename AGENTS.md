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

- Product facts come from the PowerContext repository (`oceanbase/powercontext`), especially current code, OpenAPI, and official docs under `docs/en` and `docs/zh`
- Do not treat RFCs or `docs/my` notes as shipped behavior unless code and tests confirm them
- 101 pages should link to official docs for contracts; they should not paste official reference chapters
- Do not put local absolute filesystem paths on pages or in page comments

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
- `Work Contract`
- `Task Outcome`

Say `PowerContext 101` for this site. Say `official docs` / `官方文档` for https://oceanbase.github.io/powercontext/.

## Bilingual lockstep

**Every content change must update Chinese and English together in the same turn.**

This rule applies to all of the following:

- MDX body copy
- frontmatter `title` and `description`
- new, deleted, or renamed pages
- `docs.json` tab names, group names, page lists, navbar, and footer for both `zh` and `en`

Do not finish a turn with only one locale updated. If a page is added, add `zh/<path>.mdx` and `en/<path>.mdx`, then add both paths to the matching language navigation. If a page is removed or renamed, update both files and both navigation trees.

Keep the `zh/` and `en/` directory trees mirrored. The same relative path must exist in both locales.

Code samples stay identical across locales. Translate surrounding prose and code comments, not identifiers, commands, env vars, or API names.

Internal links must stay inside the current locale: `/zh/...` on Chinese pages, `/en/...` on English pages. Do not mix locales in one page.

Do not reuse the same page path in both languages. `zh/start/index` and `en/start/index` are different paths; a bare `index` path must not appear in both language trees.

Each top-level tab must use its own subdirectory after the locale prefix (`zh/start`, `zh/mental-model`, `en/start`, `en/mental-model`). Do not put a tab's pages at `zh/index` or `en/index`. Mintlify picks the active tab by URL prefix, so a page at `/zh` would also match every other Chinese tab.

## Style preferences

- Use active voice and second person ("you" / "你")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references
- 101 tone: teach a path, then show a trick. Do not write encyclopedia pages

## Content boundaries

- Do write: mental model, API tours, framework tricks, paste-ready agent setup, hook extension
- Do not copy official OpenAPI, RFC text, or full how-to chapters into this site
- Do not document unshipped RFC goals as if they already work
- Stub pages may keep a `TODO` note until real copy is written
- Theme and branding changes belong in `docs.json`, `style.css`, and `logo/` only
- Do not restyle Mintlify component DOM to chase visual polish; selectors can break

## Theme

- Layout theme is `maple`, not the starter `mint`
- Brand colors: primary `#0b6ff4`, light `#68adff`, dark `#064faa`
- Prefer `docs.json` tokens over large custom CSS

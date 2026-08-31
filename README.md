# PowerContext 101

[English](README.md) | [中文](README.zh-CN.md)

PowerContext 101 is a bilingual tutorial site for [PowerContext](https://github.com/oceanbase/powercontext). It teaches working paths and integration boundaries: the mental model, a runnable first loop, framework adapters, and agent-host contracts.

Installation options, the OpenAPI contract, and deployment settings stay in the [official PowerContext docs](https://oceanbase.github.io/powercontext/). This site does not copy that reference. When an older RFC differs from current code and tests, 101 describes the implemented behavior.

The published site uses Chinese as the default locale. This repository README is English first.

## What the site covers

Start with the object boundaries, then finish one path that matches your work.

The **first loop** is: write one Memory, find it with `search_memory`, and use `prepare_context` to obtain a cited `PreparedContext`. Source extraction and Handoff wait until after that loop.

| Section | What you read |
|---|---|
| Start | Why PowerContext exists, a learning path by goal, and troubleshooting for symptoms already documented here |
| Mental model | `Source`, `Memory`, `Handoff`, `Experience`, `Skill`, `Scope`, and `fail-open` |
| Basic usage | Install a local Server, run the API tour, connect MCP, see the Memory in the Dashboard, then optional Source, Handoff, and Review paths |
| Frameworks | First integration is LangGraph or LangChain. Server-side Pydantic AI inference configures generation and embedding; it is not an agent adapter. The Pydantic AI Agent adapter is **Preview** |
| Common agents | Hermes, OpenClaw, WorkBuddy, Agent Plugin, and managed Skill self-extension. Hermes and OpenClaw cannot export a managed Skill |
| Coding agents | Codex, Claude Code, DSH, OpenCode, and Pi, plus hook contracts and how to start a sixth host |

Coding-agent pages are 101 verification contracts. They are not copies of official how-tos. Most real-host E2E is **Not validated**. `setup` and `doctor` do not prove recall or a live host session. Use the official docs for install parameters.

A host should continue the original task when automatic recall, prompt capture, or an optional flush fails. Explicit Memory writes, Handoff commits, Candidate Review, and Skill export must fail visibly.

## Repository layout

| Path | Role |
|---|---|
| `zh/` | Chinese MDX pages |
| `en/` | English MDX pages, same relative paths as `zh/` |
| `docs.json` | Mintlify navigation, navbar, and theme |
| `AGENTS.md` | Writing rules and source-of-truth order |

## Local preview

Install the current Mintlify CLI:

```bash
npm install --global mint
```

Start the local site from the repository root:

```bash
mint dev
```

Open `http://localhost:3000`. The preview follows the site default locale, so the first page is Chinese. Switch to `/en/start` for English.

## Validate

Check navigation and MDX frontmatter before you submit:

```bash
mint validate
```

Pull requests run the same check in `.github/workflows/docs-validate.yml`.

## Contributing

Read [AGENTS.md](AGENTS.md) before you edit.

Every content change must:

1. verify product claims against current `oceanbase/powercontext` code and tests;
2. update mirrored `zh/` and `en/` pages in the same work unit;
3. keep code samples, commands, API names, maturity labels, and limitations aligned;
4. run `/humanizer-zh` on Chinese pages and `/humanize-writing` on English pages after technical review;
5. recheck those technical facts after the editorial pass;
6. run `mint validate` and open the changed pages in the local preview.

Keep these product words in both locales: `Source`, `Memory`, `Handoff`, `Experience`, `Skill`, `Scope`, `Artifact`, `Revision`, `PreparedContext`, `Candidate`, `Review`, `fail-open`, `Work Contract`, `Task Outcome`.

Classify integration claims as `Supported`, `Preview`, `Unsupported`, `Not validated`, `Host-gated`, or `Version-gated`. Do not merge those states.

RFCs explain design history. They are not evidence that a feature has shipped.

# PowerContext 101

PowerContext 101 is a bilingual Chinese and English tutorial site for PowerContext. It teaches the mental model, runnable API workflows, framework integration, and agent-host behavior. Complete contracts and deployment reference remain in the [official PowerContext docs](https://oceanbase.github.io/powercontext/).

Published MDX pages have full copy. There are no `TODO` stubs. Navigation matches written pages.

| Section | Status |
|---|---|
| Start | Entry and learning path are written |
| Mental model | Full concept pages |
| Basic usage | Full runnable tutorials |
| Frameworks | Full integration guides. First install path is LangGraph or LangChain; the Pydantic AI Agent adapter is Preview |
| Common agents | Full Hermes, OpenClaw, WorkBuddy, Agent Plugin, and self-extension pages |
| Coding agents | Contract, capability matrix, and followable host pages exist. They are 101 verification contracts, not copies of official how-tos. Most real-host E2E is **Not validated**. `setup` and `doctor` do not prove recall or a live host session. |

Do not treat a coding-agent host page as a finished, proven host walkthrough. Use the official docs for install parameters.

## Local preview

Install the current Mintlify CLI:

```bash
npm install --global mint
```

Start the local site from the repository root:

```bash
mint dev
```

Open `http://localhost:3000`. Chinese is the default locale.

Validate the documentation before submitting changes:

```bash
mint validate
```

Pull requests also run this check in `.github/workflows/docs-validate.yml`. A broken `docs.json` entry or MDX frontmatter should fail CI.

## Content workflow

Read [AGENTS.md](AGENTS.md) before editing.

Every content change must:

1. verify product claims against the current `oceanbase/powercontext` code and tests;
2. update mirrored `zh/` and `en/` pages in the same work unit;
3. keep code blocks, commands, API names, maturity labels, and limitations aligned;
4. run `/humanizer-zh` for Chinese and `/humanize-writing` for English after technical review;
5. rerun technical and bilingual parity checks after the editorial pass;
6. run `mint validate` and inspect changed pages in the local preview.

RFCs explain design history. They are not evidence that a feature has shipped.

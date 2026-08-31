# PowerContext 101

PowerContext 101 is a bilingual Chinese and English tutorial site for PowerContext. It teaches the mental model, runnable API workflows, framework integration, and agent-host behavior. Complete contracts and deployment reference remain in the [official PowerContext docs](https://powercontext.oceanbase.io/).

The site is being written in stages. Start pages and selected Mental Model pages have full copy; remaining pages may still show an explicit `TODO` note. Navigation presence does not imply that a page is finished.

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

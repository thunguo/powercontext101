# PowerContext 101

[English](README.md) | [中文](README.zh-CN.md)

PowerContext 101 是 [PowerContext](https://github.com/oceanbase/powercontext) 的中英双语教程站。它教使用路径和集成边界：心智模型、可运行的第一条闭环、框架 adapter，以及 Agent 宿主合同。

安装参数、OpenAPI 契约和部署配置仍以 [PowerContext 官方文档](https://oceanbase.github.io/powercontext/)为准。本站不复制那份参考。当旧 RFC 与当前代码和测试冲突时，101 描述已经实现的行为。

站点默认语言是中文。本仓库 README 默认展示英文。

## 站点覆盖什么

先分清对象边界，再按你手头的工作走完一条路径。

**第一条闭环**是：写入一条 Memory，用 `search_memory` 找到它，再通过 `prepare_context` 得到带 Citation 的 `PreparedContext`。Source 抽取和 Handoff 留到这条闭环之后。

| 栏目 | 你读到什么 |
|---|---|
| 开始 | PowerContext 解决什么问题、按目标选的学习路径，以及只收本站已写症状的排错页 |
| 心智模型 | `Source`、`Memory`、`Handoff`、`Experience`、`Skill`、`Scope` 和 `fail-open` |
| 基础用法 | 安装本地 Server、跑 API 串讲、连接 MCP、用 Dashboard 看见刚写的 Memory，以及可选的 Source、Handoff 和 Review 路径 |
| 框架集成 | 第一次接入走 LangGraph 或 LangChain。Server 内的 Pydantic AI inference 只配置 generation 和 embedding，不是 Agent adapter。Pydantic AI Agent adapter 是 **Preview** |
| 通用 Agent | Hermes、OpenClaw、WorkBuddy、Agent Plugin，以及 managed Skill 自扩展。Hermes 和 OpenClaw 不能 export managed Skill |
| 编程 Agent | Codex、Claude Code、DSH、OpenCode 和 Pi，以及 Hook 合同、第六个宿主怎么立项 |

编程宿主页是 101 的验证合同，不是官方 how-to 的副本。多数真实 host E2E 是 **Not validated**。`setup` 和 `doctor` 不证明已经召回，也不证明活的宿主会话。安装参数看官方文档。

自动 recall、prompt capture 或可选 flush 失败时，宿主应继续原任务。显式 Memory 写入、Handoff commit、Candidate Review 和 Skill export 必须明确失败。

## 仓库结构

| 路径 | 作用 |
|---|---|
| `zh/` | 中文 MDX 页面 |
| `en/` | 英文 MDX 页面，相对路径与 `zh/` 镜像 |
| `docs.json` | Mintlify 导航、导航栏和主题 |
| `AGENTS.md` | 写作规则和事实优先级 |

## 本地预览

安装当前 Mintlify CLI：

```bash
npm install --global mint
```

在仓库根目录启动本地站点：

```bash
mint dev
```

打开 `http://localhost:3000`。预览跟随站点默认语言，首页是中文。英文入口是 `/en/start`。

## 校验

提交前检查导航和 MDX frontmatter：

```bash
mint validate
```

Pull request 会跑 `.github/workflows/docs-validate.yml` 里的同一项检查。

## 贡献

改页面前先读 [AGENTS.md](AGENTS.md)。

每一次内容改动都必须：

1. 用当前 `oceanbase/powercontext` 代码和测试核对产品事实；
2. 同一工作单元同时更新镜像的 `zh/` 和 `en/`；
3. 保持代码示例、命令、API 名、成熟度标签和限制一致；
4. 技术审查后再对中文页跑 `/humanizer-zh`，对英文页跑 `/humanize-writing`；
5. 润色后再核对上述技术事实；
6. 运行 `mint validate`，并在本地预览里打开改过的页。

中英页面都保留这些产品词：`Source`、`Memory`、`Handoff`、`Experience`、`Skill`、`Scope`、`Artifact`、`Revision`、`PreparedContext`、`Candidate`、`Review`、`fail-open`、`Work Contract`、`Task Outcome`。

集成能力只标 `Supported`、`Preview`、`Unsupported`、`Not validated`、`Host-gated` 或 `Version-gated`。不要合并这些状态。

RFC 解释设计历史。它不能证明功能已经上线。

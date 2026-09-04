# PowerContext 101 待办工作清单

审查基准：`main` @ `54b92ac`（2026-08-31），与 `origin/main` 同步。  
整理日期：2026-09-01。  
本文件在 `drafts/`，已被 `.mintignore` 排除，不会进入 Mintlify 发布站点。

用法：按 `Wxx` 逐项做。做完把状态改成 `done`，并在「完成记录」补 commit。  
一项未完成时不要同时开超过一个 P0。每个内容项必须中英同一工作单元改完。

---

## 工作规则（做任何一项前先读）

1. 中英 lockstep：`zh/<path>.mdx` 和 `en/<path>.mdx` 一起改；`docs.json` 两边导航一起改。
2. 产品词不要意译：`Source`、`Memory`、`Handoff`、`Experience`、`Skill`、`Scope` / `scope_id`、`Artifact`、`Revision`、`PreparedContext`、`Candidate`、`Review`、`fail-open`、`Work Contract`、`Task Outcome`。
3. 成熟度只用这六态，不要软化或合并：`Supported`、`Preview`、`Unsupported`、`Not validated`、`Host-gated`、`Version-gated`。
4. 证据顺序：`oceanbase/powercontext` 当前代码与测试 > OpenAPI > 官方 how-to / reference > RFC（仅背景）。
5. 自动 recall / capture / 可选 flush 可以 fail-open；显式 Memory 写入、Handoff commit、Review、Skill export 失败必须可见。
6. Candidate `version` 和 Artifact `Revision` 不是同一套并发域。bundled / managed / projected / external Skill 不要混用。
7. 不要复制官方 OpenAPI、RFC 或完整 how-to。不要把未发布 RFC 写成已实现。
8. 不要写本机绝对路径。代码块、命令、环境变量、API 名中英保持一致，只译周围说明。
9. 技术改完后再跑 `/humanizer-zh` 和 `/humanize-writing`；humanize 只动散文，之后必须回核第 3、4、5 条。
10. 本站说 `PowerContext 101`；官方站点说 `official docs` / `官方文档`。

对照范本：`zh/common-agents/hermes.mdx`（约 207 行）是「能跟做」的标杆。  
五个编程宿主页已按同一结构加深（W03）：约 143–180 行，含配置表、smoke、负向检查和完成检查。

---

## 建议开工顺序

先做能堵住读者断路和规则违规的项，再开新页。

| 顺序 | ID | 一句话 |
|---:|---|---|
| 1 | W01 + W02 | 把英文 coding-agents 总览 / hooks 补到中文同级 |
| 2 | W03 | 五个编程宿主页已写成 Hermes 同级（W03a–e 一次收口） |
| 3 | W05 | 改掉过时 README，避免后人误判完成度 |
| 4 | W04 + W06 | 修框架「下一页」和首页卡片承诺 |
| 5 | W08 + W09 + W10 | URL、六态标签、安装 ref 口径 |
| 6 | — | W03 其余宿主已并入本次收口 |
| 7 | W12 / W13 | MCP 或 Dashboard 短页（新页，要改导航） |
| 8 | W16 + W22 + W23 + W24 + W33 + W34 | 工程卫生、favicon、redirects，可与正文分 PR |
| 9 | W36 + W42 | 「怎么选 / 101 和官方听谁的」短页，官方 how-to 不会教 |

---

## 现状快照（方便对照，不是待办）

| 栏目 | 中英页数 | 典型篇幅 | 判断 |
|---|---:|---|---|
| 开始 | 2 / 2 | 92–105 行 | 可用，承诺和卡片需对齐 |
| 心智模型 | 7 / 7 | 140–316 行 | 完整概念栏，部分偏厚 |
| 基础用法 | 5 / 5 | 244–433 行 | 全站最完整的可运行教程 |
| 框架集成 | 6 / 6 | 168–355 行 | 完整，阅读顺序把 Preview 放太前 |
| 通用 Agent | 4 / 4 | 148–251 行 | 接近可发布 |
| 编程 Agent | 8 / 8 | 61–180 行 | 总览/hooks 已对齐；五个宿主页已写成可跟做教程（W03） |

中英路径 32 对完全镜像，页面内没有 `TODO`。  
目前唯一明显的行数失衡：

- `coding-agents/hooks-and-plugins.mdx`：中英节结构已对齐（W02）
- `coding-agents/overview.mdx`：中英节结构已对齐（W01）

最新提交 `54b92ac` 只改了英文 hooks 8 行，没有补中文，也没有把英文补到中文同级。

---

## P0：读者会断路，或已经违反维护规则

### W01 — 补齐英文编程 Agent 总览

- 状态：`done`
- 优先级：P0
- 类型：双语收口（先补英文）
- 文件：
  - `zh/coding-agents/overview.mdx`（对照源，原则上不删中文已有节）
  - `en/coding-agents/overview.mdx`（主要改这里）
- 现状：
  - 中文有 Handoff 行（Codex/Claude = MCP + Skill；DSH/OpenCode = curated HTTP；Pi = native tools）。
  - 中文有独立节「自动与显式路径」：Pi 无 UI 拒绝 durable write；DSH/OpenCode 走宿主 permission API；Codex/Claude Code 无 UI 拒绝行为是 **Not validated**。
  - 英文矩阵更短，缺上述两块。
- 要做：
  1. 英文矩阵补回 Handoff 行，列值与中文一致。
  2. 英文补「自动与显式路径」等价段落，保留六态词，不要意译成模糊句子。
  3. doctor / setup 不启动 Server、doctor 不等于 E2E，两边信息对齐。
- 完成标准：
  - 两边 `##` 节名对应（可翻译节名，不可缺节）。
  - 矩阵列数、行数、每个单元格的成熟度标签一致。
  - 代码块和命令完全相同。

### W02 — 补齐英文 Hooks 与插件合同

- 状态：`done`
- 优先级：P0
- 类型：双语收口（先补英文）
- 文件：
  - `zh/coding-agents/hooks-and-plugins.mdx`（对照源）
  - `en/coding-agents/hooks-and-plugins.mdx`
- 现状：
  - 中文约 6 个 `##`：Adapter contract、五种事件模型、安全合同、Capture 不等于 Memory、Setup 与 doctor contract、当前没有统一 HostAdapter SDK。
  - 英文约 2 个 `##`，安全 8 条、setup/doctor 6 条、可复用 helper 列表被压成两段。
  - `54b92ac` 只给英文加了 8 行，没有解决结构差。
- 要做：把英文按中文六节展开，不要把中文砍薄来「对齐」。
  - 安全合同 8 条必须逐条出现：Server down 继续；401/403 与 empty 可区分；unknown schema 不注入；oversize / timeout 有界；redirect 不泄漏 Authorization（只在实现明确拒绝的宿主承诺）；capture failure 不删除 valid recall；stale turn 不进入新 turn；diagnostics 不含 prompt / Scope / content / token。
  - Setup/doctor：版本门、幂等且保留 non-owned 配置、ownership、拒绝覆盖 foreign files、rollback 或 partial-failure、区分 installed / activated / Server running、bounded doctor + 真实 activation probe。
  - Helper 清单：`powercontext.transport`、Codex/Claude parser、Scope normalization、Pi flusher、DSH operation table、Skill projection、`hosts.py` catalog。明确写「没有统一 HostAdapter SDK」。
- 完成标准：英文读者按这一页能列出与中文相同的合同项；节结构同构。

### W03 — 把五个编程宿主页写成可跟做教程

- 状态：`done`
- 优先级：P0
- 类型：加深现有页（中英同步）
- 建议拆成 5 个连续工作单元，不要一次改五页：
  - W03a `zh/en/coding-agents/opencode.mdx`（建议最先：唯一标了真实 host E2E **Supported**，且 **Version-gated** `>=1.18.21,<2`）
  - W03b `zh/en/coding-agents/codex.mdx`（受众最大，当前最薄，约 42 行）
  - W03c `zh/en/coding-agents/claude-code.mdx`
  - W03d `zh/en/coding-agents/pi.mdx`（无 UI fail-closed 有教学价值）
  - W03e `zh/en/coding-agents/dsh.mdx`
- 对照结构（抄 Hermes，不要抄现在的 Codex）：
  1. 页首用一行复述该宿主关键状态（版本 / E2E / managed Skill export / permission 模型）
  2. 安装并激活：setup 改了哪些文件、会不会启动 Server
  3. 默认配置或关键文件（可粘贴片段，不是整份官方配置）
  4. doctor 查什么、不查什么
  5. 最小验证：在宿主里打哪句话、应看到 Citation / additional context / plugin message
  6. Scope 怎么解析
  7. 自动路径 vs 显式工具 / MCP
  8. 负向检查的预期现象（停 Server、显式写入失败、permission deny）
  9. 限制与完成检查
- 学习路径完成标志必须能在该页落地：
  - 自动 recall 失败时普通编码任务仍继续
  - 显式 Memory 或 Handoff 失败时宿主把错误告诉你
- 每页还应补学习路径那道统一题：「修改 OpenAPI 契约后，下一步应该做什么？」在该宿主里怎么存、怎么召回、怎么验证 Citation 通道。
- 注意：
  - `powercontext setup claude-code` 用连字符；Skill export target 是 `claude_code`。不要混。
  - bundled `project-context` Skill ≠ managed Skill export。OpenCode / DSH / Pi 的 export 是 **Unsupported**。
  - Codex / Claude Code 真实 host-process E2E 现为 **Not validated**，不要写成已经测过。
  - 不要粘贴官方 how-to 整章；只写 101 的验证步骤和边界。
- 完成标准：单页厚度接近 Hermes（配置表 + smoke + 负向 + 完成检查），读者不读源码也能做完学习路径该 Tab。

### W04 — 修正框架栏目阅读顺序

- 状态：`done`
- 优先级：P0
- 类型：导流修正
- 文件：
  - `zh/frameworks/overview.mdx`
  - `en/frameworks/overview.mdx`
  - 可选：`zh/start/learning-path.mdx`、`en/start/learning-path.mdx`（只在需要互相点名时）
- 现状：
  - 学习路径「我写 Python Agent」：先 Client，再选 LangGraph 或 LangChain；Pydantic AI Agent adapter 是 Preview，不要第一次接入。
  - `frameworks/overview.mdx` 文末「下一页」却先送进 `pydantic-ai-server-inference`，该页文末再送进 `pydantic-ai`（Preview、当前装不上），然后才到 LangGraph。
  - `docs.json` 导航顺序也是 Server inference → Preview adapter → LangGraph → LangChain。
- 要做（选一种，不要两套口径）：
  - 推荐 A：总览「下一页」改为 LangGraph（或一张「第一次接入选 LangGraph / LangChain」卡），Server inference / Preview 改成「需要时再读」。
  - 或 B：保留导航顺序，但总览用明确 Warning + 两列决策（可安装的第一次接入 / 不要当第一页的 Preview），并改文末下一页链接。
- 完成标准：按「下一页」走的 Python 读者，不会先撞上「当前没有可用安装命令」的 Preview 页。

### W05 — 更新 README 完成度说明

- 状态：`done`
- 优先级：P0
- 类型：仓库说明（README 被 mintignore，但仍是贡献者入口）
- 文件：`README.md`
- 现状第 5 行仍写：Start 和部分 Mental Model 有正文，其余页可能还有 `TODO`；导航在不代表写完。
- 实际：六大栏目都有正文，MDX 里已无 `TODO`。真正没写完的是编程宿主页深度，不是 stub。
- 要做：改成按栏目的诚实状态，至少写明：
  - 心智模型 / 基础用法 / 框架 / 通用 Agent：已有完整正文
  - 编程 Agent：合同和矩阵已有，宿主页仍是摘要，学习路径完成标志尚未落地
  - 官方文档入口用最终选定的 URL（与 W08 一起改）
- 完成标准：新贡献者读 README 不会以为全站还是 stub，也不会以为编程 Agent 已经能跟做完。

---

## P1：栏目不完整，或读者会反复问

### W06 — 对齐首页卡片与「第一次接触」路径

- 状态：`done`
- 完成记录：`3345e86` 方案 A，首页 / 学习路径 / install-and-run 统一为 Memory → `search_memory` → `PreparedContext`
- 优先级：P1
- 类型：承诺对齐
- 文件：
  - `zh/start/index.mdx`
  - `en/start/index.mdx`
  - `zh/start/learning-path.mdx`
  - `en/start/learning-path.mdx`
- 现状：
  - 首页「跑通常用 API」卡片：完成 Memory、Source 和 Handoff 的第一条闭环，链到 `install-and-run`。
  - 学习路径「第一次接触」完成标志只到 `remember_memory` → `search_memory` → `prepare_context`。
- 要做（二选一，中英一起改）：
  - A：卡片改成只承诺 Memory / PreparedContext，与现 Tab 一致。
  - B：给「第一次接触」加可选第二段：`source-and-memory` → `handoff-loop`，卡片保持 Source + Handoff。
- 完成标准：首页、学习路径、`install-and-run` 三处对「第一条闭环」的描述相同。

### W07 — 学习路径补上已写完但未点名的加长线

- 状态：`done`
- 完成记录：`5dee2e6` 五个 Tab 都加了可选加长路径，未改完成标志
- 优先级：P1
- 类型：导流
- 文件：`zh/start/learning-path.mdx`、`en/start/learning-path.mdx`
- 现状：Tabs 只点名部分页。心智模型的 source / memory / handoff / experience-and-skill，以及 `source-and-memory`、`handoff-loop`、`experience-skill-review`、`frameworks/tricks` 已经写完，读者只能靠栏目「下一页」碰到。
- 要做：每个 Tab 下加「加长路径」小节，明确可选，不要把加长线写成必做完成标志。
- 完成标准：扫描型读者知道站点还有这些页，且知道它们不是第一次接触的验收条件。

### W08 — 统一官方文档 URL

- 状态：`done`
- 完成记录：`57bdc8a` 正式入口取 `oceanbase/powercontext` 的 `site_url`：`https://oceanbase.github.io/powercontext/`
- 优先级：P1
- 类型：外链正确性
- 先确认哪个是正式入口，再全站替换，不要两套都留着当「都行」。
- 当前分裂：
  - `https://oceanbase.github.io/powercontext/`：`AGENTS.md`、`docs.json` 的 Official Docs anchor
  - `https://powercontext.oceanbase.io/`：`README.md`、`zh/en/start/index.mdx`、`zh/en/start/learning-path.mdx`
- 要改文件（确认后）：
  - `AGENTS.md`
  - `docs.json`
  - `README.md`
  - `zh/start/index.mdx`
  - `en/start/index.mdx`
  - `zh/start/learning-path.mdx`
  - `en/start/learning-path.mdx`
  - 以及正文里所有「官方文档」链接（改前再 grep 一次）
- 完成标准：全库只剩一个官方文档 URL；中英 start 页、navbar anchor、AGENTS.md 一致。

### W09 — 中文框架页成熟度标签改回六态

- 状态：`done`
- 完成记录：`5ff4408` pydantic-ai 两页状态表改回粗体 `Unsupported` / `Not validated`
- 优先级：P1
- 类型：术语 / 标签
- 文件：
  - `zh/frameworks/pydantic-ai-server-inference.mdx`（「当前不支持或尚未验证」表：不支持 / 本页未验证）
  - `zh/frameworks/pydantic-ai.mdx`（同上）
  - 对照保持英文标签的：`zh/frameworks/langgraph.mdx`、`langchain.mdx`、`tricks.mdx`、`overview.mdx`
- 要做：状态表改回粗体英文六态，中文只解释含义。不要把 `Unsupported` 写成「不支持」、把 `Not validated` 写成「尚未验证」后不再标英文态。
- 完成标准：框架栏目中英状态表用同一套词；`Unsupported` 与 `Not validated` 仍能一眼分开。

### W10 — 写清安装 ref 策略

- 状态：`done`
- 完成记录：`6e230a6` install-and-run 区分 `master` / pin；三处框架页统一完整 hash
- 优先级：P1
- 类型：口径统一
- 现状：
  - `@master`：`install-and-run`、Hermes、OpenClaw、coding-agents setup
  - 短 hash `4213d32`：`pydantic-ai-server-inference`
  - 完整 hash `4213d32d672a6fb16e74730eb50b9be6a38bcb10`：LangGraph / LangChain
- 要做：
  1. 在 `install-and-run`（中英）用一小段说清：本地学习可以跟文档里的 ref；可复现部署必须 pin 同一 commit，且 CLI / Server / 宿主 plugin 用同一个 ref。
  2. 框架页统一用完整 commit hash，或统一声明「此处 pin 与 Server inference 页相同」。
  3. 不要在同一栏目混用短 hash 和长 hash 而不说明它们是同一个对象。
- 完成标准：读者知道什么时候用 `master`、什么时候 pin；三处框架安装命令的 ref 写法一致。

### W11 — 给 Agent 自扩展补交叉入口

- 状态：`done`
- 完成记录：`a36e74e` 页首 Warning、文末 Codex/Claude 卡，总览与两个宿主页回链
- 优先级：P1
- 类型：导航 / 交叉链接
- 文件：
  - `zh/common-agents/agent-self-extension.mdx`
  - `en/common-agents/agent-self-extension.mdx`
  - `zh/common-agents/overview.mdx`
  - `en/common-agents/overview.mdx`
  - 可选：`zh/en/coding-agents/codex.mdx`、`claude-code.mdx`、`docs.json`
- 现状：页挂在「通用 Agent」下，但 managed export 目标只有 Codex / Claude Code。OpenClaw 读者点进来会走一段他们导不出去的路径。页内已有职责分离 Warning，菜单位置仍容易误导。
- 要做（不必挪栏目，除非你决定改导航）：
  - 页首加：Hermes / OpenClaw 不能 managed export；做完 Review 后要换 Codex 或 Claude Code。
  - 文末卡链到两个编程宿主页。
  - 两个编程宿主页回链自扩展页。
- 完成标准：OpenClaw 路径的人在点进该页 10 秒内知道自己不能 export。

### W12 — 新增 MCP 使用短页

- 状态：`done`
- 完成记录：`2799417` 新增中英 `basic-usage/mcp`，导航和 API 串讲 / 学习路径已回链
- 优先级：P1
- 类型：新页（必须同时加中英文件和两边导航）
- 建议路径：
  - `zh/basic-usage/mcp.mdx`
  - `en/basic-usage/mcp.mdx`
  - `docs.json` 两边「入门闭环 / First loop」组
- 为什么要写：安装页、API 串讲、编程 Agent 都提到 `/mcp`，但没有一页讲「用 MCP 客户端连上 Server、能调哪些工具、和 HTTP / Python Client 差在哪」。这是 101 该写、官方契约页替代不了的内容。
- 建议目录：
  1. MCP 是精选工具面，不是完整 HTTP API
  2. 默认地址 `http://127.0.0.1:8000/mcp`
  3. 可粘贴的最小客户端配置（不要写成本机路径）
  4. 能做 / 不能做
  5. 开启 Bearer 后 discovery route 也要带 header
  6. 完成检查
- 完成标准：学习路径或 API 串讲能链到这一页；中英同时进导航。

### W13 — 新增 Dashboard 最小路径短页

- 状态：`done`
- 完成记录：`8801fb7` 新增中英 `basic-usage/dashboard`，安装页 / API 串讲 / Scope / 学习路径已回链
- 优先级：P1
- 类型：新页
- 建议路径：
  - `zh/basic-usage/dashboard.mdx`
  - `en/basic-usage/dashboard.mdx`
- 现状：`install-and-run` 提到 Dashboard 空状态；`mental-model/scope.mdx` 有「写入成功但 Dashboard 看不到」。没有一页带读者走通：配 Scope → 看到刚写的 Memory → 理解它不是另一套数据库。
- 建议只写最小路径，不要做成产品手册：
  - 默认 `/`
  - 未配置 Scope 时的空状态
  - 与 Client 使用同一个 `scope_id` 和同一个 database URL
  - Dashboard 初始化失败只打 warning，HTTP / MCP 仍可用
  - configured Dashboard publication ≠ CLI export（细节已在自扩展页，这里只点一下并外链）
- 完成标准：第一次接触读者能用 Dashboard 看见 `api-tour` 刚写入的 Memory。

### W14 — 把统一验收题落到每条路径结尾

- 状态：`done`
- 完成记录：`3fadfb3` Hermes / OpenClaw / 五个编程宿主页各用宿主工具重写 5 步；学习路径回指这些页
- 优先级：P1
- 类型：教学收口
- 文件：Hermes、OpenClaw、以及 W03 加深后的五个宿主页；必要时 `learning-path.mdx`
- 统一题（已在学习路径）：「修改 OpenAPI 契约后，下一步应该做什么？」
  1. 在固定 Scope 显式保存答案
  2. 换请求或新会话再问
  3. 召回带 Citation，且只按该 adapter 约定进入模型输入
  4. 停 Server 后再问：自动 recall 可失败，原任务继续
  5. 显式写入必须明确失败
- 要做：每条宿主路径用该宿主的语言重写这 5 步（Hermes 用 `/pc` 或 tool，Codex 用 MCP，OpenClaw 用五工具），不要只重复学习路径原文。
- 完成标准：五条读者路径的完成标志都可以在对应页上逐步做完。

### W15 — 新增集中排错短页

- 状态：`done`
- 完成记录：`3da1c04` 新增中英 `start/troubleshooting`，只收已有症状并回链原页
- 优先级：P1
- 类型：新页
- 建议路径：
  - `zh/start/troubleshooting.mdx` 或 `zh/basic-usage/troubleshooting.mdx`
  - 对应英文页 + `docs.json`
- 收纳已散落的故障和误用症状，不要新编案例：
  - Scope 字面值不一致
  - 换了 `POWERCONTEXT_HOME` / database URL，看起来像 Scope 丢了
  - 401/403 被当成 `empty`
  - capture 成功但搜索不到 Memory（把整段 prompt 当成已经进了 Memory）
  - doctor 通过但召回失败
  - Dashboard 空、数据其实在
  - Preview adapter 当前装不上
  - bundled `project-context` Skill 被当成 managed Skill export
  - Candidate `version` 和 Artifact `Revision` 当成同一个版本号时的冲突症状
  - 「Preview and make no writes」却调用 `handoff_current_work`（会写 boundary Source）
  - Server down 时期待自动 recall 报错，或以为显式写入可以 fail-open
- 完成标准：101 口吻，一页一条路径；链回原页，不写成百科。更完整的误用课见 W38。

### W16 — 加上 `mint validate` CI

- 状态：`done`
- 完成记录：`5d9699b` 新增 `.github/workflows/docs-validate.yml`，只跑 `mint validate`
- 优先级：P1
- 类型：工程
- 现状：没有 `.github/`。README 要求提交前 `mint validate`，远端不会拦。
- 要做：
  1. 加一个只跑文档校验的 workflow（安装 Mintlify CLI，在仓库根执行 `mint validate`）。
  2. 可选第二 job：链接检查（lychee 或同类），至少覆盖官方文档 URL 和本语内链。当前 `docs.json` 与 Start 页的官方 URL 分裂不会被自动抓住，`54b92ac` 那种单语提交也不会被挡。
- 完成标准：PR 改坏导航或 MDX frontmatter 时 CI 红。链接检查可以后加，不要和正文大改混在一个 PR。不要在这一项里顺便加无关 lint / spellcheck。

### W17 — 加深「用 Hooks 扩展」

- 状态：`done`
- 完成记录：`5b7fb3b` 在 checklist 前补「第六个宿主怎么立项」，点名现有测试模块和 `FIRST_CLASS_HOSTS`
- 优先级：P1
- 类型：加深现有页
- 文件：`zh/en/coding-agents/extend-hooks.mdx`（两边目前约 63 行）
- 要做：在现有 checklist 前加一条「第六个宿主怎么立项」的路径：
  1. 先发现宿主 capability（prompt event、injection、permission、version probe）
  2. 对照至少两个现有宿主（链到 W02 / W03）
  3. 测试分层：unit contract / service-chain / setup-doctor / real-host E2E / 负向安全
  4. 何时才能进 first-class catalog
- 可点名现有测试模块名，不要写本机绝对路径，不要虚构 HostAdapter SDK。
- 完成标准：集成作者读完知道先写什么测试，而不是先抄 `/v1/context/prepare`。

### W18 — 编程宿主可粘贴配置与验证片段

- 状态：`done`
- 完成记录：`f1545a5` Codex/Claude `.mcp.json`、DSH `ask` 序列、OpenCode session 清理、Pi `confirmation_required` 均可逐步对照
- 优先级：P1
- 类型：可并入 W03，若 W03 做浅了再单开
- 缺且最值得补：
  - Codex / Claude Code：`.mcp.json` 应有哪些字段、hook 注册后在 `/hooks` 和 `/mcp` 应看到什么
  - DSH：`/pc review` 与 `tools/pre-execute` 的 `ask` 最小操作序列
  - OpenCode：发一条、看 exact-turn transform、删 session 后不再注入 stale context
  - Pi：无 UI 时稳定返回 `confirmation_required` 的复现方式
- 完成标准：每页至少有一块读者能直接粘贴或逐步对照的验证，而不是只有子弹列表。

### P1 整体审查

- 状态：`done`
- 完成记录：`31f96f2` 审查 W06–W18 后只修了两处遗留：
  - `api-tour` 删掉已关闭的 `/redoc`，Bearer 口径与 `_PUBLIC_PATHS` / MCP 页对齐（`/docs` 公开，`/openapi.json` 要 header）
  - 中文 `experience-and-skill` 不再把「第一条闭环」写成覆盖全部对象
- 抽查：中英 37/37 镜像；官方文档 URL 只剩 `https://oceanbase.github.io/powercontext/`；框架 pin 均为完整 hash；新页 MCP / Dashboard / 排错导航齐全；本地预览关键页 200

---

## P2：可增强，不挡主路径

### W19 — WorkBuddy / Bub 的「为什么没有专页」

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/common-agents/overview.mdx`，必要时 `learning-path.mdx`
- 现状：学习路径 Info 已声明 101 不维护这两条路径。读者若搜索名字仍可能落空。
- 要做：总览加两张短卡：WorkBuddy 去官方 how-to；Bub 去 integration-local README。保持 **不是** first-class 路径，不要新开专页除非产品状态变了。
- 不要做：把它们写成和 Hermes 同级的 101 教程。

### W20 — 版本钉死 cookbook 短页或短节

- 状态：`todo`
- 优先级：P2
- 可做成 `basic-usage` 一小节，或并入 W10，不必单独成栏目。
- 内容：CLI、Server、宿主 plugin 如何钉同一 ref；`uv tool install --force` 的更新含义；可变 `master` 作为 release input 的可复现性是 **Not validated**。

### W21 — 术语对照短页（可选）

- 状态：`todo`
- 优先级：P2
- 只做「这些词不要互相替换」一页，不要扩成术语百科。
- 必须覆盖：Source ≠ Memory；PreparedContext ≠ 持久历史；Prepared Handoff ≠ committed Revision；Candidate version ≠ Artifact Revision；bundled Skill ≠ managed export；fail-open 的适用范围。

### W22 — 更换 LICENSE 版权声明

- 状态：`todo`
- 优先级：P2
- 文件：`LICENSE`
- 现状：仍是 Mintlify 起步模板版权（Copyright (c) 2026 Mintlify）。
- 要做：改成本仓库实际版权方（需你确认法律主体后再改，不要猜）。

### W23 — 补 `.gitignore`

- 状态：`todo`
- 优先级：P2
- 现状：仓库没有 `.gitignore`。`.mintignore` 只影响 Mintlify 发布，不影响 git。
- 建议忽略：`node_modules/`、`.mintlify/`、编辑器目录、OS 垃圾文件。不要忽略 `drafts/`，除非你决定工作清单不进 git。

### W24 — `docs.json` 发布抛光

- 状态：`todo`
- 优先级：P2
- 文件：`docs.json`
- 要处理：
  1. 根级 `navbar.primary` 现在是中文「开始学习」→ `/zh/start/learning-path`。语言块里已有中英各一份。英文用户若落到根 navbar，可能被送进中文页。
  2. 根级 `search.prompt` 只有「搜索」，英文界面也会看到。按语言覆盖 `search`。
  3. `navigation.global.anchors` 只有英文 `Official Docs` / `GitHub`。中英各写一套，或至少中文界面不要只显示英文锚点。
  4. 站点级 `description` 只有中文。英文语言块补自己的 description。
  5. 没有 `seo` / Open Graph 图 / `twitter:image`（仓库也没有 `og/` 社交图）。
  6. footer 只有全局 `socials`，没有 `footer.links`，也没有按语言拆「官方文档 / 学习路径 / Discord」。
  7. `AGENTS.md` 要求 navbar **和 footer** 两边一起改；目前只覆盖了语言内 navbar 按钮。
- 页面 `keywords` / `icon` 目前只有 Start 两页有，其余约 60 个 MDX 没有。不要为凑 SEO 给每页堆关键词；若做，优先各栏目 overview。见 W48。
- 不要靠大段自定义 CSS 修 Mintlify DOM。品牌色已在 `docs.json`，`style.css` 应继续保持极简。

### W25 — 心智模型过厚处收一收（可选）

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/mental-model/memory.mdx`、`source.mdx`；`zh/en/common-agents/hermes.mdx` 的 extended tool 全名单
- 现状：对象边界写得很清楚，但 Memory 检索实现（RRF=60、builder 上限 16/8/8/2/2000 bytes）、Source Trigger/window、Hermes 工具全名单已经接近 reference。
- 要做：能外链官方文档的实现常数，101 只留「为什么你会踩到」；工具名单改成「面有哪些、和 OpenClaw 五工具差在哪」。
- 完成标准：概念页仍能教对象边界，不再像实现说明书。做完必须回核数字和 API 名仍然正确。

### W26 — 基础用法页与页之间把 ID 传下去

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/basic-usage/*.mdx`
- 现状：心智模型说「本站会保留这些值」。五页都围绕同一 OpenAPI 例子，但读者要把上一页的 `artifact_id` / Source ID 自己抄到下一页。`experience-skill-review` 后半是「替换 `SCOPE_ID` 再跑」。
- 要做：每页开头用 3 行列出「你现在应该已经有这些 ID」；考虑把 propose 流程收成「一条 Python + 一组 CLI」两段。
- 不要发明新故事线，继续用「修改 OpenAPI 契约」。

### W27 — API 串讲补学习路径第 4–5 步负向脚本

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/basic-usage/api-tour.mdx`
- 要做：在现有 `api_tour.py` 之后加「停 Server 再 `prepare_context` / 显式写入必须失败」的 Client 侧步骤，对齐学习路径验收第 4、5 步。
- 完成标准：第一次接触 Tab 的完成标志可以全部在 Client 上做完，不必先接宿主。

### W28 — Hermes / OpenClaw「换会话再召回」逐步脚本

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/common-agents/hermes.mdx`、`openclaw.mdx`
- 现状：有 smoke 和 doctor，学习路径完成标志要「新会话召回你显式保存的 Memory」，页上没有逐步脚本。
- 要做：补 5–8 步：写入 → 结束会话 → 新开 → 问同一句 → 应看到 Citation。写明 doctor 通过 ≠ 这一步已经成立（host E2E 仍是 **Not validated**）。

### W29 — 技术稳定后的文风 pass

- 状态：`todo`
- 优先级：P2
- 时机：至少 W01–W04、W03 第一宿主完成后再做，不要先改语气再改事实。
- 做法：中文 `/humanizer-zh`，英文 `/humanize-writing`。只动散文。
- 回核清单：API 名、命令、版本、六态标签、限制、能力矩阵、官方 URL。
- 不要为了好读编经历、统计或评价。

### W30 — 框架页「从 api_tour.py 迁过去」

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/frameworks/langgraph.mdx`、`langchain.mdx`
- 要做：各补一段「已经跑通 `api_tour.py` 的人，最少改哪几行接到这个 adapter」。`model` / `my_checkpointer` / `application_tools` 现在是占位符，可加 model-free 的 assert（只检查 `llm_input_messages` 或当前 request 的 `system_message`）。
- 呼应页内已有的「先做 model-free 检查」。

### W31 — 交叉链接补强（无新页）

- 状态：`todo`
- 优先级：P2
- 建议补的链（做的时候再核对是否已存在，避免重复）：
  - `mental-model/overview.mdx` 文首加卡：先读 Scope 和 fail-open（学习路径要求，文末才提）
  - 心智模型四对象页文末加「去 basic-usage 跑同一对象」
  - `mental-model/fail-open.mdx` → 各宿主负向检查
  - `coding-agents/codex.mdx` ↔ `basic-usage/handoff-loop.mdx`、`experience-skill-review.mdx`
  - `handoff_current_work` 不是零写 preview：mental-model、handoff-loop、Codex 已写，其他编码宿主回链过去

### W32 — 文档对应的 PowerContext ref / changelog

- 状态：`todo`
- 优先级：P2
- 现状：没有 changelog，也没有「这版 101 对着上游哪个 commit」的说明。
- 要做：README 或 start 页加一行当前文档验证过的上游 ref；以后改安装命令时更新这一行。不要做成产品 changelog 百科。

### W33 — 更换 starter favicon

- 状态：`todo`
- 优先级：P2
- 文件：`favicon.svg`
- 现状：仍是 `17203bc` 的绿色 Mintlify starter 标，和 `logo/light.png` / `logo/dark.png` 不是一套。
- 要做：换成与 PNG logo 同一套的 SVG（或 PNG）。不要只改 `docs.json` 路径而不换文件。
- 完成标准：浏览器标签图标与站点 logo 视觉一致。

### W34 — 补齐旧路径 redirects

- 状态：`todo`
- 优先级：P2
- 文件：`docs.json` 的 `redirects`
- 现状：已有 `/zh`、`/zh/index`、`/zh/learning-path` 及英文对等项。没有：
  - `/` → `/zh/start`（现在依赖 Mintlify 默认语言，未写死）
  - `/quickstart`、`/index`（starter 旧路径，`adf2fc3` 删了文件但没留 redirect）
  - `/docs`、`/zh/docs` 这类从官方站习惯打出来的路径（若决定做，只重定向到学习路径，不要假装 101 有官方 docs 树）
- 完成标准：旧 starter URL 和语言根路径都落到 `zh/start` 或 `en/start`，不 404。

### W35 — 各栏目 overview 补 `<Visibility for="agents">`

- 状态：`todo`
- 优先级：P2
- 现状：只有 `zh/en/start/index.mdx` 有 agent 路由块。其他 tab 的 overview 没有。
- 要做：在 `mental-model/overview`、`basic-usage/install-and-run` 或各栏目 overview 加对本栏的路由：概念 / 安装 / 框架 / 通用 Agent / 编程 Agent，以及「契约去官方文档」。
- 完成标准：Agent 从任一栏目入口进来，不会只看到 Start 页的路由表。

### W36 — 「怎么选一条路 / 什么时候不该用」短页

- 状态：`todo`
- 优先级：P2
- 类型：新页（官方 how-to 不会教选题）
- 建议路径：`zh/start/choose-a-path.mdx`、`en/start/choose-a-path.mdx`
- 要写：
  - 六个 tab 怎么只选一条，选错了会怎样，什么时候该回头
  - 什么时候不该用 PowerContext（vs 聊天记录、vs 向量 RAG、vs 旧 PowerMem）。只写决策边界，不写迁移百科（PowerMem 见 W46）
  - 无模型闭环 vs 上 generation/embedding：什么信号说明该升配；升配细节外链官方
  - Hermes 全表面 vs OpenClaw 仅 Memory：我的 Agent 只需要召回时选谁
- 不要做成产品对比软文。完成标准：读者能在一页内选出学习路径的一个 Tab。

### W37 — 编程宿主「怎么选」写成课，不要只留矩阵

- 状态：`todo`
- 优先级：P2
- 可并入 W01 / W03，若总览加深后仍只有表，再单开。
- 文件：`zh/en/coding-agents/overview.mdx`
- 要做：在矩阵下用决策树写清选错成本。例如需要 Hook + MCP + project Skill → Codex / Claude Code；需要真实 host E2E 证据 → OpenCode；需要无 UI fail-closed → Pi。宿主逐步操作已在 W03 各页落地，本项只补总览决策树。
- 不要复制官方逐宿主安装 how-to。

### W38 — 常见误用对照练习（可选独立页）

- 状态：`todo`
- 优先级：P2
- 若 W15 已经把症状写清楚，本项可标 `cancelled` 并回指 W15。
- 独立成页的理由：排错页是「坏了怎么查」，误用页是「你以为对、其实对象错了」。
- 建议只做 4–6 个对照，每个：错误做法 → 你看到的症状 → 正确对象 → 链回心智模型 / basic-usage。
- 禁止扩成百科。

### W39 — 向读者解释 `Not validated` 和「HTTP chain ≠ real-host E2E」

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/coding-agents/overview.mdx` 或 `extend-hooks.mdx`；必要时 start 短节
- 现状：标签用了很多，没有读者向的风险说明。DSH 页提到 `test_dsh_http_chain.py` 不是完整宿主 E2E，没有推广成通用课。
- 要做：用 101 口吻说明：`Not validated` 不是 `Unsupported`；只测 HTTP chain 不能证明真实宿主 injection / permission UI / 跨会话；生产上这意味着什么。
- 完成标准：读者不会把 doctor 通过或标签 Supported 以外的状态当成已经上线。

### W40 — Workstream 短说明

- 状态：`todo`
- 优先级：P2
- 现状：Workstream 散落在 Codex / Hermes，心智模型没有专页。
- 要做：优先在 `mental-model/scope.mdx` 加一节，而不是新开第七个概念页。讲清它解决什么、和 `scope_id` 的关系、两个宿主如何共享。细节外链官方。
- 不要写成 Workstream API 参考。

### W41 — 用 curl 走同一道验收题

- 状态：`todo`
- 优先级：P2
- 文件：`zh/en/basic-usage/api-tour.mdx` 一节即可，不必新页
- 现状：API 串讲说 HTTP 是完整契约，却只带 Python Client 走路。非 Python 读者会问。
- 要做：用同一道题（写入 Memory → search → prepare）给一组 curl，证明和 Client 打的是同一 Server。不要复述 OpenAPI 全表。
- 完成标准：不会 Python 的人也能完成第一次接触的完成标志。

### W42 — 「101 和官方冲突时听谁的」读者短页或短节

- 状态：`todo`
- 优先级：P2
- 现状：只在 `AGENTS.md` 和 Start 的 Info 里。读者向说明不够。
- 要做：在 `zh/en/start/index.mdx` 或学习路径加可见短节：实现和测试 > 官方正式文档 > RFC；101 教路径和验证，契约以官方为准；两套官方 URL 以 W08 选定的为准。
- 完成标准：不读 `AGENTS.md` 的人也能知道听谁的。

### W43 — Windows / WSL 已知边界页（不是安装变通）

- 状态：`todo`
- 优先级：P2
- 与「明确不做：Windows 安装变通」不冲突。本页只写边界：
  - 文档化目标是 macOS / Linux
  - 状态是 **Not validated**
  - 请用官方环境要求
  - Scope 页已提到 Windows drive-letter 不要被当成 SCP remote，这里回链
- 不要提供未跑过的 workaround。若以后真的验证了 WSL，再另开项。

### W44 — 换机器 / SQLite / 多宿主共用一台 Server

- 状态：`todo`
- 优先级：P2
- 部署细节属于官方。101 只讲坑：
  - 换电脑后 Scope 为什么对不上（路径 hash / Git remote / 换了 database URL）
  - 默认 SQLite 在用户数据目录，不是仓库里
  - 多台编码 Agent 连同一 Server 时，Scope 必须显式且一致
- 建议落在 `install-and-run` 或 W15，不要新开部署栏目。

### W45 — PowerMem 只做分流指针

- 状态：`todo`
- 优先级：P2
- 现状：101 完全没碰。官方 / PyPI 会提到升级关系，没有迁移教程。
- 要做：最多在 W36 或 start 加一句「这不是 PowerMem 迁移指南，升级关系看官方」。不要写迁移步骤，除非代码和测试证明有受支持的迁移路径。

### W46 — 页面 keywords / icon 只补 overview

- 状态：`todo`
- 优先级：P2
- 现状：`keywords` 和 `icon` 只有 Start 四页（中英 index + learning-path）。
- 要做：给六个栏目的 overview 补 `icon`（与 `docs.json` tab icon 一致即可）。`keywords` 可补产品词，不要给每页堆长尾词。
- 完成标准：侧栏和页面标题图标一致；不要为 SEO 改正文口径。

### W47 — CONTRIBUTING 短说明（可选）

- 状态：`todo`
- 优先级：P2
- 现状：没有 `CONTRIBUTING.md`。工作流写在 README 和 `AGENTS.md`。
- 要做：若要加，只写：读 `AGENTS.md`、中英同改、`mint validate`、不要抄官方。不要和本工作清单抢「做什么」的位置。

### W48 — 仓库未记录部署方式

- 状态：`todo`
- 优先级：P2
- 现状：无 CNAME、无 netlify/vercel 配置、无 `package.json` 钉住 Mint CLI 版本。本地 `mint` 版本不可复现。
- 要做：在 README 写清「用全局 `mint` 预览，发布在哪」；若需要可复现，再加 `package.json` 钉 CLI 版本。部署账号和密钥不要进仓库。

---

## 明确不做（除非产品状态变了）

这些在审查里出现过，但当前 101 已主动划界。不要当成遗漏去补。

| 主题 | 原因 |
|---|---|
| Windows 安装变通 | 学习路径和 `install-and-run` 已标明不提供未验证路径。只允许 W43 那种边界说明。 |
| WorkBuddy / Bub 完整 101 路径 | 学习路径已声明本版不维护。只允许 W19 那种指针。官方 WorkBuddy 已有 how-to，101 不要再写。 |
| 逐宿主官方安装 how-to | 官方 `how-to` 已覆盖 Codex / Claude Code / DSH / Pi / OpenClaw / OpenCode / Hermes 等。101 只教事件差异、负向检查、共享 Scope，不要抄安装章节。 |
| 完整配置、部署、鉴权、健康检查、OpenAPI 全表 | 属于官方 reference / how-to。 |
| 官方排障手册、full-capability runtime、Handoff Report、Phoenix/OTLP | 官方已有或属于运维参考。101 只在踩坑时外链。 |
| 复制官方 Codex tutorial | 官方 `tutorials/codex-quickstart` 已是完整安装教程。W03 加深的是 101 的验证合同，不是把那篇搬过来。 |
| 把 RFC 目标写成已发布 | 禁止。 |
| 第七个顶层栏目 | 主路径洞还在编程 Agent，先不要扩站。 |
| 靠 CSS 修 Mintlify 组件 DOM | `AGENTS.md` 禁止。 |
| 为了好读编用户故事或统计 | 禁止。 |

---

## 新页时的导航清单

只要新增或重命名页面，必须一次做完：

1. `zh/<tab>/<name>.mdx`
2. `en/<tab>/<name>.mdx`
3. `docs.json` 中文对应 group
4. `docs.json` 英文对应 group
5. 本语内链（不要 `/zh` 链到 `/en`）
6. 若旧 URL 会失效：加 `redirects`

Tab 必须落在 `zh/<tab>/...`、`en/<tab>/...`，不要把页面放到 `zh/index` 或 `en/index`。

---

## 完成记录

| ID | 日期 | commit | 备注 |
|---|---|---|---|
| W01 | 2026-09-01 | 553f5ea | 英文总览补齐 Handoff 行与「自动与显式路径」；Setup/doctor 明确不等于 E2E |
| W02 | 2026-09-01 | 60fad37 | 英文 Hooks 按中文六节展开；安全 8 条、setup/doctor 6 条、helper 7 项逐条可见 |
| W03 | 2026-09-01 | 未提交 | 五个宿主页按 Hermes 结构写成可跟做教程；事实核自本地 `oceanbase/powercontext` 实现与测试 |
| W04 | 2026-09-01 | 3640555 | 采用推荐 A：总览下一页改为 LangGraph / LangChain 卡；导航拆成「第一次接入」与「需要时再读」 |
| W05 | 2026-09-01 | d4cb144 | README 按栏目写诚实状态；官方入口改为 github.io；编程 Agent 标明 101 合同与 E2E Not validated |

审查来源：2026-09-01 对 `main` @ `54b92ac` 的只读审查（内容完成度 + 提交/配置/官方选题对照）。  
W33–W48 为第二轮工程与选题审查补入，不改变 W01–W03 的优先顺序。  
后续若上游 PowerContext 行为变化，先核代码和测试，再改本清单里的「现状」和完成标准。

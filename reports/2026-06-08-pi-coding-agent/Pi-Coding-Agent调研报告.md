# Pi Coding Agent：极简、可扩展的终端 Agent Harness

## 一句话概括

Pi Coding Agent 是 Mario Zechner 创建、现由 Earendil Works 维护的开源终端编码 Agent。它不是一个“功能全塞进核心”的 AI IDE，而是一个极简、模型无关、可扩展的 agent harness：核心只保留少量必要工具，把复杂能力交给 prompt、skills、AGENTS.md、TypeScript 扩展和 pi.dev packages 生态。

项目主页：[pi.dev](https://pi.dev/)  
GitHub：[earendil-works/pi](https://github.com/earendil-works/pi)  
官方文档：[pi.dev/docs/latest](https://pi.dev/docs/latest/)  
作者复盘：[I wrote a coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)  
Packages：[pi.dev/packages](https://pi.dev/packages)

## 它想解决什么问题

终端 coding agent 已经非常拥挤：Claude Code、OpenAI Codex、Gemini CLI、Aider、opencode、Amp、Goose、Devin 等工具都在尝试让模型读代码、改代码、跑命令、提交 PR。

Pi 的切入点是反方向：大多数 agent 越做越重，默认工具、权限、MCP、记忆、子 agent、浏览器、检索和 workflow 都容易堆进核心。Pi 选择把核心做小，让用户按需组合能力。

它解决的不是“如何做一个最省心的 coding agent”，而是“如何做一个开发者能理解、能改造、能扩展、能控制成本的 agent 底座”。

## 核心定位

Pi 可以理解为三层组合。

### 1. 终端 Coding Agent

Pi 运行在终端中，能阅读文件、搜索代码、编辑文件、执行 shell 命令、维护会话上下文，并根据项目指令工作。它和 Claude Code、Codex CLI、Gemini CLI、opencode、Aider 属于同一类工具。

### 2. Agent Harness

Pi 更重要的身份是 harness。它提供一套可扩展的 agent 运行框架，让用户可以自定义工具、系统提示、模型 provider、命令、权限、子 agent、workflow 和主题。

### 3. Package 化生态

Pi 的高级能力主要通过 packages 增长，例如子 agent、权限控制、MCP 适配、Web 搜索、todo、记忆、LSP 反馈和多 agent workflow。到 2026-06-07，pi.dev package catalog 已显示 3000+ 条目，生态增长很快。

这条路线让 Pi 像“npm 时代的 coding agent”：核心小，生态长。

## 为什么它省 Token

Pi 最大的优势之一是非常省 token。这个优势不是来自某个便宜模型，而是来自 harness 设计。

Tensorlake 的文章《Pi: a coding agent with efficient system prompting》指出，Pi 把系统提示和工具定义压在 1,000 token 以内，相比 Claude Code、OpenCode、Cline 这类工具动辄数千到上万 token 的系统上下文，属于约一个数量级的压缩。Agentic AI Knowledge Base 也把 Pi 概括为“四个核心工具 + 千 token 内系统提示”的 agent harness。

Pi 省 token 的原因主要有四个：

1. 系统提示很短，不把大量行为规范和工具说明常驻上下文。
2. 内置工具少，官方 usage 文档列出的 built-in tools 是 `read`、`bash`、`edit`、`write`、`grep`、`find`、`ls`。
3. Skills 采用按需加载，启动时只放名称和描述，完整 `SKILL.md`、脚本和参考资料只有在需要时加载。
4. MCP、sub-agent、permission popup、plan mode、todo、background bash 等能力不内置，而是通过扩展、package、容器或 tmux 组合。

因此，在同样的上下文窗口里，Pi 能把更多 token 留给项目代码、用户需求和最近操作，而不是消耗在固定系统提示和工具 schema 上。Reddit 上有用户反馈，同等任务下 Pi 的 token limit 能撑得比 Claude Code 长约 10 倍；这属于社区经验，不是官方 benchmark，但与 Pi 的架构逻辑一致。

需要注意的是，Pi 的省 token 不是自动魔法。如果一上来安装大量 packages、写很长系统提示、让很多 skills 常驻，优势会被抵消。Pi 的正确用法是：默认保持轻，只为当前任务打开必要能力。

## 发展脉络

Pi 的发展可以浓缩为一条线：**2025-10 个人实验诞生，2025-11 作者公开复盘，2026 年初走向日用，2026-05-07 迁移到 Earendil Works，2026-05 至 2026-06 packages 生态快速扩张**。

早期 Pi 的价值是“用最少 TypeScript 代码验证 coding agent 的最小闭环”。Mario Zechner 在 2025-11-30 的《I wrote a coding agent》中把它的叙事讲清楚：可解释、可修改、核心小。迁移到 `earendil-works/pi` 后，Pi 开始从个人实验变成组织化维护的产品线，主页、文档、包名和 package catalog 都逐渐成型。到 2026-06-07，GitHub releases 已到 v0.78.1 附近，仍处在高速迭代阶段。

## 工作机制

Pi 的典型运行链路很简单。

### 1. 读取上下文

Pi 读取配置、项目说明和 `AGENTS.md` 等文件，理解项目如何构建、测试、修改和验证。

### 2. 调用模型

Pi 不绑定单一供应商，可以接 OpenAI、Anthropic、Google Gemini、OpenRouter、Ollama 或 OpenAI-compatible endpoint。

### 3. 使用核心工具行动

Pi 通过少量 built-in tools 完成读文件、搜代码、编辑文件和执行命令。少量工具既降低 token 成本，也降低模型选择工具时的噪音。

### 4. 按需加载扩展

浏览器、Web 搜索、权限、MCP、子 agent、todo、workflow、记忆等能力通过 packages 或 extensions 接入。Pi 文档明确说明，这些 workflow-specific behavior 不应该都塞进核心。

### 5. 沉淀为文件

Pi 的很多能力最终会沉淀为配置、prompt、skills、agent 定义和 workflow 定义。它不是只靠聊天记忆，而是让项目逐渐拥有自己的 agent 工作规则。

## 关键优势

### 1. 省 token，省成本

Pi 的短 prompt、少工具、lazy skills 和按需扩展，让它的固定上下文开销很低。对于 API 计费、本地小模型、长任务、多轮代码修改来说，这是最直接的优势。

这不只是“少花钱”，还会影响 agent 的可用性：同样的上下文窗口，Pi 能留出更多空间给代码、需求和工具结果；同样的任务预算，Pi 可以多跑几轮；同样的小模型，Pi 不容易被冗长系统提示和工具 schema 挤爆。

### 2. 极简核心，容易理解

Pi 的架构更像一个能读懂的 agent 样本，而不是一个黑盒产品。它适合用来学习 coding agent 的内部机制，也适合做内部工具链改造。对 agent builder 来说，Pi 的价值在于“看得见底层如何工作”，而不是只能接受厂商预设的行为。

### 3. TypeScript 原生扩展

Pi 对 TypeScript/npm 生态友好。开发者可以写本地工具、包装内部 API、扩展命令、定义 workflow，并通过 npm 分发复用。这让 Pi 很适合做团队内部 agent 平台：公司已有的脚本、服务、网关、检索系统，都可以被封装成 package 或 extension。

### 4. 模型无关

Pi 不把用户锁进某个模型供应商。团队可以按任务在强模型、便宜模型、本地模型和企业网关之间切换。这一点对成本优化、私有化部署、本地模型实验都很重要。

### 5. 文件化工作流

`AGENTS.md`、skills、prompt、workflow、agent 定义都可以放进仓库。这让“如何和 agent 协作”从口头经验变成可版本管理的工程资产。长期看，Pi 不只是一个终端工具，而是可以成为项目工程规范的一部分。

## 主要风险

Pi 也不是无脑更优。

- 它很年轻，API、配置和 packages 可能快速变化。
- 默认产品体验不如 Claude Code、Codex、Cursor 这类成熟产品省心。
- 安全边界依赖配置和扩展质量，安装 package、执行 shell、访问网络都需要治理。
- token 优势依赖“少加载、按需加载”，如果把所有扩展和长提示都常驻，轻量优势会消失。

## 竞品对比

Pi 最直接的对比对象是终端 coding agent 和开源 agent harness。

| 产品 | 核心定位 | Pi 的优势 | Pi 的劣势 |
|---|---|---|---|
| Claude Code | Anthropic 官方终端 agent | 更开放、模型无关、可改造、固定上下文更轻 | Claude Code 默认体验、权限、MCP、企业治理更成熟 |
| OpenAI Codex | OpenAI 官方 CLI / 云端 coding agent | provider 中立、扩展更轻、token 成本更可控 | Codex 与 OpenAI 模型、沙箱、云任务结合更深 |
| Aider | 成熟开源 pair programmer | Pi 更像通用 harness，扩展空间更大 | Aider 的 git diff / patch 工作流更成熟 |
| opencode | 开源终端 TUI agent | Pi 核心更轻，TypeScript 扩展更直接 | opencode 默认功能更完整 |
| Cursor / Windsurf | AI IDE | Pi 更适合终端自动化、脚本、无头环境 | IDE 内编辑、补全、导航体验远强于 Pi |
| Devin / OpenHands | 云端或完整工程 agent | Pi 本地、透明、轻量、可控 | 自主执行环境和异步任务能力较弱 |

可以粗略概括为：

- Claude Code / Codex 更像成熟编码协作者。
- Cursor / Windsurf 更像 AI 编辑器。
- Aider / opencode 更像开源终端 agent。
- Pi 更像可编程、可拆装、低 token 成本的 agent harness。

## 适用场景

Pi 适合这些场景：

- 学习 coding agent 架构。
- 搭建组织内部 agent harness。
- 接入自有模型、自有 API、自有工具。
- 把开发规范写成 `AGENTS.md`、skills 或 workflow。
- 做多 agent 编排和 workflow 实验。
- 用终端 agent 处理项目级任务。
- 对 token 成本、上下文占用、本地模型兼容性比较敏感。

Pi 不太适合这些场景：

- 只想开箱即用，不想配置。
- 需要成熟企业权限、审计和管理后台。
- 高度依赖 IDE 补全和可视化编辑。
- 团队不熟悉 Node/npm/TypeScript。
- 没有能力管理 agent 执行命令的安全边界。

## 安装和启动

Pi 官方 Quickstart 推荐用 npm 全局安装：

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

`--ignore-scripts` 用来禁用依赖安装脚本。官方文档说明，Pi 的正常 npm 安装不需要 lifecycle scripts。

安装后进入项目目录启动：

```bash
cd /path/to/project
pi
```

第一次使用需要认证。可以在 Pi 里运行 `/login`，选择订阅或 API-key provider；也可以在启动前设置环境变量：

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

常用启动方式：

```bash
pi "Summarize this repository and tell me how to run its checks."
pi -p "Summarize this codebase"
pi @README.md "Summarize this"
pi --provider openai --model gpt-4o "Help me refactor"
pi --tools read,grep,find,ls -p "Review the code"
```

项目级指令建议写进 `AGENTS.md`：

```md
Project Instructions

- Run `npm run check` after code changes.
- Do not run production migrations locally.
- Keep responses concise.
```

Pi 会读取全局 `~/.pi/agent/AGENTS.md`，也会读取项目中的 `AGENTS.md` 或 `CLAUDE.md`。修改这些文件后，可以重启 Pi，或在交互模式中运行 `/reload`。

常用交互命令：

- `/login`：登录或配置 API key provider。
- `/model`：切换模型。
- `/settings`：调整 thinking level、主题等设置。
- `/compact`：压缩上下文，释放窗口。
- `/resume`：恢复历史会话。
- `/new`：开启新会话。
- `/session`：查看当前 session、token 和 cost。
- `/resume`：恢复历史会话。
- `/new`：开启新会话。
- `/session`：查看当前 session、token 和 cost。

## 总结

Pi Coding Agent 是一个年轻但方向鲜明的项目。它不追求做最产品化的 coding agent，而是把自己定位为极简、开源、可扩展、模型无关的终端 agent harness。

它的核心价值在于把 coding agent 从黑盒产品变成可理解、可修改、可组合的工程基础设施。尤其是低 token 开销这一点，让 Pi 在长任务、本地模型、API 计费和多轮代码修改场景中很有吸引力。

它的风险也清楚：年轻、变化快、默认治理能力要靠用户补，生态质量需要时间验证。Pi 不是最省心的选择，但可能是最适合 agent builder、平台工程团队和高阶开发者自定义工作流的选择之一。

## 参考资料

- [pi.dev 官方主页](https://pi.dev/)
- [Pi 官方文档](https://pi.dev/docs/latest/)
- [Pi GitHub 仓库：earendil-works/pi](https://github.com/earendil-works/pi)
- [Pi releases：v0.78.1](https://github.com/earendil-works/pi/releases/tag/v0.78.1)
- [Mario Zechner：I wrote a coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [pi.dev packages](https://pi.dev/packages)
- [Tensorlake：Pi: a coding agent with efficient system prompting](https://www.tensorlake.ai/blog/pi-coding-agent-efficient-system-prompting)
- [Agentic AI Knowledge Base：Pi (pi.dev)](https://agentic-ai.readthedocs.io/en/latest/AgentHarness/pi-dev/)
- [Sean's Blog：Pi - Open-Source Coding Agent](https://seanpedersen.github.io/posts/pi-agent/)

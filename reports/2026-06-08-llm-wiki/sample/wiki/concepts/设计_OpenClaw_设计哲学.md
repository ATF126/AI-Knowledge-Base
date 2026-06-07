---
type: "concept"
tags: ["openclaw", "design", "unix", "cli"]
summary: "OpenClaw 的设计哲学强调 Unix 风格、小工具、文本流、CLI 优先和 Agent 自我扩展。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 设计哲学

## 定义

OpenClaw 的设计哲学可概括为：CLI 优先、小工具、可组合、文本文件、Agent 自我扩展。

## 关键观点

- CLI 被视为 Agent 连接世界的通用接口。
- 核心工具保持极简，资料中强调 Read、Write、Edit、Bash 这类基础能力。
- 不优先依赖预构建集成，而是让 Agent 通过命令行和 Skills 自行扩展。
- 工作区、记忆和配置尽量用 Markdown/JSON 等人类可读格式保存。

## 对系统的影响

这种设计提高了可组合性和可 hack 性，也要求模型能力更强，并把安全责任更多交给部署者。一个能运行 Shell 和改写自身工具链的 Agent 必须被认真约束。

## 关联页面

- [[concepts/技术_OpenClaw_Agent工作区]]
- [[concepts/技术_OpenClaw_Skills系统]]
- [[concepts/安全_OpenClaw_安全模型]]


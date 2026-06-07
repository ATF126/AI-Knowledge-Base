---
type: "concept"
tags: ["openclaw", "workspace", "memory", "technical"]
summary: "OpenClaw Agent 工作区把身份、用户信息、长期记忆、心跳、日志和技能以文件形式组织。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw Agent 工作区

## 定义

Agent 工作区是 [[entities/项目_OpenClaw]] 的文件系统根目录，用纯文本文件承载 Agent 身份、用户信息、记忆、心跳和 Skills。

## 核心文件

- `AGENTS.md`：Agent 身份定义、行为边界和回复风格。
- `SOUL.md`：不可变人格内核。
- `USER.md`：用户结构化信息和偏好。
- `MEMORY.md`：长期记忆。
- `HEARTBEAT.md`：定时任务和主动行为。
- `memory/YYYY-MM-DD.md`：每日日志，追加写入。
- `skills/`：工作区级 Skills，优先级最高。
- `sessions.json`：会话元数据。

## 设计含义

OpenClaw 的工作区体现“一切皆文本”的设计：用户可以直接阅读、审计和修改 Agent 的长期状态。这提高了可控性，也带来记忆污染和恶意篡改风险。

## 关联页面

- [[concepts/技术_OpenClaw_记忆系统]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/设计_OpenClaw_设计哲学]]


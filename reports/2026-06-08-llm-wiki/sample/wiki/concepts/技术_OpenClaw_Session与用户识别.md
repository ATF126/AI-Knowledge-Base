---
type: "concept"
tags: ["openclaw", "session", "authentication", "technical"]
summary: "OpenClaw 用 DM 配对、白名单、群组提及和 Session 隔离管理不同用户与渠道的上下文。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw Session 与用户识别

## 定义

Session 与用户识别是 OpenClaw 判断“谁在和 Agent 交互”以及“这段上下文应如何隔离”的机制。

## 核心机制

- DM Pairing：未知私聊发送者先获得一次性配对码，等待主人批准。
- `allowFrom`：预授权用户可以跳过配对。
- `requireMention`：群聊默认只响应被提及的消息。
- Session 隔离：私聊通常进入共享 main session，群组默认独立隔离。
- 长期记忆加载：`MEMORY.md` 通常只在 main/private session 中加载。

## 安全意义

这套机制减少陌生人滥用 Agent 和 API 额度，也避免群聊读取私聊长期记忆。但它不是完整安全边界，仍需配合 Gateway 认证、工具权限和网络隔离。

## 关联页面

- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/技术_OpenClaw_记忆系统]]
- [[concepts/集成_OpenClaw_渠道接入]]


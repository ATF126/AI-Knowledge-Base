---
type: "concept"
tags: ["concept", "model", "fallback", "openclaw", "cost"]
summary: "模型配置与 Fallback 是 OpenClaw 在能力、成本和可用性之间做动态平衡的核心手段。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# 模型配置与 Fallback

## 定义

Fallback 是为 Agent 配置主模型和备选模型链。当主模型限速、不可用或成本过高时，系统切换到备选模型。

## 配置思路

- 主力模型：用于复杂推理、工具规划、关键任务。
- 轻量模型：用于问候、简单查询、常规摘要。
- 免费或本地模型：用于心跳、定时检查、低价值批处理。
- 自定义 Provider：用于接入 DeepSeek、豆包、Kimi 等非内置模型。
- `models.mode: "merge"`：保留内置 Provider，同时叠加自定义 Provider。

## 推荐策略

资料推荐的核心原则是“用对的模型做对的事”：复杂任务用强模型，日常任务用便宜模型，心跳和定时任务尽量用免费或本地模型。

## 关联页面

- [[concepts/成本_OpenClaw_成本控制]]
- [[entities/项目_OpenClaw]]


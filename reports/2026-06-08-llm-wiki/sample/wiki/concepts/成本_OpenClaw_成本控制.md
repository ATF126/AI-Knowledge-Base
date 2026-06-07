---
type: "concept"
tags: ["concept", "openclaw", "cost", "model"]
summary: "OpenClaw 成本控制依赖模型分层、Fallback、预算上限、本地模型和低频 cron。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 成本控制

## 问题定义

OpenClaw 的 token 消耗可能远高于普通聊天：多轮思考、工具调用、Skills 描述、长期记忆、Daily Logs 和 cron 都会增加请求量。

## 成本失控原因

- Agent 进入循环推理。
- 邮件/日程/网页自动化任务触发大量工具调用。
- 过多 Skills 拉长 system prompt。
- 长期记忆和日志每次进入上下文。
- 单一昂贵模型承担所有任务。

## 控制策略

- 设置每日 token 和成本预算上限。
- 使用 [[concepts/技术_模型配置与Fallback]]：强模型处理复杂任务，便宜模型处理日常任务，免费/本地模型处理心跳任务。
- 减少不必要的 cron 频率。
- 只安装真正使用的 Skills。
- 对可能循环的任务设置步数上限和人工确认点。

## 关联页面

- [[concepts/技术_OpenClaw_Skills系统]]
- [[concepts/技术_模型配置与Fallback]]
- [[concepts/安全_OpenClaw_安全模型]]


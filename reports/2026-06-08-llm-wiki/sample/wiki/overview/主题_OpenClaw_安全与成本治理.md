---
type: "overview"
tags: ["overview", "openclaw", "security", "cost"]
summary: "OpenClaw 长期运行的关键不是能否启动，而是能否持续控制权限、供应链、网络暴露和模型账单。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 安全与成本治理

## 一句话结论

OpenClaw 是一个长期在线、能调用工具和接入消息平台的 Agent 系统，因此部署后最重要的是治理：不要公网暴露 Gateway，不盲装 Skills，不让模型账单失控。

## 安全治理

- 网络：Gateway 默认应绑定 localhost，不直接暴露 `18789`。
- 认证：配置 Gateway 认证，使用 DM pairing 和群组 `requireMention`。
- 权限：限制 browser、nodes、文件、Shell 等高危工具。
- 供应链：审查 Skills，特别防范 [[concepts/安全_ClawHavoc供应链攻击]] 这类事件。
- 记忆：定期检查 `SOUL.md`、`MEMORY.md`、Daily Logs 和本地 Skills。

## 成本治理

- 设置每日 token 和金额上限。
- 配置 [[concepts/技术_模型配置与Fallback]]。
- 少装 Skills，减少 system prompt 负担。
- 降低 cron/heartbeat 频率。
- 对邮件、网页、代码执行等长任务设置步数上限和人工确认点。

## 推荐组合

```text
安全网络边界 + Gateway 认证 + 最小工具权限 + Skill 审计 + Fallback 模型链 + 每日预算上限
```

## 关联页面

- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/成本_OpenClaw_成本控制]]
- [[concepts/技术_OpenClaw_Session与用户识别]]


---
type: "source"
tags: ["source", "openclaw", "agent", "deployment", "security"]
summary: "OpenClaw 橙皮书 v1.4.0 系统介绍 OpenClaw 的架构、部署、渠道、Skills、模型、安全、成本、国内生态和国产产品。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf"]
updated: "2026-06-07"
---

# OpenClaw 橙皮书 v1.4.0

## 来源信息

- 标题：OpenClaw 橙皮书：从入门到精通
- 作者/整理：花叔
- 文档版本：v1.4.0
- 适用版本：v2026.3.13
- 发布时间：2026-03-24
- 原始文件：`raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf`
- 关联页面：[[entities/项目_OpenClaw]]、[[overview/主题_OpenClaw_综述]]

## 核心要点

- OpenClaw 被描述为开源、自托管、多渠道 AI Agent 系统，定位接近“个人 AI 操作系统”。
- 技术架构采用 Gateway-Node-Channel 三层：Gateway 负责控制平面，Node 负责设备端执行，Channel 负责连接消息平台。
- 记忆系统分为 SOUL、TOOLS、USER、Session，并通过 `MEMORY.md`、Daily Logs、向量搜索维持长期上下文。
- Skills 是能力扩展单元，按 workspace、用户级、内置三层优先级加载；ClawHub 提供市场，但存在严重供应链风险。
- 模型配置强调多 Provider、Fallback 链和预算上限；成本失控通常来自多轮工具调用、记忆上下文、定时任务和循环推理。
- 安全模型以默认不信任为原则，但 prompt injection 未被根治；资料列举了 RCE、ClawHavoc、未认证实例暴露、恶意 npm 包等事件。
- v1.4.0 增补了国内生态和国产 Claw 产品选购内容，包括 OpenClaw 封装版与独立自研版两个阵营。

## 关联实体/概念

- [[entities/项目_OpenClaw]]
- [[entities/人物_Peter_Steinberger]]
- [[entities/平台_ClawHub]]
- [[entities/平台_Moltbook]]
- [[concepts/架构_OpenClaw_Gateway_Node_Channel]]
- [[concepts/技术_OpenClaw_记忆系统]]
- [[concepts/技术_OpenClaw_Agent工作区]]
- [[concepts/技术_OpenClaw_Session与用户识别]]
- [[concepts/技术_OpenClaw_Skills系统]]
- [[concepts/设计_OpenClaw_设计哲学]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/安全_ClawHavoc供应链攻击]]
- [[concepts/成本_OpenClaw_成本控制]]
- [[concepts/生态_OpenClaw_国内生态]]
- [[concepts/生态_OpenClaw_替代产品]]
- [[comparisons/OpenClaw_vs_Claude_Code]]
- [[comparisons/OpenClaw_国内产品选购]]
- [[comparisons/OpenClaw_模型提供商对比]]

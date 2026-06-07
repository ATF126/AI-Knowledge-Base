---
type: "overview"
tags: ["overview", "agent", "react", "memory", "openclaw"]
summary: "AI Agent 可以从推理、行动、观察、记忆、权限五个维度理解，ReAct 与 OpenClaw 分别代表方法和系统实现。"
sources: ["raw/REACT.pdf", "raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf"]
updated: "2026-06-07"
---

# AI Agent：推理、行动与记忆

## 一句话结论

[[concepts/方法_ReAct]] 解释了 AI Agent 如何在任务中交替推理和行动；[[entities/项目_OpenClaw]] 展示了一个长期在线 Agent 系统如何把推理、工具、消息渠道、记忆和扩展生态组合起来。

## 总体框架

- 推理：目标分解、计划、检索策略、状态跟踪、错误恢复。
- 行动：搜索、浏览、文件、Shell、消息、日历、邮件等工具调用。
- 观察：工具返回结果，用于校正下一步推理。
- 记忆：长期事实、用户偏好、会话状态和每日日志。
- 权限：哪些工具、文件、账号和环境允许 Agent 操作。

## 两类来源的互补关系

- [[sources/来源_REACT论文]]：偏方法论，证明推理和行动交替能提高 groundedness、可解释性和交互任务成功率。
- [[sources/来源_OpenClaw橙皮书_v1.4.0]]：偏系统工程，说明真实 Agent 产品还必须处理部署、渠道、Skills、模型、成本和安全。

## 应用判断

当任务需要外部信息或真实环境反馈时，优先考虑 ReAct 式循环；当任务需要长期在线、跨渠道、跨会话自动化时，才需要 OpenClaw 这类系统级 Agent。两者都不应脱离权限控制单独讨论。

## 支撑页面

- [[concepts/概念_AI_Agent]]
- [[concepts/概念_Chain_of_Thought]]
- [[concepts/方法_ReAct]]
- [[concepts/技术_OpenClaw_记忆系统]]
- [[concepts/安全_OpenClaw_安全模型]]

---
type: "entity"
tags: ["entity", "openclaw", "agent"]
summary: "OpenClaw 是开源、自托管、多渠道 AI Agent 系统，强调长期在线、记忆、Skills、模型自由和消息平台接入。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw

## 基本信息

- 类型：开源、自托管 AI Agent 系统
- 定位：个人 AI 操作系统 / 多渠道 Agent Gateway
- 许可证：资料称为 MIT License
- 关键能力：消息渠道接入、长期记忆、工具执行、Skills 扩展、多模型配置、远程访问
- 主要来源：[[sources/来源_OpenClaw橙皮书_v1.4.0]]

## 核心特征

- 通过 [[concepts/架构_OpenClaw_Gateway_Node_Channel]] 将消息渠道、控制平面和设备执行解耦。
- 通过 [[concepts/技术_OpenClaw_记忆系统]] 让 Agent 拥有跨会话的用户偏好、历史事实和日志。
- 通过 [[concepts/技术_OpenClaw_Agent工作区]] 将身份、记忆、日志和 Skills 文件化。
- 通过 [[concepts/技术_OpenClaw_Session与用户识别]] 管理私聊、群组和跨渠道上下文。
- 通过 [[concepts/技术_OpenClaw_Skills系统]] 扩展能力，但第三方 Skill 是主要风险面。
- 支持 Claude、OpenAI、Gemini、DeepSeek、GLM、Qwen、Ollama 等模型，依赖 [[concepts/技术_模型配置与Fallback]] 控制成本与可用性。

## 风险状态

- 安全风险高：公网 Gateway、未认证实例、供应链攻击、prompt injection 都是资料反复强调的风险。
- 成本风险高：多轮推理、工具调用、记忆上下文和 cron 任务可能导致 API 账单失控。
- 生态质量不均：ClawHub 数量很大，但低质量、重复和恶意 Skill 比例高。

## 相关页面

- [[overview/主题_OpenClaw_综述]]
- [[comparisons/OpenClaw_vs_Claude_Code]]
- [[comparisons/OpenClaw_部署方案对比]]
- [[comparisons/OpenClaw_国内产品选购]]
- [[overview/主题_OpenClaw_安全与成本治理]]

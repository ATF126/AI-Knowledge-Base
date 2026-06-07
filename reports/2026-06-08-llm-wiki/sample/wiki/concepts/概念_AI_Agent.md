---
type: "concept"
tags: ["concept", "agent", "llm"]
summary: "AI Agent 是围绕目标、上下文、工具、观察和记忆进行多步闭环执行的系统。"
sources: ["raw/REACT.pdf", "raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf"]
updated: "2026-06-07"
---

# AI Agent

## 定义

AI Agent 不是普通聊天机器人，而是能接收目标、维护上下文、调用工具、观察结果并继续决策的多步执行系统。

在 [[sources/来源_REACT论文]] 中，Agent 的关键循环是“推理 - 行动 - 观察”。在 [[sources/来源_OpenClaw橙皮书_v1.4.0]] 中，Agent 被工程化为长期在线、可接入消息平台、能积累记忆和扩展能力的个人系统。

## 核心组成

- 目标：用户给出的任务或长期设定。
- 推理：目标分解、计划、状态跟踪和错误恢复。
- 行动：搜索、浏览器、文件、Shell、邮件、日历、消息等工具调用。
- 观察：外部环境或工具返回的结果。
- 记忆：用户偏好、历史事实、每日日志和会话上下文。
- 权限：决定 Agent 能访问哪些账号、文件、设备和系统资源。

## 在本知识库中的应用

- 方法层：[[concepts/方法_ReAct]] 解释如何交替生成推理和行动。
- 系统层：[[entities/项目_OpenClaw]] 展示如何把 Agent 长期接入真实消息渠道和设备环境。
- 治理层：[[overview/主题_OpenClaw_安全与成本治理]] 关注安全边界与成本上限。

## 关联页面

- [[concepts/方法_ReAct]]
- [[concepts/概念_Chain_of_Thought]]
- [[overview/主题_AI_Agent_推理行动记忆综述]]


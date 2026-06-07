---
type: "concept"
tags: ["concept", "openclaw", "architecture"]
summary: "OpenClaw 使用 Gateway-Node-Channel 三层架构解耦控制平面、设备执行和消息渠道。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 架构

## 定义

OpenClaw 的架构可概括为 Gateway-Node-Channel：

- Gateway：中央控制平面，管理 WebSocket、Session 和 Agent 调度。
- Node：设备端执行节点，负责摄像头、录屏、系统命令等本地操作。
- Channel：消息渠道层，连接 Telegram、WhatsApp、飞书、钉钉、Discord 等平台。

## 关键设计

- Gateway 默认绑定 `127.0.0.1:18789`，体现 loopback-first 的安全默认值。
- 远程访问建议经由 Tailscale Serve/Funnel 等方式，不直接暴露 Gateway 端口。
- 每台主机建议只运行一个 Gateway，避免 WhatsApp Web 等渠道会话冲突。

## 关系

- Channel 输入消息，Gateway 路由到 Agent，必要时由 Node 执行工具，再由 Channel 回复用户。
- 架构风险集中在 Gateway 暴露、认证缺失和 Node 权限过大。

## 关联页面

- [[entities/项目_OpenClaw]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/集成_OpenClaw_渠道接入]]


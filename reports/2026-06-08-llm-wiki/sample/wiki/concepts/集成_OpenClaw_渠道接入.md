---
type: "concept"
tags: ["concept", "openclaw", "channel", "integration"]
summary: "OpenClaw 通过统一 Channel 层连接 Telegram、Discord、WhatsApp、飞书、钉钉等消息平台。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 渠道接入

## 定义

渠道接入是 OpenClaw 将 Agent 接入即时通讯或办公平台的能力。统一流程通常是：创建平台凭证，写入配置，启动 Gateway，完成配对。

## 常见渠道

- 国际：Telegram、Discord、WhatsApp、Slack、Signal、iMessage、Google Chat、LINE、Teams 等。
- 国内：飞书、钉钉、企业微信、QQ、微信个人号等。

## 新手选择

- Telegram：最简单，不需要公网 IP，适合入门。
- QQ：国内扫码绑定体验较轻。
- 飞书：适合国内团队协作和企业场景。
- WhatsApp/Slack/企业微信：更贴近日常或企业沟通，但配置和安全要求更高。

## 安全注意

- 默认启用 DM pairing，未知用户需要配对码。
- 群聊建议保持 `requireMention`，避免 token 被群聊噪音消耗。
- 多人平台不应连接高权限本机环境，优先使用 VM 或专用服务器。

## 关联页面

- [[concepts/架构_OpenClaw_Gateway_Node_Channel]]
- [[concepts/安全_OpenClaw_安全模型]]


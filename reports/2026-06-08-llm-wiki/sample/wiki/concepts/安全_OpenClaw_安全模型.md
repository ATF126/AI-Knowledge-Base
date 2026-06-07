---
type: "concept"
tags: ["concept", "openclaw", "security"]
summary: "OpenClaw 的安全模型以默认不信任为原则，但仍需用户自己处理 prompt injection、权限和供应链风险。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 安全模型

## 定义

OpenClaw 的安全模型建立在“默认不信任”之上：未知私聊需要配对，群组默认隔离，工具可通过 allowlist/denylist 控制，Gateway 认证逐步强制化。

## 主要机制

- DM Pairing：陌生私聊需要一次性配对码。
- 群组隔离：群组 session 默认不加载 `MEMORY.md`。
- 工具访问控制：allowlist、denylist、browser/canvas/nodes 开关。
- Gateway 认证：资料称 v2026.3.7 起要求显式设置 `gateway.auth.mode`。
- ACP Provenance：资料称 v2026.3.8 引入代理身份验证，用于减少身份伪造。

## 主要风险

- Prompt injection 未被根治。
- Gateway 公网暴露可导致远程控制。
- 第三方 Skill 等同受信任代码，可能窃取凭证、篡改长期记忆或执行后门。
- 高权限本机 Node 让 Agent 能触达真实文件、摄像头、浏览器和系统命令。

## 操作底线

- 不公网暴露 `18789`。
- 不盲装 ClawHub Skill。
- 不在主账号上连接高风险外部服务。
- 定期检查 `SOUL.md`、`MEMORY.md` 和已安装 Skills。

## 关联页面

- [[entities/平台_ClawHub]]
- [[concepts/安全_ClawHavoc供应链攻击]]
- [[concepts/技术_OpenClaw_记忆系统]]
- [[concepts/技术_OpenClaw_Skills系统]]
- [[overview/主题_OpenClaw_安全与成本治理]]

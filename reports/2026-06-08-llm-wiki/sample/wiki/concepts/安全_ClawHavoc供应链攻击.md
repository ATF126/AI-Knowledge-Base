---
type: "concept"
tags: ["openclaw", "security", "supply-chain", "skills"]
summary: "ClawHavoc 是 OpenClaw 生态中的大规模恶意 Skill 供应链攻击，暴露了 ClawHub 审核和本地权限风险。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# ClawHavoc 供应链攻击

## 定义

ClawHavoc 是 OpenClaw 社区在 2026 年初遭遇的大规模恶意 Skill 供应链攻击。攻击者通过 [[entities/平台_ClawHub]] 发布看似正常的 Skill，诱导用户安装后植入恶意行为。

## 攻击特征

- 恶意 Skill 伪装成专业工具。
- 通过额外 helper、脚本或 agent 增强功能诱导执行。
- 目标包括凭证、钱包、长期记忆和 Agent 行为指令。
- 资料特别强调 `SOUL.md` 与 `MEMORY.md` 被篡改的风险。

## 为什么严重

Skill 本质上是受信任代码。一旦安装，它可能拥有 OpenClaw 实例同级权限，可以访问邮件、日历、消息、文件系统和长期记忆。

## 防护原则

- 不盲装 ClawHub Skill。
- 安装前读源码和 `SKILL.md`。
- 拒绝要求下载 zip、执行未知 shell 脚本、输入密码的 Skill。
- 定期检查 `SOUL.md`、`MEMORY.md` 和本地 Skills 目录。

## 关联页面

- [[concepts/技术_OpenClaw_Skills系统]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[entities/平台_ClawHub]]


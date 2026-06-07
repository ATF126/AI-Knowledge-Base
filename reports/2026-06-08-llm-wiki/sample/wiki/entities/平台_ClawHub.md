---
type: "entity"
tags: ["entity", "openclaw", "skills", "security"]
summary: "ClawHub 是 OpenClaw 的 Skill 注册表和市场，也是供应链安全风险的集中来源。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# ClawHub

## 基本信息

- 类型：OpenClaw Skill 注册表 / 市场
- 类比：资料将其类比为 npm 之于 Node.js
- 能力：Skill 发布、搜索、下载、评分、安全扫描

## 关键状态

- 资料称 ClawHub 注册 Skills 数量达到万级，但质量分布极不均。
- 社区精选列表从大量 Skills 中过滤掉垃圾、重复和恶意内容。
- [[concepts/安全_ClawHavoc供应链攻击]] 说明第三方 Skill 应被视为受信任代码，而不是普通配置。

## 使用原则

- 优先使用内置 Skill 或可信精选列表。
- 安装前读取源码，特别检查 `SKILL.md`、脚本安装、外部下载、凭证访问和 shell 执行。
- 与 [[concepts/安全_OpenClaw_安全模型]]、[[concepts/技术_OpenClaw_Skills系统]] 联动管理。

## 关联页面

- [[concepts/技术_OpenClaw_Skills系统]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/安全_ClawHavoc供应链攻击]]

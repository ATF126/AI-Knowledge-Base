---
type: "concept"
tags: ["concept", "openclaw", "skills", "extension"]
summary: "OpenClaw Skills 是能力扩展单元，按三层优先级加载，也构成主要供应链风险面。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw Skills 系统

## 定义

Skill 是 OpenClaw 的能力扩展单元，最小结构是一个目录加 `SKILL.md`。系统通过 Skill 的描述、触发条件和指令把能力注入 Agent 上下文。

## 加载优先级

1. `<workspace>/skills/`：项目级，优先级最高。
2. `~/.openclaw/skills/`：用户级，全局生效。
3. bundled skills：内置技能，优先级最低。

## 使用原则

- 不要一次安装太多 Skill，因为每个 Skill 都会增加 system prompt 长度和 token 成本。
- 自建 Skill 适合项目级流程固化。
- 第三方 Skill 必须审查源码，尤其是下载、执行脚本、读取凭证和修改记忆的逻辑。

## 关联页面

- [[entities/平台_ClawHub]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/安全_ClawHavoc供应链攻击]]
- [[concepts/成本_OpenClaw_成本控制]]

---
type: "concept"
tags: ["concept", "openclaw", "memory"]
summary: "OpenClaw 通过 SOUL、TOOLS、USER、Session 四层记忆和文件化日志保持上下文连续性。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 记忆系统

## 定义

OpenClaw 的记忆系统由四层构成：

- SOUL：不可变身份内核，通常位于 `SOUL.md`。
- TOOLS：当前可用工具和 Skills。
- USER：用户偏好、历史事实、长期记忆，通常关联 `MEMORY.md` 和向量数据库。
- Session：当前对话上下文和会话级状态。

## 关键机制

- Daily Logs：每天追加到 `memory/YYYY-MM-DD.md`，Session 启动时读取今日和昨日日志。
- Pre-Compaction：接近 token 上限时，后台保存重要记忆并压缩旧上下文。
- 语义搜索：结合 embedding 与 BM25，用于模糊回忆和精确匹配。
- Session 隔离：私聊加载长期记忆，群组默认隔离，降低泄露风险。

## 风险

- 长期记忆会进入后续上下文，因此一旦被污染，会影响长期行为。
- Skills 攻击如果篡改 `SOUL.md` 或 `MEMORY.md`，风险高于普通一次性 prompt injection。

## 关联页面

- [[concepts/概念_AI_Agent]]
- [[concepts/技术_OpenClaw_Agent工作区]]
- [[concepts/技术_OpenClaw_Session与用户识别]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[entities/项目_OpenClaw]]

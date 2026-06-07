---
type: "comparison"
tags: ["comparison", "openclaw", "model", "cost"]
summary: "OpenClaw 模型选择要在能力、价格、上下文、工具调用稳定性和可用性之间平衡。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 模型提供商对比

## 比较对象

- 国际模型：Claude、OpenAI GPT、Gemini。
- 国产模型：DeepSeek、GLM、Qwen、豆包、文心、Kimi、MiniMax。
- 本地模型：Ollama、LM Studio 等。

## 共同点

所有模型方案最终都要服务同一个目标：让 Agent 能稳定规划、调用工具、理解上下文并控制成本。

## 差异维度

| 维度 | 强模型 | 低价云模型 | 本地模型 |
|---|---|---|---|
| 典型用途 | 复杂推理、关键任务 | 日常对话、批处理、简单自动化 | 隐私敏感、心跳、低成本实验 |
| 成本 | 高 | 低到中 | API 成本为零 |
| 稳定性 | 通常较好 | 取决于供应商和高峰期 | 取决于本机硬件 |
| 工具调用 | 通常更强 | 需要实测 | 模型差异大 |
| 数据控制 | 依赖云 API | 依赖云 API | 本地控制最好 |

## 结论

OpenClaw 不应长期依赖单一昂贵模型。更合理的方案是使用 [[concepts/技术_模型配置与Fallback]]：强模型处理复杂任务，低价模型处理日常任务，本地或免费模型处理心跳和低价值任务。

## 关联页面

- [[concepts/成本_OpenClaw_成本控制]]
- [[concepts/技术_模型配置与Fallback]]


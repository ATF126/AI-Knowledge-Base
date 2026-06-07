---
type: "comparison"
tags: ["comparison", "react", "cot", "agent"]
summary: "ReAct、CoT 和 Act-only 的核心差异在于是否同时拥有内部推理与外部环境反馈。"
sources: ["raw/REACT.pdf"]
updated: "2026-06-07"
---

# ReAct vs CoT vs Act-only

## 比较对象

- [[concepts/概念_Chain_of_Thought|CoT]]：只生成推理链，不与外部环境交互。
- Act-only：只生成动作并接收观察，不显式维护推理轨迹。
- [[concepts/方法_ReAct]]：交替生成推理、动作和观察。

## 相同点

- 都可基于少量示例进行 prompting。
- 都可用于多步任务。
- 都依赖基础模型的语言能力和任务示例质量。

## 不同点

| 维度 | CoT | Act-only | ReAct |
|---|---|---|---|
| 信息来源 | 内部知识 | 外部观察 | 内部推理 + 外部观察 |
| 优势 | 推理结构灵活 | 可获取环境反馈 | 更 grounded，便于纠错 |
| 常见失败 | 幻觉、错误传播 | 无目标分解、动作重复 | 检索失败、结构约束导致推理错误 |
| 可解释性 | 中等 | 低 | 高 |
| 适用场景 | 数学/逻辑/纯文本推理 | 简单工具调用 | 检索问答、网页导航、长程决策 |

## 结论

ReAct 不是 CoT 的简单替代，而是把 CoT 的内部推理与工具/环境反馈连接起来。在知识任务中，ReAct + CoT-SC 的混合策略更稳；在交互式任务中，ReAct 的稀疏推理显著提升目标分解与状态跟踪。

## 关联页面

- [[sources/来源_REACT论文]]
- [[concepts/概念_AI_Agent]]
- [[concepts/概念_Chain_of_Thought]]

---
type: "concept"
tags: ["concept", "reasoning", "cot", "llm"]
summary: "Chain-of-Thought 是让模型显式生成中间推理链的提示范式，但不直接接入外部环境。"
sources: ["raw/REACT.pdf"]
updated: "2026-06-07"
---

# Chain-of-Thought

## 定义

Chain-of-Thought（CoT）是一种让语言模型显式生成中间推理步骤的提示方法。它擅长把问题拆成可读的推理过程，但通常只依赖模型内部知识。

## 与 ReAct 的关系

[[concepts/方法_ReAct]] 继承了“显式推理轨迹”的优点，但把推理轨迹放进外部行动循环中，让模型可以通过工具或环境获得新信息。

## 主要优势

- 推理结构灵活。
- 适合数学、逻辑、多步文本推理等内部知识足够的任务。
- 通过 self-consistency 可用多条推理链投票提高稳定性。

## 主要局限

- 不与外部环境交互，容易把过时或错误内部知识当事实。
- 在知识密集型任务中容易出现事实幻觉和错误传播。
- 中间推理可读，但不一定忠实于模型真实决策过程。

## 关联页面

- [[comparisons/ReAct_vs_CoT_vs_Act]]
- [[sources/来源_REACT论文]]


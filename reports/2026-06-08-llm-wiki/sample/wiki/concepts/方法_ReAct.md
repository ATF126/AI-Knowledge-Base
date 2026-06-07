---
type: "concept"
tags: ["concept", "react", "agent", "reasoning", "acting"]
summary: "ReAct 是一种把语言推理轨迹和环境动作交替生成的 Agent 范式。"
sources: ["raw/REACT.pdf"]
updated: "2026-06-07"
---

# ReAct

## 定义

ReAct 是 Reasoning + Acting 的缩写，是一种让语言模型交替生成推理轨迹与任务动作的方法。它把模型动作空间扩展为“外部动作 + 语言 thought”，让模型在任务轨迹中同时进行计划、行动、观察和修正。

典型循环：

```text
Thought -> Action -> Observation -> Thought -> ...
```

## 解决的问题

- 纯 [[concepts/概念_Chain_of_Thought|CoT]] 能推理，但容易依赖内部知识并产生事实幻觉。
- 纯 Act 能调用外部环境，但缺少高层目标分解、状态跟踪和检索策略。
- ReAct 让推理指导行动，也让行动获取的新信息反过来修正推理。

## 使用场景

- 多跳问答与事实验证：检索外部资料后再推理。
- 网页导航与购物任务：根据用户约束选择搜索、筛选和购买动作。
- 文本环境决策：分解子目标，追踪当前状态，避免重复无效动作。
- 人机协作：人可以检查或编辑中间 thought 来纠偏。

## 论文结果摘要

- HotpotQA / Fever：ReAct 比 Act-only 更稳，和 CoT 各有优劣；ReAct + CoT-SC 混合策略表现最好。
- ALFWorld：ReAct 最佳试验成功率达到 71%，高于 Act-only 和 BUTLER。
- WebShop：ReAct 成功率为 40.0%，高于 IL 和 IL+RL 基线。

## 局限

- 对检索结果质量敏感；搜索不到有效信息时容易偏离。
- 结构化轨迹会提高可信度，但也可能降低自由推理灵活性。
- 接入真实动作空间时存在安全风险，需要限制工具权限与环境。

## 关联页面

- [[sources/来源_REACT论文]]
- [[comparisons/ReAct_vs_CoT_vs_Act]]
- [[concepts/概念_AI_Agent]]

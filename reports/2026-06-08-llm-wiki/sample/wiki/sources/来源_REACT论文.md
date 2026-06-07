---
type: "source"
tags: ["source", "paper", "react", "agent", "llm"]
summary: "ReAct 提出让语言模型交替生成推理轨迹与环境动作，用外部反馈增强任务求解。"
sources: ["raw/REACT.pdf"]
updated: "2026-06-07"
---

# ReAct: Synergizing Reasoning and Acting in Language Models

## 来源信息

- 标题：ReAct: Synergizing Reasoning and Acting in Language Models
- 作者：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- 发表：ICLR 2023
- 原始文件：`raw/REACT.pdf`
- 关联页面：[[concepts/方法_ReAct]]、[[comparisons/ReAct_vs_CoT_vs_Act]]、[[overview/主题_AI_Agent_推理行动记忆综述]]

## 核心要点

- ReAct 的核心是让模型在同一条轨迹中交替产生 `Thought`、`Action`、`Observation`，把内部推理和外部环境反馈合成一个闭环。
- 在知识密集型任务中，ReAct 通过 Wikipedia API 检索事实，降低纯 CoT 中常见的事实幻觉和错误传播。
- 在 HotpotQA 和 Fever 上，ReAct 与 CoT 各有优势；将 ReAct 与 CoT-SC 组合，通常比单独使用任一方法更稳。
- 在 ALFWorld 和 WebShop 这类交互式决策任务中，稀疏推理帮助模型分解子目标、跟踪状态、选择下一步行动。
- 论文报告 ReAct 在 ALFWorld 最佳试验中达到 71% 成功率，明显高于 Act-only 与 BUTLER；在 WebShop 中成功率达到 40.0%，比此前 IL/RL 基线更高。
- ReAct 的可解释性来自可读的推理轨迹；人类可以检查并编辑中间 thought 来修正行为。
- 论文也指出风险：把语言模型接入外部动作空间会带来访问隐私信息或执行有害动作的可能，需要限制动作空间和环境。

## 适合沉淀的概念

- [[concepts/方法_ReAct]]
- [[concepts/概念_Chain_of_Thought]]
- [[concepts/概念_AI_Agent]]
- [[comparisons/ReAct_vs_CoT_vs_Act]]
- [[overview/主题_AI_Agent_推理行动记忆综述]]

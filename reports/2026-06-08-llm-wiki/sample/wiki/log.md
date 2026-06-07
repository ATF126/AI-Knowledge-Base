## [2026-06-07] ingest | raw/REACT.pdf → wiki/sources/来源_REACT论文.md

- 新建 [[sources/来源_REACT论文]]
- 新建 [[concepts/方法_ReAct]]
- 新建 [[comparisons/ReAct_vs_CoT_vs_Act]]

## [2026-06-07] ingest | raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf + raw/OpenClaw橙皮书_extracted.txt → OpenClaw wiki pages

- 新建来源页：[[sources/来源_OpenClaw橙皮书_v1.4.0]]、[[sources/来源_OpenClaw橙皮书_v1.1.0_抽取文本]]
- 新建实体页：[[entities/项目_OpenClaw]]、[[entities/人物_Peter_Steinberger]]、[[entities/平台_ClawHub]]、[[entities/工具_Claude_Code]]
- 新建概念页：[[concepts/架构_OpenClaw_Gateway_Node_Channel]]、[[concepts/技术_OpenClaw_记忆系统]]、[[concepts/技术_OpenClaw_Skills系统]]、[[concepts/集成_OpenClaw_渠道接入]]、[[concepts/部署_OpenClaw]]、[[concepts/安全_OpenClaw_安全模型]]、[[concepts/成本_OpenClaw_成本控制]]、[[concepts/技术_模型配置与Fallback]]、[[concepts/文化_养虾文化]]
- 新建比较页：[[comparisons/OpenClaw_vs_Claude_Code]]、[[comparisons/OpenClaw_部署方案对比]]、[[comparisons/OpenClaw_国内产品选购]]
- 新建总览页：[[overview/主题_OpenClaw_综述]]、[[overview/主题_AI_Agent_推理行动记忆综述]]
- 更新 [[index]]

## [2026-06-07] maintenance | rename wiki page prefixes by semantic type

- 将 `entities/实体_*` 改为更具体的 `项目_`、`人物_`、`平台_`、`工具_` 前缀
- 将 `concepts/概念_*` 改为更具体的 `方法_`、`技术_`、`架构_`、`集成_`、`部署_`、`安全_`、`成本_`、`文化_` 前缀
- 同步更新全库 wikilink，断链检查结果为 0

## [2026-06-07] reingest | raw/ → semantic wiki restructure

- 使用 `pdftotext -layout` 重新抽取 `raw/REACT.pdf` 与 `raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf`
- 保留抽象概念页的 `概念_` 前缀，例如 [[concepts/概念_AI_Agent]]、[[concepts/概念_Chain_of_Thought]]
- 对工程主题使用更具体前缀：`技术_`、`架构_`、`安全_`、`成本_`、`部署_`、`集成_`、`设计_`、`生态_`、`文化_`
- 新增页面：[[concepts/技术_OpenClaw_Agent工作区]]、[[concepts/技术_OpenClaw_Session与用户识别]]、[[concepts/设计_OpenClaw_设计哲学]]、[[concepts/安全_ClawHavoc供应链攻击]]、[[concepts/生态_OpenClaw_国内生态]]、[[concepts/生态_OpenClaw_替代产品]]、[[entities/平台_Moltbook]]、[[comparisons/OpenClaw_模型提供商对比]]、[[overview/主题_OpenClaw_安全与成本治理]]
- 将 Agent 总览改名为 [[overview/主题_AI_Agent_推理行动记忆综述]]
- 重写 [[index]]

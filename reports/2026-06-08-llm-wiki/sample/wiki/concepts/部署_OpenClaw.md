---
type: "concept"
tags: ["concept", "openclaw", "deployment"]
summary: "OpenClaw 可通过本地 npm、Docker、国内云一键部署和 SaaS 封装方式运行。"
sources: ["raw/OpenClaw-Complete-Guide-zh-v1.4.0.pdf", "raw/OpenClaw橙皮书_extracted.txt"]
updated: "2026-06-07"
---

# OpenClaw 部署

## 定义

OpenClaw 部署方式覆盖本地开发、容器、云服务器和云端封装产品。选择依据主要是技术能力、安全要求、渠道需求和预算。

## 主要方式

- 本地 npm：适合开发者和完全掌控数据的用户。
- Docker/Podman：适合长期运行、迁移和环境隔离。
- 国内云一键部署：适合新手，重点看模型套餐和 IM 生态，而不是只看服务器价格。
- SaaS/封装版：适合零门槛体验，但更新、安全和生态兼容性需要确认。

## 部署底线

- Gateway 不应直接暴露公网。
- 必须配置认证和防火墙。
- 必须持久化配置和 workspace 目录。
- 必须设置模型预算上限和 Fallback。

## 关联页面

- [[comparisons/OpenClaw_部署方案对比]]
- [[concepts/安全_OpenClaw_安全模型]]
- [[concepts/成本_OpenClaw_成本控制]]
- [[overview/主题_OpenClaw_安全与成本治理]]

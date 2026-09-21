<div align="center">

<img src="assets/hero.svg" alt="Everything about Jev" width="100%">

# ⚡ Everything about Jev

### 中文资料库 · Bilingual field guide · Source-backed ecosystem map

[![Docs](https://img.shields.io/badge/docs-bilingual-2563eb?style=for-the-badge)](docs/system-overview.md)
[![Demos](https://img.shields.io/badge/demos-Python%20%2B%20TypeScript-0f766e?style=for-the-badge)](demos/)
[![Sources](https://img.shields.io/badge/sources-dated%20%26%20linked-f59e0b?style=for-the-badge)](docs/sources.md)
[![Unofficial](https://img.shields.io/badge/status-independent%20community-64748b?style=for-the-badge)](CONTRIBUTING.md)

**Jev is a decision layer, not a chat box.**<br>
**Jev 是决策层，不是聊天框。**

[中文说明](#中文) · [English](#english) · [项目地图](catalog/projects.md) · [参与贡献](CONTRIBUTING.md)

</div>

---

<a id="中文"></a>

## 中文

Jev 是 TypeSafe AI 的 **System One** 模型：输入应用状态和预先定义的问题，得到 Choice、Score、Noul 等结构化答案与概率，供代码直接路由、评分、校验或触发人工复核。

```text
state + typed questions  →  constrained decisions + probabilities  →  your code
状态 + 类型化问题          →  受限决策 + 概率                    →  业务代码
```

这个仓库把分散的官方文档、GitHub 项目、博客、X / Reddit 讨论和可运行样例整理在一起，并明确标出 **官方主张 / 独立测量 / 社区观点**。我们借鉴了多个 awesome-jev 列表的分类方法，但增加了双语系统说明、工程边界、证据等级、失败模式、原始 HTTP、Python/TypeScript demo 和动态信息核验记录。

**研究快照 · Research snapshot**：5 个上游仓库 · 735 个候选仓库链接 · 8 组查询 · 19 页 · 337 条去重帖子。

[来源与致谢](ATTRIBUTION.md) · [发现索引](catalog/discovery.md) · [Demo 地图](catalog/demos.md)

### 从这里开始

| 你想做什么 | 入口 |
| --- | --- |
| 30 秒理解 Jev | [系统说明](docs/system-overview.md) |
| 发出第一个请求 | [快速开始](docs/getting-started.md) |
| 设计阈值、兜底和审计 | [工程模式](docs/patterns.md) |
| 直接运行代码 | [Python](demos/python/jev_demo.py) · [TypeScript](demos/typescript/jev-demo.ts) |
| 找 SDK、网关、应用和开源替代品 | [项目地图](catalog/projects.md) |
| 看支持与质疑 | [讨论与争议](docs/discussions.md) |
| 查看本次 X 分页检索 | [X 索引](docs/x-index.md) |
| 核对每条出处 | [来源记录](docs/sources.md) |

### 三个关键判断

- **答案空间先于模型调用**：Choice / Score / Noul 让输出可以进入类型化分支。
- **概率不是正确性证明**：设置阈值、保存完整分布，为低置信度保留人工或更强模型路径。
- **决策和副作用分离**：Jev 可以建议退款队列，真正退款必须由权限、幂等和事务代码执行。

> 当前公开资料把 Jev 描述为托管 API。社区的 OpenJev、Simple Jev、Kev、NanoJev 等是兼容层或独立研究，不应写成 TypeSafe 官方权重。

### 快速运行

```bash
pip install -r requirements.txt
# PowerShell
$env:TYPESAFE_API_KEY = "your-key"
python demos/python/jev_demo.py
```

密钥只放环境变量或密钥管理器；`.env` 已被忽略，绝不提交。

---

<a id="english"></a>

## English

Jev is TypeSafe AI’s **System One** model. You provide application state and typed questions; it returns constrained decisions and probabilities that software can consume directly. It is designed for classification, routing, scoring, verification, ranking, and guardrails—not open-ended writing or chat.

This repository is an independent, bilingual field guide. It combines primary sources, GitHub projects, runnable examples, and community discussion while labeling official claims, independent measurements, and opinions separately. It borrows the useful taxonomy of several awesome-jev lists and adds engineering guidance, failure modes, evidence levels, and reproducible starter code.

### Start here

- [System overview](docs/en/system-overview.md)
- [Getting started](docs/en/getting-started.md)
- [Production patterns and boundaries](docs/en/patterns.md)
- [Python and TypeScript demos](demos/)
- [Projects, SDKs, gateways, and research](catalog/projects.md)
- [X, blogs, and community debates](docs/en/discussions.md)
- [Paginated X search index](docs/x-index.md)
- [Source ledger and review dates](docs/en/sources.md)

### The practical rule

Use Jev to make a bounded judgment, then let ordinary code enforce thresholds, permissions, retries, idempotency, and side effects. A probability is a signal to calibrate on your data, not a guarantee.

## About this repository

- **Independent**: not affiliated with or endorsed by TypeSafe AI.
- **Bilingual**: Chinese first, English for global discoverability.
- **Evidence-led**: every dynamic claim carries a source and snapshot date.
- **Runnable**: examples use defensive validation and never print secrets.
- **Continuously revisable**: Jev aliases, prices, limits, gateways, and stars can change.

If you find a project, benchmark, failure case, or source worth adding, see [CONTRIBUTING.md](CONTRIBUTING.md).

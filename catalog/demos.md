# Demo 地图 / Demo map

[首页 / Home](../README.md) · [候选项目 / Discovery](discovery.md)

以下为上游发现与项目自述整理，未逐一运行。每个项目都给出值得观察的实验问题；性能声称需回到原始实验。These are project-reported demonstrations, not demos we have benchmarked.

| 场景 / Scenario | 项目 / Source | Jev 的角色 / Role | 应观察什么 / Inspect |
| --- | --- | --- | --- |
| 浏览器 / Browser | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 动作与目标选择 / Action and target selection | 动态 DOM、误点击、文本输入 / DOM changes and wrong actions |
| 语音 / Voice | [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | 部分转录到意图 / Partial transcript to intent | 等待还是执行 / When to wait |
| 手机 / Mobile | [mobile-jev](https://github.com/droidrun/mobile-jev) | 有限动作空间 / Bounded device actions | 操作是否可撤销 / Reversibility |
| 桌面 / Desktop | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) | OCR 后选动作 / Actions from OCR state | 文本感知误差 / OCR errors |
| 上下文 / Context | [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 工具历史保留 / History selection | 任务结果、缓存总成本 / Task success and cache costs |
| 日志 / Logs | [jevlogs](https://github.com/reachjalil/jevlogs) | 筛选诊断价值 / Diagnostic relevance | 漏掉真正错误的比例 / Missed incidents |
| 数据库 / SQL | [duckdb-jev](https://github.com/colliber/duckdb-jev) | 行级分类 / Row classification | 每行成本、并发和重试 / Per-row cost and retries |
| 搜索 / Retrieval | [jev-reranker](https://github.com/hotchpotch/jev-reranker) | 相关性判断 / Relevance judgment | 相对纯检索的增益 / Gain over retrieval alone |
| 代码 / Code quality | [supercov](https://github.com/supercorp-ai/supercov) | 文件优先级 / File prioritization | 是否找到真实缺陷 / Actual defects found |
| 游戏 / Games | [jev-tetris](https://github.com/thelau/jev-tetris) | 选择合法落点 / Placement selection | 规则基线与随机对照 / Rule and random baselines |
| 仿真 / Simulation | [jevpilot](https://github.com/standardagents/jevpilot) | 候选路径与速度 / Path and speed selection | 仿真不能证明实车能力 / Simulation is not road validation |
| 客服 / Support | [jev-experiments](https://github.com/dabit3/jev-experiments) | 意图与升级 / Intent and escalation | 边界输入与人工回退 / Ambiguity and review |
| 本地 / Local | [kev](https://github.com/jaredpalmer/kev) | 独立决策模型 / Independent model | 不同硬件与质量 / Hardware and quality |
| 兼容层 / Compatibility | [simple-jev](https://github.com/featherless-ai/simple-jev) | 从 logits 构造概率 / Probabilities from logits | 接口兼容不等于同等质量 / Schema versus quality |

## 本仓库示例 / Our examples

- [Python](../demos/python/jev_demo.py)：官方 SDK 客服路由、概率分布门槛、人工回退。
- [TypeScript](../demos/typescript/jev-demo.ts)：相同场景，使用推断类型的 Choice。
- [X collector](../scripts/collect_x.py)：独立的数据采集工具，不调用 Jev；包含分页和公开审计。

Examples demonstrate integration and policy; offline fixtures are synthetic and are not model measurements.

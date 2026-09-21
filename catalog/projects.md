# Jev 项目与 demo 目录

以下是 2026-09-21 的 GitHub API 搜索快照。stars 会变化，项目归类依据 README / 仓库描述，社区项目不代表 TypeSafe 官方背书。

## 官方与生态

| 项目 | 类型 | 说明 |
| --- | --- | --- |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 官方 skills | 面向 agent 的 System One 使用指导 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | 资源列表 | 项目、集成和讨论索引 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | 资源列表 | 含 SDK、网关和社区入口 |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 应用集成 | 浏览器自动化中的快速决策实验 |
| [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | demo | 语音意图到浏览器动作 |

## SDK、兼容层与服务

| 项目 | 说明 | 注意 |
| --- | --- | --- |
| [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) | 用开源模型构造 Jev 风格分类 endpoint | 是兼容/研究实现，不是官方 Jev |
| [razorback16/openjev](https://github.com/razorback16/openjev) | Jev-compatible 开源决策服务 | 自托管方案，需独立评估 |
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | 基于开源模型的兼容 endpoint | 偏基础设施实验 |
| [kazz187/jev-sdk-go](https://github.com/kazz187/jev-sdk-go) | 非官方 Go client | 使用前审查版本、协议和许可证 |
| [danvega/jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter) | Spring Boot starter | 社区维护 |

## 本地 / Jev-like 研究

| 项目 | 方向 |
| --- | --- |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 基于 Qwen 的可本地训练决策模型 |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | parallel decisions 与训练 pipeline |
| [wfzyx/von](https://github.com/wfzyx/von) | 非自回归本地决策模型 |
| [Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) | 校准决策 engine 与基准 |
| [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) | rerank / 分数差 benchmark |

## 选择建议

- 想调用 TypeSafe 服务：先读官方文档和 SDK，再看网关。
- 想理解协议：阅读 `simple-jev` 和 `openjev` 的输入/输出验证。
- 想本地实验：把 `kev`、`NanoJev`、`von` 当研究项目，单独核对数据集和 benchmark。
- 想找真实业务案例：先检查是否有可复现实验、测试和失败案例，不要只看 stars。

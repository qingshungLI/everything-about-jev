"""文档生成流水线：双语编辑内容 → 统一视觉导航 → 输出两个 README。

本脚本不采集数据、不调用模型，避免重建文档时产生 API 费用。
实测数字仅来自已保存的案例，候选项目数量不冒充已验证项目数。
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADER = '''<div align="center">

<img src="assets/hero.svg" alt="Everything about Jev" width="100%">

# Everything about Jev

[![Checks](https://github.com/qingshungLI/everything-about-jev/actions/workflows/checks.yml/badge.svg)](https://github.com/qingshungLI/everything-about-jev/actions/workflows/checks.yml)
[![License](https://img.shields.io/github/license/qingshungLI/everything-about-jev?color=14b8a6)](LICENSE)

[简体中文](README.md) · [English](README.en.md)

</div>

'''

ZH = '''这里整理了 Jev 的使用方法、示例代码、社区项目和讨论。如果你刚听说这个模型，可以先读下面的介绍，再选一个 demo 跑起来。

[快速开始](#快速开始) · [示例](#示例) · [社区讨论](#社区讨论) · [项目目录](catalog/projects.md)

## Jev 是什么

Jev 是 TypeSafe AI 的决策模型。你给它一段文本或业务状态，再定义问题和可选答案，它会返回选择、评分和概率。

比如收到一条“我的订阅扣了两次钱”的消息，你可以让 Jev 判断该交给哪个团队、是否需要人工处理，以及紧急程度。它返回的字段可以直接用于程序里的条件分支。

| 类型 | 用法 | 返回值 |
| --- | --- | --- |
| Choice | 从“账单、技术、其他”中选择 | 选项、confidence、各选项概率 |
| Noul | 判断是否需要人工处理 | “是”的概率 |
| Score | 按给定量表评估紧急程度 | 评分和概率分布，评分可能为小数 |

Jev 适合分类、路由、筛选和有限动作选择。需要写回复时，可以接生成模型；需要查最新信息时，由应用先检索，再把结果传给 Jev。`confidence` 和获选项概率是不同字段，接入时要注意区分。

[系统说明](docs/system-overview.md)介绍了这三类问题、模型边界，以及如何在应用里处理不确定的结果。

## 快速开始

需要 Python 3.10+。下面使用 [jevai.org 社区 API](https://www.jevai.org/docs)；使用 TypeSafe 官方密钥的读者请看[官方 SDK 示例](docs/official-sdk.md)。

```bash
git clone https://github.com/qingshungLI/everything-about-jev.git
cd everything-about-jev
python -m pip install -r requirements.txt
```

在根目录创建 `.env`：

```dotenv
JEVAI_API_KEY=你的社区服务密钥
```

运行：

```bash
python demos/python/quickstart.py
```

默认示例把“把页面变暗一点，晚上看太刺眼了”匹配到 `dark_mode`。它只返回动作名称，不操作浏览器。密钥文件已加入 `.gitignore`。

也可以用 TypeScript（Node.js 20+）：

```bash
npm ci
npm run demo:community
```

遇到限流或密钥问题，参见[接入说明](docs/getting-started.md)。社区 API 和官方 API 使用各自的密钥，具体区别见[供应方对照](docs/providers.md)。

## 示例

| 示例 | 内容 | Python 参数 |
| --- | --- | --- |
| 命令面板 | 根据一句话选择深色模式、导出或帮助 | `--case palette` |
| 工单分类 | 同时判断队列、人工需求和紧急度 | `--case ticket` |
| 资料核对 | 判断提供的资料是否支持一个说法 | `--case research` |
| 模型路由 | 从给定候选中选择适合任务的模型 | `--case model-route` |
| 工具检查 | 检查工具调用是否符合操作规则 | `--case tool-guard` |
| 完成检查 | 根据已完成工作和缺失项判断任务状态 | `--case completion` |

例如：

```bash
python demos/python/quickstart.py --case model-route
```

更多语言和演示入口：

- [Python](demos/python/quickstart.py)、[TypeScript](demos/typescript/community-demo.ts)、[Node.js](demos/node/tool-guard.mjs)、[Bash / curl](demos/curl/tool-guard.sh)。
- [浏览器演示](demos/web/index.html)：离线模拟，适合讲解交互流程。
- [录屏说明](demos/README.md)：启动方式和演示顺序。
- [Agent 与 MCP 接入](docs/agent.md)：在 Agent 中使用这些判断。

示例使用合成数据。API 调用结果和限流情况放在[运行记录](docs/live-validation.md)中。

## 社区讨论

讨论里最常被提到的是速度、成本，以及把分类判断放进现有程序的便利。分歧更多出现在具体用法上：用 Jev 选一个按钮很直观，但用它删减长对话、评价复杂推理或规划多步任务，还需要看整个任务的表现。

几个值得一起读的观点：

- [Tùng Đinh](https://x.com/tdinh_me/status/2100803719575343138)认为通用分类本身并不新，快和便宜才是值得关注的地方。
- [Tamara](https://x.com/tamarajtran/status/2100694549362553153)尝试给工具历史打分，删除不再相关的内容；[Theo](https://x.com/theo/status/2100762304862384257)担心这种压缩会丢掉任务状态，并增加缓存开销。
- [Karminski](https://x.com/karminski3/status/2101941770003361893)报告了迷宫中反复绕圈的案例，提醒使用者区分单步判断与多步规划。

[社区总结](docs/community-report.md)展开了这些讨论，也包括概率校准、本地替代模型和实际应用。材料来自 337 条公开帖子的采集与选读，不代表整个社区的意见比例。

## 更多资料

- [工程模式](docs/patterns.md)：阈值、人工回退、日志与评估。
- [Demo 地图](catalog/demos.md)：浏览器、语音、SQL、游戏等项目。
- [项目目录](catalog/projects.md)与[发现索引](catalog/discovery.md)：后者包含从五个上游列表整理的候选链接，尚未逐项筛选。
- [来源](docs/sources.md)与[致谢](ATTRIBUTION.md)。

欢迎补充项目、分享使用经验或纠正文档，见[贡献指南](CONTRIBUTING.md)。本仓库由社区维护，与 TypeSafe AI 和 jevai.org 无隶属关系。
'''

EN = '''A collection of Jev guides, code examples, community projects and discussions. If you are new to the model, start with the introduction below, then try a demo.

[Quickstart](#quickstart) · [Examples](#examples) · [Community discussion](#community-discussion) · [Projects](catalog/projects.md)

## What is Jev?

Jev is a decision model from TypeSafe AI. Give it text or application state, define questions and possible answers, and it returns choices, scores and probabilities.

For a message such as “I was charged twice,” you could ask which team should handle it, whether someone needs to review it, and how urgent it is. The returned fields can feed directly into application logic.

| Type | Example | Returns |
| --- | --- | --- |
| Choice | Choose billing, technical or other | A choice, confidence and probabilities |
| Noul | Does this need human review? | The probability of yes |
| Score | Assess urgency using a supplied rubric | A score and distribution; the score can be fractional |

Jev fits classification, routing, filtering and selection among known actions. Use a generative model to write replies, and retrieve current information before passing it to Jev. Note that `confidence` and the selected option's probability are separate fields.

The [system overview](docs/en/system-overview.md) covers question types, limitations and handling uncertain results.

## Quickstart

Requires Python 3.10+. This example uses the [jevai.org community API](https://www.jevai.org/docs). For TypeSafe-issued keys, use the separate [official SDK example](demos/python/jev_demo.py).

```bash
git clone https://github.com/qingshungLI/everything-about-jev.git
cd everything-about-jev
python -m pip install -r requirements.txt
```

Create `.env` in the repository root:

```dotenv
JEVAI_API_KEY=your-community-service-key
```

Run:

```bash
python demos/python/quickstart.py
```

The default example maps a Chinese request for a darker page to `dark_mode`. It returns an action name without controlling a browser. The key file is excluded from Git.

For TypeScript, with Node.js 20+:

```bash
npm ci
npm run demo:community
```

See [getting started](docs/en/getting-started.md) for rate limits and key setup. The community and official APIs use separate credentials; see the [provider comparison](docs/providers.md).

## Examples

| Example | Task | Python argument |
| --- | --- | --- |
| Command palette | Match a request to dark mode, export or help | `--case palette` |
| Ticket classification | Assess queue, review needs and urgency | `--case ticket` |
| Claim check | Check whether supplied material supports a claim | `--case research` |
| Model routing | Select a model from supplied candidates | `--case model-route` |
| Tool check | Check a proposed action against a policy | `--case tool-guard` |
| Completion check | Review completed work and remaining gaps | `--case completion` |

For example:

```bash
python demos/python/quickstart.py --case model-route
```

Other languages and demos:

- [Python](demos/python/quickstart.py), [TypeScript](demos/typescript/community-demo.ts), [Node.js](demos/node/tool-guard.mjs) and [Bash / curl](demos/curl/tool-guard.sh).
- [Browser demo](demos/web/index.html): an offline simulation for explaining the interaction.
- [Recording notes](demos/README.md): setup and a suggested walkthrough.
- [Agent and MCP integration](docs/agent.md): using these decisions in an agent.

Examples use synthetic inputs. API responses and rate-limit observations are in the [run notes](docs/live-validation.md).

## Community discussion

Speed, cost and ease of integration come up often. The disagreements tend to be about particular uses: selecting a button is straightforward, while pruning long conversations, judging complex reasoning or planning several steps calls for evaluating the whole task.

A few views worth reading together:

- [Tùng Đinh](https://x.com/tdinh_me/status/2100803719575343138) argues that general classification is familiar; speed and cost are the interesting part.
- [Tamara](https://x.com/tamarajtran/status/2100694549362553153) proposes scoring tool history and dropping irrelevant content. [Theo](https://x.com/theo/status/2100762304862384257) questions whether that preserves task state and saves money after cache costs.
- [Karminski](https://x.com/karminski3/status/2101941770003361893) reports a maze experiment in which the model repeats moves, raising questions about using local decisions for planning.

The [community report](docs/en/community-report.md) covers these discussions, calibration, local alternatives and applications. It draws on a collected sample of 337 public posts and selected readings, not a representative opinion poll.

## More resources

- [Engineering patterns](docs/en/patterns.md): thresholds, review paths, logging and evaluation.
- [Demo map](catalog/demos.md): browser, voice, SQL, game and other projects.
- [Project guide](catalog/projects.md) and [discovery index](catalog/discovery.md): the latter contains candidate links from five upstream lists, still awaiting individual review.
- [Sources](docs/en/sources.md) and [acknowledgments](ATTRIBUTION.md).

Contributions, experience reports and corrections are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). This is a community repository, unaffiliated with TypeSafe AI or jevai.org.
'''


def main() -> None:
    """输出双语 README，假设仓库已有图与文档。

    Args:
        None: 内容来自本文件中的双语编辑文本。

    Returns:
        None: 更新根目录两个 README。
    """
    for name, body in (("README.md", ZH), ("README.en.md", EN)):
        (ROOT / name).write_text(HEADER + body, encoding="utf-8")


if __name__ == "__main__":
    main()

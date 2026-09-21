# 真实调用记录 / Live validation

本轮使用用户授权的 **jevai.org 社区 REST API**，输入为仓库公开合成案例。没有使用真实工单、客户信息或个人数据，也没有执行返回的动作。没有向官方端点试发社区密钥。

These are actual calls using synthetic inputs to the authorized community provider. They test integration, not accuracy. No suggested action was executed. The service did not return a pinned model version, so these records cannot identify the underlying version independently.

## 成功记录 / Successful calls

| 案例 / Case | 真实返回 / Actual result | 耗时 / Elapsed | 请求次数 / Attempts | Artifact |
| --- | --- | ---: | ---: | --- |
| Python command palette | `dark_mode`, confidence 1 | 1,392.1 ms | 1 | [JSON](../data/live-palette.json) |
| Evidence check | `reject`; probability 0.55; confidence 0.33 | 1,289.9 ms | 1 | [JSON](../data/live-research.json) |
| Model router | `decision-model`; escalate 0.12 | 20,947.7 ms | 3 | [JSON](../data/live-model-route.json) |
| Tool guard | `deny`; Noul 0.98; Score 2.99 | 7,236.1 ms | 2 | [JSON](../data/live-tool-guard.json) |

耗时为客户端观察的单次案例总耗时，含网络、服务处理及限流退避。不能从这些数值推导平均延迟或 SLA，也没有扣除网络以伪造模型速度。

Elapsed time includes network, service handling and retry backoff. These are individual observations, not averages or an SLA. `confidence=1` is a returned value, not measured 100% accuracy. Service preset guidance is distinguished from model-generated prose.

## 失败与边界 / Failures and limits

- 多次请求返回 HTTP 429，正文为限流错误，未提供 Retry-After。Python 仅对 429 有限重试（最多四次）；TypeScript 明确失败，要求稍后重跑。
- `--all` 曾在首个三问题工单上耗尽限流预算。不能保证共享服务随时有可用配额。逐个案例比并发调用更容易排查。
- 官方 SDK 示例经过构造、类型检查和离线测试；本轮没有用官方直连凭据进行真实推理。
- 用户原有小写变量是兼容别名；推荐社区 key 使用 `JEVAI_API_KEY`，官方 key 使用 `TYPESAFE_API_KEY`。

Repeated HTTP 429 responses lacked Retry-After. The all-cases run exhausted its retry budget on the ticket case. We do not promise continuous availability or claim that a successful community call validates the official direct API.

## 复现 / Reproduce

```bash
python demos/python/quickstart.py --case palette --output data/my-run.json
python demos/python/quickstart.py --case research
npm run demo:community
```

新的运行可能返回不同概率。私有输入不应保存为公开 artifact。`data/live-*.json` 只包含本仓库案例和返回，无认证头。字段与地址参照 [社区 API 文档](https://www.jevai.org/docs)。

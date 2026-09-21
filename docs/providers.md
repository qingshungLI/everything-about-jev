# 密钥与接入方式 / Providers and credentials

| 项目 / Item | jevai.org 社区 / Community | TypeSafe 官方 / Official |
| --- | --- | --- |
| 文档 / Docs | https://www.jevai.org/docs | https://docs.typesafe.ai/ |
| 地址 / Endpoint | `https://www.jevai.org/api/v1/decisions` | `https://api.typesafe.ai/v1/systemone` |
| 密钥 / Key | 社区个人 key，推荐变量 `JEVAI_API_KEY` | 官方 console key，`TYPESAFE_API_KEY` |
| 认证 / Authentication | Bearer | Bearer（SDK 自动处理） |
| 请求 / Request | state + questions；另外有业务预设 | state + questions |
| 响应 / Response | `{code,message,data}` | SDK 类型化响应 / typed SDK result |
| Python 示例 | `demos/python/quickstart.py` | `demos/python/jev_demo.py` |
| TypeScript 示例 | `npm run demo:community` | `npm run demo` |
| 本轮状态 / Validation scope | 实际发送合成输入并保存返回 / live calls recorded | SDK 类型检查与离线测试 / offline only |

本轮 `.env` 中用户使用小写 `typesafe_api_key` 命名社区服务凭据，示例兼容这个历史名称。**不要因此推断不同供应方密钥可以互换。** 新用户请使用 `JEVAI_API_KEY`，避免含义混淆。官方大写变量不会自动转发到社区主机。

The lowercase legacy variable is supported for this workspace only as an explicit compatibility alias. Names do not establish credential interchangeability. Use a key issued by the endpoint you intend to call. The official uppercase variable is not forwarded to the community host.

社区文档描述的 `guidance_source=jev_preset` 表示服务预设；不能据此宣称 Jev 本身生成了长解释。服务未提供模型版本时，实测记录保留缺失，不伪造 `jev-1.13.0`。HTTP 429 曾实际出现，属于服务调用限制，不是分类结果。

Preset guidance is server-provided text. Missing model-version metadata stays missing. An HTTP 429 is a service failure, not a model prediction. Our records measure client-observed latency, including any retries; they do not isolate inference time.

# 快速开始

## 1. 获取访问权限

[官方公告](https://x.com/typesafeai/status/2101786156572823624)于 2026-09-20 UTC 宣布取消 waitlist。前往 [console](https://console.typesafe.ai/settings/keys) 创建 Jev 密钥。GetXAPI 密钥不能调用 Jev。以 [TypeSafe 官方站点](https://typesafe.ai/) 的当前说明为准。部分用户也通过 Vercel AI Gateway、OpenRouter 等网关访问；网关会有自己的模型 ID、计费和限流规则。

## 2. 设置密钥

```powershell
$env:TYPESAFE_API_KEY = "your-key"
```

本仓库根目录的 `.env` 仅用于本地工具配置，已被 `.gitignore` 排除。不要复制或提交真实密钥。

## 3. 发送第一个请求

官方 Python SDK 会把 Choice / Score / Noul 映射为类型化对象。原始 HTTP 结构仍适合调试网关，但字段名、endpoint 和响应字段可能随 API 版本调整，生产代码请对照官方文档。

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "category": Choice(
                instructions="What is this ticket about?",
                criteria={"billing": None, "technical": None, "other": None},
            ),
        },
    )

answer = response.choices["category"]
print(answer.choice, answer.confidence, answer.probabilities)
```

安装：`pip install typesafe-sdk`。JavaScript / TypeScript 使用 `npm install @typesafe-ai/sdk`，并调用 `client.systemOne({ state, questions })`。

```bash
curl https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-latest",
    "state": {"message": "I was charged twice for my subscription."},
    "questions": {
      "queue": {
        "type": "choice",
        "instructions": "Which queue should handle this message?",
        "criteria": {"billing": null, "technical": null, "other": null}
      }
    }
  }'
```

## 4. 把概率接入代码

```python
winner = result.choices["queue"].choice
probability = result.choices["queue"].confidence
action = winner if probability >= 0.80 else "human_review"
print(action)
```

阈值 `0.80` 只是示意。生产环境要用带标签的历史数据选择阈值，并记录模型版本、问题定义、state 摘要、完整分布和最终人工结果。

## 常见错误

- 把 `Jev` 当聊天 API，请它“写一封邮件”。
- 只保存最高选项，丢失平局和不确定性。
- 把用户可控文本直接拼进问题规则，导致判定标准被输入覆盖。
- 用精确计算替代普通代码。
- 将社区的 OpenJev / Simple Jev / Jev-like 项目误称为 TypeSafe 官方模型。


[Read in English](en/getting-started.md)

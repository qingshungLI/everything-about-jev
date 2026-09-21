"""客服路由流水线：验证消息 → 构造 Choice → 调用 SDK → 门槛 → 建议动作。

门槛使用 confidence；它是独立字段，不假定等于获选类别概率。
空消息和无效门槛报错，未知队列和平局复核。示例不执行业务副作用。
"""

from __future__ import annotations

import json
import os
import math

from typesafe_sdk import Choice, SystemOneResponse, TypeSafeClient


MODEL = os.getenv("TYPESAFE_MODEL", "jev-latest")
THRESHOLD = 0.80


def build_state(message: str) -> dict[str, str]:
    """构造非空客服状态，拒绝缺失或空白消息。

    Args:
        message: 非空客服消息。

    Returns:
        可序列化的状态字典。
    """
    if not isinstance(message, str) or not message.strip():
        raise ValueError("message must not be empty")
    return {"message": message}


def call_jev(state: dict[str, str]) -> SystemOneResponse:
    """通过官方 SDK 调用 Jev，假设环境中已设置服务密钥。

    Args:
        state: 已验证的客服状态。

    Returns:
        官方 SDK 的类型化响应。
    """
    if not os.getenv("TYPESAFE_API_KEY", "").strip():
        raise ValueError("TYPESAFE_API_KEY is required")
    with TypeSafeClient() as client:
        return client.system_one(
            state=state,
            model=MODEL,
            questions={
                "queue": Choice(
                    instructions="Which queue should handle this message?",
                    criteria={"billing": None, "technical": None, "other": None},
                ),
            },
        )


def decide(data: SystemOneResponse, threshold: float = THRESHOLD) -> str:
    """根据 confidence 门槛建议队列，平局与未知类别复核。

    Args:
        data: 官方 SDK 的响应。
        threshold: 零至一的示例门槛，生产环境需自行校准。

    Returns:
        billing、technical 或 human_review。
    """
    if not math.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    answer = data.choices["queue"]
    value = str(answer.choice)
    probability = float(answer.confidence)
    if not 0.0 <= probability <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if value not in {"billing", "technical", "other"}:
        raise ValueError("unexpected queue")
    distribution = answer.probabilities
    if set(distribution) != {"billing", "technical", "other"}:
        raise ValueError("unexpected probability keys")
    if any(not 0 <= p <= 1 for p in distribution.values()):
        raise ValueError("invalid probabilities")
    if not math.isclose(sum(distribution.values()), 1, abs_tol=0.01):
        raise ValueError("probabilities must sum to approximately one")
    maximum = max(distribution.values())
    tied = sum(math.isclose(p, maximum, abs_tol=1e-9) for p in distribution.values()) > 1
    if value == "other" or tied:
        return "human_review"
    return value if probability >= threshold else "human_review"


def main() -> None:
    """读取示例消息、调用服务并打印动作；密钥永远不写入输出。"""
    result = call_jev(build_state("I was charged twice for my subscription."))
    print(json.dumps({"action": decide(result)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
